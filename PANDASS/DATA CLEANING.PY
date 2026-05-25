# DAY 3: Data Cleaning (FULL Nepali + English mix) 🚀

# 👉 यो Pandas को सबैभन्दा practical skill हो (real world data यही हो)

# 🧹 DATA CLEANING के हो?


# 👉 Real data perfect हुँदैन 😵

# यसमा हुन्छ:


# Missing values (NaN)

# Duplicate data

# Wrong format

# Empty cells


# 👉 यी सबै fix गर्ने process = Data Cleaning

# 📊 Example Dataset (Dirty Data 😵)

import pandas as pd


data = { 
    "name" : ["nirmal", "saud", "aura"],
    "marks" : [90, 80, 70],
    "age" : [17, 18, 19]
}

df = pd.DataFrame(data)
print(df)


import pandas as pd



print(pd.__version__)



# 🔍 1️⃣ Missing Values Check


# 👉 Missing value = खाली data (NaN, None)

# Real world data मा अक्सर हुन्छ:

# student marks missing

# name missing

# age missing

# 👉 यस्ता खाली values detect गर्ने process = Missing Values Check


# Pandas मा missing value:

# NaN
# None

# ले देखाइन्छ ❌

# 🧠 Why Check Missing Values?



# | name | marks |
# | ---- | ----- |
# | Ram  | 80    |
# | Hari | NaN   |


# for example

import pandas as pd


data = {
    "name": ["Ram", "Hari", None, "Gita"],
    "marks": [80, None, 85, 70],
    "age": [20, 21, None, 22]
}

df = pd.DataFrame(data)
print(df.isnull())


# 🔥 df.isnull() के हो?

# 👉 Missing value छ कि छैन भनेर check गर्ने method

# Simple मा:

# missing छ → True
# missing छैन → False


# 🔍 1 Check Missing Values (True/False)


df.isnull()

# 👉 Pandas मा missing values check गर्न:



# 👉 df.isnull() = Pandas मा missing value (NaN / None) छ कि छैन check गर्ने method

# Simple मा:
# 👉 Data भित्र खाली (missing) छ कि छैन भनेर True/False देखाउँछ

# 📊 Example
import pandas as pd
import numpy as np

data = {
    "name": ["Ram", "Hari", None],
    "marks": [80, None, 85],
    "age": [20, 21, None]
}

df = pd.DataFrame(data)

print(df.isnull())


# 📤 Original Data
#    name  marks   age
# 0   Ram   80.0  20.0
# 1  Hari    NaN  21.0
# 2  None   85.0   NaN
# 🔍 Missing Values Check

df.isnull()




# | Value | Meaning          |
# | ----- | ---------------- |
# | False | data छ ✔         |
# | True  | data missing छ ❌ |



# 🔢 2️ Count Missing Values (IMPORTANT 🔥)


df.isnull().sum()


# 👉 df.isnull().sum() = प्रत्येक column मा कति missing value छ भनेर count गर्ने method

# Simple मा:
# 👉 True/False होइन, अब number (count) दिन्छ 🔥


import pandas as pd
import numpy as np

data = {
    "name": ["Ram", "Hari", None],
    "marks": [80, None, 85],
    "age": [20, 21, None]
}

df = pd.DataFrame(data)
print(df.isnull().sum())


# 📤 Original Data
#    name  marks   age
# 0   Ram   80.0  20.0
# 1  Hari    NaN  21.0
# 2  None   85.0   NaN



# 🔢 3 Missing Values Count

df.isnull().sum()


# 🧠 बुझ्ने तरिका

# 👉 प्रत्येक column मा:

# name → 1 missing
# marks → 1 missing
# age → 1 missing

# 🔥 Inside Logic (Simple)

# df.isnull()  → True/False matrix बनाउँछ

# .sum()       → True को count गर्छ

# 👉 True = 1
# 👉 False = 0

# 📊 Extra Powerful Trick 🔥
# 👉 Total missing values (whole dataset)


import pandas as pd
import numpy as np

data = {
    "name": ["Ram", "Hari", "sita"],
    "marks": [80, None, 85],
    "age": [20, 21, None]
}

df = pd.DataFrame(data)

print(df.isnull().sum().sum())


# 🧪 Practice (IMPORTANT 🔥)
# Q1

# Create dataset with missing values and count them

# Q2

# Find total missing values in whole DataFrame

# Q3

