# Passender Aufwand für Softwarequalität

Eine eigenständige neue HTML-Präsentation mit fünf sofort vollständig sichtbaren Inhaltsfolien. Weiße Fläche, Georgia-Titel, Arial/Helvetica-Text, Petrol und Senfgelb. Keine externen Bibliotheken, Webfonts, Bilder, Animationen oder benötigten Buildschritte.

## Überarbeitung des roten Fadens

Stand: 27.10.2026. Nach der Kritik an der Verständlichkeit hat ein neuer Autoragent die Argumentation überarbeitet. Er erhielt den Originalauftrag und den aktuellen Arbeitsordner, las die bestehende Fassung und die verbindlichen Layoutregeln, aber keine ältere Nachbarpräsentation oder früheren Agentenberichte. Ein separater Kritiker untersuchte zunächst unabhängig den Ausgangsstand und anschließend die Überarbeitung. Seine Hinweise zum passenden Versandkostenfall, zur Unterscheidung zwischen Fachregel- und Programmänderungen sowie zu den Automatisierungsbedingungen im Pilot wurden eingearbeitet. In der abschließenden gezielten Prüfung sah er keine weiteren konkreten Verständlichkeitsbrüche. Das ist eine Agentenprüfung, kein Test mit menschlichen Zuhörern.

Verbindliche Gestaltungsgrundlage: [Layoutkonzept vom 26.10.2026](/home/tim/Desktop/fachhochschule-gitlab/7-semester/statistics-and-learning-theory/layout/LAYOUTKONZEPT.md). Der dortige Bausteinkatalog dient als Auswahl, nicht als Pflichtschema für jede Folie.

Die Leitfrage steht auf der ersten Folie: **Wo setzen wir unsere knappe QS-Zeit ein?** Eine erfundene Rabattfunktion trägt den gesamten Vortrag. Zuerst zeigt sie mögliche Nacharbeit durch späte Klärung. Danach folgen frühe gemeinsame Erwartungen, eine begründete Auswahl der Prüftiefe und die Entscheidung über wiederholte Prüfungen. Der Pilot übernimmt genau diese Maßnahmen. Er soll eine Grundlage für die nächste Aufwandsentscheidung schaffen.

## Öffnen

`index.html` lokal im Browser öffnen. Die Dateien funktionieren offline. Alternativ den gesamten Ordner mit einem gewöhnlichen lokalen Webserver bereitstellen. Alle Dateien müssen zusammenbleiben.

## Vortragen

- Pfeil rechts/unten oder Bild ab: nächste Folie.
- Pfeil links/oben oder Bild auf: vorherige Folie.
- Q: Kapitel, Nachlese, Quellen und Links zu den Lesefassungen.
- H: Hilfe.
- N: private Sprecheransicht in einem separaten Fenster.
- F: Vollbild ein-/ausschalten, soweit der Browser dies unterstützt.
- Esc: offenen Dialog oder Vollbild schließen.

Die Navigation endet bei der ersten und letzten Folie. Es gibt keine unsichtbaren Reveals. Eingabefelder behalten ihre eigene Tastaturbedienung. Dialoge lassen sich mit Tab bedienen und mit Esc schließen.

Die Sprecheransicht sollte nur auf dem privaten Bildschirm stehen. Wird nur ein Fenster geteilt, das Präsentationsfenster auswählen. Ein Popup-Blocker kann das Öffnen mit N verhindern. Ein direkter Link ist über Q oder die Hilfe erreichbar.

## Fassungen

- `index.html`: Vortrag mit Tastaturnavigation und nativen Dialogen.
- `statisch.html`: eigenständige, skriptfreie Fassung aller fünf Folien mit vollständiger Nachlese und Quellen.
- `sprechfassung.html`: vollständiges Manuskript, auch ohne JavaScript lesbar. Die Dauer ist noch nicht durch eine Sprechprobe bestätigt.
- `sprecher.html`: private Ansicht aller Sprechtexte, mit JavaScript folienweise auswählbar. Ohne JavaScript stehen alle Notizen untereinander. Sie funktioniert unabhängig vom Präsentationsfenster.
- `styles.css`, `app.js`, `sprecher.js`, `notes.js`: lokale Gestaltung, Bedienung und Notizdaten.

Wenn die Sprecheransicht über N geöffnet wurde, synchronisieren sich die ausgewählte Folie und die Notizen in beide Richtungen. Nur die jeweils bekannten Fenster können die Kopplung steuern. Ohne Kopplung bleiben die Notizen selbstständig auswählbar. Die vollständige Sprechfassung bleibt immer als eigener Link erreichbar.

## Fünf Erkläraufgaben und Kompositionen

1. **Leitfrage mit Beispiel:** Eine kurz vor der Freigabe entdeckte Mehrdeutigkeit der Rabattregel kann Nacharbeit auslösen. Die Zeitfrage wird dadurch konkret.
2. **Prozessfolge:** Die gleiche Regel vor dem Code gemeinsam prüfen, eine Erwartung vereinbaren und knappe Grenzfälle festhalten. Technische Testdetails folgen bei stabilerer Lösung. Bei geänderter Fachregel passen wir die Beispiele an. Der Versandkostenfall beantwortet die Eingangsfrage sichtbar.
3. **Offene Vergleichstabelle:** Zwei Fehler derselben Rabattfunktion erklären, weshalb Wahrscheinlichkeit und Folgen unterschiedliche Prüftiefe begründen. Diese Auswahl steht vor der Automatisierungsfrage.
4. **Vergleich der Wiederholung:** Nach Programmänderungen prüfen wir die wichtigen Grenz- und Versandfälle bei unveränderter Fachregel erneut, von Hand oder automatisch. Aufbau und Pflege gehen in die Entscheidung ein.
5. **Pilot mit Bitte:** Den nächsten Rabattauftrag mit genau diesen Maßnahmen erproben. Tatsächlichen Aufwand und Rückmeldungen auswerten und über Fortsetzung entscheiden.

