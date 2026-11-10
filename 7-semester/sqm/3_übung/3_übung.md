# Übung 3 - Testen und Qualität

## Hinweise zu den KI-Aufgabenteilen

Einige Aufgaben enthalten Teile, die Sie mit einem KI-Assistenten (z. B. ChatGPT, Claude, Copilot oder Mistral Le Chat) bearbeiten sollten. Sie sind wie folgt gekennzeichnet:

- **KI – sokratisch:** Die KI ist Ihr Tutor, nicht Ihr Lösungslieferant. Sie bearbeiten den Grundteil zuerst selbst. Die KI darf nur Fragen stellen, Annahmen hinterfragen und Lücken aufzeigen, aber keine Lösung vorgeben.
- **KI – Werkzeug:** Wie in der Industrie häufig (leider) üblich, nutzen Sie die KI als Lösungswerkzeug. Ihre eigentliche Leistung ist die fachliche Prüfung: Was ist richtig, was falsch, was fehlt – und wie belegen Sie das?

**Vorlage für den sokratischen Modus (als ersten Prompt verwenden):**

> Du bist Tutor im Fach Softwarequalitätsmanagement (Master). Gib mir keine Lösungen und keine Musterantworten. Stelle mir stattdessen jeweils genau eine gezielte Frage zu meiner Antwort, die mich auf Lücken, unscharfe Begriffe oder ungeprüfte Annahmen hinweist. Nur wenn ich ausdrücklich um einen Hinweis bitte, gib mir einen kleinen Denkanstoß. Hier ist meine Antwort: …

**Dokumentation:** Geben Sie zu jedem KI-Teil (1) Ihre Prompts, (2) einen aussagekräftigen Ausschnitt der KI-Antwort und (3) Ihre eigene Bewertung in 3–5 Sätzen ab. Geben Sie keinen vertraulichen oder fremden, nicht freigegebenen Code in öffentliche KI-Dienste ein.

## Aufgabe 1

### Aufgabenstellung

**a)** Wie würden Sie „Änderbarkeit von Quellcode“ messbar/prüfbar für ein fiktives Projekt definieren?

Tipp: Denken Sie an das in der Vorlesung gezeigte Vorgehen bzgl. der Definition von Qualitätseigenschaften und deren Verfeinerung bis hin zu Qualitätsindikatoren.

**b)** Welche Maßnahmen würden Sie in Ihrem Team umsetzen, um die Änderbarkeit der entwickelten Software auch während des Entwicklungsprozesses bereits zu ermöglichen.

**c) KI – sokratisch:** Legen Sie Ihr Qualitätsmodell aus a) einer KI im sokratischen Modus vor und lassen Sie sich mindestens vier Rückfragen stellen. Überarbeiten Sie danach Ihr Modell.

- Welche Rückfragen haben Ihr Modell am stärksten verändert, und warum?

**d) KI – Werkzeug:** In vielen Teams erzeugen KI-Coding-Assistenten (z. B. GitHub Copilot, Cursor, Claude Code) inzwischen einen erheblichen Teil des Quellcodes. Ergänzen Sie Ihre Maßnahmen aus b):

- Welche Risiken bringt KI-generierter Code für die Änderbarkeit mit sich (z. B. Duplikate, uneinheitlicher Stil, Code, den im Team niemand wirklich versteht, rechtliche Fragestellungen)?
- Welche Regeln und Prüfungen würden Sie einführen (z. B. Review-Pflicht, Qualitäts-Gates in der CI-Pipeline, Architekturregeln, Kennzeichnung KI-generierter Änderungen)? Begründen Sie Ihre Auswahl.

### Bearbeitung

#### a) Änderbarkeit messbar/prüfbar definieren

Die Änderbarkeit von Quellcode beschreibt den Grad, in dem der Quellcode geändert werden kann, ohne die zugrunde liegende Systemarchitektur zu verletzen. Dabei soll der Quellcode keine ungewollten Redundanzen aufweisen und die Code-Komplexität (gemessen z. B. anhand einer No-Nesting-Policy) nicht zu hoch sein.

