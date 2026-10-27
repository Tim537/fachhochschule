# Übung 1 - Einführung, Motivation

## Aufgabe 0

### Aufgabenstellung

Bearbeiten Sie die Aufgabe 5 des 0.ten Aufgabenblattes.

### Bearbeitung

Siehe [Übung 0, Aufgabe 5](../0_übung/1_aufgabe.md#aufgabe-5).

## Aufgabe 1

### Aufgabenstellung

Ein Programm ist zu testen, das 3 ganzzahlige positive Werte einliest und als Längen eines Dreiecks interpretiert. Das Programm gibt eine Meldung aus, ob es sich um ein ungleichseitiges, gleichschenkliges oder gleichseitiges Dreieck handelt.

**a)** Schätzen Sie zunächst, ohne Aufgabenteil b) oder c) bearbeitet zu haben, welche Anzahl an Tests für dieses Programm benötigt werden.

**b)** Beschreiben Sie, mit welchen Testdaten Sie das Programmstück testen würden.

Beispiel:

- (2,2,2): gültiges gleichseitiges Dreieck
- (2,1,4): unzulässige Eingabe, da kein Dreieck konstruierbar

**c)** Geben Sie allgemeingültige Bedingungen an für

1. ein gleichschenkliges Dreieck,
2. ein gleichseitiges Dreieck, und
3. ein ungleichseitiges Dreieck.

Achten Sie darauf, dass die allgemeingültigen Bedingungen ebenfalls die Zulässigkeit der Eingabedaten berücksichtigen.

**d)** Wie könnten Sie die allgemeingültigen Bedingungen in Ihrem Programm (beispielsweise codiert in Java) in der Entwicklungsphase verwenden?

**e)** Implementieren Sie das Programm in Java (oder einer anderen Sprache) und führen Sie Ihre in Aufgabenteil b) definierten Tests durch. (Sie müssen hier nicht alle Tests durchführen.)

### Bearbeitung

#### a) Geschätzte Anzahl an Tests

- 3 Tests für ints
- 3 Tests für >=0
- 2 Tests für gleichseitig oder nicht
- 4 Tests für gleichschenkelig: AB, AC, BC oder nicht
- 2 Tests für ungleichseitig oder nicht

=> 3 + 3 + 2 + 4 + 2 = 14 Tests

#### b) Testdaten

| Testfall | Eingabewerte | Erwartetes Ergebnis |
| -------- | ------------ | ------------------- |
| 1        | (A,2,3)      | ERROR NOT INT       |
| 2        | (1,B,3)      | ERROR NOT INT       |
| 3        | (1,2,C)      | ERROR NOT INT       |
| 4        | (-1,2,3)     | ERROR <0            |
| 5        | (1,-2,3)     | ERROR <0            |
| 6        | (1,2,-3)     | ERROR <0            |
| 7        | (1,1,1)      | Gleichseitig        |
| 8        | (1,2,3)      | Ungleichseitig      |
| 9        | (1,1,3)      | Gleichschenkelig    |
| 10       | (1,2,1)      | Gleichschenkelig    |
| 11       | (1,2,2)      | Gleichschenkelig    |
| 12       | (2,2,2)      | Gleichseitig        |
| 13       | (3,3,3)      | Gleichseitig        |
| 14       | (1,2,3)      | Ungleichseitig      |

#### c) Allgemeingültige Bedingungen

##### i. Gleichschenkliges Dreieck

2 Seiten sind gleich lang: a == b or a == c or b == x

##### ii. Gleichseitiges Dreieck

Alle 3 Seiten sind gleich lang: a == b and b == c

##### iii. Ungleichseitiges Dreieck

Alle 3 Seiten sind unterschiedlich lang: a != b and a != c and b != c

#### d) Verwendung der Bedingungen in der Entwicklungsphase

Die allgemeingültigen Regel sollen einerseits dafür genutzt werden die eigentliche Funktion zu schreiben indem der Ausdruck in Code übersetzt wird und andererseits sollen sie genutzt werden um die bewusst Fehlerhaften Tests zu schreiben.

#### e) Implementierung und Testdurchführung

##### Implementierung

- [Implementierung: classify_triangle.py](classify_triangle.py)
- [Tests: test_classify_triangle.py](test_classify_triangle.py)

##### Testergebnisse

