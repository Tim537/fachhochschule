import json
from collections import Counter

movies = None
counter = Counter()

with open("movies.json") as file:
    movies = json.load(file)


for movie in movies:
    counter["movies"] += 1
    
    if len(movie["cast"]) < 1:
        counter["cast_missing"] += 1

    if len(movie["genres"]) < 1:
        counter["genre_missing"] += 1

    if movie["year"] is None:
        counter["year_missing"] += 1

completeness = 1 - (
    (counter["cast_missing"] / counter["movies"]) * 0.5
    + (counter["genre_missing"] / counter["movies"]) * 0.2
    + (counter["year_missing"] / counter["movies"]) * 0.3
)

print(completeness)
# 0.9776975169300226