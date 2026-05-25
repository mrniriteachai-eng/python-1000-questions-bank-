# 📊 Matplotlib के हो?

# Matplotlib Python को एउटा powerful library हो जसले graphs / charts / data visualization बनाउन प्रयोग हुन्छ।

# 👉 Simple भाषामा:

# Data लाई picture (graph) मा बदल्ने tool हो।

# 🔥 Matplotlib किन प्रयोग गर्ने?

# 📈 Line graph (trend देखाउन)

# 📊 Bar chart (comparison)

# 🥧 Pie chart (percentage)

# 📉 Data analysis visualization (AI/ML मा धेरै use हुन्छ)

# ⚙️ Install गर्ने तरिका

# VS Code terminal मा:

# pip install matplotlib


# 🎯 AI/Engineering मा किन important?

# Data analysis गर्न

# Machine learning result visualize गर्न

# Reports बनाउने

# Eg


import matplotlib.pyplot as plt

subjects = ["Math", "Science", "English"]
marks = [80, 90, 75]

plt.plot(subjects, marks)
plt.show()


#### 

import matplotlib.pyplot as plt

name  = ["nirmal", "bhupen", "mahesh"]

age = [18, 19, 20]

plt.plot(name, age)
plt.show()




####


# 👉 यो simple line graph हो।




# 📊 MATPLOTLIB FULL COURSE (STEP BY STEP)

# 🟢 Lesson 1: Introduction + Setup


# 📦 Install

# pip install matplotlib

# 🟢 Lesson 2: Line Graph (Basic)



import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)

plt.title("My First Graph")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.show()

import matplotlib.pyplot as plt

x = [3, 4, 5]

y = [4, 6, 7]

plt.plot(x, y)

plt.title("my first graph")
plt.xlabel("num")
plt.ylabel("number")

plt.show()





# 📌 यहाँ:

# title() = graph name

# xlabel() = num

# ylabel() = number




# 🔍 Step-by-step explanation


# 1️⃣
import matplotlib.pyplot as plt

# 👉 यहाँ:

# matplotlib.pyplot = graph बनाउने module

# plt = shortcut name (बारम्बार लेख्न सजिलो)

# 2️⃣

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# 👉 यो data हो:

# x = horizontal axis (X-axis)

# y = vertical axis (Y-axis)

# 📌 pair बन्यो:

(1,2)
(2,4)
(3,6)
(4,8)
(5,10)

# 3️⃣

# plt.plot(x, y)

# 👉 यो main line हो:

# plot() = graph बनाउँछ
# x र y लाई जोडेर line बनाउँछ

# 📈 Result: straight line (किनकि y = 2x)

# 4️⃣

# plt.title("My First Graph")

# 👉 Graph को name/title सेट गर्छ

# 5️⃣
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

# 👉 Axis को नाम:

# X-axis → "X Axis"
# Y-axis → "Y Axis"

# 6️⃣ (सबैभन्दा important)

plt.show()

# 👉 बिना यस:

# ❌ graph देखिँदैन

# 👉 यसले:

# ✔️ graph screen मा देखाउँछ

# 🎯 Final Output के हुन्छ?

# 👉 एउटा straight line graph

# left to right बढ्दै जाने 📈

# title = My First Graph

# axis labels = X Axis, Y Axis

# 🧠 Important concept

# 👉 यहाँ relation:

# y = 2x

# 🔥 Quick Check (तिमी answer देउ)

# 👉 यदि:

y = [1, 4, 9, 16, 25]

# भयो भने graph कस्तो हुन्छ?


# 🟢 Lesson 3: Bar Chart









# 📊 Bar Chart के हो?





# 👉 Bar Chart = different चीजहरू compare गर्न प्रयोग हुन्छ



# उदाहरण:

# Subjects vs Marks
# Products vs Sales
# Students vs Scores

# 📌 Straight bars (columns) हुन्छन्

# 🧑‍💻 Basic Example

import matplotlib.pyplot as plt

subjects = ["Math", "Science", "English"]
marks = [85, 90, 78]

plt.bar(subjects, marks)

