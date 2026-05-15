# 📅 : 
# 4
# GROUPBY (🔥 REAL DATA ANALYSIS POWER)

# 👉 GroupBy = data लाई group गरेर analysis गर्ने method

# Simple मा:
# 👉 समान category भएका data लाई group गरेर sum, mean, count निकाल्ने


# 📊 Example Dataset

import pandas as pd

data = {
    "name": ["Ram", "Hari", "Sita", "Gita", "Ram"],
    "subject": ["Math", "Math", "Science", "Math", "Science"],
    "marks": [80, 90, 85, 70, 95]
}

df = pd.DataFrame(data)
print(df.groupby("subject"))




# 🔥 1️⃣ Basic GroupBy

# 👉 Subject अनुसार group
df.groupby("subject")

# 👉 यो alone ले output देखाउँदैन
# 👉 but group बनाउँछ internally

# 💡 मतलब:

# Math group बन्यो
# Science group बन्यो
# 🔥 Group लाई देखाउने तरीका
# 👉 Sum निकालेर देखाउने



import pandas as pd

data = {
    "name": ["Ram", "Hari", "Sita", "Gita", "Ram"],
    "subject": ["Math", "Math", "Science", "Math", "Science"],
    "marks": [80, 90, 85, 70, 95]
}

df = pd.DataFrame(data)
print(df.groupby("subject")["marks"].sum())


####

df.groupby("subject")["marks"].sum()


# 🧠 बुझ्ने तरिका

# 👉 Math group:

# 80 + 90 + 70 = 240

# 👉 Science group:

# 85 + 95 = 180
# ⚡ Simple Concept

# 👉 groupby() = data लाई category अनुसार छुट्याउने method



# 🔥 Real Life Example

# 👉 School मा:

# subject wise result निकाल्ने
# class wise average
# department wise salary

# ⚠️ Important Note

# ❌ मात्र groupby ले output देखाउँदैन
# ✔ sum / mean / count चाहिन्छ

# ⚡ One Line Summary

# 👉 Basic GroupBy = समान category data लाई group गर्ने process

# 🧪 Practice 🔥
# Q1

# Group by subject

# Q2

# Group by subject and find sum

# Q3

# Try groupby on name column



# 🔥 2️⃣ Sum निकाल्ने (MOST IMPORTANT)


# 🔥 GroupBy + Sum के हो?

# 👉 group गरेर values को total (sum) निकाल्ने

# Simple मा:

# 👉 एउटै category का सबै values जोड्ने ➕




import pandas as pd

data = {
    "name": ["Ram", "Hari", "Sita", "Gita", "Ram"],
    "subject": ["Math", "Math", "Science", "Math", "Science"],
    "marks": [80, 90, 85, 70, 95]
}
df.groupby("subject")["marks"].sum()
df = pd.DataFrame(data)
print(df)


#### sum

import pandas as pd

data = {
    "name": ["Ram", "Hari", "Sita", "Gita", "Ram"],
    "subject": ["Math", "Math", "Science", "Math", "Science"],
    "marks": [80, 90, 85, 70, 95]
}

df = pd.DataFrame(data)

print(df.groupby("subject")["marks"].sum())




########
import pandas as pd

data = {
    "name" : ["nirmal", "mohan", "bhupendra"],
    "subject" : ["math", "physics" , "physics", "math"],
    "marks" : [80, 90, 100,70]

}
df = pd.DataFrame(data)

print(df.groupby("subject")["marks"].sum())





# 📊 Mean (Average) के हो?


# 👉 Mean = सबै values add गरेर total count ले divide गर्ने

# Formula:

# MEAN = SUM OF VALUE / NUMBER OF VALUE


# Math marks:

80, 90, 70

# 🔥 Step-by-step Calculation

# 👉 Step 1: Add all values

80 + 90 + 70 = 240

# 👉 Step 2: Count values

# 3 values

# 👉 Step 3: Divide

# 240÷3=80

# 📤 Final Mean

# Math average = 80

# 🔥 Pandas मा कसरी गर्ने?




import pandas as pd

data = {
    "name": ["Ram", "Hari", "Sita", "Gita", "Ram"],
    "subject": ["Math", "Math", "Science", "Math", "Science"],
    "marks": [80, 90, 85, 70, 95]
}

df = pd.DataFrame(data)

print(df.groupby("subject")["marks"].mean())


df.groupby("subject")["marks"].mean()


