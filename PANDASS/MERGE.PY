# 📅  — 5
# 🔗 MERGE / JOIN in Pandas

# 👉 Merge/Join = दुईटा DataFrame लाई combine गर्ने method

# Simple मा:
# 👉 अलग-अलग tables लाई एउटै table बनाउने 🔥


# 🧠 Real Life Example

# सोच:

# 📄 Table 1 → Student 



# # | id | name |
# # | -- | ---- |
# # | 1  | Ram  |
# # | 2  | Hari |
# # | 3  | Sita |


# # 📄 Table 2 → Marks

# | id | marks |
# | -- | ----- |
# | 1  | 80    |
# | 2  | 90    |
# | 3  | 85    |


# 👉 अब हामी चाहन्छौँ:


# | id | name | marks |
# | -- | ---- | ----- |
# | 1  | Ram  | 80    |
# | 2  | Hari | 90    |
# | 3  | Sita | 85    |


# 👉 यही काम merge() ले गर्छ 🔥

# 🔥 1️⃣ Basic Merge

import pandas as pd

df1 = pd.DataFrame({
    "id": [1, 2, 3],
    "name": ["Ram", "Hari", "Sita"]
})

df2 = pd.DataFrame({
    "id": [1, 2, 3],
    "marks": [80, 90, 85]
})

result = pd.merge(df1, df2, on="id")

print(result)


# ANOTHER EXAMPLE OF MERGE 

import pandas as pd 

df1 = pd.DataFrame({
    "id" : [1, 2, 3],
    "name" : ["nirmal", "mohan gatho", "bhupendra"]

    })

df2 = pd.DataFrame({
    "id" : [1, 2, 3],
    "marks" : [80, 90, 100]
})

result = pd.merge(df1, df2, on="id")
print(result)



# 🧠 बुझ्ने तरिका

# 👉 on="id" मतलब:

# id common column हो

# त्यसैको आधारमा join गर

# ⚡ Merge Formula

pd.merge(df1, df2, on="common_column")


# 🔥 2️⃣ INNER JOIN (default)

# 👉 common values मात्र राख्छ


👉 INNER JOIN = केवल common (matching) data मात्र राख्ने method

# Simple मा:

# 👉 दुईटा table बीच जुन ID दुवैमा छ, त्यही मात्र आउने 🔥

# 📊 Example Data

# Table 1 (Students)

pd.merge(df1, df2, on="id", how="inner")

import pandas as pd

df1 = pd.DataFrame({
    "id": [1, 2, 3],
    "name": ["Ram", "Hari", "Sita"]
})


# Table 2 (Marks)

df2 = pd.DataFrame({
    "id": [2, 3, 4],
    "marks": [90, 85, 70]
})


)
# 🔥 INNER JOIN

pd.merge(df1, df2, on="id", how="inner")


# 🧠 कसरी आयो? (Step-by-step)

# 📌 df1 IDs:

1, 2, 3
# 📌 df2 IDs:
2, 3, 4
# 🔍 Common IDs खोजियो

# 👉 दुवैमा भएको मात्र:

2, 3

# 📊 Final Merge

# id	name	marks
# 2	Hari	90
# 3	Sita	85
# ⚠️ Important Point

# 👉 inner join = missing data हटाइन्छ automatically

# id=1 ❌ (marks छैन)
# id=4 ❌ (name छैन)


# 🧠 Real Life Example

# 👉 School system:

# Student list
# Exam marks list

# 👉 Only students who appeared in exam = INNER JOIN 🔥

# ⚡ One Line Summary

# 👉 INNER JOIN = दुवै table मा भएको common data मात्र combine गर्ने method

# 🧪 Practice 🔥
# Q1

# Create two tables and try inner join

# Q2

# What happens if no IDs match?

# Q3

# Change IDs and test output




# 📊 Base Data (same example)

# 👉 Table 1 (Students)

import pandas as pd

df1 = pd.DataFrame({
    "id": [1, 2, 3],
    "name": ["Ram", "Hari", "Sita"]
})
# 👉 Table 2 (Marks)