plt.title("Student Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.show()



import matplotlib.pyplot as plt

name = ["nirmal", "saud", "ram"]

marks = [90, 95, 100]

plt.bar(name , marks, color=["red", "blue", "green"])

plt.title("students marks")
plt.xlabel("name")
plt.ylabel("marks")
plt.show()

######




# 🔍 Step-by-step बुझौँ

# 1️⃣ 


# x axis 
subjects = ["Math", "Science", "English"]

marks = [85, 90, 78]

# 👉

# X-axis = subjects
# Y-axis = marks

# 2️⃣ Main Function

plt.bar(subjects, marks)

# 👉 bars बनाउँछ
# 👉 each subject को एउटा bar हुन्छ

# 3️⃣ Labels + Title

plt.title("Student Marks")

plt.xlabel("Subjects")

plt.ylabel("Marks")

# 👉 graph readable बनाउँछ

# 4️⃣ Show

plt.show()

# 👉 graph display हुन्छ

# 📈 Output कस्तो देखिन्छ?

# 👉 3 वटा vertical bars:

# Math → 85
# Science → 90
# English → 78



# 🎨 Customize Bar Chart





plt.bar(subjects, marks, color="green")

# 👉 color change

🔥 Advanced Example

import matplotlib.pyplot as plt

subjects = ["Math", "Science", "English"]
marks = [85, 90, 78]

plt.bar(subjects, marks, color=["red", "blue", "green"])

plt.title("Marks Comparison")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.show()


######




# 🧠 Important Concept


# 👉 Length of bar = value

# 👉 Bigger value = taller bar

# 🎯 Practice (Must do)

# 👉 यो बनाऊ:

# Subjects: Computer, Math, Science

# Marks: 95, 80, 88

# Title: "My Marks Chart"

# Color: any 3 different colors









# 🥧 Pie Chart के हो?



# 👉 Pie Chart = data लाई percentage / भाग (portion) मा देखाउने chart

# 📌 Circle लाई टुक्रा-टुक्रा (slices) मा divide गर्छ

# 👉 Each slice = data को हिस्सा

# 🧑‍💻 Basic Example

import matplotlib.pyplot as plt

labels = ["Math", "Science", "English"]
marks = [85, 90, 75]

plt.pie(marks, labels=labels, autopct="%1.1f%%")

plt.title("Marks Distribution")

plt.show()

# 🔍 Step-by-step बुझौँ

# 1️⃣ Data

labels = ["Math", "Science", "English"]
marks = [85, 90, 75]

# 👉 labels = नाम
# 👉 marks = value (size of slice)

# 2️⃣ Main Function


plt.pie(marks, labels=labels)

# 👉 pie chart बनाउँछ

# 👉 प्रत्येक value अनुसार slice size हुन्छ

# 3️⃣ Title

plt.title("Marks Distribution")

# 4️⃣ Show

plt.show()

# 👉 chart display हुन्छ

# 🎯 Output कस्तो हुन्छ?

# 👉 circle (pie) देखिन्छ

# Math → एउटा हिस्सा
# Science → अर्को हिस्सा
# English → अर्को हिस्सा

# 👉 Science को slice सबैभन्दा ठूलो हुन्छ (90 highest)

# 🎨 Percentage देखाउने (Important)

plt.pie(marks, labels=labels, autopct="%1.1f%%")

# 👉 %1.1f%% = percentage show (like 35.2%)

# 🎨 Colors add गर्ने

import matplotlib.pyplot as plt

labels = ["Math", "Science", "English"]
marks = [85, 90, 75]


plt.pie(marks, labels=labels, autopct="%1.1f%%",
        colors=["red", "blue", "green"])

plt.title("Marks Distribution")

plt.show()

# autopct="%1.1f%%"

# यसको काम:

# 👉 Pie chart मा percentage show गर्ने


plt.pie(marks, labels=labels, autopct="%1.1f%%",
        colors=["red", "blue", "green"])

# ⭐ Slice highlight (explode)

# explode = [0, 0.1, 0]  # Science highlight

plt.pie(marks, labels=labels, autopct="%1.1f%%",)
        
        # explode=explode)

# 👉 0.1 = त्यो slice बाहिर निस्किन्छ

# 🧠 Important Concept

# 👉 Total = 100%

# 👉 सबै values मिलेर pie बनाउँछ

# 🎯 Practice (Must do)

👉 Create pie chart:

# Labels: Computer, Math, Science
# Values: 95, 80, 85
# Show percentage
# Highlight highest value




# 📊 Multiple Lines Graph के हो?





# 👉 एउटै graph मा धेरै lines देखाउने


# 👉 Compare गर्न use हुन्छ

# उदाहरण: example

# 2 students को marks compare
# Sales of 2 products
# Temperature vs humidity

# 🧑‍💻 Basic Example

import matplotlib.pyplot as plt

x = [1, 2, 3, 4]

y1 = [2, 4, 6, 8]   # Line 1
y2 = [1, 3, 5, 7]   # Line 2


plt.plot(x, y1, color="red", linestyle="--", marker="o", label="Line 1")
plt.plot(x, y2, color="blue", linestyle="-", marker="*", label="Line 2")

plt.legend()

plt.title("Multiple Lines Graph")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.show()

# 🔍 Step-by-step बुझौँ

# 1️⃣ Data
x = [1, 2, 3, 4]
y1 = [2, 4, 6, 8]
y2 = [1, 3, 5, 7]

# 👉 एउटै X-axis

# 👉 दुई वटा Y-values (2 lines)

# 2️⃣ दुई पटक plot()

plt.plot(x, y1, label="Line 1")
plt.plot(x, y2, label="Line 2")

# 👉 each plot() = एउटा line
# 👉 label = line को नाम

# 3️⃣ Legend (important)

plt.legend()

# 👉 graph मा box देखाउँछ

# 👉 कुन line के हो भनेर देखाउँछ

# 4️⃣ Labels + Title

plt.title("Multiple Lines Graph")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

# 5️⃣ Show

plt.show()

# 📈 Output कस्तो हुन्छ?

# 👉 एउटै graph मा:

# 2 lines

# Different slopes

# Legend box (Line 1, Line 2)

# 🎨 Style change (Advanced)

plt.plot(x, y1, color="red", linestyle="--", marker="o", label="Line 1")
plt.plot(x, y2, color="blue", linestyle="-", marker="*", label="Line 2")


# 🧠 Important Concept

# 👉 Multiple lines = comparison
# 👉 Same graph = better understanding

# 🎯 Practice (Must do)

# 👉 Create graph:

# x = [1,2,3,4]
# Student A marks = [60,70,80,90]
# Student B marks = [50,65,75,85]
# Add legend + title



# 🟢 Lesson 6: Style Change



# 🎨 Style Change के हो?

# 👉 Graph लाई सुन्दर / readable / professional बनाउन styling गरिन्छ

# 🧑‍💻 Basic Example

import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [2, 4, 6, 8]

plt.plot(x, y, color="red", linestyle="--", marker="o")

plt.title("Styled Graph")
plt.show()


#####

import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [3, 4, 6, 7,]

plt.plot(x,y, color = "red", linestyle="--", marker="o")

plt.title("styled graph")
plt.show()


###

# 🔍 Main Styling Options

# 1️⃣ Color (रंग)

plt.plot(x, y, color="green")

# 👉 Common colors:

"red"
"blue"
"green"
"black"

# 2️⃣ Line Style (रेखा type)

plt.plot(x, y, linestyle="--")

# 👉 Types:

"-" → solid
"--" → dashed
":" → dotted
"-." → dash-dot

# 3️⃣ Marker (points देखाउने)

plt.plot(x, y, marker="o")

# 👉 Types:

"o" → circle
"*" → star
"s" → square
"^" → triangle


# 🎯 Combine Style

plt.plot(x, y, color="blue", linestyle=":", marker="*")

# 👉 सबै styling एउटै लाइनमा गर्न मिल्छ

# 🧠 Real Example (Professional)

import matplotlib.pyplot as plt

x = [1,2,3,4]
y1 = [2,4,6,8]
y2 = [1,3,5,7]

plt.plot(x, y1, color="red", linestyle="--", marker="o", label="Line 1")
plt.plot(x, y2, color="blue", linestyle="-", marker="*", label="Line 2")

plt.legend()
plt.title("Styled Multiple Lines")
plt.show()


# ✨ Extra Styling (Bonus)

# Grid add गर्ने

# plt.grid()

# Figure size change

plt.figure(figsize=(8,5))


📌 Output

# 👉 Graph अब:

# colorful हुन्छ 🎨
# clear हुन्छ 👀
# professional देखिन्छ 😎
# 🎯 Practice (Must do)

# 👉 Create styled graph:

x = [1,2,3,4,5]
y = [5,10,15,20,25]
# color = green
# linestyle = dashed
# marker = circle
# grid add गर





