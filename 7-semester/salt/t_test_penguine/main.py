import pandas as pd
import matplotlib.pyplot as plt
import scipy

df = pd.read_csv("penguins.csv")

print(df.head())

# filter for "Adelie"
df = df[df["species"] == "Adelie"]

# get body_mass_g by sex
male = df.loc[df["sex"] == "male", "body_mass_g"].dropna()
female = df.loc[df["sex"] == "female", "body_mass_g"].dropna()

# render boxplot
plt.boxplot([
    male,
    female,
], tick_labels=["Male", "Female"])
plt.ylabel("body_mass_g")
plt.title("Comparison by sex")
plt.show()

# perform t-test (h0: same average body_mass_g)
ttest_student = scipy.stats.ttest_ind(male, female, equal_var=True, alternative="two-sided")
ttest_welch = scipy.stats.ttest_ind(male, female, equal_var=False, alternative="two-sided")

print(ttest_student)
# statistic: 13.126285923485874
# pvalue: 2.2206436307866212e-26
# df: 144.0

print(ttest_welch)
# statistic: 13.126285923485874
# pvalue: 6.402319748031804e-26
# df: 135.69357893530383