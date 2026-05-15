# 🔥 3️⃣ Handling Missing Values (Advanced Pandas)

# 👉 Missing values = NaN / None / खाली data

# Simple मा:
# 👉 data हराएको ठाउँलाई smart तरिकाले handle गर्ने method 🔥

# 🧠 Why important?

# 👉 Real dataset मा:

# salary missing 💸
# marks missing 📊
# age missing 👤

# 👉 If not handled → wrong AI result ❌

# 📊 Example Data
# import pandas as pd
# import numpy as np

# df = pd.DataFrame({
#     "name": ["Ram", "Hari", "Sita", "Gita"],
#     "marks": [80, np.nan, 85, np.nan],
#     "age": [20, 21, np.nan, 22]
# })

# print(df)
# 📤 Output
#    name  marks   age
# 0   Ram   80.0  20.0
# 1  Hari    NaN  21.0
# 2  Sita   85.0   NaN
# 3  Gita    NaN  22.0
# 🔥 1️⃣ Check Missing Values
# df.isnull().sum()

# 👉 कति missing छ देखाउँछ

# 📤 Output
# name     0
# marks    2
# age      1
# 🔥 2️⃣ Fill with Mean (BEST for numbers)
# df["marks"].fillna(df["marks"].mean(), inplace=True)
# 🧠 Meaning

# 👉 marks को missing value → average ले replace

# 🔢 Mean calculation

# 2
# 80+85
# 	​

# =82.5

# 🔥 3️⃣ Fill with Median (robust method)
# df["age"].fillna(df["age"].median(), inplace=True)
# 🧠 Meaning

# 👉 middle value use हुन्छ (outlier safe)

# 🔥 4️⃣ Fill with custom value
# df["name"].fillna("Unknown", inplace=True)
# 🔥 5️⃣ Forward Fill (ffill)

# 👉 previous value copy गर्छ

# df.fillna(method="ffill")
# 📤 Example
# 80 → 80 → 85 → 85
# 🔥 6️⃣ Backward Fill (bfill)
# df.fillna(method="bfill")
# 🧠 Meaning

# 👉 next value ले fill गर्छ

# 🔥 7️⃣ Drop vs Fill (IMPORTANT)
# Method	Meaning
# dropna()	data delete ❌
# fillna()	data fix ✔
# ⚠️ Real Rule

# 👉 ML / AI मा:

# ❌ drop धेरै data → bad model
# ✔ fill smart way → good model
# 🔥 Real Life Example

# 👉 Student dataset:

# marks missing → mean fill
# age missing → median fill
# name missing → "Unknown"
# ⚡ One Line Summary

# 👉 Missing values handle = data clean + AI ready बनाउने process

# 🧪 Practice 🔥
# Q1

# Fill marks with mean

# Q2

# Fill age with median

# Q3

# Fill name with "N/A"

# Q4

# Try forward fill

# 🚀 Next Step

# 👉 अब तिमी advanced Pandas expert level मा पुग्यौ 💪