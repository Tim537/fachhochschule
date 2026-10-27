# Aufgabe 3 - Unabhängige Entwürfe und Prüfung

## Auftrag und Vorgehen

Drei Agenten haben unabhängig voneinander Inhalte für einen Kurzvortrag mit fünf Folien erarbeitet. Sie haben die anderen Entwürfe nicht gelesen. Anschließend erhalten drei weitere Agenten denselben Entwurfssatz zur unabhängigen Kritik. Die Folienvorbereitung wird danach in `1_aufgabe.md` zusammengeführt.

Auftrag: Mitarbeitende und Unternehmensführung zu angemessenem Aufwand für Software-Qualitätssicherung überzeugen. Vier Einwände: keine Zeit für Automatisierung; frühe Testvorbereitung verursacht Änderungen; erst entwickeln, dann testen; kein Geld und keine Zeit für QS.

## Entwurf 1

### Folie 1: Qualitätssicherung hält Lieferung und Risiko im Gleichgewicht

- QS braucht Zeit - Fehlersuche und Nacharbeit ebenfalls.
- Geschäftskritische Fehler verdienen mehr Aufmerksamkeit als kosmetische Mängel.
- Ziel: ausreichende Sicherheit für die nächste Auslieferung.

Sprechernotiz: QS soll nicht jede denkbare Abweichung verhindern. Wir entscheiden bewusst, welche Fehler besonders schaden würden und welche Prüfungen dafür angemessen sind. Mitarbeitende profitieren von verständlichen Erwartungen, die Führung von transparenten Freigaberisiken. Einen festen, für alle Projekte richtigen QS-Anteil gibt es daraus nicht.

### Folie 2: Früh vorbereiten heißt Annahmen prüfen

- Frühe Testideen machen unklare Anforderungen sichtbar.
- Zunächst Beispiele und Akzeptanzkriterien, anschließend detaillierte Tests.
- Bei Änderungen Testvorbereitung gezielt anpassen.

Sprechernotiz: Zum Einwand „Frühe Testvorbereitung erzeugt Änderungen“: Ja, vorbereitete Tests können später geändert werden müssen. Deshalb schreiben wir bei unsicheren Anforderungen zunächst wenige verständliche Beispiele. Wenn diese einen Widerspruch aufdecken, können wir die Entscheidung vor ihrer Umsetzung klären. Aufwendige Automatisierung folgt dort, wo Verhalten und Schnittstellen ausreichend klar sind.

### Folie 3: Automatisierung dort, wo Wiederholung Aufwand rechtfertigt

- Häufige, stabile und wichtige Prüfungen zuerst automatisieren.
- Erstellung, Wartung und Auswertung kosten dauerhaft Zeit.
- Neue und schwer beschreibbare Risiken auch manuell untersuchen.

Sprechernotiz: Zum Einwand „Für Testautomatisierung haben wir keine Zeit“: Nicht jeder Test muss automatisiert werden. Ein kleiner automatischer Regressionstest für häufig veränderte Kernlogik kann wiederholte Handarbeit unterstützen. Ob er sich lohnt, hängt von Wiederholung, Änderungsrate und Wartungsaufwand ab. Wir beginnen mit wenigen geeigneten Fällen und überprüfen den tatsächlichen Nutzen.

### Folie 4: Prüfen während der Entwicklung erleichtert die Rückmeldung

- Kleine Änderungen mit passenden Prüfungen verbinden.
- Fehler untersuchen, solange der Änderungskontext noch präsent ist.
- Gesamtsystem vor der Freigabe zusätzlich prüfen.

Sprechernotiz: Zum Einwand „Erst kräftig entwickeln, dann testen“: Bei einem großen Änderungspaket kommen viele mögliche Fehlerursachen zusammen. Rückmeldung nach kleinen Schritten kann die Eingrenzung erleichtern. Das ersetzt die abschließenden Integrations- und Systemtests nicht. Sinnvoll sind beispielsweise klare Akzeptanzkriterien, ein Review und gezielte Tests für die jeweilige Änderung.

### Folie 5: Mit begrenztem Budget einen überprüfbaren Anfang machen

- Eine risikoreiche Funktion für einen Pilot auswählen.
- Prüfaufwand und Nacharbeit gemeinsam sichtbar machen.
- Nach dem Pilot über Ausbau oder Anpassung entscheiden.

