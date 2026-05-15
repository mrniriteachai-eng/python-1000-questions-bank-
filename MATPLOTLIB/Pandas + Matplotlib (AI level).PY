# 🤖 Pandas + Matplotlib के हो?

# 👉 Pandas = data handle गर्ने (read, clean, analyze)

# 👉 Matplotlib = data visualize गर्ने (graph बनाउने)

# 📌 AI workflow:

# Data → Pandas (process) → Matplotlib (visualize) → Insight 🔥

# 📁 Step 1: Real dataset (AI style)

import pandas as pd

data = {
    "StudyHours": [1, 2, 3, 4, 5, 6],
    "Marks": [40, 50, 60, 70, 85, 95]
}

df = pd.DataFrame(data)
print(df)

# 📊 Step 2: Basic Line Plot (Trend analysis)

import matplotlib.pyplot as plt

plt.plot(df["StudyHours"], df["Marks"], marker="o")

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.grid()
plt.show()





# 🧠 First Important Thing

# 👉 यहाँ:

df

# = Pandas DataFrame हो

# Example:

import pandas as pd

data = {
    "StudyHours": [1,2,3,4,5],
    "Marks": [40,50,60,75,90]
}

df = pd.DataFrame(data)

# 🔍 Line-by-line Explanation

# 1️⃣ Import Library

import matplotlib.pyplot as plt

# 👉 matplotlib को plotting module import

# 👉 plt

# = shortcut name

# 2️⃣ Main Plot Function

plt.plot(df["StudyHours"], df["Marks"], marker="o")


plt.plot(df["StudyHours"],df["marks"], marker ="o")

# 👉 line graph बनाउँछ

# अब यसलाई part-by-part बुझौँ 👇

# 🔹 df["StudyHours"]

df["StudyHours"]

# 👉 DataFrame को:

# StudyHours column

# select गर्छ

# 📊 Example Output
1
2
3
4
5

# 👉 X-axis data

# 🔹 df["Marks"]
df["Marks"]

# 👉 Marks column select गर्छ

# 📊 Example Output
40
50
60
75
90

# 👉 Y-axis data

# 🧠 Data Pairing

# | StudyHours | Marks |
# | ---------- | ----- |
# | 1          | 40    |
# | 2          | 50    |
# | 3          | 60    |
# | 4          | 75    |
# | 5          | 90    |




# 📈 Meaning

# 👉 study hours बढ्दै जाँदा
# 👉 marks पनि बढ्दैछ

# 🔹 marker="o"
marker="o"

# 👉 each data point मा circle dot ⚪

# Without marker:

# ❌ only line

# With marker:

# ✅ exact points visible

# 📈 Graph Shape

# Points:

(1,40)
(2,50)
(3,60)
(4,75)
(5,90)

# 👉 line ले connect गर्छ

# 3️⃣ Title

plt.title("Study Hours vs Marks")

# 👉 graph heading/title

# 📌 Meaning

# Graph के देखाइरहेको छ?

# Study Hours vs Marks relationship

# 4️⃣ X-axis Label

plt.xlabel("Study Hours")

# 👉 X-axis को नाम


# 📌 Meaning

# Horizontal axis =
# study hours

# 5️⃣ Y-axis Label

plt.ylabel("Marks")

# 👉 Vertical axis को नाम

# 📌 Meaning

# Vertical axis =
# marks

# 6️⃣ Grid

plt.grid()

# 👉 background मा guide lines add

# 📌 Why useful?

# values compare गर्न सजिलो
# graph पढ्न सजिलो

# 7️⃣ Show Graph

plt.show()

# 👉 graph display गर्छ

# ⚠️ बिना show():
# graph देखिँदैन

# 📈 Final Output

# 👉 upward line graph 📈

# circle markers
# grid lines
# title + labels
# 🧠 AI/Data Science Concept

# This graph helps in:

# trend analysis
# relationship analysis
# prediction understanding
# 🤖 ML Insight

