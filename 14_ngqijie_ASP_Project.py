import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

country = pd.read_excel('IMVA.xls', sheet_name='IMVA')

df_country = country[['Periods', "Americas", "Canada", "USA", "Other Markets In Americas", "Oceania", "Australia", "New Zealand",
                      "Other Markets In Oceania", "Africa", "Egypt", "Mauritius", "South Africa (Rep Of)", "Other Markets In Africa"]]
print(df_country.columns)

df1 = df_country['Periods'].str.split(' ', n=1, expand=True)
df_country = df_country.assign(Year=df1[0])

print('----------Split Year----------')
df_country['Year'] = pd.to_numeric(df_country['Year'])
df2 = df_country['Year'].dtypes
print("Year type is", df2)

print("----------Dropped Periods----------")
print(df_country.drop(['Periods'], axis=1))
df_country1 = df_country[(df_country['Year'] >= 2006) & (df_country['Year'] <= 2017)]

print('----------df_country1----------')
print(df_country1)

df_country2 = df_country1[["Americas", "Canada", "USA", "Other Markets In Americas", "Oceania", "Australia", "New Zealand",
                            "Other Markets In Oceania", "Africa", "Egypt", "Mauritius", "South Africa (Rep Of)", "Other Markets In Africa"]]
print('----------df_country2----------')
print(df_country2)
print('sorted')

df_country3 = df_country2.replace(',', '', regex=True)
df_country4 = df_country3.replace('na', '0', regex=True)

print('----------df_country4----------')
print(df_country4)
df_country5 = df_country4.astype(int)
print(df_country5.dtypes)
NotSorted = df_country5.sum()
Sorted = df_country5.sum().sort_values(ascending=False)

print('----------Sorted----------')
print(Sorted)
df_allcountry = Sorted

print('----------Top 3 Countries----------')
top3 = Sorted.head(3)
print(top3)
total=top3.values.sum()
mean=round(top3.values.mean(),2)

print("The Total No. of Visitors for the Top 3 Countries is ",total)
print("The Mean Value for the Top 3 Countries is ",mean)

indexAll = np.arange(len(df_allcountry.index))

plt.figure(figsize=(10, 10))
plt.title('All other Countries from(Period:2006-2017)')
plt.xlabel('Countries', fontsize=8)
plt.ylabel('No. of Travellers (in thousands)', fontsize=8)
plt.xticks(indexAll, df_allcountry.index, fontsize=6, rotation=30)
plt.bar(df_allcountry.index, df_allcountry.values / 1000)
plt.show()

indexAll = np.arange(len(df_allcountry.index))

plt.figure(figsize=(10, 10))
plt.xlabel('Countries', fontsize=8)
plt.ylabel('No. of Travellers (in thousands)', fontsize=8)
plt.xticks(indexAll, df_allcountry.index, fontsize=6, rotation=30)
plt.bar(top3.index, top3.values / 1000)
plt.show()