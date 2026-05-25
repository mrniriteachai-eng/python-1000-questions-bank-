#  2
# : Selection + Filtering (FULL Nepali explanation) 🚀

# 👉 यो Pandas को सबैभन्दा powerful part हो

# 🎯 आज के सिक्ने?

# 1) Column select गर्ने

# 2) Row select गर्ने

# 3) Multiple select

# 4) Filtering (condition use गरेर data निकाल्ने 🔥)


# 📊 Example Dataset


import pandas as pd

data = {
    "name": ["Ram", "Hari", "Sita", "Gita"],
    "marks": [80, 90, 85, 70],
    "age": [20, 21, 19, 22]
}

df = pd.DataFrame(data)
print(df)



# 📊 तिम्रो DataFrame

#    name  marks  age
# 0   Ram     80   20
# 1  Hari     90   21
# 2  Sita     85   19
# 3  Gita     70   22

# 👉 अब यही data बाट हामी Selection + Filtering apply गर्छौँ

# 🔍 1️⃣ Column Select


import pandas as pd


data = {
    "name" : ["nirmal", "saud"],
    "marks": [ 90,100]
}
df = pd.DataFrame(data)
print(df["name"])


df["name"]



# 💡 मतलब: only name column निकालियो

df[["name", "marks"]]

# 👉 Output: name + marks मात्र



# 🔍 2️⃣ Row Select

# 👉 loc (label-based)

df.loc[0]

# 👉 first row आउँछ

# 👉 iloc (index-based)
df.iloc[0]


import pandas as pd


data = {
    "name" : ["nirmal", "saud"],
    "marks": [ 90,100]
}
df = pd.DataFrame(data)
print(df.iloc[0])

# 👉 same result (index use गरेर)

# 👉 Multiple rows

df.iloc[0:2]

# 👉 row 0 र 1

df.loc[0]

# 👉 Ram को पूरा row

df.iloc[0:2]

# 👉 Ram + Hari


# 🔥 loc vs iloc (Important)

# | Method | Use                |
# | ------ | ------------------ |
# | loc    | label (name/index) |
# | iloc   | position (0,1,2)   |






# 🔥 FILTERING के हो?

# 👉 Filtering = condition लगाएर data निकाल्ने process

# Simple मा:
# 👉 जुन data चाहिन्छ, त्यही मात्र निकाल्ने 🔍


# FOR EXAMPLE


import pandas as pd

data = {
    "name" : ["nirmal", "mohan", "bhupendra"],
    "marks" : [20,  95,  90],
    "age" : [18, 20, 21]

}

df = pd.DataFrame(data)

print(df[df["marks"] > 80])



# 🔍 1️⃣ Basic Filtering


# 👉 Marks > 80

df[df["marks"] > 80]

# 💡 Meaning:
# 👉 only those students whose marks > 80


# 🔍 2️⃣ Age condition


# 👉 Age < 21

df[df["age"] < 21]

import pandas as pd 

data = {
    "name" : ["nirmal" , "mohan", "bhupendra"],
    "age" : [18, 20, 22],
    "marks" : [80, 90, 100]

}

df = pd.DataFrame(data)

print(df[(df["marks"] > 80) & (df["age"] < 21)])



# 🔗 3️⃣ Multiple Conditions (IMPORTANT 🔥)


# 👉 AND condition (&)

df[(df["marks"] > 80) & (df["age"] < 21)]


# 👉 OR condition (|)



import pandas as pd 

data = {
    "name" : ["nirmal" , "mohan", "bhupendra"],
    "age" : [18, 20, 22],
    "marks" : [80, 90, 100]

}

df = pd.DataFrame(data)


print(df[(df["marks"] > 85) | (df["age"] > 20)])


# ⚠️ Important Rule

# ❌ Wrong:

df["marks"] > 80 & df["age"] < 21

# ✔ Correct:

(df["marks"] > 80) & (df["age"] < 21)

# 👉 bracket MUST हुन्छ


# in details

import pandas as pd

data = {
    "name": ["Ram", "Hari", "Sita", "Gita"],
    "marks": [80, 90, 85, 70],
    "age": [20, 21, 19, 22]
}

df = pd.DataFrame(data)
print(df)



# 🔥 1️⃣ AND Condition (&)

# 👉 मतलब: दुबै condition true हुनुपर्छ

# 👉 Example:

# Marks > 80 AND Age < 21

import pandas as pd

