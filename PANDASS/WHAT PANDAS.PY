# 1  
# 🐼 Pandas भनेको के हो?


# 👉 Pandas = Python को library हो जसले data (table form) लाई handle गर्न help गर्छ

# Simple मा:
# 👉 Pandas ले data लाई store, clean, analyze गर्न मिल्छ



# 📊 Real Example

# तिमी Excel use गर्छौ होला नि?

# | Name  | Marks |
# | ----- | ----- |
# | Ram   | 80    |
# | Shyam | 90    |


# 👉 यो table = Pandas DataFrame

# So,

# Excel table = Pandas DataFrame
# SQL table = Pandas DataFrame


# 🧠 किन Pandas चाहिन्छ?

# Real life मा data clean हुँदैन 😅
# जस्तो:

# missing values (NaN)
# duplicate data
# wrong format

# 👉 Pandas ले solve गर्छ:

# ✔ Data clean गर्ने
# ✔ Filter गर्ने
# ✔ Calculation (sum, average)
# ✔ Analysis गर्ने

# 🔥 Simple Code Example


import pandas as pd

data = {
    "name": ["Ram", "Shyam"],
    "marks": [80, 90]
}

df = pd.DataFrame(data)

print(df)


# 🧱 Pandas का main parts

# 1. Series (1D)

# 👉 single column जस्तो

import pandas as pd

data = { 
    "name" : ["nirmal", "saud"],
    "marks" : [90,100]
}

pf = pd.DataFrame(data)

print(pf)


s = pd.Series([10,20,30])

# 2. DataFrame (2D)

# 👉 full table

df = pd.DataFrame(data)

# 👉 सबैभन्दा important = DataFrame


# ⚡ Short मा

# 👉 Pandas = Python भित्रको Excel

# 🎯 कहाँ use हुन्छ?

# Data Science

# AI / Machine Learning

# Business

# Student result analysis

# 💡 Real Understanding

# Without Pandas ❌

# 👉 Data handle गर्न गाह्रो

# With Pandas ✅

# 👉 Easy + Fast + Powerful