Sprechernotiz: Zum Einwand „Weder Zeit noch Geld für QS“: Auch ein kleiner Einstieg beansprucht Kapazität; dafür müssen andere Arbeiten gegebenenfalls zurückgestellt werden. Vorschlag für die nächste Iteration: Für eine ausgewählte Kernfunktion Akzeptanzbeispiele, ein Review und wenige geeignete Tests vereinbaren. Aufwand, gefundene Probleme und Wartung festhalten. Danach entscheiden Team und Führung anhand dieser Erfahrungen über den nächsten Schritt.

## Entwurf 2

### Folie 1: Qualitätssicherung macht Lieferungen verlässlicher

- Fehler können Nutzung, Termine und Vertrauen beeinträchtigen.
- QS umfasst klare Anforderungen, Reviews und Tests.
- Der Aufwand richtet sich nach Risiko und Bedeutung.

Sprechernotiz: Angemessene QS bedeutet, unsere begrenzte Zeit gezielt einzusetzen. Mitarbeitende brauchen verständliche Erwartungen und Rückmeldung; die Führung braucht eine nachvollziehbare Grundlage für die Freigabe. Vollständige Fehlerfreiheit können wir damit nicht versprechen.

### Folie 2: „Für Testautomatisierung haben wir keine Zeit“

- Automatisierung benötigt Aufbau und laufende Pflege.
- Häufige, stabile und wichtige Prüfungen zuerst automatisieren.
- Neue oder wechselnde Funktionen zusätzlich manuell erkunden.

Sprechernotiz: Nicht jeder Test lohnt sich als automatisierter Test. Bei wiederholten Prüfungen kann Automatisierung Arbeit abnehmen; bei einmaligen oder stark veränderlichen Abläufen kann ihre Pflege mehr kosten als sie spart. Wir wählen deshalb gezielt aus und berücksichtigen den Aufwand ausdrücklich in der Planung.

### Folie 3: „Frühe Testvorbereitung erzeugt doch nur Änderungen“

- Akzeptanzbeispiele machen unklare Erwartungen sichtbar.
- Früh das erwartete Verhalten klären, Details später ausarbeiten.
- Änderungen an Anforderungen und Tests gemeinsam einplanen.

Sprechernotiz: Der Einwand ist berechtigt, wenn wir zu früh sämtliche Details festschreiben. Wir können zunächst wenige konkrete Beispiele besprechen: Was soll bei einer normalen Eingabe passieren, was bei einem Fehler? Diese Vorbereitung kann Unklarheiten zeigen. Ändert sich später eine Anforderung, müssen passende Tests ebenfalls angepasst werden.

### Folie 4: „Erst kräftig entwickeln, dann testen“

- Kleine Arbeitsschritte entwickeln, prüfen und besprechen.
- Fehlerhinweise nutzen, solange der Zusammenhang noch präsent ist.
- Abschließende Systemtests und Freigabe bleiben erforderlich.

Sprechernotiz: Wer sämtliche Prüfungen ans Projektende verschiebt, erhält auch deren Rückmeldung erst dann. Änderungen müssen anschließend in bereits aufgebauten Zusammenhängen umgesetzt werden. Kurze Prüfzyklen unterstützen die Entwicklung; sie ersetzen jedoch weder das Zusammenspiel der Komponenten noch die Prüfung des vollständigen Produkts.

### Folie 5: „Für QS fehlen Zeit und Geld“: begrenzt anfangen

- Gemeinsam einen geschäftskritischen Ablauf auswählen.
- Akzeptanzbeispiele, Review und wenige wiederholbare Tests erproben.
- Aufwand und Nutzen auswerten; anschließend über den Ausbau entscheiden.

Sprechernotiz: QS kostet Zeit und Geld; Fehlerbehebung und Störungen ebenfalls. Wir schlagen deshalb einen begrenzten Versuch für einen wichtigen Ablauf vor. Das Team vereinbart dafür Aufwand und Verantwortlichkeit. Danach betrachten wir beispielsweise Pflegeaufwand, hilfreiche Fehlerfunde und den Aufwand wiederholter Prüfungen. Die Führung entscheidet auf dieser Grundlage, ob und wo wir weiter investieren.

## Entwurf 3

### Folie 1: Qualität braucht einen bewussten Aufwand

- Fehler gefährden Kundennutzen, Termine und Vertrauen.
- Qualitätssicherung umfasst klare Anforderungen, Reviews und Tests.
- Aufwand nach Risiko wählen: Was wäre bei einem Fehler besonders teuer?