# Find column with most missing values




# 2️⃣ Drop Missing Data

# 👉 dropna() = missing values (NaN / None) भएको row या column हटाउने method

# Simple मा:
# 👉 जहाँ data खाली छ, त्यो पुरै हटाइदिन्छ ❌

# 📊 Example Data
import pandas as pd
import numpy as np

data = {
    "name": ["Ram", "Hari", None, "Gita"],
    "marks": [80, None, 85, 70],
    "age": [20, 21, None, 22]
}

df = pd.DataFrame(data)
print(df.dropna())



# 📤 Original Data
#    name  marks   age
# 0   Ram   80.0  20.0
# 1  Hari    NaN  21.0
# 2  None   85.0   NaN
# 3  Gita   70.0  22.0

# # 1️⃣ Drop rows with missing values

df.dropna()


# 🧠 बुझ्ने तरिका

# 👉 Row 1 र Row 2 हट्यो किनकि त्यहाँ NaN थियो

# ⚠️ Important Point

# 👉 dropna() default मा row हटाउँछ

# 🧹 2️⃣ Drop columns with missing values
# df.dropna(axis=1)

# 👉 axis=1 = column हटाउने


# 🔥 3️⃣ Inplace (original data change)
# df.dropna(inplace=True)

# 👉 मतलब:

# original df नै change हुन्छ


# | Option       | Meaning          |
# | ------------ | ---------------- |
# | axis=0       | row remove       |
# | axis=1       | column remove    |
# | inplace=True | permanent change |




# ⚡ Real Life Example

# 👉 Student database:

# missing marks ❌
# missing name ❌

# 👉 Clean data चाहिन्छ analysis को लागि

# ⚠️ Problem with dropna

# 👉 data loss हुन्छ 😬
# 👉 धेरै data हट्न सक्छ

# 🧪 Example (safe check)
# df.dropna().shape

# 👉 कति data बाँकी रह्यो हेर्न


# 🧪 Practice 🔥
# Q1

# Drop all rows with missing values

# Q2

# Drop only columns with missing values

# Q3

# Check shape before and after dropna()


# 🔥 3️⃣ Fill Missing Data (fillna()) — BEST METHOD

# 👉 fillna() = missing values (NaN / None) लाई कुनै value ले भरिदिने method

# Simple मा:
# 👉 खाली ठाउँ (missing data) हटाउनुको सट्टा भर्ने काम गर्छ 🧠


# 📊 Example Data
import pandas as pd
import numpy as np

data = {
    "name": ["Ram", "Hari", None, "Gita"],
    "marks": [80, None, 85, 70],
    "age": [20, 21, None, 22]
}

df = pd.DataFrame(data)
print(df.fillna(0))

# 📤 Original Data
#    name  marks   age
# 0   Ram   80.0  20.0
# 1  Hari    NaN  21.0
# 2  None   85.0   NaN
# 3  Gita   70.0  22.0

# 🔥 1️⃣ Fill all missing values with a number
df.fillna(0)

# 👉 fillna(0) = DataFrame भित्र भएका सबै NaN / missing values लाई 0 ले replace गर्ने method

# Simple मा:
# 👉 जहाँ खाली छ, त्यहाँ 0 हालिदिन्छ 🧠


# 📊 Example Data

import pandas as pd
import numpy as np

data = {
    "name": ["Ram", "Hari", None, "Gita"],
    "marks": [80, None, 85, 70],
    "age": [20, 21, None, 22]
}

df = pd.DataFrame(data)
print(df.fillna("hari"))
# 📤 Original Data
#    name  marks   age
# 0   Ram   80.0  20.0
# 1  Hari    NaN  21.0
# 2  None   85.0   NaN
# 3  Gita   70.0  22.0
# 🔥 Apply fillna(0)
df.fillna(0)

# 🧠 बुझ्ने तरिका

# 👉 सबै खाली ठाउँहरू:

# NaN → 0
# None → 0
# ⚠️ Important Point

# 👉 fillna(0) = simple but not always best

# किन?

# name column मा 0 आउनु logical होइन 😅
# 📊 When to use?

# ✔ numbers (marks, age, salary)
# ❌ text (name, city)

# 🔥 Better Practice (Real World)

df["marks"].fillna(df["marks"].mean(), inplace=True)
df["age"].fillna(df["age"].median(), inplace=True)
df["name"].fillna("Unknown", inplace=True)