| Testfall aus b) | Tatsächliches Ergebnis            | Test bestanden? |
| --------------- | --------------------------------- | --------------- |
| 1               | `ValueError: A is not an integer` | Ja              |
| 2               | `ValueError: B is not an integer` | Ja              |
| 3               | `ValueError: C is not an integer` | Ja              |
| 4               | `ValueError: A is smaller than 0` | Ja              |
| 5               | `ValueError: B is smaller than 0` | Ja              |
| 6               | `ValueError: C is smaller than 0` | Ja              |
| 7               | `Gleichseitig`                    | Ja              |
| 8               | `Ungleichseitig`                  | Ja              |
| 9               | `Gleichschenkelig`                | Ja              |
| 10              | `Gleichschenkelig`                | Ja              |
| 11              | `Gleichschenkelig`                | Ja              |
| 12              | `Gleichseitig`                    | Ja              |
| 13              | `Gleichseitig`                    | Ja              |
| 14              | `Ungleichseitig`                  | Ja              |

## Aufgabe 2

### Aufgabenstellung

Ein einfaches Programm soll getestet werden, das aus vier Verzweigungen (IF-Anweisungen) und einer umfassenden Schleife besteht und somit fünf mögliche Wege im Schleifenrumpf enthält. Nehmen Sie an, dass die Verzweigungen voneinander unabhängig sind und nehmen Sie weiter an, dass eine Beschränkung der Schleifendurchläufe auf maximal 20 gegeben ist.

Wie lange dauert das Austesten dieses Programms bei 100.000 Testfällen pro Sekunde?

### Bearbeitung

Für Schleifenlängen von 1 bis 20 ergibt sich folgende Gesamtzahl an Testfällen:

$$
N = \sum_{n=1}^{20} 5^n = 119\,209\,289\,550\,780
$$

Bei 100.000 Testfällen pro Sekunde beträgt die benötigte Zeit:

$$
t = \frac{N}{100\,000\;\text{Testfälle/s}}
  = \frac{119\,209\,289\,550\,780\;\text{Testfälle}}{100\,000\;\text{Testfälle/s}}
  = 1\,192\,092\,895{,}5078\;\text{s}
$$

Umgerechnet in Jahre (mit 365 Tagen pro Jahr):

$$
t_{\text{Jahre}} = \frac{1\,192\,092\,895{,}5078}{60 \cdot 60 \cdot 24 \cdot 365}
\approx 37{,}8
$$

Das vollständige Austesten aller Wegeabfolgen für Schleifenlängen von 1 bis 20 würde somit etwa **37,8 Jahre** dauern.

## Aufgabe 3

### Aufgabenstellung

Typische Aussagen bezüglich Software-Qualitätssicherung, die man in Firmen immer wieder hört, sind beispielsweise:

- „Für Testautomatisierung haben wir keine Zeit“,
- „Mit der Testvorbereitung können wir jetzt noch nicht beginnen. Sonst müssen wir die Testfälle noch oft ändern“,
- „Jetzt müssen wir erst mal kräftig entwickeln, damit wir dann was zu testen haben“,
- „Wir haben weder Zeit noch Geld für Software-Qualitätssicherung“.

Stellen Sie sich vor, dass Sie der/die SW-Qualitätsbeauftragte Ihrer Firma sind und mit diesen Aussagen von Ihren Mitarbeitern konfrontiert werden.

Erstellen Sie einen Kurzvortrag (3-5 Folien), den Sie nutzen würden, um Ihre Mitarbeiter und Ihre Unternehmensführung davon zu überzeugen zukünftig den aus Ihrer Sicht passenden Aufwand in die Qualitätssicherung zu investieren. Den Kurzvortrag können Sie gerne in Teamarbeit erstellen.

### Bearbeitung

Inhaltliche Vorbereitung für fünf Folien. Die Stichpunkte sind für die Folien vorgesehen, die Sprechernotizen als Hilfe beim Vortragen. Die Beispiele und der Pilot sind eigene Vorschläge für eine angenommene Firma.

[Browserpräsentation nach den neuen Layoutregeln](praesentation/index.html) · [Sprechfassung](praesentation/sprechfassung.html) · [Bedienung](praesentation/README.md)

#### Folie 1: Qualitätssicherung gezielt einplanen

- QS umfasst Anforderungsklärung, Reviews und Tests.
- Aufwand nach Eintrittswahrscheinlichkeit und möglichen Fehlerfolgen priorisieren.
- Prüfkosten und mögliche Folgen unentdeckter Fehler gemeinsam betrachten.

**Sprechernotiz:** Unser Ziel ist ein zum Produkt passender QS-Aufwand. Bei einem Bestellabschluss können falsche Beträge oder verlorene Bestellungen schwerer wiegen als ein Darstellungsfehler. Für Mitarbeitende sollen Erwartungen und Prüfaufgaben klar sein; die Führung braucht eine begründete Freigabeentscheidung. Vollständiges Testen ist in der Regel nicht möglich. [1, Abschnitte 1.3 und 5.2]

#### Folie 2: „Für Testautomatisierung haben wir keine Zeit“

