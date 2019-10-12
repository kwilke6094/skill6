from matplotlib import pyplot as plt
import pandas as pd
url = "https://raw.githubusercontent.com/datasets/gdp/0be54c18d900edc37123f25b4eff014731c9e459/data/gdp.csv"
data=pd.read_csv(url)
data.columns = data.columns.str.replace(" ", "")
us = data[data.CountryName == 'United States']
eu = data[data.CountryName == 'European Union']
china = data[data.CountryName == 'China']

fix = 10**9

plt.plot(us.Year, us.Value / fix)
plt.plot(eu.Year, eu.Value / fix, "g--")
plt.plot(china.Year, china.Value / fix, "ro")

plt.title("Kevin Wilke's GDP Plot")
plt.legend(["United States", "EU", "China"])
plt.xlabel("Year")
plt.ylabel("GDP")

plt.savefig("Skill6_WilkeKevin.png")
plt.show()