Sprechernotiz: Unser Ziel ist weder Fehlerfreiheit um jeden Preis noch möglichst viel Testaktivität. Wir wollen mit begrenztem Aufwand die wichtigsten Risiken senken. Deshalb unterscheiden wir kritische Funktionen von Bereichen, in denen ein Fehler leichter zu verkraften ist.

### Folie 2: Frühe Testvorbereitung schafft Klarheit

- Schon bei Anforderungen konkrete Erfolgs- und Fehlerbeispiele sammeln.
- Nur so weit vorbereiten, wie die Anforderungen belastbar sind.
- Beispiele bei Änderungen gemeinsam mit den Anforderungen anpassen.

Sprechernotiz: Der Einwand „Frühe Vorbereitung erzeugt später Änderungen“ ist berechtigt: Testmaterial muss gepflegt werden. Deshalb schreiben wir früh keine umfangreichen, detaillierten Testskripte für unsichere Funktionen. Wenige Beispiele helfen zunächst, unterschiedliche Erwartungen sichtbar zu machen. Änderungen bleiben möglich; sie werden bewusster entschieden.

### Folie 3: Automatisierung gezielt investieren

- Einrichtung und Pflege kosten Entwicklungszeit.
- Kandidaten: häufig wiederholte Prüfungen wichtiger, stabiler Abläufe.
- Neue oder wechselhafte Funktionen auch manuell erkunden.

Sprechernotiz: „Keine Zeit für Testautomatisierung“ beschreibt einen realen Zielkonflikt. Automatisierung ist sinnvoll, wenn die wiederholte Prüfung und ihre Bedeutung den Erstellungs- und Pflegeaufwand rechtfertigen. Wir beginnen klein und prüfen, ob die ausgewählten Tests im Alltag tatsächlich helfen. Ein instabiler Test, dessen Ergebnis ständig untersucht werden muss, kann mehr Aufwand schaffen als sparen.

### Folie 4: Entwickeln und Prüfen in kleinen Schritten

- Kleine Funktionspakete entwickeln, prüfen und integrieren.
- Reviews und Tests geben vor dem nächsten Ausbau Rückmeldung.
- Am Ende weiterhin das Zusammenspiel und die Nutzung prüfen.

Sprechernotiz: „Erst kräftig entwickeln, dann testen“ verschiebt Rückmeldung ans Projektende. Dann können Fehler mehrere Funktionen betreffen und mit anderen Änderungen zusammenfallen. Kleine Schritte begrenzen den Bereich, in dem wir suchen und korrigieren müssen. Die laufende Prüfung ersetzt jedoch weder abschließende Systemtests noch die fachliche Abnahme.

### Folie 5: Mit begrenztem Budget konkret anfangen

- Ein wichtiges Funktionspaket als Pilot auswählen.
- Akzeptanzbeispiele, Review und ausgewählte Tests fest einplanen.
- Danach Aufwand, gefundene Probleme und Nacharbeit bewerten.

Sprechernotiz: Wenn Zeit und Geld knapp sind, müssen wir Prioritäten setzen. Die Führung entscheidet mit, welche Risiken tragbar sind und welcher QS-Aufwand dafür eingeplant wird. Unser nächster Schritt: Für das nächste Funktionspaket wählen Fachseite, Entwicklung und Führung gemeinsam die wichtigsten Risiken und passende Prüfungen aus. Nach dem Paket bewerten wir den Nutzen einschließlich Pflegeaufwand und passen das Vorgehen an.

## Kritiken und Überarbeitung

Die folgenden Abschnitte fassen die drei unabhängig eingegangenen Kritiken zusammen. Jeder Kritiker erhielt alle drei Entwürfe, ohne die Urteile der anderen Kritiker zu lesen. Die Übereinstimmung der Agenten ersetzt keine Quellenprüfung.

### Kritiker 1 - Zusammenfassung

- Bevorzugt Entwurf 2 wegen der sichtbaren Zuordnung zu allen vier Einwänden und der breiten Einordnung von QS.
- Hauptmangel aller Entwürfe: keine konkret entscheidbare Führungsbitte mit Budget, Zuständigkeit und Termin.
- Messung präzisieren: Erstellungs-, Ausführungs-, Analyse- und Pflegeaufwand sowie bedeutsame Befunde statt bloßer Fehlerzahlen. Ein kurzer Pilot beweist keine langfristigen Einsparungen.
- Frühe QS ohne ausführbaren Code ausdrücklich erklären; Eintrittswahrscheinlichkeit und Schadensausmaß berücksichtigen.
- Aus Entwurf 1 den realen Kapazitätskonflikt übernehmen; aus Entwurf 3 gemeinsame Risikoauswahl und fachliche Abnahme.
- Automatisierung auch für veränderliche, kritische Funktionen erwägen; manuelle Erkundung ist eine Ergänzung.

