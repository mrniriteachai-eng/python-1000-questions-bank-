

# 📅 DATE & TIME (Pandas Full Guide 🔥)

# 👉 Pandas मा Date & Time handling = datetime data manage गर्ने method

# Simple मा:
# 👉 time, date, year, month, day analysis गर्न use हुन्छ ⏰

# 🧠 Why Date & Time important?

# 👉 Real world data मा:

# sales date 📊
# student attendance 📅
# stock price ⏰
# weather data 🌦️

# 🔥 1️⃣ Convert to DateTime

# 👉 string date → proper datetime


import pandas as pd

df = pd.DataFrame({
    "date": ["2026-01-01", "2026-01-02", "2026-01-03"],
    "sales": [100, 150, 200]
})

df["date"] = pd.to_datetime(df["date"])

print(df)


import pandas as np


df = pd.DataFrame({
    "data" : ["2083-01-24", "2083-o1-25", "2083-01-26"],
    "sales" : [100, 300, 200]


})


# 🧠 Meaning

# 👉 अब date column “string” होइन
# 👉 datetime type भयो


# 🔥 2️⃣ Extract Year / Month / Day


import pandas as pd

df = pd.DataFrame({
    "date": ["2026-01-01", "2026-01-02", "2026-01-03"],
    "sales": [100, 150, 200]
})

df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["day"] = df["date"].dt.day

print(df)


# 🧠 बुझ्ने तरिका

# 👉 .dt = datetime tools


# | Feature  | Meaning        |
# | -------- | -------------- |
# | dt.year  | year निकाल्ने  |
# | dt.month | month निकाल्ने |
# | dt.day   | day निकाल्ने   |



# 🔥 3️⃣ Date Filtering (VERY IMPORTANT 🔥)
# 👉 Specific date filter


# df[df["date"] == "2026-01-02"]



# 👉 Range filter


# df[df["date"] > "2026-01-01"]



# 🔥 4️⃣ Set Date as Index


# df.set_index("date", inplace=True)
# print(df)



# 🧠 Why useful?

# 👉 time series analysis easy हुन्छ



# 5️⃣ Resample (Advanced 🔥)

# 👉 monthly / weekly summary


# df.resample("D").sum()


# | Code | Meaning |
# | ---- | ------- |
# | "D"  | daily   |
# | "M"  | monthly |
| "Y"  | yearly  |


# 📊 Real Life Example

# 👉 Shop sales:

# daily sales total
# monthly profit
# yearly growth
# ⚡ One Line Summary

# 👉 Date & Time in Pandas = time-based data analysis (trends, patterns निकाल्ने)

# 🧪 Practice 🔥
# Q1

# Convert string date to datetime

# Q2

# Extract year, month, day

# Q3

# Filter data by date

# Q4

# Try set_index("date")