#### b) Maßnahmen im Entwicklungsprozess

Ich würde zu Beginn des Projekts, noch bevor Code geschrieben wird, gemeinsam mit dem Team ein Regelwerk festlegen. Dieses soll konkrete Vorgaben dazu enthalten, welche Qualität der Quellcode aufweisen soll und wie diese gemessen wird. Außerdem soll die Verwendung der erarbeiteten Architektur verpflichtend sein.

#### c) Qualitätsmodell im sokratischen Dialog überarbeiten

##### Prompt

```
Du bist Tutor im Fach Softwarequalitätsmanagement (Master). Gib mir keine Lösungen und
keine Musterantworten. Stelle mir stattdessen jeweils genau eine gezielte Frage zu meiner
Antwort, die mich auf Lücken, unscharfe Begriffe oder ungeprüfte Annahmen hinweist. Nur
wenn ich ausdrücklich um einen Hinweis bitte, gib mir einen kleinen Denkanstoß.

Das ist die Aufgabenstellung:
Wie würden Sie „Änderbarkeit von Quellcode“ messbar/prüfbar für ein fiktives Projekt
definieren?
Tipp: Denken Sie an das in der Vorlesung gezeigte Vorgehen bzgl. der Definition von
Qualitätseigenschaften und deren Verfeinerung bis hin zu Qualitätsindikatoren.

Das ist meine Antwort:
Die Änderbarkeit von Quellcode beschreibt den Grad, in dem der Quellcode geändert werden kann, ohne die zugrunde liegende Systemarchitektur zu verletzen. Dabei soll der Quellcode keine ungewollten Redundanzen aufweisen und die Code-Komplexität (gemessen an z.B. No-Nesting-Policy) nicht zu hoch sein.
```

##### KI-Antworten: mindestens vier Rückfragen

1. GPT-Astra-6 (Ultra): Wie würdest du für dein fiktives Projekt „Code-Komplexität nicht zu hoch“ so präzisieren, dass zwei unabhängige Prüfende zum gleichen Urteil kommen?
2. GLM-5.3 (high): Was genau müsstest du dafür noch festlegen, damit eine dritte Person – ohne dich befragen zu können – an jedem beliebigen Code-Fragment objektiv entscheiden kann, ob diese Anforderung erfüllt oder verletzt ist?
3. Flint (high): Wie operationalisierst du den von dir beschriebenen „Grad der Änderbarkeit" konkret als Messgröße – und wie genau würdest du anhand deiner Kriterien (Redundanz, No-Nesting-Policy) prüfen, ob eine Änderung die Architektur tatsächlich verletzt?
4. GPT-OSS-120b (high): Welche konkreten Messgrößen bzw. Messverfahren würden Sie aus Ihrer Definition ableiten, um (1) die Gefahr einer Verletzung der Systemarchitektur, (2) ungewollte Redundanzen und (3) die Code‑Komplexität (z. B. durch die No‑Nesting‑Policy) quantifizier‑ und prüfbar zu machen?

##### Überarbeitetes Qualitätsmodell

Die Änderbarkeit von Quellcode beschreibt den Grad, in dem der Quellcode geändert werden kann, ohne die zugrunde liegende Systemarchitektur zu verletzen. Ob die Systemarchitektur verletzt wurde, soll anhand eines Regelwerks, beispielsweise mithilfe von Linting-Regeln, geprüft werden.

Der Grad der Änderbarkeit wird zu gleichen Teilen anhand der Redundanz und der Einhaltung der Nesting-Regel gemessen. Die Redundanz beschreibt dabei, wie viel Prozent des geänderten Codes bereits in gleicher Form existieren. Für die Berechnung gilt folgende Formel:

`Nesting-Boolean * 0,5 + 0,5 * (Anzahl-Geänderte-Redundante-Codezeilen / Anzahl-Geänderte-Codezeilen)`

Der Quellcode soll keine ungewollten Redundanzen aufweisen. Als Kriterium gilt, dass Codeblöcke mit einer Länge von mehr als zehn Zeilen nicht mehrfach vorkommen dürfen. Die Code-Komplexität wird anhand der Verschachtelungstiefe gemessen; diese darf nicht größer als zwei sein.

