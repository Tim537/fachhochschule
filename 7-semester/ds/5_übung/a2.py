import json
from collections import Counter

def year_valid_value(year):   
    if year < 1880:
        return False
    elif year > 2026:
        return False
    else:
        return True

def year_is_int(year):
    if type(year) != int:
        return False
    else:
        return True

def cast_has_space(cast):
    if " " not in cast:
        return False
    else:
        return True

def cast_is_string(cast):
    if type(cast) != str:
        return False
    else:
        return True

def genre_is_string(cast):
    if type(cast) != str:
        return False
    else:
        return True

def genre_starts_with(cast):
    if cast[0].isupper():
        return True
    else:
        return False

year_rules = [year_is_int, year_valid_value]
cast_rules = [cast_has_space, cast_is_string]
genre_rules = [genre_is_string, genre_starts_with]
rules = [*year_rules, *cast_rules, *genre_rules]

movies = None
counter = Counter()

for rule in rules:
    counter[rule.__name__] = 0

with open("movies.json") as file:
    movies = json.load(file)

for movie in movies:
    counter["movies"] += 1
    
    if len(movie["cast"]) < 1:
        counter["cast_missing"] += 1
    else:
        for cast in movie["cast"]:
            for rule in cast_rules:
                if not rule(cast):
                    counter[rule.__name__] += 1

    if len(movie["genres"]) < 1:
        counter["genre_missing"] += 1
    else:
        for genre in movie["genres"]:
            for rule in genre_rules:
                if not rule(genre):
                    counter[rule.__name__] += 1
            

    if movie["year"] is None:
        counter["year_missing"] += 1
    else:
        for rule in year_rules:
            if not rule(movie["year"]):
                counter[rule.__name__] += 1

completeness = 1 - (
    (counter["cast_missing"] / counter["movies"]) * 0.5
    + (counter["genre_missing"] / counter["movies"]) * 0.2
    + (counter["year_missing"] / counter["movies"]) * 0.3
)

print(completeness)
print(counter)
# 0.9776975169300226