# ⚡ One Line Summary

# 👉 df.fillna(0) = सबै missing values लाई 0 ले replace गर्ने quick method

# 🧪 Practice 🔥
# Q1

# Create dataset with NaN and apply fillna(0)

# Q2

# Check difference between:

# fillna(0)
# dropna()
# Q3

# Try fillna with different values (10, 100, "N/A")



# 🔁 4️⃣ Duplicate Data Remove


# 
# 👉 drop_duplicates() = repeated (same) data हटाउने method
# 
# Simple मा:
# 👉 एउटै data 2–3 पटक repeat भयो भने, extra copy हटाइदिन्छ ❌

# 📊 Example Data

import pandas as pd

data = {
    "name": ["Ram", "Hari", "Hari", "Sita", "Ram"],
    "marks": [80, 90, 90, 85, 80]
}

df = pd.DataFrame(data)
print(df.drop_duplicates())

# 📤 Original Data
#    name  marks
# 0   Ram     80
# 1  Hari     90
# 2  Hari     90
# 3  Sita     85
# 4   Ram     80
# 🔁 1️⃣ Remove duplicate rows

df.drop_duplicates()


# 🧠 बुझ्ने तरिका

# 👉 duplicate rows हटाइयो:

# Hari (repeat)
# Ram (repeat)
# ⚠️ Important Point

# 👉 default मा पूरै row match भए मात्र duplicate मानिन्छ

मानिन्छ

# 🔥 2️⃣ Specific column basis duplicate remove

df.drop_duplicates(subset=["name"])


# 👉 name repeat भए पनि एकचोटि मात्र राख्यो


# 🔥 3️⃣ Keep option (important)


df.drop_duplicates(keep="first")

# 👉 first occurrence राख्छ

df.drop_duplicates(keep="last")

# 👉 last occurrence राख्छ

# 🧠 Real Life Example

# 👉 Student database मा:

# same student 2 पटक entry भयो 😵
# salary record duplicate भयो 💸

# 👉 Fix = drop_duplicates()

# ⚡ One Line Summary

# 👉 drop_duplicates() = repeated data हटाउने method

# 🧪 Practice 🔥
# Q1

# Create duplicate dataset and remove duplicates

# Q2

# Remove duplicates based only on "name"

# Q3

# Try keep="last"


# 📏 5️⃣ Data Info Check (df.info())

# 👉 df.info() = DataFrame को full summary (information) देखाउने method

# Simple मा:
# 👉 Data भित्र के–के छ भनेर पूरा overview दिन्छ 🔍

# 📊 Example Data
import pandas as pd

data = {
    "name": ["Ram", "Hari", "Sita"],
    "marks": [80, 90, 85],
    "age": [20, 21, 19]
}

df = pd.DataFrame(data)
print(df.info())


# 📏 Use info()
df.info()


# 🧠 बुझ्ने तरिका

# 👉 df.info() ले 4 main कुरा देखाउँछ:

# 1️⃣ Column names

# 👉 name, marks, age

# 2️⃣ Non-Null Count

# 👉 कति data खाली छैन


# Example:

# name → 3 non-null (सबै filled)
# marks → 3 non-null

# 3️⃣ Data Type (Dtype)

# | Column | Type           |
# | ------ | -------------- |
# | name   | object (text)  |
# | marks  | int64 (number) |
# | age    | int64          |

# 4️⃣ Memory usage

# 👉 dataset कति memory use गर्छ

# 🔥 Why info() is important?

# 👉 Real world मा यो first step हुन्छ:

# ✔ missing data check
# ✔ data type check
# ✔ dataset understand गर्न

# ⚡ Real Life Example

# 👉 School database:

# कुन column मा data missing छ?
# marks number हो कि text?
# dataset clean छ कि छैन?

# 👉 सबै answer df.info() ले दिन्छ

# 🧠 One Line Summary

# 👉 df.info() = DataFrame को full summary (structure + missing + type) देखाउने method

# 🧪 Practice 🔥
# Q1

# Run df.info() on dataset with missing values

# Q2

# Check:

# which column has object type
# which has int type
# Q3

# Compare:

df.info() vs df.describe()

# summary

# | Method            | Use               |
# | ----------------- | ----------------- |
# | isnull()          | check missing     |
# | dropna()          | remove missing    |
# | fillna()          | replace missing   |
# | drop_duplicates() | remove duplicates |