##### Besonders einflussreiche Rückfragen und Begründung

- Flint: Die Rückfrage hat mir konkret aufgezeigt, worüber ich nachdenken sollte.

#### d) Änderbarkeit bei KI-generiertem Code

##### Prompts

```
Das ist meine Aufgabenstellung:
Aufgabe 1
a) Wie würden Sie „Änderbarkeit von Quellcode“ messbar/prüfbar für ein fiktives Projekt
definieren?
Tipp: Denken Sie an das in der Vorlesung gezeigte Vorgehen bzgl. der Definition von
Qualitätseigenschaften und deren Verfeinerung bis hin zu Qualitätsindikatoren.
b) Welche Maßnahmen würden Sie in Ihrem Team umsetzen, um die Änderbarkeit der
entwickelten Software auch während des Entwicklungsprozesses bereits zu ermöglichen.
c) In vielen Teams erzeugen KI-Coding-Assistenten (z. B. GitHub Copilot,
Cursor, Claude Code) inzwischen einen erheblichen Teil des Quellcodes. Ergänzen Sie Ihre
Maßnahmen aus b):
– Welche Risiken bringt KI-generierter Code für die Änderbarkeit mit sich (z. B.
Duplikate, uneinheitlicher Stil, Code, den im Team niemand wirklich versteht, rechtliche
Fragestellungen)?
– Welche Regeln und Prüfungen würden Sie einführen (z. B. Review-Pflicht, Qualitäts-
Gates in der CI-Pipeline, Architekturregeln, Kennzeichnung KI-generierter
Änderungen)? Begründen Sie Ihre Auswahl.


Das ist meine Antwort zu a)
Die Änderbarkeit von Quellcode beschreibt den Grad, in dem der Quellcode geändert werden kann, ohne die zugrunde liegende Systemarchitektur zu verletzen. Ob die Systemarchitektur verletzt wurde, soll anhand eines Regelwerks, beispielsweise mithilfe von Linting-Regeln, geprüft werden.

Der Grad der Änderbarkeit wird zu gleichen Teilen anhand der Redundanz und der Einhaltung der Nesting-Regel gemessen. Die Redundanz beschreibt dabei, wie viel Prozent des geänderten Codes bereits in gleicher Form existieren. Für die Berechnung gilt folgende Formel:

`Nesting-Boolean * 0,5 + 0,5 * (Anzahl-Geänderte-Redundante-Codezeilen / Anzahl-Geänderte-Codezeilen)`

Der Quellcode soll keine ungewollten Redundanzen aufweisen. Als Kriterium gilt, dass Codeblöcke mit einer Länge von mehr als zehn Zeilen nicht mehrfach vorkommen dürfen. Die Code-Komplexität wird anhand der Verschachtelungstiefe gemessen; diese darf nicht größer als zwei sein.

Das ist meine Antwort zu b)
Ich würde zu Beginn des Projekts, noch bevor Code geschrieben wird, gemeinsam mit dem Team ein Regelwerk festlegen. Dieses soll konkrete Vorgaben dazu enthalten, welche Qualität der Quellcode aufweisen soll und wie diese gemessen wird. Außerdem soll die Verwendung der erarbeiteten Architektur verpflichtend sein.

Bitte erledige c) für mich.
```

##### KI-Antwort (Flint)