data = {
    "name": ["Ram", "Hari", "Sita", "Gita"],
    "marks": [80, 90, 85, 70],
    "age": [20, 21, 19, 22]
}

df = pd.DataFrame(data)



print(df[(df["marks"] > 80) & (df["age"] < 21)])



# 🧠 Meaning:
# Sita को marks > 80 ✔
# Sita को age < 21 ✔
# 👉 both true → selected

# 🔥 2️⃣ OR Condition (|)

# 👉 मतलब: कम्तीमा एउटा condition true भए पुग्छ

# 👉 Example:

# Marks > 85 OR Age > 21


import pandas as pd

data = {
    "name": ["Ram", "Hari", "Sita", "Gita"],
    "marks": [80, 90, 85, 70],
    "age": [20, 21, 19, 22]
}

df = pd.DataFrame(data)



print(df[(df["marks"] > 85) | (df["age"] > 21)])



# ⚠️ VERY IMPORTANT RULE 🔥


# ❌ गलत:

df["marks"] > 80 & df["age"] < 21

# ✔ सही:

(df["marks"] > 80) & (df["age"] < 21)

# 👉 कारण:

# Python precedence issue हुन्छ
# bracket MUST हुन्छ

# 🧠 Easy Trick (Exam Tip 💡)

# 👉 Always याद गर:

# AND = &
# OR = |
# प्रत्येक condition = ( ) भित्र
# 📊 Real-Life Example

# 👉 सोच:

# College filter:
# marks > 80 (good student)
# age < 21 (young student)

# 👉 result = scholarship candidates 🎓

# ⚡ One Line Summary

# 👉 Multiple conditions = multiple rules apply गरेर specific data निकाल्ने

# 🧪 Practice (IMPORTANT 🔥)
# Q1

# Marks > 80 AND age > 20

# Q2

# Marks > 85 OR age < 20

# Q3

# Only show names where:

# marks > 80 AND age < 21



# 🔗 Multiple Conditions के हो?

# 👉 Multiple conditions = एकभन्दा धेरै condition एकैचोटि apply गर्ने

# Simple मा:
# 👉 “यो पनि पूरा हुनुपर्छ + त्यो पनि पूरा हुनुपर्छ” type filtering





# 🎯 4️⃣ Specific Column after Filtering के हो?

# 👉 Filtering गरेर निकालिएको data बाट केवल एउटा column मात्र लिनु

# Simple मा:

# 👉 पहिले condition लगाउने

# 👉 अनि चाहिएको column मात्र निकाल्ने

# 📊 Example Data
import pandas as pd

data = {
    "name": ["Ram", "Hari", "Sita", "Gita"],
    "marks": [80, 90, 85, 70],
    "age": [20, 21, 19, 22]
}

# df = pd.DataFrame(data)
# 🔥 Example 1: Marks > 80 भए name मात्र निकाल्ने

df[df["marks"] > 80]["name"]



# 🧠 बुझ्ने तरिका

# 👉 Step by step:

# Step 1: Filter

df["marks"] > 80

# 👉 true/false बनाउँछ

# Step 2: Data filter हुन्छ

df[df["marks"] > 80]

# Step 3: Only column निकालिन्छ

["name"]
# 🔥 Example 2: Age < 21 भए marks मात्र
df[df["age"] < 21]["marks"]



# | Code                           | Result      |
# | ------------------------------ | ----------- |
# | `df[df["marks"] > 80]`         | पूरा row    |
# | `df[df["marks"] > 80]["name"]` | केवल column |


# 🎯 Real Life Example

# 👉 सोच:

# School database छ
# Filter: marks > 80
# अनि केवल "name" चाहियो

# 👉 यही हो real use 🔥

# ⚡ One Line Summary

# 👉 Filter + Column select = specific result निकाल्ने method


🧪 Practice (IMPORTANT 🔥)
Q1

Marks > 80 भए केवल age निकाल

Q2

Age < 21 भए केवल name निकाल

Q3

Marks > 85 भए name + age (hint: double column)


import pandas  as pd
data = {
"name" : ["nirmal", "mohan", "bhupendra"],
"marks" : [10, 20, 30],
"age"  : [18, 19, 20]
}
df = pd.DataFrame(data)
print(df)


import pandas as pd

data = {
    "name": ["Ram", "Hari", "Sita", "Gita"],
    "marks": [80, 90, 85, 70],
    "age": [20, 21, 19, 22]
}

df = pd.DataFrame(data)
print(df)
