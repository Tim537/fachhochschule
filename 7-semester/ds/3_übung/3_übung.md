# Übung 3

## Aufgabe 1

### Aufgabenstellung

Betrachten Sie die Daten, die Sie auf dem Rechner infbdt13.fh-trier.de im Verzeichnis
/data/9/imdb finden. Diese beschreiben Filme, Schauspieler, Regisseure usw. aus der Internet
Movie Database. Einen Account dsXYZ, mit dem Sie sich dort per SSH einwählen können, habe ich
Ihnen per Mail zugesandt.
Entwickeln Sie aus diesen Daten ein Entity-Relationship-Diagramm, das möglichst vollständig die
Informationen in diesem Datensatz wiedergibt.

### Bearbeitung

title.akas Spalten: **titleId**, ordering, title, region, language, types, attributes, isOriginalTitle
title.basics Spalten: **tconst**, titleType, primaryTitle, originalTitle, isAdult, startYear, endYear, runtimeMinutes, genres
title.crew Spalten: **tconst**, **directors**, writers
title.principals Spalten: **tconst**, ordering, **nconst**, category, job, characters
title.ratings Spalten: **tconst**, averageRating, numVotes
title.episode Spalten: **tconst**, **parentTconst**, seasonNumber, episodeNumber
name.basics Spalten: **nconst**, primaryName, birthYear, deathYear, primaryProfession, knownForTitles

[ER-Diagramm](3_übung_ER.png)

## Aufgabe 2

### Aufgabenstellung

Geben Sie für alle Attribute aller Dateien die entsprechenden Skalenniveaus an.
Schreiben Sie außerdem ein Programm in einer Programmiersprache Ihrer Wahl, das beschreibende
Statistiken ausgibt:

1. über die gesamte Datei
   1.1 Anzahl der Datensätze insgesamt
2. für nominal und ordinal skalierte Attribute
   2.1 emprische Verteilung (Häufigkeiten der einzelnen Ausprägungen),
3. für kardinal skalierte Attribute
   3.1 Minimum, Maximum, arithmetisches Mittel

Sie können Ihr Programm so aufbauen, dass Sie die Nummer einer Spalte und ein Skalenniveau (nominal, ordinal oder kardinal) mitgeben. Die Daten lesen Sie zweckmäßigerweise von stdin, so dass wir auch mit komprimierten Daten umgehen können

### Bearbeitung

[main.py](main.py)

### 0

```
python3 main.py --skalenniveaus
```

```
name.basics.tsv.gz
Spalte  Attribut              Skalenniveau
1       nconst                nominal
2       primaryName           nominal
3       birthYear             kardinal
4       deathYear             kardinal
5       primaryProfession     nominal
6       knownForTitles        nominal

title.akas.tsv.gz
Spalte  Attribut              Skalenniveau
1       titleId               nominal
2       ordering              ordinal
3       title                 nominal
4       region                nominal
5       language              nominal
6       types                 nominal
7       attributes            nominal
8       isOriginalTitle       nominal

title.basics.tsv.gz
Spalte  Attribut              Skalenniveau
1       tconst                nominal
2       titleType             nominal
3       primaryTitle          nominal
4       originalTitle         nominal
5       isAdult               nominal
6       startYear             kardinal
7       endYear               kardinal
8       runtimeMinutes        kardinal
9       genres                nominal

title.crew.tsv.gz
Spalte  Attribut              Skalenniveau
1       tconst                nominal
2       directors             nominal
3       writers               nominal

title.episode.tsv.gz
Spalte  Attribut              Skalenniveau
1       tconst                nominal
2       parentTconst          nominal
3       seasonNumber          ordinal
4       episodeNumber         ordinal

title.principals.tsv.gz
Spalte  Attribut              Skalenniveau
1       tconst                nominal
2       ordering              ordinal
3       nconst                nominal
4       category              nominal
5       job                   nominal
6       characters            nominal

title.ratings.tsv.gz
Spalte  Attribut              Skalenniveau
1       tconst                nominal
2       averageRating         kardinal
3       numVotes              kardinal
```

#### 1.1

```
gzip -dc imdb/title.basics.tsv.gz | python3 main.py 2 nominal
```

Attribut: titleType  
Datensätze: 6205363

#### 2.1

```
gzip -dc imdb/title.principals.tsv.gz | python3 main.py 4 nominal
```

Attribut: category  
Datensätze: 35740426

actor: 8336819 (23.33%)  
actress: 6181257 (17.29%)  
self: 6052553 (16.93%)  
writer: 4719033 (13.20%)  
director: 4079467 (11.41%)  
producer: 2140109 (5.99%)  
composer: 1291118 (3.61%)  
cinematographer: 1273249 (3.56%)  
editor: 1176817 (3.29%)  
production_designer: 282878 (0.79%)  
archive_footage: 205000 (0.57%)  
archive_sound: 2126 (0.01%)

#### 3.1

```
gzip -dc imdb/title.basics.tsv.gz | python3 main.py 8 kardinal
```

Attribut: runtimeMinutes  
Datensätze: 6205363

Minimum: 0.0  
Maximum: 125156.0  
Mittelwert: 45.1484121439181

## Aufgabe 3

### Aufgabenstellung

Erweitern Sie Ihr Programm aus der vorigen Aufgabe, so dass es Quantile einer beliebigen kardinalen Spalte berechnen kann (es würde eine Ordinalskala ausreichen, aber dann müssten wir verschiedene Sortierkriterien für Zahlen und Strings implementieren). Wenn ein Wert p ∈ [0, 1] angegeben wird, soll das p-Quantil der genannten Spalte berechnet werden. Wird kein Wert p angegeben, sollen die Quartile berechnet werden.

### Bearbeitung

```
gzip -dc imdb/title.basics.tsv.gz | python3 main.py 8 kardinal
```

Attribut: runtimeMinutes  
Datensätze: 6205363

Minimum: 0.0  
Maximum: 125156.0  
Mittelwert: 45.1484121439181  
Quantil p=0.25: 15.0  
Quantil p=0.5: 30.0  
Quantil p=0.75: 61.0

```
gzip -dc imdb/title.basics.tsv.gz | python3 main.py 8 kardinal 0.9
```

Attribut: runtimeMinutes  
Datensätze: 6205363

Minimum: 0.0  
Maximum: 125156.0  
Mittelwert: 45.1484121439181  
Quantil p=0.9: 96.0