```
Risiken: KI-generierter Code birgt insbesondere die Gefahr von Duplikaten und Redundanz (logische Kopien an unterschiedlichen Stellen), uneinheitlichem Stil sowie unübersichtlichen, für das Team unverständlichen Code. Änderungen verteilen sich dadurch auf mehrere Stellen oder werden falsch priorisiert. Zudem können rechtlich und technisch unsaubere Inhalte auftreten.

Maßnahmen:
1. Review-Pflicht: Alle KI-generierten Änderungen müssen durch einen menschlichen Reviewer geprüft werden – bei kritischen Architekturbereichen zusätzlich durch einen Architekten. Begründung: Kein automatischer Filter kann semantische Korrektheit und Domänenverständnis ersetzen.
2. Quality Gates in CI: Vor Merge müssen Lint, Formatierung, Typprüfung, statische Analyse und Tests (inkl. Mindest-Coverage) bestehen. Begründung: Frühe Isolation von Fehlern über die Änderbarkeitsgrenzen.
3. Architekturregeln: Enforce Architektur-Tests / Abhängigkeitsregeln. Begründung: Verhindert, dass KI-Entscheidungen Architektur verletzt oder unübersichtlichen Code erzeugt.
4. Kennzeichnung: Co-authored-by, Label, Dokumentation. Begründung: Nachverfolgbarkeit und klare Verantwortungszuordnung.
```

##### Bewertung
Die genannten Maßnahmen und Risiken sind korrekt, aber unvollständig. Ich hätte ergänzt, dass die KI mitunter Änderungen vornimmt, die über den eigentlichen Auftrag hinausgehen.

Belege: eigene Erfahrung


## Aufgabe 2

### Aufgabenstellung

**a)** Recherchieren Sie den Begriff „Code Smell“, der auf Kent Beck zurückgeht, und erläutern Sie anhand von 5 Beispielen, was mit Code Smell gemeint ist.

**b)** Was sind mögliche Folgen, wenn ein Software-Programm Code Smells enthält?

**c) KI – Werkzeug:** Wählen Sie ein kurzes Programmstück (ca. 60–100 Zeilen) aus einem eigenen früheren Projekt oder einem Open-Source-Projekt. Lassen Sie eine KI darin Code Smells identifizieren und ein Refactoring vorschlagen.

- Analysieren Sie denselben Code mit einem statischen Analysewerkzeug (z. B. SonarQube, PMD, Ruff oder Pylint). Welche Smells finden beide, welche nur eines der Werkzeuge?
- Ordnen Sie die KI-Befunde ein: richtig erkannt / übersehen / falsch-positiv.
- Wie stellen Sie sicher, dass das vorgeschlagene Refactoring das Verhalten des Programms nicht verändert?

### Bearbeitung

#### a) Begriff und fünf Beispiele

##### Definition

Ein Code Smell ist ein Begriff für häufig auftretende Muster in schlecht strukturiertem Code, die keine direkten Fehler darstellen, sondern als Warnzeichen für mangelnde Codequalität gelten.

##### Beispiele

1. Bloaters: Codeblöcke werden zu groß, wodurch das Lesen und Warten des Codes erschwert wird.
   ```

def bestellung_pruefen(bestellung):
    if bestellung:
        if bestellung["kunde"]:
            if bestellung["produkte"]:
                if bestellung["bezahlt"]:
                    if bestellung["adresse"]:
                        if bestellung["lagerbestand"]:
                            print("Bestellung wird versendet")
                        else:
                            print("Nicht auf Lager")
                    else:
                        print("Adresse fehlt")
                else:
                    print("Nicht bezahlt")
            else:
                print("Keine Produkte")
        else:
            print("Kein Kunde")
    else:
        print("Keine Bestellung")

   ```
2. Couplers: Eine Klasse verwendet die internen Felder oder Methoden einer anderen Klasse.
```p
class Kunde:
    def __init__(self):
        self._kontostand = 100

class Bestellung:
    def bezahlen(self, kunde):
        kunde._kontostand -= 50
```
3. Middle Man: Eine Klasse, deren einzige Aufgabe darin besteht, Aufgaben an andere zu delegieren.
```

class Drucker:
    def drucken(self):
        print("Dokument wird gedruckt")

class DruckerManager:
    def __init__(self):
        self.drucker = Drucker()

    def drucken(self):
        self.drucker.drucken()
```
4. Toter Code: Codeelemente, die nicht (mehr) ausgeführt werden.
```

def begruessung():
    print("Hallo!")

    if False:
        print("Willkommen!")

```
5. Functional Abusers: Methoden, die mehr leisten, als ihr Name oder ihr primärer Zweck vermuten lassen.
```

def berechne_preis(produkt):
    preis = produkt["preis"] * 1.19

    datenbank.speichern(produkt)
    email_service.sende_bestaetigung()

    return preis
```