df2 = pd.DataFrame({
    "id": [2, 3, 4],
    "marks": [90, 85, 70]


    # 🔥 1️⃣ LEFT JOIN (FULL DETAIL)


    pd.merge(df1, df2, on="id", how="left")



#     🧠 Line-by-line meaning
# 🔹 pd.merge()

# 👉 दुईटा DataFrame combine गर्ने function

# 🔹 df1

# 👉 LEFT table (main table)

# 🔹 df2

# 👉 RIGHT table (supporting table)

# 🔹 on="id"

# 👉 common column = id

# 🔹 how="left"

# 👉 LEFT table को सबै data राख्ने

# 📤 LEFT JOIN Output
#    id  name  marks
# 0   1   Ram    NaN
# 1   2  Hari   90.0
# 2   3  Sita   85.0
# 🧠 LEFT JOIN बुझ्ने तरिका

# 👉 df1 (left table) full आउँछ
# 👉 df2 मा नभएको data → NaN हुन्छ

# 🔥 Key Idea
# id=1 → marks छैन ❌ → NaN
# id=2 → match ✔
# id=3 → match ✔
# ⚡ Simple Rule

# 👉 LEFT JOIN = left table full + right match मात्र



# 🔥 2️⃣ RIGHT JOIN (FULL DETAIL)


pd.merge(df1, df2, on="id", how="right")



# 🧠 Line-by-line meaning
# 🔹 how="right"

# 👉 RIGHT table को सबै data राख्ने



# 🧠 RIGHT JOIN बुझ्ने तरिका

# 👉 df2 (right table) full आउँछ
# 👉 df1 मा नभएको data → NaN हुन्छ

# 🔥 Key Idea
# id=4 → name छैन ❌ → NaN
# id=2 → match ✔
# id=3 → match ✔



# ⚡ Simple Rule

# 👉 RIGHT JOIN = right table full + left match मात्र


# 📊 LEFT vs RIGHT (SUPER EASY)


# | Type       | Full data from | Missing data |
# | ---------- | -------------- | ------------ |
# | LEFT JOIN  | df1            | df2 → NaN    |
# | RIGHT JOIN | df2            | df1 → NaN    |



# 🧠 Real Life Example


# 👉 LEFT JOIN (Student system)

# All students list चाहियो

# marks missing भए पनि देखाउने

# 👉 RIGHT JOIN (Exam system)

# All exam records चाहियो

# student missing भए NaN

# ⚡ One Line Summary

# 👉 LEFT JOIN = left table full
# 👉 RIGHT JOIN = right table full

# 🧪 Practice 🔥
# Q1

# Swap df1 and df2 and test LEFT JOIN

# Q2

# What happens if no match?

# Q3

# Compare inner vs left vs right



# 🔥 OUTER JOIN (FULL DETAIL – Pandas MERGE)



# 👉 OUTER JOIN = दुईवटै table को सबै data राख्ने method

# Simple मा:
# 👉 सबै records आउँछ + missing ठाउँमा NaN बस्छ 🔥

# 📊 Base Data
# 👉 Table 1 (Students)



import pandas as pd

df1 = pd.DataFrame({
    "id": [1, 2, 3],
    "name": ["Ram", "Hari", "Sita"]
})


# 👉 Table 2 (Marks)


df2 = pd.DataFrame({
    "id": [2, 3, 4],
    "marks": [90, 85, 70]
})


# 🔥 OUTER JOIN Code


pd.merge(df1, df2, on="id", how="outer")




# 🧠 Line-by-line बुझाइ
# 🔹 pd.merge()

# 👉 दुईटा DataFrame combine गर्ने function

# 🔹 df1

# 👉 left table

# 🔹 df2

# 👉 right table

# 🔹 on="id"

# 👉 common column = id

# 🔹 how="outer"

# 👉 दुवै table को सबै data राख्ने

# 📤 OUTER JOIN Output

#    id  name  marks
# 0   1   Ram    NaN
# 1   2  Hari   90.0
# 2   3  Sita   85.0
# 3   4   NaN   70.0
# 🧠 Step-by-step बुझाइ
# 📌 df1 IDs:
# 1, 2, 3
# 📌 df2 IDs:
# 2, 3, 4
# 🔍 Outer Join Logic

# 👉 सबै unique IDs combine हुन्छ:

# 1, 2, 3, 4



# 📊 Match Analysis


# | id | name | marks | reason        |
# | -- | ---- | ----- | ------------- |
# | 1  | Ram  | NaN   | marks missing |
# | 2  | Hari | 90    | match         |
# | 3  | Sita | 85    | match         |
# | 4  | NaN  | 70    | name missing  |


# ⚡ OUTER JOIN meaning

# 👉 Left + Right = Everything combined

# 🧠 Real Life Example

# 👉 School system:

# Student list
# Exam result list

# 👉 OUTER JOIN gives:

# all students

# all exam records

# missing data → NaN

# 🔥 Comparison (VERY IMPORTANT)

# Join Type	Result

# INNER	only match

# LEFT	left full

# RIGHT	right full

# OUTER	both full 🔥

# ⚡ One Line Summary

# 👉 OUTER JOIN = दुवै table को सबै data combine गर्ने method

# 🧪 Practice 🔥
# Q1

# Change IDs and test outer join

# Q2

# Add more missing values and observe NaN

# Q3

# Compare all joins:

# inner
# left
# right
# outer



