from pathlib import Path
import pandas as pd

datenordner = Path(__file__).resolve().parent / "imdb"

# Aufgabe 1
# read files
df_basics = pd.read_csv(
    datenordner / "title.basics.tsv.gz",
    sep="\t"
)

df_ratings = pd.read_csv(
    datenordner / "title.ratings.tsv.gz",
    sep="\t"
    )

df_basics_sample = df_basics.sample(n=100)

print(df_basics_sample)