##### Quellen:
- https://www.ibm.com/de-de/think/topics/code-smells
- Die Beispiele stammen von ChatGPT.


#### b) Mögliche Folgen von Code Smells

Schlechte Codequalität => schlechte Wartbarkeit => erhöhte Fehleranfälligkeit

#### c) Codeanalyse und Refactoring

##### Ausgewähltes Programmstück

```
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
```

##### Prompts

Bitte identifiziere alle Code-Smells im mitgegebenen Code und schlage einen refactor vor.

##### Ausschnitt der KI-Antwort

| Code-Smell | Stelle und Problem | Refactoring |
| ---------- | ------------------ | ----------- |
| **Long Method / zu viele Verantwortlichkeiten** | Der Handler übernimmt HTTP, Validierung, Geschäftsregeln, Datenzugriff, Geldtransfer und Preisberechnung. | HTTP-Handler und Kauf-Service trennen; Berechnungen in reine Funktionen auslagern. |
| **Duplicate Code** | Verkäufergutschrift, Käuferbelastung, Unternehmenspreis und Erfolgsantwort stehen in beiden `UserShares`-Zweigen. | Nur die Behandlung des Käuferbestands verzweigen; gemeinsame Schritte einmal ausführen. |
| **Wiederholte Berechnungen und Konvertierungen** | `parseInt(SharesToBuy)` und die Kaufpreismultiplikation werden ständig wiederholt. | Einmal `quantity` und einen verbindlichen `totalPrice` bestimmen. |
| **Uneinheitliche und unklare Namen** | `actual_user`, `UserShares`, `UpdateShare`, `userBuyIn`; `sharesToSell` bezeichnet tatsächlich den Restbestand. | Beispielsweise `buyerId`, `buyerHolding`, `remainingQuantity`, `companyId`. Lokale Variablen einheitlich in `camelCase`. |
| **Magic Numbers und Strings** | `0.001`, `"buy"` sowie mehrfach gleiche Fehlermeldungen. | Preisregel benennen; fachliche Zustände und Fehlercodes zentral definieren. |
| **Überflüssige Verzweigung** | Nach dem zurückkehrenden `if (UserShares)` ist `if (!UserShares)` unnötig. | `if/else` oder einen gemeinsamen Ablauf verwenden. |
| **Dead Code und Scope-Fehler** | Der letzte `newShare.save()`-Block ist unerreichbar. Außerdem ist `newShare` außerhalb seines Blocks nicht verfügbar. | Den gesamten abschließenden Block entfernen. |
| **Unnötige Prüfungen nach `save()`** | `if (!saveShare)` behandelt nicht den normalen Fehlerfall von Mongoose. | Fehler über Exceptions behandeln. Bei Erfolg liefert `save()` das Dokument; bei Fehlern wird das Promise verworfen. Die Nullprüfung nach einer Suche bleibt dagegen sinnvoll. [Mongoose Model API](https://mongoosejs.com/docs/api/model.html) |
| **Unklare Fehlerbehandlung** | Wiederholte generische Fehlertexte, `console.log(error)` ohne Kaufkontext, ungenutztes `next`. | Fachliche Fehlercodes, zentrale HTTP-Fehlerbehandlung und strukturiertes Logging verwenden. |
| **Ungünstige Reihenfolge** | Weitere Datenbankabfragen erfolgen, bevor grundlegende Eingaben und `share` geprüft sind. | Eingaben zuerst validieren; abhängige Daten erst nach erfolgreicher Existenzprüfung laden. |

##### Statisches Analysewerkzeug und Ergebnisse

| Regel | Bereinigter Befund |
| ----- | ------------------ |
| **S3827** | `newShare` wird außerhalb seines Gültigkeitsbereichs verwendet. |
| **S1541** | Zyklomatische Komplexität: **19**, erlaubter Wert: **10**. |
| **S3776** | Kognitive Komplexität: **26**, erlaubter Wert: **15**. |
| **S1192** | Stringliterale werden mehrfach wiederholt. |
| **S1117** | Die innere Variable `saveShare` überschattet die gleichnamige Variable im äußeren Scope. |
| **S3801** | Uneinheitliche Verwendung von `return`. |
| **S1172** | Der Parameter `next` wird nicht verwendet. |
| **S117** | `actual_user` entspricht nicht der konfigurierten Namenskonvention. |
| **S121** | Bei mehreren `if`-Anweisungen fehlen geschweifte Klammern. |
| **S2427** | Bei `parseInt()` fehlt die explizite Zahlenbasis. |
| **S7773** | `Number.parseInt` wird gegenüber `parseInt` bevorzugt. |
| **S1441** | Doppelte statt einfacher Anführungszeichen. |
| **S1131** | Überflüssige Leerzeichen am Zeilenende. |
| **S1537** | Abschließendes Komma wird beanstandet. |
| **S106** | `console.log()` widerspricht der konfigurierten Logging-Regel. |
| **S1438** | Abschließendes Semikolon fehlt. |
| **S113** | Abschließender Zeilenumbruch fehlt. |

##### Vergleich und Einordnung der Befunde

Der Vergleich bezieht sich auf die oben dokumentierten KI-Antworten und die bereitgestellten statischen Befunde. „Nein“ bedeutet, dass der Befund in der jeweiligen Liste nicht genannt wird. „Teilweise“ kennzeichnet eine thematische Überschneidung ohne denselben konkreten Befund.

| Befund | Von KI erkannt? | Vom statischen Analysewerkzeug erkannt? | Anmerkung |
| ------ | --------------- | -------------------------------------- | --------- |
| Zu viele Verantwortlichkeiten im Handler | Ja | Teilweise (S1541, S3776) | |
| Zyklomatische Komplexität über dem Grenzwert | Teilweise | Ja (S1541) | |
| Kognitive Komplexität über dem Grenzwert | Teilweise | Ja (S3776) | |
| Doppelte Abläufe in beiden `UserShares`-Zweigen | Ja | Nein | |
| Wiederholte Berechnungen und Konvertierungen | Ja | Nein | |
| Namenskonvention bei `actual_user` | Ja | Ja (S117) | |
| Weitere uneinheitliche oder unklare Namen | Ja | Nein | |
| Magic Number `0.001` und fachlicher String `"buy"` | Ja | Teilweise (S1192) | |
| Wiederholte Stringliterale bzw. Fehlermeldungen | Ja | Ja (S1192) | |
| Überflüssige Verzweigung `if (!UserShares)` | Ja | Nein | |
| Unerreichbarer abschließender `newShare.save()`-Block | Ja | Nein | |
| `newShare` außerhalb seines Gültigkeitsbereichs | Ja | Ja (S3827) | |
| Unnötige Prüfung von `saveShare` nach `save()` | Ja | Nein | |
| Generische Fehlertexte und fehlender Kaufkontext im Logging | Ja | Teilweise (S1192, S106) | |
| Verwendung von `console.log(error)` | Ja | Ja (S106) | |
| Ungenutzter Parameter `next` | Ja | Ja (S1172) | |
| Datenbankabfragen vor Eingabe- und Existenzprüfung | Ja | Nein | |
| Überschattung der Variable `saveShare` | Nein | Ja (S1117) | |
| Uneinheitliche Verwendung von `return` | Nein | Ja (S3801) | |
| Fehlende geschweifte Klammern bei `if`-Anweisungen | Nein | Ja (S121) | |
| Fehlende explizite Zahlenbasis bei `parseInt()` | Nein | Ja (S2427) | |
| Bevorzugung von `Number.parseInt` gegenüber `parseInt` | Nein | Ja (S7773) | |
| Doppelte statt einfacher Anführungszeichen | Nein | Ja (S1441) | |
| Überflüssige Leerzeichen am Zeilenende | Nein | Ja (S1131) | |
| Beanstandetes abschließendes Komma | Nein | Ja (S1537) | |
| Fehlendes abschließendes Semikolon | Nein | Ja (S1438) | |
| Fehlender abschließender Zeilenumbruch | Nein | Ja (S113) | |

##### Absicherung des Verhaltens beim Refactoring

Durch Tests, die die Funktionalität überprüfen, soll festgestellt werden, dass das Verhalten des Programms nicht unbeabsichtigt verändert wird.

## Aufgabe 3

### Aufgabenstellung

Recherchieren Sie mindestens drei Metriken zur Bewertung von Softwareentwicklungen. Metriken können sowohl die Produkt- als auch die Prozessebene betreffen.

**a)** Nennen Sie jeweils deren Anwendungsgebiet, Berechnungsvorschrift und Interpretation.