# 🧠 Science कसरी आयो?

# Science marks:

85, 95

# 👉 Add:

85 + 95 = 180

# 👉 Count:

# 2 values

# 👉 Mean:

# 180÷2=90

# ⚡ Easy Trick

# mean = sum ÷ count

# 🧠 Real Life Example


# 👉 Student average marks
# 👉 Company average salary
# 👉 Average sales

# ⚡ One Line Summary

# 👉 Mean = total values ÷ total number of values

# 🧪 Practice 🔥
# Q1

# Find mean of:

# 10, 20, 30
# Q2

# Use Pandas:

df.groupby("subject")["marks"].mean()




# 🔥 count() in Pandas GroupBy





# 👉 count() = कति वटा values/data छन् भनेर count गर्ने method

# Simple मा:

# 👉 number of entries गणना गर्ने 🔢

📊 Example Data

import pandas as pd

data = {
    "name": ["Ram", "Hari", "Sita", "Gita", "Ram"],
    "subject": ["Math", "Math", "Science", "Math", "Science"],
    "marks": [80, 90, 85, 70, 95]
}

df = pd.DataFrame(data)
print(df.groupby("subject")["marks"].count())
    



    # 🔥 Count by Subject

df.groupby("subject")["marks"].count()


# 🧠 कसरी आयो
# 👉 Math group

# Math marks:

80, 90, 70

# 👉 total values = 3

# 👉 Science group

# Science marks:

85, 95

# 👉 total values = 2

# 📊 Visual Understanding
# Subject	Students Count
# Math	3
# Science	2
# ⚡ Meaning

# 👉 Math subject मा 3 वटा entries छन्
# 👉 Science subject मा 2 वटा entries छन्

# 🔥 Another Example
# 👉 Name-wise count


df.groupby("name")["marks"].count()


# 🧠 Meaning

# 👉 Ram दुई पटक आएको छ
# 👉 अरू 1-1 पटक

# ⚠️ Important

# 👉 count() only non-null values count गर्छ

# Example:

# NaN भए count गर्दैन ❌
# ⚡ One Line Summary

# 👉 count() = data कति वटा छ भनेर गणना गर्ने method

# 🧪 Practice 🔥
# Q1

# Count students per subject

# Q2

# Count entries per name

# Q3

# Add NaN and test count()

# 🔥 agg() in Pandas (Multiple Analysis)

# 👉 agg() = एउटै time मा multiple operations गर्ने method

# Simple मा:
# 👉 एकैचोटि:

# sum
# mean
# count
# max
# min

# सबै निकाल्न मिल्छ 🔥

# 📊 Example Data

import pandas as pd

data = {
    "name": ["Ram", "Hari", "Sita", "Gita", "Ram"],
    "subject": ["Math", "Math", "Science", "Math", "Science"],
    "marks": [80, 90, 85, 70, 95]
}

df = pd.DataFrame(data)
print(df.groupby("subject")["marks"].agg(["sum", "mean", "count"]))


# 🔥 Basic agg() Syntax


df.groupby("subject")["marks"].agg(["sum", "mean", "count"])


# 🧠 Step-by-step Understanding

# 👉 Math Group


# Marks:

80, 90, 70


# 🔢 sum

80 + 90 + 70 = 240

# 📊 mean

# 240÷3=80

# 🔢 count

# 3 values

# 👉 Science Group


# Marks:


85, 95

# 🔢 sum

85 + 95 = 180

# 📊 mean

# 180÷2=90

# 🔢 count

# 2 values

# ⚡ Why agg() is Powerful?


# 👉 Without agg:

df.groupby("subject")["marks"].sum()
df.groupby("subject")["marks"].mean()
df.groupby("subject")["marks"].count()

# 👉 धेरै lines 😵

# 👉 With agg:

df.groupby("subject")["marks"].agg(["sum", "mean", "count"])

# 👉 one line 🔥

# 🔥 More Functions

df.groupby("subject")["marks"].agg(["max", "min"])

# 🧠 Real Life Use

# 👉 Company:

# department salary analysis

# 👉 School:

# subject result summary

# 👉 Shop:

# product sales report
# ⚡ One Line Summary

# 👉 agg() = multiple analysis functions एकैचोटि चलाउने method

# 🧪 Practice 🔥
# Q1

# Use:

# agg(["sum", "mean", "count"])
# Q2

# Try:

# agg(["max", "min"])
# Q3

# Group by name and use agg()