# Übung 5

Betrachten Sie für diese Aufgaben die Daten über amerikanische Filme, die Sie in
`infbdt13.hochschule-trier.de:/data/9/movies` finden.

Benutzen Sie zur Lösung der Aufgaben Python mit der Bibliothek `json` wie in der Vorlesung
gezeigt. Mit `json_pp` können Sie die Originaldaten lesbarer gestalten; dann lassen sich auch
leichter Textstellen suchen.

## Aufgabe 1

### Aufgabenstellung

Lesen Sie die Datei `movies.json` ein.

- Führen Sie mit, wie viele Filme Sie insgesamt bearbeitet haben, sowie die Anzahl der
  Filme, bei denen Genre, Cast oder Jahr fehlen.
- Berechnen Sie die Vollständigkeit des Datensatzes, wobei wir den Cast mit 0.5, das Jahr mit
  0.3 und die Information über Genres mit 0.2 gewichten.

Hinweis: Mit `collections.defaultdict` oder `collections.Counter` können Sie die
zweidimensionale Datenstruktur (z. B. Person → Jahr → Anzahl) für die Zählung deutlich
komfortabler gestalten, als wenn Sie selbst Dictionaries von Dictionaries pflegen.

### Bearbeitung

## Aufgabe 2

### Aufgabenstellung

Sehen Sie in Ihrem Programm aus der vorigen Aufgabe die Möglichkeit vor, Konsistenzregeln auf
Attributebene vorzugeben. Prüfen Sie nicht nur, ob die Daten konsistent sind oder nicht, sondern
weisen Sie die Anzahl der Regelverletzungen pro Regel aus. Dabei wäre es sinnvoll, wenn die
Regeln Namen hätten.

Denken Sie daran, dass in Python Funktionen wie Daten behandelt werden können. Sie können also
eine Liste von Konsistenzregeln als eine Liste von (Lambda-)Funktionen implementieren, so wie es
in den Vorlesungsfolien skizziert ist. Alternativ ist natürlich auch eine objektorientierte
Implementierung mit einer Klasse `AttributeRule` o. Ä. denkbar mit einer Operation wie
`AttributeRule.check(tuple) → bool`, so dass jede Regel ein Objekt ist.

Als Beispiele können folgende Konsistenzregeln dienen (die nicht alle unbedingt fachlich sinnvoll
sind):

- Attribut Cast: Länge < 10
- Attribut Jahr: Jahr zwischen 1880 und 2030

### Bearbeitung

## Aufgabe 3

### Aufgabenstellung

Erweitern Sie Ihr Programm aus Aufgabe 2, so dass es Regeln auf Tupelebene unterstützt.

### Bearbeitung