**b)** Erläutern Sie jeweils, wie die gefundenen Metriken im Rahmen einer Software-(System-)Entwicklung sinnvoll eingesetzt werden können.

### Bearbeitung

#### Metrik 1: Change lead time

##### a) Anwendungsgebiet, Berechnungsvorschrift und Interpretation

- **Anwendungsgebiet:** Bewertung der Update-Durchlaufzeit
- **Berechnungsvorschrift:** Zeit vom Commit bis zur Inbetriebnahme
- **Interpretation:** Eine kürzere Change Lead Time bedeutet, dass Code schneller in Betrieb genommen wird.

##### b) Sinnvoller Einsatz in der Entwicklung

- Die Metrik sollte vor allem bei Fehlerkorrekturen in der Entwicklung minimiert werden, damit Fehler so schnell wie möglich behoben werden.

#### Metrik 2: Deployment frequency

##### a) Anwendungsgebiet, Berechnungsvorschrift und Interpretation

- **Anwendungsgebiet:** Bewertung der Deployment-Häufigkeit
- **Berechnungsvorschrift:** Anzahl der Deployments pro Woche/Monat/Jahr
- **Interpretation:** Eine höhere Frequenz bedeutet regelmäßige Updates.

##### b) Sinnvoller Einsatz in der Entwicklung

