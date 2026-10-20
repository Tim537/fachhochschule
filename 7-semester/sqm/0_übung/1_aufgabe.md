# Übung 0 - Einführung, Motivation

## Aufgabe 1

### Aufgabenstellung

In der Vorlesung wurde argumentiert, dass Software „den Unterschied“ macht bei heutigen Entwicklungen. Dieser Trend ist in vielen Branchen zu beobachten, wie beispielsweise in der Luft-/Raumfahrt, in der Medizintechnik oder in der Automobilindustrie. Wir haben weiterhin die Dimensionen Kosten, Flexibilität und Differenzierung von Software in diesem Zusammenhang kurz angesprochen.

Welche Gefahren sind mit diesen Entwicklungen (Software wird zunehmend zum Mittelpunkt der Systeme) verbunden? (Begründen Sie jeweils Ihre Antwort)

### Bearbeitung

- Ausfall der Systeme: Es besteht die Gefahr, dass das System komplett ausfällt, weil die Software keine redundanten Systeme hat.
- Schäden durch Software-Fehler: Es besteht die Gefahr, dass es zu Unfällen mit Sach- und/oder Personenschäden kommt, weil die Software fehlerhaft ist und andere sicherheitskritische Systeme von ihr abhängig sind.
- Ausfall/Fehlverhalten durch Updates: Es besteht die Gefahr, dass Software nicht mehr (korrekt) funktioniert, weil eine andere Software, von der sie abhängig ist, aktualisiert wurde, sich Schnittstellen geändert haben und keine Rückwärtskompatibilität besteht.
- Cyber-Security: Es besteht die Gefahr, dass bei langer Nutzung von Hardware die Cyber-Security-Gefahr steigt, weil der Hersteller keine Sicherheitsupdates mehr bereitstellt und Sicherheitslücken gefunden wurden.

## Aufgabe 2

### Aufgabenstellung

Es wird heutzutage häufig vom Internet der Dinge und von cyber-physischen Systemen gesprochen.

1. Geben Sie jeweils eine Definition und ein dazugehöriges Beispiel an.

2. Welchen Zusammenhang können Sie zwischen IoT und cyber-physischen Systemen auf der einen Seite und dem Softwarequalitätsmanagement auf der anderen Seite herstellen?

### Bearbeitung

#### Definition: IoT

> Der Begriff Internet der Dinge oder Internet of Things (IoT) steht für eine vernetzte Welt aus "smarten", d.h. intelligenten, Geräten. Diese IoT-Geräte verhalten sich wie Computer und sind lokal oder über das Internet mit anderen Geräten vernetzt.