Die Sprechtexte stellen bei jedem Folienwechsel die offene Anschlussfrage oder den nächsten Schritt her. Die sichtbaren Folien tragen dieselbe Folge auch ohne die Notizen.

## Fachliche Grundlage

ISTQB, *Certified Tester Foundation Level Syllabus v4.0.1*, 15.09.2024:

https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf

Verwendete Abschnitte: 1.2.1–1.2.2, 1.3, 2.1.2, 2.1.5–2.1.6, 2.2.3, 3.1, 4.5.2, 5.2 und 6.2. Die Zuordnung zu jeder Folie steht in der Nachlese und den Sprechtexten. Der Online-Link benötigt Internet, die vollständigen Vortragsinhalte dagegen nicht.

Der Auftrag, die vereinbarte Rabattregel und die Risikoeinschätzungen sind eigene Beispiele. Zwei Wochen, der nächste Rabattauftrag und insgesamt 20 Teamstunden sind eigene Planungsannahmen für den Pilot. Sie belegen keine Einsparung und legen keinen dauerhaft ausreichenden QS-Aufwand fest. Ein ausgeschöpftes Budget ersetzt keine notwendigen Prüfungen und rechtfertigt keine Freigabe bei unvertretbaren offenen Risiken.

## Kleine Fenster und Druck

Bei geringer Breite oder Höhe darf die Seite vertikal scrollen. Inhalte werden nicht auf die Fensterhöhe abgeschnitten.

Das Druck-CSS zielt auf fünf Seiten im A4-Querformat, je eine Seite pro Folie. Im Druckdialog A4, Querformat und möglichst keine Browser-Kopf-/Fußzeilen auswählen. Die Nachlese wird beim Drucken der Folien ausgeblendet. Die Sprechfassung lässt sich separat drucken. Das Druck-CSS ist kein bestätigter PDF-Export.

## Bearbeiten

Die fertigen Dateien sind direkt les- und editierbar. `create.py` ist lediglich das verwendete lokale Autorenskript für die inhaltlich übereinstimmenden HTML-Lesefassungen und Notizdaten. Es ist zum Vortragen nicht erforderlich und führt keine Netzabfragen durch. Änderungen an CSS und Bedienung liegen direkt in den jeweiligen Dateien.


## Prüfung dieses Überarbeitungsstands

Geprüft am 27.10.2026: Python-Syntax des Generators und JavaScript-Syntax, fünf identische Folien in Vortrags- und statischer Fassung, eindeutige IDs und alle lokalen Link- und Ankerziele. Die fünf Notiztitel stimmen in allen Fassungen überein. Das Manuskript umfasst 892 Wörter.

Die überarbeiteten Folien wurden im Browser bei 1280 × 720 geprüft. Alle fünf passen in diese Fläche. Der zusätzliche vertikale Überlauf der zweiten Folie bei 1600 × 900 wurde über die Abstände behoben und nachgemessen. Bei 390 × 844 haben alle fünf Folien keinen horizontalen Seitenüberlauf; längere Folien bleiben vertikal scrollbar. Die geänderten Folien wurden visuell kontrolliert, der Tastaturwechsel zur Pilotfolie geprüft. `vorschau.jpg` zeigt die zweite Folie vor der anschließenden Überarbeitung der unteren Hinweisblöcke und ist keine aktuelle Vorschau mehr. Die Popup-Synchronisation der Sprecheransicht, ein PDF-Export und die Vortragsdauer wurden in dieser Überarbeitung nicht erneut praktisch geprüft.


## Untere Hinweisblöcke überarbeitet

Stand: 27.10.2026. Für jeden unteren Textblock geprüft, ob er neue Information beiträgt und ob diese direkt zum Hauptinhalt gehört.

- Folie 1: Die mögliche Nacharbeit steht direkt beim Rabattbeispiel. Die wiederholende Aussage zu fehlender QS-Zeit entfällt.
- Folie 2: Frühe QS steht im Titel. Das Anpassen der Beispiele bei geänderter Fachregel steht beim dritten Schritt. Technische Testdetails bleiben in den Sprechtexten.
- Folie 3: Der untere Absatz entfällt, da die Tabelle die Priorisierung bereits erklärt.
- Folie 4: Einstieg, stabile Regel und häufige Wiederholung stehen direkt bei der Automatisierung. Die erneute gemeinsame Klärung neuer Fragen bleibt im Sprechtext und ist bereits Thema der zweiten Folie.
- Folie 5: Das Budget ist am Betrag als Pilotvorschlag erkennbar. Die Auswertung steht direkt beim Zeitraum; notwendige Prüfungen stehen im Maßnahmenblock. Das Vorgehen am Budgetlimit bleibt in den Sprechtexten. Nur die konkrete Bitte um Freigabe und Benennung einer verantwortlichen Person bleibt als Abschluss unten.

Vortragsfassung und statische Fassung wurden gemeinsam regeneriert; die Notiztitel sind synchronisiert. Geprüft: Python-Syntax, fünf identische Folien in beiden Fassungen, eindeutige IDs, lokale Link- und Ankerziele, Notiztitel und entfernte Fußblöcke. Die bisherigen Browsermessungen gelten für den vorherigen Stand. Eine erneute visuelle Browserprüfung war wegen der Sicherheitsrichtlinie für lokale Datei-URLs nicht möglich. Die vorhandene Vorschau wurde nicht aktualisiert.