- Die Metrik sollte stabil auf einem mit den Stakeholdern festgelegten Niveau gehalten werden.

#### Metrik 3: Change fail rate

##### a) Anwendungsgebiet, Berechnungsvorschrift und Interpretation

- **Anwendungsgebiet:** Bewertung der Deployment-Qualität
- **Berechnungsvorschrift:** Fehlerhafte Deployments / alle Deployments
- **Interpretation:** Eine niedrige Quote spricht für stabile Deployments.

##### b) Sinnvoller Einsatz in der Entwicklung

- Die Metrik sollte als Warnsignal interpretiert werden. Ein Anstieg der Quote könnte auf eine geringe Softwarequalität hindeuten.

#### Quellen

- https://dora.dev/guides/dora-metrics/

## Aufgabe 4

### Aufgabenstellung

**a)** Erläutern Sie den Unterschied zwischen Testen und Debugging.

**b)** Definieren und erläutern Sie die Begriffe Verifizierung und Validation.

**c)** Definieren und erläutern Sie die Begriffe Qualitätssicherung und Qualitätssteuerung.

### Bearbeitung

#### a) Testen und Debugging

Testen hat das Ziel, einen Fehlerzustand aufzudecken. Debugging dient dazu, die Ursache des Fehlerzustands zu finden und zu beheben.

#### b) Verifizierung und Validation

Verifizierung: Der Prozess der Bestätigung, dass ein Arbeitsergebnis seine Spezifikation erfüllt.

Validierung: Bestätigung durch Überprüfung, dass ein Arbeitsergebnis den Bedürfnissen eines Stakeholders entspricht.

Ein Ergebnis kann verifiziert werden, also seinen Spezifikationen entsprechen, beispielsweise ein Auto, das entsprechend seiner Spezifikation gebaut wurde. Die Validierung kann jedoch fehlschlagen, weil die Stakeholder einen Verbrenner wollten, aber ein Elektroauto geliefert wurde.

#### c) Qualitätssicherung und Qualitätssteuerung

