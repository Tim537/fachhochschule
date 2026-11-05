import argparse
import csv
import gzip
import sys
from collections import Counter
from pathlib import Path


SKALENNIVEAUS = {
    "nconst": "nominal",
    "primaryName": "nominal",
    "birthYear": "kardinal",
    "deathYear": "kardinal",
    "primaryProfession": "nominal",
    "knownForTitles": "nominal",
    "titleId": "nominal",
    "ordering": "ordinal",
    "title": "nominal",
    "region": "nominal",
    "language": "nominal",
    "types": "nominal",
    "attributes": "nominal",
    "isOriginalTitle": "nominal",
    "tconst": "nominal",
    "titleType": "nominal",
    "primaryTitle": "nominal",
    "originalTitle": "nominal",
    "isAdult": "nominal",
    "startYear": "kardinal",
    "endYear": "kardinal",
    "runtimeMinutes": "kardinal",
    "genres": "nominal",
    "directors": "nominal",
    "writers": "nominal",
    "parentTconst": "nominal",
    "seasonNumber": "ordinal",
    "episodeNumber": "ordinal",
    "category": "nominal",
    "job": "nominal",
    "characters": "nominal",
    "averageRating": "kardinal",
    "numVotes": "kardinal",
}


def zeige_skalenniveaus(ordner):
    dateien = sorted(ordner.glob("*.tsv.gz"))
    if not dateien:
        parser.error(f"Keine IMDb-Dateien in {ordner} gefunden")

    for datei in dateien:
        with gzip.open(datei, "rt", encoding="utf-8", newline="") as eingabe:
            kopf = next(csv.reader(eingabe, delimiter="\t", quoting=csv.QUOTE_NONE), [])

        for attribut in kopf:
            if attribut not in SKALENNIVEAUS:
                parser.error(f"Unbekanntes IMDb-Attribut in {datei.name}: {attribut}")

        print(f"\n{datei.name}")
        print(f"{'Spalte':<7} {'Attribut':<21} Skalenniveau")
        for nummer, attribut in enumerate(kopf, start=1):
            print(f"{nummer:<7} {attribut:<21} {SKALENNIVEAUS[attribut]}")


def berechne_quantil(sortierte_werte, p):
    position = (len(sortierte_werte) - 1) * p
    unten = int(position)
    oben = min(unten + 1, len(sortierte_werte) - 1)
    anteil = position - unten

    return (
        sortierte_werte[unten]
        + anteil * (sortierte_werte[oben] - sortierte_werte[unten])
    )


parser = argparse.ArgumentParser()
parser.add_argument("spalte", type=int, nargs="?", help="Spaltennummer ab 1")
parser.add_argument("niveau", nargs="?", choices=["nominal", "ordinal", "kardinal"])
parser.add_argument(
    "p", type=float, nargs="?",
    help="Quantil zwischen 0 und 1; ohne p werden die Quartile ausgegeben",
)
parser.add_argument(
    "--skalenniveaus", action="store_true",
    help="Skalenniveaus aller Attribute der lokalen IMDb-Dateien anzeigen",
)
args = parser.parse_args()

if args.skalenniveaus:
    if any(wert is not None for wert in (args.spalte, args.niveau, args.p)):
        parser.error("--skalenniveaus wird ohne Spaltennummer, Niveau und p aufgerufen")
    zeige_skalenniveaus(Path(__file__).resolve().parent / "imdb")
    parser.exit()

if args.spalte is None or args.niveau is None:
    parser.error("Für die Statistik sind Spaltennummer und Skalenniveau erforderlich")

if args.p is not None:
    if not 0 <= args.p <= 1:
        parser.error("p muss zwischen 0 und 1 liegen")
    if args.niveau != "kardinal":
        parser.error("Ein p-Quantil wird nur für kardinale Spalten unterstützt")

reader = csv.reader(sys.stdin, delimiter="\t", quoting=csv.QUOTE_NONE)

kopf = next(reader, [])
if not 1 <= args.spalte <= len(kopf):
    parser.error("Ungültige Spaltennummer")

index = args.spalte - 1

gesamt = anzahl = 0
haeufigkeiten = Counter()
summe = 0.0
minimum = maximum = None
zahlen = []

for zeile in reader:
    gesamt += 1
    wert = zeile[index]

    if wert == r"\N" or wert == "":
        continue

    anzahl += 1

    if args.niveau in ("nominal", "ordinal"):
        haeufigkeiten[wert] += 1
    else:
        zahl = float(wert)
        zahlen.append(zahl)
        summe += zahl
        minimum = zahl if minimum is None else min(minimum, zahl)
        maximum = zahl if maximum is None else max(maximum, zahl)

print("Attribut:", kopf[index])
print("Datensätze:", gesamt)
print("----------")

if anzahl == 0:
    print("Keine gültigen Werte vorhanden.")
elif args.niveau in ("nominal", "ordinal"):
    for wert, n in haeufigkeiten.most_common():
        print(f"{wert}: {n} ({n / anzahl:.2%})")
else:
    print("Minimum:", minimum)
    print("Maximum:", maximum)
    print("Mittelwert:", summe / anzahl)

    zahlen.sort()
    quantile = [args.p] if args.p is not None else [0.25, 0.5, 0.75]
    for p in quantile:
        print(f"Quantil p={p:g}:", berechne_quantil(zahlen, p))
