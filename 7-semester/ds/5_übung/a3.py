import json
from collections import Counter

rules = [
    ("year_is_even_and_has_cast", lambda movie: year_is_even_and_has_cast(movie)),
    ("year_is_odd_and_has_genre", lambda movie: year_is_odd_and_has_genre(movie))
]

def year_is_even_and_has_cast(movie):
    if movie["year"] % 2 != 0:
        return False
    elif len(movie["cast"]) < 1:
        return False
    else:
        return True

def year_is_odd_and_has_genre(movie):
    if movie["year"] % 2 != 1:
        return False
    elif len(movie["genres"]) < 1:
        return False
    else:
        return True

movies = None
counter = Counter()

for name, _ in rules:
    counter[name] = 0

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

    for name, rule in rules:
        if rule(movie):
            continue
        else:
            counter[name] += 1

completeness = 1 - (
    (counter["cast_missing"] / counter["movies"]) * 0.5
    + (counter["genre_missing"] / counter["movies"]) * 0.2
    + (counter["year_missing"] / counter["movies"]) * 0.3
)

print(completeness)
print(counter)
# 0.9776975169300226
