#  6

# 🔥 Reshaping Data (Pandas)

# 👉 Reshaping = data को shape (structure) change गर्ने process


# Simple मा:

# 👉 rows ↔ columns change गर्ने काम 🔁


# 🧠 Why Reshaping?

# Real data messy हुन्छ:

# long format
# wide format
# columns धेरै / कम

# 👉 analysis को लागि shape change गर्नुपर्छ


# 📊 Example Data (LONG format)

import pandas as pd

data = {
    "name": ["Ram", "Ram", "Hari", "Hari"],
    "subject": ["Math", "Science", "Math", "Science"],
    "marks": [80, 85, 90, 95]
}

df = pd.DataFrame(data)
print(df)


# 🔥 1️⃣ Pivot (MOST IMPORTANT 🔥)

# 👉 rows → columns बनाउने

import pandas as pd

data = {
    "name": ["Ram", "Ram", "Hari", "Hari"],
    "subject": ["Math", "Science", "Math", "Science"],
    "marks": [80, 85, 90, 95]
}

df = pd.DataFrame(data)
print(df.pivot(index="name", columns="subject", values="marks"))

df.pivot(index="name", columns="subject", values="marks")


# 🧠 बुझ्ने तरिका

# 👉 name = rows
# 👉 subject = columns
# 👉 marks = values



# 🔥 2️⃣ Melt (Reverse of Pivot)

👉 columns → rows बनाउने



import pandas as pd

data = {
    "name": ["Ram", "Ram", "Hari", "Hari"],
    "subject": ["Math", "Science", "Math", "Science"],
    "marks": [80, 85, 90, 95]
}

df = pd.DataFrame(data)


print(df_wide = df.pivot(index="name", columns="subject", values="marks").reset_index())



import pandas as pd

data = {
    "name": ["Ram", "Ram", "Hari", "Hari"],
    "subject": ["Math", "Science", "Math", "Science"],
    "marks": [80, 85, 90, 95]
}

df = pd.DataFrame(data)


print(df
import pandas as pd

data = {
    "name": ["Ram", "Hari", "Sita", "Gita", "Ram"],
    "subject": ["Math", "Math", "Science", "Math", "Science"],
    "marks": [80, 90, 85, 70, 95]
}

df = pd.DataFrame(data)

print(df.groupby("subject")["marks"].sum()))

pd.melt(df_wide, id_vars="name")





# 🧠 Meaning

# 👉 wide data लाई फेरि long बनाउने 🔁


🔥 3️⃣ Pivot Table (Advanced 🔥)

👉 aggregation सहित pivot


👉 Pivot Table = data reshape + aggregation (calculation) एकैचोटि गर्ने method

Simple मा:
👉 rows/columns organize गर्छ + sum/mean/count निकाल्छ 🔥


import pandas as pd

data = {
    "name": ["Ram", "Ram", "Hari", "Hari", "Sita"],
    "subject": ["Math", "Science", "Math", "Science", "Math"],
    "marks": [80, 85, 90, 95, 88]
}

df = pd.DataFrame(data)
print(df.pivot_table(values="marks", index="name", columns="subject", aggfunc="sum"))


# 🔥 Pivot Table (Basic)

df.pivot_table(values="marks", index="name", columns="subject", aggfunc="mean")


# 🧠 Step-by-step बुझाइ

🔹 values="marks"

# 👉 कुन data calculate गर्ने? → marks

🔹 index="name"

# 👉 rows मा के राख्ने? → student name

🔹 columns="subject"

# 👉 columns मा के राख्ने? → subject

🔹 aggfunc="mean"

# 👉 calculation के गर्ने? → average

# 🔥 Why Pivot Table Powerful?

# 👉 एकैचोटि:

# reshape data 🔁

# calculation 📊

# 🔥 2️⃣ Sum with Pivot 

df.pivot_table(values="marks", index="name", columns="subject", aggfunc="sum")



# 🔥 3️⃣ Count Example

df.pivot_table(values="marks", index="subject", aggfunc="count")

# 🧠 Pivot vs Pivot Table

# | Feature            | pivot          | pivot_table       |
# | ------------------ | -------------- | ----------------- |
# | duplicate handling | ❌              | ✔                 |
# | aggregation        | ❌              | ✔                 |
# | use                | simple reshape | advanced analysis |

# 🔥 Real Life Use

# 👉 School result system
# 👉 Business sales report
# 👉 AI dataset summary
# 👉 Excel reporting (very common in jobs)

# ⚡ One Line Summary

# 👉 Pivot Table = reshape + calculate (mean/sum/count) together

# 🧪 Practice 🔥
# Q1

# Find average marks using pivot_table

# Q2

# Find sum of marks per subject

# Q3

# Try count aggregation
