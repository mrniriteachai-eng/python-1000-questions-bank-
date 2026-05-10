# 🔥 2️⃣ Lambda Function (Quick function in Pandas)

# 👉 Lambda = छोटो (one-line) function

# Simple मा:
# 👉 normal function लेख्नु भन्दा fast + short way हो ⚡

# 🧠 Normal Function vs Lambda
# ❌ Normal function
# def add(x):
#     return x + 5
# ⚡ Lambda function
# lambda x: x + 5
# 📊 Example Data
# import pandas as pd

# df = pd.DataFrame({
#     "name": ["Ram", "Hari", "Sita"],
#     "marks": [80, 90, 85]
# })
# 🔥 1️⃣ Add 5 to marks using lambda
# df["marks_plus_5"] = df["marks"].apply(lambda x: x + 5)
# print(df)
# 📤 Output
#    name  marks  marks_plus_5
# 0   Ram     80            85
# 1  Hari     90            95
# 2  Sita     85            90
# 🧠 बुझ्ने तरिका

# 👉 प्रत्येक marks मा:

# 80 → 85
# 90 → 95
# 85 → 90
# 🔥 2️⃣ Pass/Fail using Lambda
# df["result"] = df["marks"].apply(lambda x: "Pass" if x >= 80 else "Fail")
# print(df)
# 📤 Output
#    name  marks result
# 0   Ram     80   Pass
# 1  Hari     90   Pass
# 2  Sita     85   Pass
# 🧠 Logic

# 👉 condition:

# marks >= 80 → Pass ✔
# else → Fail ❌
# 🔥 3️⃣ Lambda with multiple columns
# df["grade"] = df["marks"].apply(lambda x: "A" if x >= 85 else "B")
# 🧠 Why Lambda important?

# 👉 AI / Data Science मा:

# fast transformation ⚡
# clean code 🧹
# dataset processing 📊
# ⚡ Real Life Use

# 👉 Salary increase
# 👉 Pass/Fail system
# 👉 Data cleaning
# 👉 Feature engineering (AI 🔥)

# ⚡ One Line Summary

# 👉 Lambda = छोटो function जसले एकै line मा data transform गर्छ

# 🧪 Practice 🔥
# Q1

# Add 10 to all marks

# Q2

# Make grade system:

# 90+ = A
# 80+ = B
# else = C
# Q3

# Create "High/Low" column