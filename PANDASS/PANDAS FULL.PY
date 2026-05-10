# 🚀 MODULE 1: INTRO TO PANDAS

# What is Pandas?

# Library for data analysis

# Works like Excel table / SQL table

# Install

# pip install pandas

# Import

import pandas as 


# 📊 MODULE 2: CORE DATA STRUCTURES


# 1. Series (1D)

s = pd.Series([10,20,30])

print(s)

# 2. DataFrame (2D table)

data = {
    "name": ["Ram","Shyam"],
    "marks": [80,90]
}
df = .DataFrame(data)
print(df)

# 👉 These are the main objects in Pandas


# 🔍 MODULE 3: VIEW & SELECT DATA


# df.head()
# df.tail()
# df.info()
# df.describe()

# Select

df["name"]          # column
df.loc[0]           # row
df.iloc[0:2]        # slicing

# 🧹 MODULE 4: DATA CLEANING (VERY IMPORTANT)


# df.isnull()
# df.dropna()
# df.fillna(0)
# df.duplicated()
# df.drop_duplicates()

# 👉 Real-world data is messy — cleaning is core skill

# 🔃 MODULE 5: FILTERING & SORTING

df[df["marks"] > 80]

df.sort_values("marks")

# 📊 MODULE 6: GROUPBY (MOST IMPORTANT)

df.groupby("name")["marks"].mean()

# 👉 Used for analysis like:


# average

sum
# count

# 🔗 MODULE 7: MERGE / JOIN

# pd.merge(df1, df2, on="id")

# 👉 Like SQL JOIN


# 🔄 MODULE 8: RESHAPING DATA

df.pivot_table(values="marks", index="name")

# 📅 MODULE 9: DATE & TIME

df["date"] = pd.to_datetime(df["date"])

# 👉 Important for real datasets


# 📈 MODULE 10: VISUALIZATION

df.plot()

# 🧠 MODULE 11: ADVANCED

# apply()

map()

# lambda functions

# vectorization

# 🧪 MODULE 12: MINI PROJECT (VERY IMPORTANT)


# Do this after learning:


# Student marks analysis
# Sales dashboard
# CSV dataset cleaning

# 👉 Real projects = real skill

# ⚡ FAST LEARNING PLAN (7 DAYS)

# Day 1 → Basics + DataFrame
# Day 2 → Selection + Filtering
# Day 3 → Cleaning
# Day 4 → GroupBy
# Day 5 → Merge + Join
# Day 6 → Time + Advanced
# Day 7 → Project

# 💡 IMPORTANT ADVICE (REAL TALK)

# From community experience:

# “Best way to learn pandas is using real data”

# 👉 Don’t just watch — code daily