Qualitätssicherung: Aktivitäten, die darauf abzielen, Vertrauen in die Erfüllung der Qualitätsanforderungen zu schaffen.

Qualitätssteuerung: Aktivitäten, die der Bewertung der Qualität einer Komponente oder eines Systems dienen.

Qualitätssicherung schafft durch eigene Prozesse Vertrauen in die Erfüllung der Qualitätsanforderungen, z. B. durch die Vorgabe, jede Softwareänderung zu testen. Qualitätssteuerung bewertet die Qualität beispielsweise durch Tests, die prüfen, ob eine geänderte Funktion das richtige Ergebnis liefert.

#### Quelle

Quelle: International Software Testing Qualifications Board (ISTQB®), ISTQB® Glossary

## Aufgabe 5

### Aufgabenstellung

Beschreiben Sie die folgenden Qualitätsmerkmale der ISO 25010 mit Bezug auf das Beispiel einer Online-Banking-App, wie in der Vorlesung vorgestellt:

**a)** Modularität (Submerkmal der Wartbarkeit)

**b)** Wiederverwendbarkeit (Submerkmal der Wartbarkeit)

**c)** Zeitverhalten (Submerkmal der Performanz)

Gehen Sie dabei jeweils auf folgende Punkte ein:

- Was bedeutet das Qualitätsmerkmal allgemein?
- Wie zeigt es sich konkret im Beispiel einer Online-Banking-App?
- Was wären positive bzw. negative Ausprägungen am Beispiel der Online-Banking-App?

**d) KI – Werkzeug:** Lassen Sie eine KI drei Qualitätsanforderungen zum Zeitverhalten der Online-Banking-App formulieren.

- Prüfen Sie jede Anforderung: Ist sie messbar und prüfbar (Messgröße, Zielwert, Lastsituation, Messpunkt)? Ist sie realistisch?
- Verbessern Sie mindestens eine Anforderung und begründen Sie die Änderung.

**e) KI – sokratisch:** Legen Sie Ihre Antworten zu a) und c) einer KI im sokratischen Modus vor. Die KI soll Ihnen Fragen stellen, die einen möglichen Zielkonflikt zwischen Modularität und Zeitverhalten sichtbar machen. Beschreiben Sie den Zielkonflikt anschließend in eigenen Worten und skizzieren Sie, wie Sie ihn in der App auflösen würden.

### Bearbeitung

#### a) Modularität

- **Allgemeine Bedeutung:** …
- **Bezug zur Online-Banking-App:** …
- **Positive Ausprägung:** …
- **Negative Ausprägung:** …

#### b) Wiederverwendbarkeit

- **Allgemeine Bedeutung:** …
- **Bezug zur Online-Banking-App:** …
- **Positive Ausprägung:** …
- **Negative Ausprägung:** …

#### c) Zeitverhalten

- **Allgemeine Bedeutung:** …
- **Bezug zur Online-Banking-App:** …
- **Positive Ausprägung:** …
- **Negative Ausprägung:** …

#### d) Qualitätsanforderungen zum Zeitverhalten prüfen

##### Prompts

-

##### Ausschnitt der KI-Antwort: drei Qualitätsanforderungen

1. …
2. …
3. …

##### Prüfung der Anforderungen

| Anforderung | Messgröße | Zielwert | Lastsituation | Messpunkt | Messbar und prüfbar? | Realistisch? Begründung |
| ----------- | --------- | -------- | ------------- | --------- | ------------------- | ---------------------- |
| 1           | …         | …        | …             | …         | …                   | …                      |
| 2           | …         | …        | …             | …         | …                   | …                      |
| 3           | …         | …        | …             | …         | …                   | …                      |

##### Verbesserte Anforderung und Begründung

-

##### Eigene Bewertung (3–5 Sätze)

-

#### e) Zielkonflikt zwischen Modularität und Zeitverhalten

##### Prompts

-

##### Ausschnitt der KI-Antwort

-

##### Zielkonflikt in eigenen Worten

-

##### Skizze zur Auflösung in der App

-

##### Eigene Bewertung (3–5 Sätze)

-
