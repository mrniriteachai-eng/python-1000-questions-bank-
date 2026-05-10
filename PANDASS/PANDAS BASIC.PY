# 📅  1: Pandas Basics (FULL)

# आज तिमीले सिक्ने:

# Pandas import

# Series के हो
# DataFrame के हो
# DataFrame create गर्ने
# Basic operations



# 1️⃣ Pandas Import

# सबैभन्दा पहिले:

import pandas as pd

# 👉 pd = shortcut (sabai le use गर्छ)


# 2️⃣ Series के हो?

# 👉 Series = 1D data (single column)


import pandas as pd

s = pd.Series([1,2,3,4])
print(s)

# 💡 बुझ:

# left side = index
# right side = value


# 🧠 Important Parts

# 👉 Series मा 2 वटा main चीज हुन्छ:

# 1. Index (left side)
# 0, 1, 2
# 2. Values (right side)
# 80, 90, 85

# 👉 Format:

# index    value


# 🎯 Custom Index दिन मिल्छ

import pandas as pd
s = pd.Series([80, 90, 85], index=["Ram", "Hari", "Sita"])
print(s)
print(s["Ram"])

# ⚡ Series vs List
# | Feature | List       | Series                 |
# | ------- | ---------- | ---------------------- |
# | Index   | No control | Custom index possible  |
# | Data    | Simple     | Powerful (with labels) |


# 🧠 Real Understanding

# 👉 Series = DataFrame को single column

# 👉 DataFrame = धेरै Series मिलेर बनेको

# 🧪 Practice (Try Yourself)
# Q1

# Create Series:

# values: 10, 20, 30
# index: A, B, C

# Q2

# Print value of B



# 📊 DataFrame के हो?

# 👉 DataFrame = 2D data structure (rows + columns)

# Simple मा:
# 👉 DataFrame = table जस्तो data (Excel जस्तै)


# for example
# | Name | Marks |
# | ---- | ----- |
# | Ram  | 80    |
# | Hari | 90    |


# 👉 यो पूरा table = DataFrame


# 🧠 Core Idea

# 👉 DataFrame = धेरै Series मिलेर बनेको हुन्छ

# Example:

# "Name" = 1 Series
# "Marks" = अर्को Series


### for example 
import pandas as pd

data = {
    "name": ["Ram", "Hari", "Sita"],
    "marks": [80, 90, 85]
}

df = pd.DataFrame(data)

print(df)


import pandas as pd

# 👉 Pandas library import गरियो
# 👉 pd = shortcut name

data = {
    "name": ["Ram", "Hari", "Sita"],
    "marks": [80, 90, 85]
}

# 👉 यहाँ तिमीले dictionary बनायौ

# 💡 बुझ:

# "name" = column 1
# "marks" = column 2

# 👉 Values:

# Ram → 80
# Hari → 90
# Sita → 85
df = pd.DataFrame(data)

# 👉 यहाँ dictionary → DataFrame (table) मा convert भयो

# 💡 Important:

# keys = column names
# values = column data
print(df)


# | index | name | marks |
# | ----- | ---- | ----- |
# | 0     | Ram  | 80    |
# | 1     | Hari | 90    |
# | 2     | Sita | 85    |


# ⚡ Important Points

# ✔ index automatically create हुन्छ (0,1,2)
# ✔ each column = Series
# ✔ पूरा table = DataFrame


# 🧱 DataFrame Structure (Full Concept)

# 👉 DataFrame = rows + columns + data (table)


# 📊 Example फेरि हेरौँ

import pandas as pd
data  = {
    "name" : ["nirmal","mohan","bhupendra"],
    "marks" : [20, 97, 99]

}

pf = pd.DataFrame(data)
print(df)



# 🧠 Structure Breakdown
# 1️⃣ Rows (Horizontal)

# 👉 यो line-wise data हो

# 0 → nirmal, 20  
# 1 → mohan, 97 
# 2 → bhupendra, 99 

# 👉 Total rows = 3

# 2️⃣ Columns (Vertical)

# 👉 Data को categories

# name
# marks

# 👉 Total columns = 2+

# 3️⃣ Index (Row labels)

# 👉 left side मा देखिने number

0, 1, 2

# 👉 Pandas automatically बनाउँछ

# 4️⃣ Data (Actual values)

# 👉 Real content

# nirmal, mohan, bhupendra  
20, 97, 99
# 📦 Visual Understanding
#         columns
#         ↓
#     name   marks
# 0   Ram      80   → row 0
# 1   Hari     90   → row 1
# 2   Sita     85   → row 2
# ↑
# index
# 🔥 Important Concept

# 👉 Each column = Series

# Example:

# df["name"]   → Series
# df["marks"]  → Series


# ⚡ Access Structure

# Column access

df["name"]
# Row access
df.loc[0]
# Shape (rows, columns)

# df.shape


# 🧠 One Line Summary

# 👉 DataFrame = collection of Series arranged in rows & columns

# 🧪 Practice (Must Do 🔥)
# Q1

# Find:

# number of rows
# number of columns
# Q2

# Print:

# only "marks" column
# only first row
# Q3

# Add new column:

# age = [20, 21, 19]


# ⚡ Create DataFrame (Different Ways)

# 1. Dictionary बाट (most common)





# 👉 Dictionary = column → data

data = {
    "column_name": [values]
}

# 👉 अनि त्यसलाई DataFrame मा convert गर्छौँ:

df = pd.DataFrame(data)


# 📊 Full Example

import pandas as pd

data = {
    "name": ["Ram", "Hari", "Sita"],
    "marks": [80, 90, 85]
}

df = pd.DataFrame(data)

print(df)


# 🧠 Deep Understanding

# 👉 Dictionary structure:

"name"  → ["Ram", "Hari", "Sita"]
"marks" → [80, 90, 85]

# 👉 मतलब:

# keys = column names
# values = column data
# ⚠️ Important Rule

# 👉 All columns must have same number of values

# ❌ Wrong:

data = {
    "name": ["Ram", "Hari"],
    "marks": [80, 90, 85]   # extra value ❌
}

# ✔ Correct:

# same length for all columns

# 🔥 More Columns Example
data = {
    "name": ["Ram", "Hari", "Sita"],
    "marks": [80, 90, 85],
    "age": [20, 21, 19]
}

df = pd.DataFrame(data)
print(df)


# 🎯 Custom Index दिन मिल्छ

df = pd.DataFrame(data, index=["A", "B", "C"])
print(df)


# ⚡ Column Order Control
df = pd.DataFrame(data, columns=["name", "age", "marks"])
# 🧠 One Line Summary

# 👉 Dictionary (key:value) → DataFrame (column:data)

# ⚡ List of Lists बाट DataFrame बनाउने


import pandas as pd

data = [
    ["Ram", 80],
    ["Hari", 90],
    ["Sita", 85]
]

df = pd.DataFrame(data, columns=["name", "marks"])

print(df)




# 🧪 Practice (DO THIS 🔥)
Q1

# Create DataFrame:

name: Ram, Shyam, Hari
age: 20, 22, 21

Q2

# Add new column:

marks: 80, 85, 

Q3

# Set custom index:

X, Y, Z