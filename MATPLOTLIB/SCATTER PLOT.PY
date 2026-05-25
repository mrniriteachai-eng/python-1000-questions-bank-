# 📊 Scatter Plot के हो?

# 👉 Scatter Plot = data points (dots) देखाउने graph

# 📌 Use:

# 2 variables बीच relationship बुझ्न

# Pattern / trend / correlation देख्न

# 🧑‍💻 Basic Example

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 6]

plt.scatter(x, y)

plt.title("Scatter Plot Example")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.show()



import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [3, 4, 5, 6]

plt.scatter(x,y)

plt.title("Scatter Plot Example")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()





# 🔍 Explanation

# ✅ plt.scatter(x, y)

# 👉 scatter plot बनाउँछ

# Points:

(3,8)
(4,9)
(5,6)
(6,7)


### 

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 6]

plt.scatter(x, y)

plt.title("Scatter Plot Example")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.show()

# 🔍 Step-by-step बुझौँ

# 1️⃣ Data

x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 6]

# 👉 (x, y) = points
# 👉 each pair = एउटा dot

# 2️⃣ Main Function

plt.scatter(x, y)

# 👉 dots draw गर्छ (line होइन ❌)

# 📈 Output कस्तो हुन्छ?

# 👉 graph मा dots मात्र हुन्छ
# 👉 line connect हुँदैन

# 🧠 Important Concept: Correlation

# 👉 Scatter plot बाट:

# Positive trend 📈 (x बढ्दा y बढ्छ)
# Negative trend 📉 (x बढ्दा y घट्छ)

# No relation ❓


# 🧑‍💻 तिम्रो code:

plt.scatter(x, y, color="red", marker="o")



# 🔍 Breakdown

# 1️⃣ plt.scatter(x, y)



# 👉 Scatter plot बनाउँछ

# 👉 (x, y) = points (dots)


# 2️⃣ color="red"


# 👉 सबै dots red color हुन्छ 🔴

# 📌 Example:

"blue"
"green"
"black"


# 3️⃣ marker="o"

# 👉 dot को shape define गर्छ

# 📌 Common markers:

# "o" → circle ⚪
# "*" → star ⭐
# "s" → square ⬛
# "^" → triangle 🔺
# 🎨 More Customization (Important 🔥)
# 👉 Size change
# plt.scatter(x, y, s=100)

# 👉 dot size ठूलो हुन्छ

# 👉 Different colors for each point

colors = ["red", "blue", "green", "orange", "purple"]

plt.scatter(x, y, c=colors)


# 👉 Transparency (opacity)



import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 6]

plt.scatter(x, y, alpha=0.5)


plt.title("Scatter Plot Example")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.show()

plt.scatter(x, y, alpha=0.5)

# 👉 0 = invisible
# 👉 1 = full visible

# 👉 Edge color

plt.scatter(x, y, edgecolors="black")

# 🚀 Full Styled Example

import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,4,5,4,6]

plt.scatter(
    x, y,
    color="blue",
    marker="o",
    s=100,
    edgecolors="black",
    alpha=0.7
)

plt.title("Advanced Scatter Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid()

plt.show()



# 1️⃣ Import library

import matplotlib.pyplot as plt

# 👉 matplotlib.pyplot

# = graph बनाउने module

# 👉 plt

# = shortcut name

# 📌 अब:

plt.scatter()
plt.plot()
plt.show()

# लेख्न सजिलो हुन्छ

# 2️⃣ X-axis data

x = [1,2,3,4,5]

# 👉 Horizontal axis values

# 📌 X-axis मा:

# 1 2 3 4 5

# देखिन्छ

# 3️⃣ Y-axis data

y = [2,4,5,4,6]

# 👉 Vertical axis values

# 🧠 Data pairs

# Python ले यसलाई pair बनाउँछ:

(1,2)
(2,4)
(3,5)
(4,4)
(5,6)

# 👉 प्रत्येक pair = एउटा dot

# 4️⃣ Scatter Plot

plt.scatter(

# 👉 scatter graph start

# 📌 dots बनाउँछ

# ❌ line connect गर्दैन

# 5️⃣ Data pass

x, y,

# 👉 x-axis data
# 👉 y-axis data

# 6️⃣ Color

color="blue",

# 👉 सबै dots blue हुन्छ 🔵

# Other colors:

# red
# green
# black
# yellow

# 7️⃣ Marker Shape

marker="o",

# 👉 "o" = circle marker ⚪

# Other markers:

# Marker	Shape
# "*"	star
# "s"	square
# "^"	triangle

# 8️⃣ Size

# s=100,

# 👉 dot size

# 📌 bigger value = bigger dots

# Example:

# s=20   # small
# s=200  # large

# 9️⃣ Edge Color

# edgecolors="black",

👉 dots को border black हुन्छ

# 📌 Without this:

# plain color only

# 📌 With this:

# dots clear देखिन्छ 👀


# 🔟 Transparency

alpha=0.7


| Value | Meaning       |
| ----- | ------------- |
| 0     | invisible     |
| 1     | fully visible |




👉 0.7

# = slightly transparent

# 1️⃣1️⃣ Titl

# plt.title("Advanced Scatter Plot")

# 👉 graph माथिको title

# 1️⃣2️⃣ X Label

# plt.xlabel("X Axis")

# 👉 X-axis को नाम

# 1️⃣3️⃣ Y Label

# plt.ylabel("Y Axis")

# 👉 Y-axis को नाम

# 1️⃣4️⃣ Grid

# plt.grid()

# 👉 background मा lines add

# 📌 graph पढ्न सजिलो हुन्छ

# 1️⃣5️⃣ Show Graph

plt.show()

# 👉 graph screen मा display

# ⚠️ बिना show():

# graph देखिँदैन

# 📈 Final Output

# 👉 Blue circle dots
# 👉 Black border
# 👉 Grid background
# 👉 Labels + title

# 🧠 Important AI/Data Science Concept

# Scatter Plot use for:

# relationship analysis
# pattern finding
# outlier detection
# correlation checking

# Example:


# Study Hours vs Marks
# Age vs Salary
# Height vs Weight
# 🎯 Quick Challenge

# Try this:

marker="*"
color="red"
s=200

# 🧠 Important Insight

# 👉 Scatter plot = data relationship
# 👉 Style = clarity + presentation

🎯 Practice (Must do)

# 👉 Create:

x = [5,10,15,20,25]

y = [3,7,8,12,15]

# color = purple

# marker = star *

# size = 150

# grid add गर


# ⭐ Advanced Example

import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,4,5,4,6]

plt.scatter(x, y, color="blue", marker="*")

plt.title("Styled Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")

plt.grid()

plt.show()


#$#$#$#
import matplotlib.pyplot as plt

x = [4, 5,6,7,8]

y = [8, 9, 8 , 6,7]
plt.scatter(x,y, color ="blue",marke="o")

plt.title("nirmal")
plt.xlabel("x")
plt.ylabel("y")

plt.graid()

plt.show()


# 🧠 Real-life use (AI/ML)

# 👉 Feature relationship check गर्न:

# height vs weight
# study time vs marks
# age vs salary

# 👉 Outliers detect गर्न 🔍

# 🎯 Practice (Must do)

# 👉 Create scatter plot:

x = [10,20,30,40,50]
y = [15,25,35,45,55]
# color = green
marker = *
# grid add गर