### Kritiker 2 - Zusammenfassung

- Bevorzugt Entwurf 2, ergänzt um die gemeinsame Risikoentscheidung aus Entwurf 3.
- Konkreter Pilot als ausdrücklich eigene Planungsannahme: nächste zweiwöchige Iteration, zwei Personentage, Teamleitung verantwortlich, Auswertung am Iterationsende.
- Vorbereitungs-, Durchführungs-, Analyse- und Pflegeaufwand getrennt betrachten. Wiederholungsaufwand nur für vergleichbare Prüfungen vergleichen.
- Geprüfte und offene Risiken dokumentieren; Fehlerfunde allein sind kein Nachweis für Qualität oder Wirtschaftlichkeit.
- Frühe Anforderungs- und Entwurfsprüfung benötigt keinen ausführbaren Code. Seltene, folgenschwere Fehler dürfen bei der Priorisierung nicht verdrängt werden.
- Die fünf Folien sind realistisch, Garantien und erfundene Belege wurden nicht festgestellt.

### Kritiker 3 - Zusammenfassung

- Bevorzugt Entwurf 2 mit den Automatisierungsgrenzen aus Entwurf 3.
- Hauptpriorität ist eine entscheidbare Ressourcenbitte mit Kapazitätsgrenze, verantwortlicher Rolle, Termin und Entscheidung über Fortsetzung, Anpassung oder Abbruch.
- Risiko umfasst Wahrscheinlichkeit und Folgen; die Folgen dürfen nicht allein auf Geld reduziert werden.
- Befunde nach Bedeutung, untersuchten Risiken und Aufwand beurteilen. Keine vermiedenen Kosten ohne Vergleichsdaten behaupten.
- Zwischen verändertem Code und verändertem Sollverhalten unterscheiden: Eine Berechnungsregel kann trotz Codeänderungen stabil bleiben.
- „Kleine Schritte können die Fehlereingrenzung erleichtern“ statt einer uneingeschränkten Wirkungszusage verwenden.

### Zusammenführung durch den Hauptagenten

| Prüfbefund | Umsetzung in der Vorbereitung |
| ---------- | ----------------------------- |
| Alle vier Einwände sichtbar adressieren | Entwurf 2 als Grundstruktur; Folien 2 bis 5 greifen jeweils einen Einwand auf. |
| QS breiter als Testausführung darstellen | Folie 1 nennt Anforderungsklärung, Reviews und Tests; Folien 3 und 4 behandeln frühe Prüfung. |
| Argumente für die angenommene Firma konkretisieren | Durchgehendes Beispiel Bestellabschluss mit Betrag, Rabattregel und Gesamtablauf. |
| Risikoorientierung präzisieren | Wahrscheinlichkeit und Fehlerfolgen nennen; keine pauschale QS-Quote behaupten. |
| Automatisierungskosten und Grenzen berücksichtigen | Aufwand für Erstellung, Ausführung, Auswertung und Pflege; manuelle Ergänzung und keine Fehlerfreiheitsgarantie. |
| Führungsentscheidung konkret machen | Zweiwöchige Iteration und zwei Personentage als ausdrückliches Planungsbeispiel; Führung reserviert Kapazität, Teamleitung koordiniert, Fachseite bestimmt Akzeptanzkriterien. |
| Erfolg nicht mit Fehlerzahlen gleichsetzen | Aufwand, bedeutende Befunde und geprüfte/offene Risiken auswerten; kurzer Pilot beweist keine langfristige Rentabilität. |
| Prüfungen am Ende weiter vorsehen | Integrationstests, Systemtests und fachliche Abnahme bleiben Teil des Vorgehens. |

Die Folieninhalte wurden mit dem [offiziellen ISTQB-CTFL-Lehrplan v4.0.1](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf) abgeglichen, insbesondere Abschnitte 1.3, 2.1, 2.2, 3.1, 4.5.2, 5.2 und 6.2. Die Pilotgröße und das Firmenbeispiel sind eigene Vorschläge, keine empirisch belegten Optimalwerte.

Die zusammengeführte Vorbereitung steht in [Aufgabe 3 der Ausarbeitung](1_aufgabe.md#aufgabe-3).
