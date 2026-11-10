router.post("/shares/:shareId/buySharesFromUser", validateJWT, async (req, res, next) => {
  const actual_user = req.id;
  const { shareId } = req.params;
  const { SharesToBuy } = req.body;
  try {
    const share = await Shares.findOne({_id: shareId});
    const corpShares = await Shares.findOne({corp: share.userBuyIn, operation: "buy"});
    const userBuy = await User.findOne({_id: actual_user });
    if( !share ) return res.json({status: false, error: "Error finding share"});
    if(parseInt(SharesToBuy) > share.buyShares) return res.json({status: false, error: "You can't sell a number greater than your shares"});
    if(parseInt(SharesToBuy) < 0 || parseInt(SharesToBuy) === 0) return res.json({status: false, error: "You can't issue a negative number of shares"});
    if(userBuy.money < ( parseInt(SharesToBuy) * share.priceToSell)) return res.json({status: false, error: "You don't have enough money"});
    const sharesToSell = share.buyShares - parseInt(SharesToBuy);
    const UserShares = await Shares.findOne({user: actual_user, userBuyIn: share.userBuyIn, operation: "buy"});
    if(SharesToBuy < 0 || sharesToSell === 0){
    const UpdateShare = await Shares.findByIdAndDelete( shareId ); 
    if( !UpdateShare ) return res.json({status: false, error: "Error updating shares"});

    }else{
    const UpdateShare = await Shares.findByIdAndUpdate( shareId, {buyShares: share.buyShares - parseInt(SharesToBuy)} );
    if( !UpdateShare ) return res.json({status: false, error: "Error updating shares"});

    }
    if(UserShares){
    const UpdateUserShares = await Shares.findByIdAndUpdate( UserShares._id, {buyShares: UserShares.buyShares + parseInt(SharesToBuy)} );
    if( !UpdateUserShares ) return res.json({status: false, error: "Error updating shares"});
    const UserSelling = await User.findOne({_id: share.user});
    const updateUser = await User.findByIdAndUpdate( UserSelling._id, {money: UserSelling.money + (Math.round(parseInt(SharesToBuy) * share.priceToSell))} );
    if( !updateUser ) return res.json({status: false, error: "Error updating user"});
    const updateUserBuy = await User.findByIdAndUpdate( userBuy._id, {money: userBuy.money - (Math.round(parseInt(SharesToBuy) * share.priceToSell))} );
    if( !updateUserBuy ) return res.json({status: false, error: "Error updating user"});

    corpShares.pricePerShare = Math.round((corpShares.pricePerShare + 0.001 * SharesToBuy));
    corpShares.save();

    return res.json({status: true, message: "Buy successful"});

    }

    if(!UserShares){
    const UserSelling = await User.findOne({_id: share.user});
    const updateUser = await User.findByIdAndUpdate( UserSelling._id, {money: UserSelling.money + (Math.round(parseInt(SharesToBuy) * share.priceToSell))} );
    if( !updateUser ) return res.json({status: false, error: "Error updating user"});
    const updateUserBuy = await User.findByIdAndUpdate( userBuy._id, {money: userBuy.money - (Math.round(parseInt(SharesToBuy) * share.priceToSell))} );
    if( !updateUserBuy ) return res.json({status: false, error: "Error updating user"});

    const newShare = new Shares({
        userBuyIn: share.userBuyIn,
        user: actual_user,
        buyShares: parseInt(SharesToBuy),
        operation: "buy",
    });

    const saveShare = await newShare.save();
    if( !saveShare ) return res.json({status: false, error: "Error saving shares"});

    corpShares.pricePerShare = Math.round((corpShares.pricePerShare + 0.001 * SharesToBuy));
    corpShares.save();

    return res.json({status: true, message: "Buy successful"});
    }


    const saveShare = await newShare.save();
    if( !saveShare ) return res.json({status: false, error: "Error saving shares"});

    return res.json({status: true, message: "Buy successful"});
  } catch (error) {
    console.log(error);
    res.json({status: false, error: "Error performing action"});
  }
})