from pathlib import Path
import pandas as pd
import hashlib

dir_path = Path(__file__).resolve().parent / "imdb"

# Aufgabe 1
# read files
df_basics = pd.read_csv(
    dir_path / "title.basics.tsv.gz",
    sep="\t"
)

df_ratings = pd.read_csv(
    dir_path / "title.ratings.tsv.gz",
    sep="\t"
    )

def hash_id(tconst):
    tconst_hash = hashlib.sha256(tconst.encode("utf-8")).hexdigest()
    return int(tconst_hash, 16)

df_basics["tconst_hash"] = df_basics["tconst"].map(hash_id)
df_ratings["tconst_hash"] = df_ratings["tconst"].map(hash_id)

df_basics_sample = df_basics[df_basics["tconst_hash"] % 62000 == 0]
df_ratings_sample = df_ratings[df_ratings["tconst_hash"] % 62000 == 0]

# Aufgabe 2

df_merged = pd.merge(
    df_ratings_sample,
    df_basics_sample,
    on="tconst",
    how="inner"
)

df_merged = df_merged.sort_values("averageRating", ascending=False).head(10)
"""
       tconst  averageRating  numVotes                                      tconst_hash_x  titleType  ... startYear endYear runtimeMinutes                       genres                                      tconst_hash_y
14  tt8827264            9.7         6  2355816481475050304272722060449217712064666508...  tvEpisode  ...      2015      \\N             \\N                        Adult  2355816481475050304272722060449217712064666508...
5   tt0819334            9.0        22  9407414323959960652196728861209944212236687242...  tvEpisode  ...      2006      \\N             \\N                        Drama  9407414323959960652196728861209944212236687242...
15  tt9169598            9.0       326  6256664221846665658260866985260942731925002781...   tvSeries  ...      2016      \\N             10             Comedy,Talk-Show  6256664221846665658260866985260942731925002781...
9   tt1748524            8.9         9  9509253829768627659617819410501435589909208367...  tvEpisode  ...      1985      \\N             95            Drama,History,War  9509253829768627659617819410501435589909208367...
2   tt0505246            8.7        29  5098390221943658094308785465674488953086137585...  tvEpisode  ...      1972      \\N             30           Comedy,Crime,Drama  5098390221943658094308785465674488953086137585...
8   tt1730390            8.2         5  5137585372733498853436928490456539945688366796...  tvEpisode  ...      2009      \\N             20       Documentary,Reality-TV  5137585372733498853436928490456539945688366796...
4   tt0745618            8.2       415  1682086779775093200388203530415072545552417312...  tvEpisode  ...      2003      \\N             42                        Drama  1682086779775093200388203530415072545552417312...
6   tt1499921            7.4        11  6268886906685373841899588740612510960257982926...      video  ...      2008      \\N            260                       Comedy  6268886906685373841899588740612510960257982926...
3   tt0598038            7.3        32  8226992381485800779097241511893738809493638595...  tvEpisode  ...      1977      \\N             50          Crime,Drama,Mystery  8226992381485800779097241511893738809493638595...
13  tt4760186            7.1       312  1909562850340397232231761734832290747909710220...      movie  ...      2017      \\N             82  Biography,Documentary,Drama  1909562850340397232231761734832290747909710220...

[10 rows x 13 columns]
"""

# Aufgabe 3

from lxml import etree

tree = etree.parse("orders.xml")

# Welche Bestellungen (order_id ist gesucht) hat Mitarbeiter 338 abgewickelt?
orders = tree.xpath("//order[employee_id = 338]/order_id/text()")
# => ['50014', '50024', '50178']

# Wer hat Produkt 2449 gekauft?
customer_id = list(set(tree.xpath("//order_item[product_id = 2449]/../../customer_id/text()")))
# => ['190', '198', '202', '188', '203', '200', '186', '185', '197', '187', '199', '"unbekannt"', '201', '195', '192', '194', '204', '196', '193', '191', '189']

# Welche Produkte wurden zusammen mit Produkt 2449 gekauft?
products_bought_together = list(set(tree.xpath("//order_item[product_id = 2449]/../order_item[product_id != 2449]/product_id/text()")))
# => ['18', '3359', '3354', '1804', '3361', '2470', '3350', '1726', '2468', '1805', '1788', '2457', '2439', '3337', '3353', '1806', '3355', '1733', '1729']