# 👉 This shows:

# positive correlation

# 📈 more study → more marks

# 🎯 Experiment (IMPORTANT)

# Try:

# marker="*"

# Then:

# color="red"
# linestyle="--"

# 👉 AI insight:
# 📈 study बढ्दा marks बढ्दैछ

# 📊 Step 3: Scatter Plot (AI correlation 🔥)


import pandas as pd

data = {
    "StudyHours": [1, 2, 3, 4, 5, 6],
    "Marks": [40, 50, 60, 70, 85, 95]
}

df = pd.DataFrame(data)
print(df)

import matplotlib.pyplot as plt



plt.scatter(df["StudyHours"], df["Marks"], color="green")

plt.title("Correlation: Study vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.grid()
plt.show()


# 🔍 Line-by-line Explanation??

# 1️⃣ Import Pandas
import pandas as pd

# 👉 pandas
# = data handling library

# 👉 pd
# = shortcut name

# 🧠 Pandas use for:
# table data
# CSV files
# analysis
# AI preprocessing

# 2️⃣ Create Dictionary Data
# data = {

# 👉 dictionary start

# 🔹 First Column
# "StudyHours": [1, 2, 3, 4, 5, 6],

# 👉 column name:

# StudyHours

# 👉 values:

# 1,2,3,4,5,6
# 🔹 Second Column
# "Marks": [40, 50, 60, 70, 85, 95]

# 👉 column name:

# Marks

# 👉 values:

# 40,50,60,70,85,95
# 🧠 Relationship

# | StudyHours | Marks |
# | ---------- | ----- |
# | 1          | 40    |
# | 2          | 50    |
# | 3          | 60    |
# | 4          | 70    |
# | 5          | 85    |
# | 6          | 95    |


# 👉 बढी study → बढी marks 📈


# 3️⃣ Create DataFrame

df = pd.DataFrame(data)

# 👉 dictionary लाई:

# table format

# मा convert गर्छ

# 📊 DataFrame Output


#    StudyHours  Marks
# 0           1     40
# 1           2     50
# 2           3     60
# 3           4     70
# 4           5     85
# 5           6     95


# 4️⃣ Print Data

print(df)

# 👉 terminal मा table display

# 5️⃣ Import Matplotlib

import matplotlib.pyplot as plt

# 👉 graph plotting library

# 👉 plt
# = shortcut

# 6️⃣ Scatter Plot

plt.scatter(df["StudyHours"], df["Marks"], color="green")

# 👉 scatter plot बनाउँछ


# अब यसलाई break गरौँ 👇

🔹 df["StudyHours"]
df["StudyHours"]

# 👉 X-axis data

# Output:

# 1
# 2
# 3
# 4
# 5
# 6
# 🔹 df["Marks"]
# df["Marks"]

# 👉 Y-axis data

# Output:

# 40
# 50
# 60
# 70
# 85
# 95
# 🔹 color="green"
# color="green"

# 👉 dots green हुन्छ 🟢

# 📈 Final Points

# Graph मा points:

# (1,40)
# (2,50)
# (3,60)
# (4,70)
# (5,85)
# (6,95)
# 🧠 Important AI Concept

# Scatter plot helps find:

# correlation
# 📈 Here correlation is:
# positive correlation


# Correlation

# 👉 relationship

# Between:

# Study Hours ↔ Marks

# 👉 study बढ्दा marks पनि बढ्दैछ

# 7️⃣ Title

plt.title("Correlation: Study vs Marks")

# 👉 graph heading

# 8️⃣ X-axis Label

plt.xlabel("Study Hours")

# 👉 horizontal axis name

# 9️⃣ Y-axis Label

plt.ylabel("Marks")

# 👉 vertical axis name


# 🔟 Grid

plt.grid()

# 👉 background guide lines


# 📌 graph पढ्न सजिलो हुन्छ


# 1️⃣1️⃣ Show Graph

plt.show()

# 👉 graph display


# ⚠️ बिना यस:
# ❌ graph देखिँदैन

# 📊 Final Output Meaning

# 👉 green scatter dots
# 👉 upward pattern 📈

# Meaning:

# More study hours = higher marks
# 🤖 Real AI/Data Science Use

# Same concept used in:

# salary prediction
# stock analysis
# ML feature analysis
# student performance prediction
# 🎯 Experiment

# Try adding:

s=200
marker="*"

# inside scatter:

plt.scatter(..., s=200, marker="*")


# 👉 AI use:

# pattern detect गर्न

# prediction prepare गर्न

# 📊 Step 4: Bar Chart (Comparison view)

plt.bar(df["StudyHours"], df["Marks"], color="skyblue")

plt.title("Performance Overview")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.show()

# 🧠 Step 5: Add Insight Column (AI thinking)

df["Performance"] = ["Low", "Low", "Medium", "Medium", "High", "High"]
print(df)

# 🔥 Step 6: Real AI Insight Graph

plt.scatter(df["StudyHours"], df["Marks"], s=100)

for i in range(len(df)):
    plt.text(df["StudyHours"][i], df["Marks"][i], df["Marks"][i])

plt.title("AI Style Annotated Data")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.grid()
plt.show()

# 🚀 What you learned (AI level)

# 👉 Pandas:   PANDAS

# dataset creation
# data structuring

# 👉 Matplotlib:

# line trend

# scatter correlation

# bar comparison

# annotation (AI insight)

# 🧠 Real AI Concept


# 👉 This is EXACT same step used in:

# Machine Learning preprocessing

# Data analysis reports

# Prediction modeling

# 🎯 Mini Challenge


# 👉 Try this:


# Add 2 more students
# # Plot:
# Study vs Marks (line + scatter)
# Highlight highest marks



# 🌍 Project: Real World Data Analysis (CSV)

# 👉 अब हामी manual data होइन
# 👉 CSV file (real dataset style) use गर्नेछौँ

# 📁 Step 1: CSV File बनाउने

# मानौँ file name: students.csv

# Name,StudyHours,Marks
# Ram,1,40
# Sita,2,50
# Hari,3,60
# Gita,4,70
# Nirmal,5,85


# 📥 Step 2: CSV Read गर्ने (Pandas)

import pandas as pd

df = pd.read_csv("students.csv")
print(df)

# 👉 अब data file बाट load भयो

# 📊 Step 3: Basic Visualization
import matplotlib.pyplot as plt

plt.plot(df["StudyHours"], df["Marks"], marker="o")

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.grid()
plt.show()

# 🔥 Step 4: Scatter Plot (AI Insight)

plt.scatter(df["StudyHours"], df["Marks"], color="red", s=100)

plt.title("Correlation Analysis")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.grid()
plt.show()

# 👉 यहाँ AI concept:

# relationship detect

# pattern analysis

# 📊 Step 5: Bar Chart (Student Comparison)

plt.bar(df["Name"], df["Marks"], color="skyblue")

plt.title("Student Performance")
plt.xlabel("Name")
plt.ylabel("Marks")

plt.show()

# 🧠 Step 6: AI Feature (Average)

df["Performance"] = df["Marks"].apply(
    lambda x: "High" if x >= 75 else "Low"
)

print(df)

# 🔥 Step 7: Topper Highlight (Pro Level)

max_marks = df["Marks"].max()

colors = ["green" if mark == max_marks else "blue" for mark in df["Marks"]]

plt.bar(df["Name"], df["Marks"], color=colors)

plt.title("Top Performer Highlighted")
plt.show()

# 🧠 What you learned (REAL AI FLOW)

# 👉 Step 1: Data (CSV)
# 👉 Step 2: Pandas read
# 👉 Step 3: Analysis
# 👉 Step 4: Visualization
# 👉 Step 5: Insight generation

# # 🚀 This is EXACT AI workflow

# Used in:

# Machine Learning preprocessing
# Data Science reports
# Business analytics dashboards


# 🎯 FINAL CHALLENGE 🔥

# Try this:

# Add 2 more students in CSV

# Plot:
# Line + Scatter together

# Highlight top 2 students

# Add average column


# 🚢 1) Full AI Data Science Project (Titanic / Salary style)


# हामी example रूपमा Titanic dataset style लिन्छौं (real-world survival analysis)


# 📁 Step 1: Dataset (sample version)

import pandas as pd

data = {
    "Name": ["Ram", "Sita", "Hari", "Gita", "Nirmal"],
    "Age": [22, 25, 30, 18, 28],
    "Fare": [10, 20, 15, 30, 25],
    "Survived": [0, 1, 0, 1, 1]
}

df = pd.DataFrame(data)
print(df)

# 🧠 Step 2: Basic Analysis (AI thinking)

print(df.groupby("Survived")["Age"].mean())

# 👉 survival भएका vs नभएका को age pattern


# 📊 Step 3: Visualization (Survival count)

import matplotlib.pyplot as plt

df["Survived"].value_counts().plot(kind="bar")

plt.title("Survival Count")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Count")

plt.show()

# 📈 Step 4: Age vs Fare (AI pattern)

plt.scatter(df["Age"], df["Fare"], c=df["Survived"], cmap="coolwarm")

plt.title("Age vs Fare (Survival Pattern)")
plt.xlabel("Age")
plt.ylabel("Fare")

plt.show()

# 👉 AI insight:


# color = survival
# pattern detect
# 🎨 2) Advanced Plotting (Seaborn Intro 🔥)


# 👉 Seaborn = Matplotlib को advanced version (beautiful + easier)


# 📦 Install
# pip install seaborn


# 📊 Basic Seaborn Plot

import seaborn as sns
import matplotlib.pyplot as plt

sns.scatterplot(data=df, x="Age", y="Fare", hue="Survived")

plt.title("Seaborn Scatter Plot")
plt.show()
📊 Distribution Plot (AI important)
sns.histplot(df["Age"], bins=5, kde=True)

plt.title("Age Distribution")
plt.show()

# 👉 kde=True = smooth curve (AI distribution)

# 📊 Correlation Heatmap (VERY IMPORTANT 🔥)


import numpy as np

sns.heatmap(df.corr(numeric_only=True), annot=True)

plt.title("Correlation Heatmap")
plt.show()

# 👉 AI use:

# feature selection
# relationship detection
# 📊 3) Mini AI Dashboard (Simple Version 😎)

# 👉 multiple graphs together

fig, axs = plt.subplots(1, 2, figsize=(10,4))

axs[0].bar(df["Name"], df["Fare"])
axs[0].set_title("Fare Comparison")

axs[1].scatter(df["Age"], df["Fare"], c=df["Survived"])
axs[1].set_title("Age vs Fare")

plt.tight_layout()
plt.show()


# 🧠 What you just learned (REAL AI level)

# ✔ Data creation (DataFrame)
# ✔ Group analysis (mean, pattern)
# ✔ Matplotlib visualization
# ✔ Seaborn advanced plots
# ✔ Correlation heatmap (ML concept)
# ✔ Mini dashboard (real analytics)

# 🚀 Real-world meaning

# यो same workflow use हुन्छ:

# 🏦 Salary prediction systems
# 🚢 Titanic survival ML model
# 🏥 medical data analysis
# 📊 business dashboards
# 🎯 Next Level Options

# अब तिमी 3 बाट choose गर्न सक्छौ:

# 🔥 1. Full Machine Learning start (from scratch)

👉 regression, classification

# 📊 2. Seaborn deep mastery

# 👉 10+ advanced plots

# 📈 3. Real dashboard project (like PowerBI style)

# 👉 interactive graphs