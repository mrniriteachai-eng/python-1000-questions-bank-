# हो

# 🌍 Real-world Dataset Plotting के हो?

# 👉 अब हामी manually list (x, y) होइन

# 👉 CSV / real data file बाट graph बनाउँछौँ

# 📌 Example data:

# students marks file
# sales data
# weather data



# 🧑‍💻 Step 1: Simple Real Dataset (Without file)

# पहिला easy example:

import matplotlib.pyplot as plt

students = ["Ram", "Sita", "Hari", "Gita"]
marks = [80, 90, 75, 85]

plt.bar(students, marks)

plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()

# 👉 यो real-life style data हो


# 📊 Step 2: Scatter (Real relationship example)

import matplotlib.pyplot as plt

study_hours = [1, 2, 3, 4, 5]
marks = [50, 55, 65, 80, 90]

plt.scatter(study_hours, marks, color="green")

plt.title("Study vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.grid()

plt.show()


# 👉 AI concept:
# 📈 more study → more marks


# 📁 Step 3: Real CSV File (IMPORTANT 🔥)

# 👉 Suppose file: data.csv

# name,marks
# Ram,80
# Sita,90
# Hari,75
# Gita,85

# 🧑‍💻 Load with Pandas + Plot


import pandas as pd

data


import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

plt.bar(df["name"], df["marks"])

plt.title("CSV Data Plot")
plt.xlabel("Name")
plt.ylabel("Marks")

plt.show()


# 🧠 What is happening?

# 👉 pandas = data read गर्छ
# 👉 matplotlib = graph बनाउँछ

# 🔥 AI/ML Connection

# Real-world plotting helps:

# 📊 data understanding
# 🔍 pattern finding
# 🤖 model training insights

# Example:

# height vs weight
# salary vs experience
# age vs spending
# 🎯 Practice (Must do)

# 👉 Create dataset:

# names: A, B, C, D
# scores: 60, 70, 85, 95

# Then:

# Bar chart बनाऊ
# Scatter chart बनाऊ
# Title + labels add गर

# 🚀 Mini Project: Student Performance Analysis

# 👉 हामी एउटा real-style dataset बनाउनेछौँ र analyze गर्नेछौँ

# 📁 Step 1: Dataset बनाउने/

import pandas as pd

data = {
    "Name": ["Ram", "Sita", "Hari", "Gita", "Nirmal"],
    "Math": [80, 90, 75, 85, 95],
    "Science": [70, 88, 80, 90, 92],
    "English": [75, 85, 78, 88, 90]
}

df = pd.DataFrame(data)
print(df)

# 📊 Step 2: Average Score निकाल्ने

df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)
print(df)

# 👉 प्रत्येक student को average score

# 📈 Step 3: Bar Chart (Average Score)

import matplotlib.pyplot as plt

plt.bar(df["Name"], df["Average"], color="skyblue")

plt.title("Student Average Performance")
plt.xlabel("Students")
plt.ylabel("Average Marks")

plt.show()


# 📊 Step 4: Subject Comparison (Line Plot)

plt.plot(df["Name"], df["Math"], marker="o", label="Math")
plt.plot(df["Name"], df["Science"], marker="o", label="Science")
plt.plot(df["Name"], df["English"], marker="o", label="English")


plt.title("Subject Wise Comparison")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.legend()
plt.grid()

plt.show()

# 🔥 Step 5: Scatter Plot (Performance Trend)

plt.scatter(df["Math"], df["Science"], color="green")

plt.title("Math vs Science Performance")
plt.xlabel("Math Marks")
plt.ylabel("Science Marks")

plt.grid()

plt.show()

# 🧠 What you learned here

# 👉 Pandas:

# data create
# average calculation

# 👉 Matplotlib:

# bar chart
# line chart
# scatter plot

# 👉 Real AI skill:

# data understanding + visualization

# 🚀 Final Challenge (Important 🔥)

# 👉 Add:

# highest scorer highlight
# pie chart of averages
# CSV file save + load