const SHARE_PURCHASE_PRICE_IMPACT = 0.001;

class SharePurchaseError extends Error {
  constructor(statusCode, message) {
    super(message);
    this.name = "SharePurchaseError";
    this.statusCode = statusCode;
  }
}

function requireSharePurchase(condition, statusCode, message) {
  if (!condition) {
    throw new SharePurchaseError(statusCode, message);
  }
}

function parseSharePurchaseQuantity(value) {
  const normalized = typeof value === "string" ? value.trim() : value;

  const validType =
    typeof normalized === "number" ||
    (typeof normalized === "string" && /^\d+$/.test(normalized));

  const quantity = validType ? Number(normalized) : NaN;

  requireSharePurchase(
    Number.isSafeInteger(quantity) && quantity > 0,
    400,
    "SharesToBuy must be a positive whole number"
  );

  return quantity;
}

async function purchaseSharesFromUser({ buyerId, shareId, quantity }) {
  if (Shares.db !== User.db) {
    throw new Error(
      "Shares and User must use the same database connection"
    );
  }

  await Shares.db.transaction(async (session) => {
    const share = await Shares.findById(shareId).session(session);

    requireSharePurchase(share, 404, "Share not found");

    // Falls dein Schema einen Verkaufsstatus besitzt, diesen hier prüfen.
    requireSharePurchase(
      share.user &&
        share.userBuyIn &&
        Number.isFinite(share.priceToSell) &&
        share.priceToSell > 0,
      409,
      "Share is not available for purchase"
    );

    requireSharePurchase(
      String(share.user).toLowerCase() !== buyerId,
      400,
      "You cannot buy your own shares"
    );

    requireSharePurchase(
      Number.isSafeInteger(share.buyShares) &&
        share.buyShares >= quantity,
      409,
      "Not enough shares available"
    );

    const buyer = await User.findById(buyerId).session(session);
    const seller = await User.findById(share.user).session(session);

    const companyShares = await Shares.findOne({
      corp: share.userBuyIn,
      operation: "buy",
    }).session(session);

    requireSharePurchase(buyer, 404, "Buyer not found");
    requireSharePurchase(seller, 404, "Seller not found");
    requireSharePurchase(companyShares, 404, "Company shares not found");

    // Bestehende Rundungsregel: denselben Betrag prüfen und buchen.
    const totalPrice = Math.round(quantity * share.priceToSell);

    requireSharePurchase(
      Number.isSafeInteger(totalPrice) && totalPrice > 0,
      409,
      "Purchase total is outside the supported range"
    );

    requireSharePurchase(
      Number.isFinite(buyer.money) &&
        buyer.money >= 0 &&
        buyer.money <= Number.MAX_SAFE_INTEGER &&
        Number.isFinite(seller.money) &&
        seller.money >= 0 &&
        seller.money <= Number.MAX_SAFE_INTEGER - totalPrice,
      409,
      "Account balance is outside the supported range"
    );

    requireSharePurchase(
      buyer.money >= totalPrice,
      409,
      "Not enough money"
    );

    requireSharePurchase(
      Number.isFinite(companyShares.pricePerShare) &&
        companyShares.pricePerShare >= 0,
      409,
      "Invalid company share price"
    );

    const newCompanyPrice = Math.round(
      companyShares.pricePerShare +
        SHARE_PURCHASE_PRICE_IMPACT * quantity
    );

    requireSharePurchase(
      Number.isSafeInteger(newCompanyPrice),
      409,
      "Company share price is outside the supported range"
    );

    // Bestand nur reduzieren, wenn ausreichend Aktien vorhanden sind.
    const updatedOffer = await Shares.findOneAndUpdate(
      {
        _id: share._id,
        buyShares: { $gte: quantity },
      },
      {
        $inc: { buyShares: -quantity },
      },
      { session, new: true }
    );

    requireSharePurchase(
      updatedOffer,
      409,
      "Share availability changed"
    );

    // Guthabenprüfung und Abbuchung erfolgen in einem Update.
    const updatedBuyer = await User.findOneAndUpdate(
      {
        _id: buyer._id,
        money: { $gte: totalPrice },
      },
      {
        $inc: { money: -totalPrice },
      },
      { session, new: true }
    );

    requireSharePurchase(updatedBuyer, 409, "Not enough money");

    const updatedSeller = await User.findByIdAndUpdate(
      seller._id,
      { $inc: { money: totalPrice } },
      { session, new: true }
    );

    requireSharePurchase(
      updatedSeller,
      409,
      "Seller no longer exists"
    );

    const buyerHolding = await Shares.findOne({
      user: buyer._id,
      userBuyIn: share.userBuyIn,
      operation: "buy",
    }).session(session);

    // Nur die Behandlung des Käuferbestands unterscheidet sich.
    if (buyerHolding) {
      requireSharePurchase(
        Number.isSafeInteger(buyerHolding.buyShares) &&
          buyerHolding.buyShares >= 0 &&
          Number.isSafeInteger(buyerHolding.buyShares + quantity),
        409,
        "Buyer share balance is outside the supported range"
      );

      buyerHolding.buyShares += quantity;
      await buyerHolding.save({ session });
    } else {
      const newHolding = new Shares({
        user: buyer._id,
        userBuyIn: share.userBuyIn,
        buyShares: quantity,
        operation: "buy",
      });

      await newHolding.save({ session });
    }

    if (updatedOffer.buyShares === 0) {
      const deletion = await Shares.deleteOne(
        { _id: share._id, buyShares: 0 },
        { session }
      );

      requireSharePurchase(
        deletion.deletedCount === 1,
        409,
        "Offer changed"
      );
    }

    companyShares.pricePerShare = newCompanyPrice;
    await companyShares.save({ session });
  });
}

router.post(
  "/shares/:shareId/buySharesFromUser",
  validateJWT,
  async (req, res) => {
    try {
      const buyerId = String(req.id ?? "").toLowerCase();
      const shareId = req.params.shareId;
      const objectIdPattern = /^[a-f\d]{24}$/i;

      requireSharePurchase(
        objectIdPattern.test(buyerId),
        401,
        "Invalid user"
      );

      requireSharePurchase(
        objectIdPattern.test(shareId),
        400,
        "Invalid share ID"
      );

      const quantity = parseSharePurchaseQuantity(
        req.body?.SharesToBuy
      );

      await purchaseSharesFromUser({ buyerId, shareId, quantity });

      // Erst nach erfolgreichem Commit antworten.
      return res.status(200).json({
        status: true,
        message: "Buy successful",
      });
    } catch (error) {
      if (error instanceof SharePurchaseError) {
        return res.status(error.statusCode).json({
          status: false,
          error: error.message,
        });
      }

      console.error("Share purchase failed", {
        shareId: req.params.shareId,
        buyerId: req.id,
        error,
      });

      return res.status(500).json({
        status: false,
        error: "Error performing action",
      });
    }
  }
);