- Wichtige, häufig wiederholte Prüfungen als Kandidaten auswählen.
- Erstellung, Ausführung, Auswertung und Pflege mit einplanen.
- Automatische Prüfungen durch manuelle Erkundung ergänzen.

**Sprechernotiz:** Der Einwand benennt einen echten Kapazitätskonflikt. Ein automatischer Test der Bestellsumme kann wiederholte Handarbeit verringern; Einrichtung und Wartung kosten aber ebenfalls Zeit. Entscheidend sind Risiko, Wiederholung und Wartbarkeit. Auch bei verändertem Code kann die erwartete Berechnungsregel stabil bleiben. Automatisierung prüft definierte Erwartungen und garantiert keine Fehlerfreiheit. [1, Abschnitte 1.3 und 6.2]

#### Folie 3: „Frühe Testvorbereitung erzeugt nur Änderungen“

- Früh wenige konkrete Akzeptanzbeispiele gemeinsam festlegen.
- Details entsprechend der Klarheit der Anforderungen ausarbeiten.
- Änderungen an Anforderungen und Tests gemeinsam planen.

**Sprechernotiz:** Akzeptanzbeispiele beschreiben, woran wir richtiges Verhalten erkennen. Beim Bestellabschluss könnten wir vor der Programmierung klären: Gilt ein Rabatt auch bei genau erreichtem Mindestbestellwert? Dazu brauchen wir keinen ausführbaren Code. Ändert sich die Regel, entsteht Anpassungsaufwand. Das ist ein Grund für angemessene Vorbereitung und Pflege. [1, Abschnitte 3.1 und 4.5.2]

#### Folie 4: „Erst kräftig entwickeln, dann testen“

- Anforderungen und Entwürfe bereits vor ausführbarem Code prüfen.
- Kleine Änderungen mit Reviews und passenden Tests verbinden.
- Zusammenspiel und fachliche Eignung vor der Freigabe prüfen.

**Sprechernotiz:** Wer alle Prüfungen ans Ende verschiebt, erhält deren Rückmeldung ebenfalls erst dann. Kleine Schritte können die Fehlereingrenzung erleichtern. Beim Bestellabschluss würden wir einzelne Berechnungen während der Entwicklung prüfen und später zusätzlich den gesamten Ablauf mit Zahlung und Bestätigung untersuchen. Frühe Prüfung ergänzt Integrationstests, Systemtests und fachliche Abnahme. [1, Abschnitte 2.1, 2.2 und 3.1]

#### Folie 5: „Für QS fehlen Zeit und Geld“ - einen begrenzten Pilot beschließen

- Vorschlag: nächste zweiwöchige Iteration, zwei Personentage zusätzliches QS-Budget.
- Teamleitung koordiniert; Fachseite vereinbart Kriterien für einen wichtigen Ablauf.
- Am Iterationsende Aufwand und offene Risiken bewerten; über Fortsetzung entscheiden.

**Sprechernotiz:** Die zwei Personentage sind eine Planungsannahme für diesen Vorschlag, keine allgemeine Empfehlung. Das Team schätzt zunächst den Umfang; die Führung reserviert die Kapazität und verschiebt dafür gegebenenfalls eine weniger wichtige Funktion. Wir erproben Akzeptanzbeispiele, ein Review und ausgewählte Tests. Erfasst werden Vorbereitungs-, Ausführungs-, Analyse- und Pflegeaufwand sowie bedeutende Befunde und geprüfte beziehungsweise offene Risiken. Führung und Team entscheiden danach über Fortsetzung, Anpassung oder Abbruch. Reine Fehlerzahlen und ein kurzer Pilot belegen keine langfristige Rentabilität; bestehende notwendige Prüfungen laufen weiter.

**Abschlusssatz:** „Bitte geben Sie diesen begrenzten Pilot frei, damit wir den weiteren QS-Aufwand auf Basis eigener Erfahrungen entscheiden können.“

#### Fachliche Grundlage und Arbeitsunterlagen

[1] ISTQB: *Certified Tester Foundation Level Syllabus*, v4.0.1, 15.09.2024. Verwendet für Testgrundsätze, frühe Prüfung, Akzeptanzkriterien, Risikoorientierung sowie Chancen und Grenzen von Automatisierung. [Zum offiziellen Lehrplan](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf), abgerufen am 26.10.2026.

Die konkreten Firmenbeispiele, die Pilotgröße und die vorgeschlagene Auswertung sind eigene Ausgestaltungen; sie sind keine Vorgaben des Lehrplans.

[Drei unabhängige Entwürfe, drei unabhängige Kritiken und übernommene Änderungen](aufgabe_3_agentenpruefung.md)