Quelle: BSI: "Internet der Dinge" <br>
[Zur Quelle](https://www.bsi.bund.de/dok/10072124), abgerufen am 17.10.2026

Beispiel: Lampen, die über ein Smart-Home-System z. B. durch Alexa gesteuert werden.

#### Definition: Cyber-physische Systeme

> Cyberphysische Systeme [...] sind Systeme, bei denen informations- und softwaretechnische mit mechanischen Komponenten verbunden sind, wobei Datentransfer und -austausch sowie Kontrolle bzw. Steuerung über eine Infrastruktur wie das Internet in Echtzeit erfolgen.

Quelle: Oliver Bendel: "Cyberphysische Systeme"<br>
Gabler Wirtschaftslexikon, 13.07.2021 <br>
[Zur Quelle](https://wirtschaftslexikon.gabler.de/definition/cyber-physische-systeme-54077/version-384624), abgerufen am 17.10.2026

Beispiel: Heizungssteuerung, die das Heizungsventil blockiert, wenn ein Fenstersensor meldet, dass ein Fenster offen ist.

#### Zusammenhang

IoT und CPS erfassen, verarbeiten und übertragen Daten. CPS führen auf dieser Grundlage zudem Aktionen aus, die unmittelbar auf die physische Welt einwirken. Für das Softwarequalitätsmanagement ergibt sich daraus die Anforderung, die Datenintegrität sicherzustellen, sodass die erhobenen Daten unverändert und vollständig ankommen. Darüber hinaus sollten die Daten einer Plausibilitätsprüfung unterzogen werden, damit mögliche Sensorfehler anhand auffälliger Messwerte erkannt und gemeldet werden können. Ob diese Anforderungen erfüllt werden, lässt sich beispielsweise durch automatisierte Tests überprüfen.

## Aufgabe 3

### Aufgabenstellung

1. Geben Sie eine Definition des Begriffs Bug Bounty an. Lesen Sie ebenfalls den [folgenden Artikel](https://www.heise.de/security/meldung/US-Bug-Bountys-lassen-gute-Hacker-in-die-Falle-tappen-3946508.html) durch, den wir im Rahmen der Übung kurz besprechen werden.<br>
   Ebenfalls interessant in diesem Kontext ist die [folgende Seite](https://de.wikipedia.org/wiki/Zerodium).

2. Geben Sie eine Definition des Begriffs Zero-Day-Exploit an.

### Bearbeitung

#### Definition: Bug Bounty

> Ein Bug-Bounty-Programm ist ein von einem Unternehmen oder einer Organisation ausgeschriebenes Programm, dass Prämien wie Geld- oder Sachpreise für das Entdecken von Schwachstellen in Software, Anwendungen oder Web-Diensten auslobt. Es richtet sich an IT-Security-Experten und ist Teil der Sicherheitsstrategie des Unternehmens oder der Organisation.

Quelle: Stefan Luber: "Was ist ein Bug-Bounty-Programm?" <br>
Security-Insider: 25.08.2021 <br>
[Zur Quelle](https://www.security-insider.de/was-ist-ein-bug-bounty-programm-a-1052493/), abgerufen am 17.10.2026

#### Definition: Zero-Day-Exploit

> Ein Zero-Day-Exploit (auch Zero-Day-Bedrohung genannt) ist ein Angriff, bei dem böswillige Akteure eine Sicherheitslücke ausnutzen, für die es noch keine Lösung gibt. Man spricht von einer „Zero-Day“-Bedrohung, weil der Entwickler oder das Unternehmen, sobald die Schwachstelle entdeckt wird, „null Tage“ Zeit hat, um eine Lösung zu finden.

Quelle: Cloudflare: "Was ist ein Zero-Day-Exploit?" <br>
[Zur Quelle](https://www.cloudflare.com/de-de/learning/security/threats/zero-day-exploit/), abgerufen am 17.10.2026

## Aufgabe 4

### Aufgabenstellung

Wir haben in der Vorlesung die folgende Folie besprochen:

> Software Qualitätsmanagement und KI
>
> Das Fach Software Qualitätsmanagement bleibt nicht nur relevant, sondern wird zu einer Schlüsselkompetenz in der Ära generativer KI.
>
> Während LLMs operative Aufgaben der Qualitätssicherung teilweise übernehmen können, bedarf es menschlicher Expertise, um Qualitätsziele zu definieren, Prozesse zu steuern und KI-generierte Ergebnisse kritisch zu evaluieren. (Human-in-the-loop)
>
> „Qualitätsmanagement für KI-gestützte Softwareentwicklung“ Methoden, Standards und Denkweisen, die sicherstellen, dass automatisierte Systeme weiterhin verlässlich, nachvollziehbar und ethisch vertretbar agieren.

Diskutieren Sie kritisch die Aussage:

> „Menschliche Expertise bleibt auch in KI-gestützten Qualitätsprozessen unverzichtbar.“

Beziehen Sie in Ihre Argumentation mögliche Grenzen menschlicher Urteilsfähigkeit in hochautomatisierten KI-basierten Systemen mit ein. Zudem sollten Sie die Chancen und Risiken einer zunehmenden Delegation von Erstellung und Qualitätsprüfung von und durch KI-Systeme mit einbeziehen und die jeweiligen Implikationen für Verantwortlichkeit und Nachvollziehbarkeit von Entscheidungen betrachten.

### Bearbeitung

Die Aussage „Menschliche Expertise bleibt auch in KI-gestützten Qualitätsprozessen unverzichtbar“ ist differenziert zu betrachten. Menschen verfügen über eine begrenzte Prüfkapazität. Wenn KI große Mengen an Code und Tests erzeugt, kann eine vollständige manuelle Prüfung schwierig werden. Deshalb müssen Organisationen geeignete Prüfverfahren festlegen. Dazu können automatisierte Prüfungen, unabhängige Tests und risikoorientierte Codeprüfungen gehören. Welche Prüfungen erforderlich sind, sollte sich unter anderem nach den möglichen Folgen eines Fehlers richten. Stichproben müssen entsprechend begründet werden.

Die Organisation trägt dabei Verantwortung für die Gestaltung des Prüfverfahrens, ausreichende Ressourcen wie Zeit, fachlich qualifiziertes Personal und geeignete Prüfwerkzeuge und die akzeptierten Restrisiken. Die prüfende Person verantwortet die sorgfältige Durchführung der vorgesehenen Prüfung und die wahrheitsgemäße Darstellung ihrer Ergebnisse. Dadurch werden Verantwortungsbereiche klar zugeordnet. Eine Freigabe sollte erkennen lassen, welche Nachweise vorlagen und welche Unsicherheiten bestehen blieben.

Die Delegation an KI bietet Chancen: Wiederkehrende Aufgaben können schneller bearbeitet werden, und KI kann zusätzliche Testfälle oder Hinweise auf mögliche Fehler vorschlagen. Die gewonnene Zeit kann für die Untersuchung komplexer und sicherheitskritischer Sachverhalte genutzt werden. Gleichzeitig besteht das Risiko, dass Menschen KI-Ergebnisse unkritisch übernehmen. Auch können Fehler unentdeckt bleiben, wenn beispielsweise Code und Tests auf derselben falsch verstandenen Anforderung beruhen. Übermäßiges Vertrauen in automatisierte Ergebnisse ist daher eine relevante Grenze menschlicher Kontrolle.

Für die Nachvollziehbarkeit sollten Anforderungen, zugehörige Codeversionen, Tests, Testergebnisse und begründete Freigabeentscheidungen dokumentiert werden. Diese Dokumentation ermöglicht eine spätere Überprüfung. Ihre Wirksamkeit setzt voraus, dass die dokumentierten Nachweise tatsächlich kritisch bewertet werden.

Die „Ironien der Automation“ verdeutlichen eine weitere Schwierigkeit: Menschen sollen gerade bei außergewöhnlichen Störungen eingreifen, obwohl ihnen durch weitgehende Automatisierung praktische Übung und aktuelles Prozessverständnis verloren gehen können. [Bainbridge, 1983](https://gwern.net/doc/sociology/technology/1983-bainbridge.pdf)

Menschliche Expertise bleibt somit für die Festlegung angemessener Qualitätsziele, die Bewertung von Risiken und die Begründung von Freigabeentscheidungen wesentlich. Wirksame menschliche Kontrolle erfordert jedoch Arbeitsbedingungen, unter denen diese Expertise erhalten und eingesetzt werden kann.

#### Frage an den Professor

> Wie würden Sie in der Praxis sicherstellen, dass Softwareentwickler bei zunehmender KI-Unterstützung ihre eigenen Programmier- und Analysefähigkeiten erhalten, sodass sie KI-Ergebnisse weiterhin kritisch prüfen und bei Fehlern eigenständig eingreifen können?

## Aufgabe 5

### Aufgabenstellung

1. Lassen Sie ein Sprachmodell die Kosten schlechter Softwarequalität in den USA recherchieren. Prüfen Sie jede Zahl gegen die Primärquelle (CISQ, IBM, NIST) – achten Sie auf Einheiten (billion / trillion) und das Bezugsjahr.
2. Lassen Sie ein Sprachmodell eine Ursachenanalyse zum CrowdStrike-Vorfall entwerfen.
    - Vergleichen Sie diese mit der offiziellen Fehleranalyse von CrowdStrike
    - Ordnen Sie zu: Fehlhandlung, Fehlerzustand, Fehlerwirkung (ISTQB-Glossar)
    - Welche Maßnahmen im Entwicklungsprozess hätten potenziell zu einer frühen Fehlerfindung beitragen können?

3. Reflexion: Wo war die KI hilfreich, wo lag sie falsch – und woran haben Sie es gemerkt?

### Bearbeitung

#### a) Kosten schlechter Softwarequalität in den USA

| Quelle                         | Geprüfte Zahl                                                 | Bedeutung                                                                                       |
| ------------------------------ | ------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| CISQ, Bericht 2022 [1]         | Mindestens 2,41 Billionen USD; Original: $2.41 trillion       | Geschätzte Kosten schlechter Softwarequalität in den USA für 2022                               |
| NIST/RTI, Studie 2002 [2]      | 59,5 Milliarden USD jährlich; Original: $59.5 billion         | Historische Schätzung der US-Kosten unzureichender Softwaretest-Infrastruktur                   |
| NIST/RTI, gleiche Studie [2]   | 22,2 Milliarden USD jährlich; Original: $22.2 billion         | Mögliches Einsparpotenzial durch verbesserte Testinfrastruktur; keine zusätzliche Schadenssumme |
| IBM, Veröffentlichung 2004 [3] | Rund 60 Milliarden USD jährlich; Original: almost $60 billion | IBM übernimmt die NIST-Schätzung von 2002. Es handelt sich um keine eigene IBM-Schätzung.       |

##### Quellen zu a)

[1] Herb Krasner / CISQ: _The Cost of Poor Software Quality in the US: A 2022 Report_.
2022, S. 3; Methodik auf S. 59–61.
[Zum Bericht](https://www.it-cisq.org/wp-content/uploads/sites/6/2022/11/CPSQ-Report-Nov-22-2.pdf),
abgerufen am 17.10.2026.

[2] Research Triangle Institute im Auftrag von NIST:
_The Economic Impacts of Inadequate Infrastructure for Software Testing_.
Planning Report 02-3, Mai 2002, S. 8-1, Tabelle 8-1
(PDF-Seite 169).
[Zum Bericht](https://www.nist.gov/document/report02-3pdf),
abgerufen am 17.10.2026.

[3] Geoffrey Bessin / IBM: _The business value of software quality_.
Dezember 2004, S. 7.
[Zum Dokument](https://public.dhe.ibm.com/software/rational/web/whitepapers/BusinessValueofSoftwareQuality.pdf),
abgerufen am 17.10.2026.

#### b) Ursachenanalyse zum CrowdStrike-Vorfall

##### Vergleich der Modelle

| Modell | Ergebnis                                                         | Bewertung nach Quellenprüfung |
| ------ | ---------------------------------------------------------------- | ----------------------------- |
| Luna   | Erkannte die technische Ursache und die Testlücke.               | korrekt                       |
| Sol    | Erklärte Ursache, Testlücke und Gegenmaßnahmen.                  | korrekt                       |
| Astra  | Trennte Ursachen, Begriffszuordnung und Verbesserungsvorschläge. | korrekt                       |

##### Ursachenanalyse

Am 19. Juli 2024 verteilte CrowdStrike ein Konfigurationsupdate, das einen bereits vorhandenen Fehler aktivierte. Eine Vorlage erwartete 21 Eingabewerte, der Sensor lieferte jedoch nur 20. Das Update erforderte die Auswertung des fehlenden 21. Werts. Da eine Grenzprüfung fehlte, wurde außerhalb des vorgesehenen Speicherbereichs gelesen. Dies führte zu Windows-Abstürzen mit Bluescreen.

Die bisherigen Tests verwendeten im 21. Feld ausschließlich Platzhalter. Dadurch wurde der problematische Zugriff nicht ausgelöst. Diese Erklärung stimmt mit der offiziellen CrowdStrike-Analyse überein. [4]

##### Zuordnung nach ISTQB

Die folgenden Beispiele sind eine eigene Zuordnung anhand der ISTQB-Begriffe. Die Definitionen wurden ergänzend im offiziellen Glossar überprüft. [5]

| Begriff       | Bedeutung                                                   | Beispiel beim Vorfall                                                                                                                     |
| ------------- | ----------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Fehlhandlung  | Menschliche Handlung, die ein falsches Ergebnis verursacht. | Mögliches Übersehen der unterschiedlichen Feldanzahl beim Implementieren oder Prüfen. Die konkrete Handlung und Person sind nicht belegt. |
| Fehlerzustand | Ein Mangel im Arbeitsergebnis.                              | Die widersprüchliche Feldanzahl und die fehlende Grenzprüfung.                                                                            |
| Fehlerwirkung | Fehlerhaftes Verhalten bei der Ausführung.                  | Windows stürzt mit einem Bluescreen ab.                                                                                                   |

##### Möglichkeiten zur früheren Fehlererkennung

- Erwartete und tatsächlich gelieferte Feldanzahl automatisch vergleichen.
- Jedes Feld mit konkreten Werten testen, besonders das letzte.
- Neue Konfigurationsdateien zusammen mit dem tatsächlichen Sensor in einer Testumgebung prüfen.

Diese Maßnahmen hätten den Fehler früher sichtbar machen können. Sie entsprechen Verbesserungen aus der offiziellen Fehleranalyse. [4]

##### Quellen zu b)

[4] CrowdStrike:
_External Technical Root Cause Analysis — Channel File 291_.
06.08.2024, S. 2–5.
[Zum Bericht](https://www.crowdstrike.com/wp-content/uploads/2024/08/Channel-File-291-Incident-Root-Cause-Analysis-08.06.2024.pdf),
abgerufen am 17.10.2026.

[5] ISTQB / German Testing Board:
_Standardglossar der Testbegriffe Englisch/Deutsch_.
Version 3.21, 29.04.2019, S. 11, 14 und 15.
[Zum Glossar](https://swisstestingboard.org/wp-content/uploads/2019/05/ISTQB-GTB-Standardglossar-der-Testbegriffe-Englisch-Deutsch-V3.21.pdf),
abgerufen am 17.10.2026.

#### c) Reflexion

Die KI war hilfreich, um Quellen zu finden, Ergebnisse zu vergleichen und den CrowdStrike-Vorfall verständlich zu erklären. Die Ergebnisse mussten jedoch auf ihre Bedeutung und Vollständigkeit geprüft werden.

| Beobachtung                                                                                    | Was zeigte die Gegenprüfung?                                                                                                                             |
| ---------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Die Modelle lieferten richtige Zahlen, wählten bei IBM aber zunächst Datenleckberichte.        | Diese beantworten die Frage nach den gesamten Kosten schlechter Softwarequalität nicht direkt und wurden deshalb ausgeschlossen.                         |
| Die zusammenfassende KI-Antwort behauptete zunächst zu allgemein, IBM nenne keine Gesamtsumme. | Eine weitere Suche fand die IBM-Veröffentlichung von 2004. Diese übernimmt allerdings die NIST-Schätzung und liefert keine unabhängige zweite Schätzung. |
| Die CrowdStrike-Analysen stimmten in den technischen Kernaussagen überein.                     | Diese Aussagen konnten anhand der offiziellen Fehleranalyse bestätigt werden.                                                                            |

Die wichtigste Erkenntnis ist, dass eine plausible Antwort und die Übereinstimmung mehrerer Modelle keine ausreichenden Belege sind. Entscheidend sind die ursprüngliche Quelle, das Bezugsjahr, die Einheit und die Frage, was eine Zahl tatsächlich beschreibt. Auch eine richtige Zahl kann für die konkrete Aufgabenstellung unpassend sein.
