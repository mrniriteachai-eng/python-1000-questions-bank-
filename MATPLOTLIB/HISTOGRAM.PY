# 📊 Histogram के हो?

# 👉 Histogram = data को distribution (spread) देखाउने graph

# 📌 Example:

# marks कति range मा धेरै छन्?

# ages कता बढी छन्?

# data uniform छ कि skewed?

# 👉 Bar chart जस्तो देखिन्छ, तर:

# Bar chart → categories compare
# Histogram → numeric data को range देखाउँछ



# 🧑‍💻 Basic Example

import matplotlib.pyplot as plt

marks = [40, 50, 55, 60, 65, 70, 75, 80, 85, 90]

plt.hist(marks)

plt.title("Marks Distribution")
plt.xlabel("Marks Range")
plt.ylabel("Frequency")

plt.show()



# 🔍 Step-by-step बुझौँ

# 1️⃣ Data

marks = [40, 50, 55, 60, 65, 70, 75, 80, 85, 90]

# 👉 Students marks data

# 👉 Continuous numeric data

# 2️⃣ Main Function

plt.hist(marks)

# 👉 Data लाई groups (bins) मा divide गर्छ

# 👉 प्रत्येक group मा कति values छन् भनेर देखाउँछ



# 🧠 What Histogram does?

# Histogram ले data लाई:

# groups / ranges / bins

# मा divide गर्छ


# 🧠 Internally What Happens?

# Matplotlib:

# data लाई ranges मा divide गर्छ
# प्रत्येक range मा कति values छन् count गर्छ


# 📊 Example Counting
# | Range | Count |
# | ----- | ----- |
# | 40–50 | 2     |
# | 50–60 | 2     |
# | 60–70 | 2     |
# | 70–80 | 2     |
# | 80–90 | 2     |



# 👉 त्यसपछि bars बनाउँछ



# 🧠 Important Concept: Bins

# 👉 bins = data divide गर्ने intervals

plt.hist(marks, bins=5)

# 👉 Example:

# 0–20
# 20–40
# 40–60
# 60–80


# 📈 Histogram vs Bar Chart

# | Histogram      | Bar Chart     |
# | -------------- | ------------- |
# | Numeric ranges | Categories    |
# | Joined bars    | Separate bars |
# | Distribution   | Comparison    |




# Styled Histogram

import matplotlib.pyplot as plt

marks = [40, 50, 55, 60, 65, 70, 75, 80, 85, 90]

plt.hist(
    marks,
    bins=5,
    color="skyblue",
    edgecolor="black"
)

plt.title("Marks Distribution")
plt.xlabel("Marks Range")
plt.ylabel("Frequency")

plt.grid()

plt.show()


# 1️⃣ Import Library

import matplotlib.pyplot as plt

# 👉 matplotlib.pyplot

# = graph plotting module

# 👉 plt
# = shortcut name

# 2️⃣ Data

marks = [40, 50, 55, 60, 65, 70, 75, 80, 85, 90]

# 👉 Students marks data

# 📌 Total values:

10

# 3️⃣ Histogram Function

plt.hist(

# 👉 histogram graph start गर्छ

# 4️⃣ Data pass

# marks,

# 👉 histogram को data



# 5️⃣ bins=5 (VERY IMPORTANT 🔥)

bins=5,

# 👉 data लाई:


# 5 groups / intervals

# मा divide गर्छ

# 🧠 What ranges are created?

# Minimum:

# 40

# Maximum:

# 90

# Range:

# 90 - 40 = 50

# Now:

# 50 ÷ 5 = 10

# 👉 each bin width ≈ 10


# 📊 Approx bins

marks = [40, 50, 55, 60, 65, 70, 75, 80, 85, 90]

# | Bin   | Values | f
# | ----- | ------ |
# | 40–50 | 40, 50 |1
# | 50–60 | 55, 60 |2
# | 60–70 | 65, 70 |2
# | 70–80 | 75, 80 |2
# | 80–90 | 85, 90 |3



# 📈 Frequency Meaning

# Example:

# 40–50 → 2 values

# 👉 त्यसैले bar height = 2

# 6️⃣ Color

color="skyblue",

# 👉 bars को fill color

# 📌 "skyblue" = light blue

# Other colors:

# red
# green
# yellow
# purple

# 7️⃣ Edge Color

edgecolor="black"

# # 👉 bars को border black हुन्छ

# # 📌 यसले graph clear देखाउँछ 👀

# Without edgecolor:
# ❌ bars merge जस्तो देखिन सक्छ

# 8️⃣ Title

plt.title("Marks Distribution")

# 👉 graph माथिको heading

# 9️⃣ X-axis Label

plt.xlabel("Marks Range")

# 👉 X-axis:
# marks intervals/ranges

# Example:

# 40–50
# 50–60
# 🔟 Y-axis Label

plt.ylabel("Frequency")

# 👉 Frequency =
# कति values छन्

# Example:

# 70–80 → 2 students

# 1️⃣1️⃣ Grid
plt.grid()

# 👉 background मा horizontal/vertical lines

# 📌 graph पढ्न सजिलो हुन्छ

# 1️⃣2️⃣ Show Graph
plt.show()

# 👉 graph display गर्छ

# ⚠️ बिना show():
# graph देखिँदैन

📈 Final Output

👉 Light blue histogram
👉 Black borders
👉 Grid background
👉 Frequency analysis

🧠 AI/Data Science Concept

Histogram use for:

distribution analysis
skew detection
data spread understanding
outlier finding
🔥 Experiment (Important)

Try this:

bins=2

Then:

bins=10


# 🎯 Customized Histogram (Full Control)


# 🧑‍💻 Example

import matplotlib.pyplot as plt

marks = [40, 50, 55, 60, 65, 70, 75, 80, 85, 90]

plt.hist(marks, bins=5, edgecolor="black")

plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.grid()

plt.show()





import matplotlib.pyplot as plt

marks = [50, 60, 70, 80, 90, 55, 60, 65, 75, 85, 95]

plt.hist(marks, bins=5, edgecolor="black")

plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.grid()

plt.show()


# 1️⃣ Import Library

import matplotlib.pyplot as plt

# 👉 matplotlib.pyplot

# = graph plotting module

# 👉 plt
# = shortcut name

# 📌 अब:

plt.hist()
plt.plot()
plt.scatter()

# सजिलै लेख्न मिल्छ

# 2️⃣ Data

marks = [40, 50, 55, 60, 65, 70, 75, 80, 85, 90]

# 👉 students को marks data

# 📌 Total:

10 values

🧠 Important Concept

Histogram continuous numeric data को distribution देखाउँछ

# 3️⃣ Histogram Function

plt.hist(marks, bins=5, edgecolor="black")

# 👉 Histogram graph बनाउँछ

# अब यसलाई टुक्रा-टुक्रा बुझौँ 👇

# 🔹 marks

marks

👉 graph मा use हुने data

# 🔹 bins=5 (VERY IMPORTANT 🔥)
bins=5

# 👉 data लाई:

5 intervals/groups

मा divide गर्छ

🧠 Internally What Happens?

Minimum value:

40

Maximum value:

90

Range:

90 - 40 = 50

Now:

50 ÷ 5 = 10

👉 each bin width ≈ 10

📊 Approx Bins


# | Bin   | Values |
# | ----- | ------ |
# | 40–50 | 40,50  |
# | 50–60 | 55,60  |
# | 60–70 | 65,70  |
# | 70–80 | 75,80  |
# | 80–90 | 85,90  |


# 📈 Frequency Meaning

# Example:

# 40–50 → 2 values

# 👉 त्यसैले:

bar height = 2

🔹 edgecolor="black"
edgecolor="black"

👉 bars को border black हुन्छ

# 📌 Why useful?

# Without edgecolor:
❌ bars merge जस्तो देखिन सक्छ

With edgecolor:
✅ each bar clearly visible 👀

# 4️⃣ Title

plt.title("Marks Distribution")

👉 graph को heading/title

📌 Purpose

Graph हेर्दा तुरुन्त बुझिन्छ:

यो marks distribution हो

# 5️⃣ X-axis Label

plt.xlabel("Marks")

👉 X-axis मा marks ranges देखिन्छ

# Example:

# 40–50
# 50–60

# 6️⃣ Y-axis Label

plt.ylabel("Number of Students")

# 👉 Y-axis:

# कति students त्यो range मा छन्

# 📊 Example

# 70–80 → 2 students

# 7️⃣ Grid

plt.grid()

# 👉 background मा guide lines add

# 📌 Why useful?
# graph पढ्न सजिलो
# height compare गर्न सजिलो
# 8️⃣ Show Graph

plt.show()

# 👉 graph display गर्छ

# ⚠️ बिना show():
# graph देखिँदैन

# 📈 Final Output

👉 Histogram with:

5 bins
black borders
grid lines
marks distribution
🧠 AI/Data Science Meaning

Histogram helps in:

data distribution analysis
skewness detection
outlier detection
ML preprocessing
🔥 Important Experiment

Try:

bins=2

Then:

bins=10


# 🔍 Customization Details

# 1️⃣ bins (सबैभन्दा important)

plt.hist(marks, bins=5)

# 👉 Data लाई 5 वटा groups मा divide गर्छ
# 👉 bins बढाउँदा → more detail
# 👉 bins घटाउँदा → simple view

# 2️⃣ edgecolor

edgecolor="black"

# 👉 bars को border clear देखिन्छ 👀

# 3️⃣ grid

plt.grid()

# 👉 graph पढ्न सजिलो हुन्छ

# 🎨 Extra Customization (Pro Level)

import matplotlib.pyplot as plt

marks = [40, 50, 55, 60, 65, 70, 75, 80, 85, 90]

plt.hist(
    marks,
    bins=5,
    color="skyblue",
    edgecolor="black"
)

plt.title("Advanced Histogram")
plt.xlabel("Marks Range")
plt.ylabel("Frequency")

plt.grid()

plt.show()

# 🧠 Important Concept

# 👉 Histogram ले देखाउँछ:

# data कहाँ concentrate छ
# spread कस्तो छ
# skew (left/right) छ कि छैन


# 📈 Example Insight

# 👉 यदि धेरै values 70–90 मा छन् भने:

# ➡️ students high scoring छन्

# 🎯 Practice (Must do)

# 👉 Create customized histogram:

# Data: [10,20,20,30,30,30,40,50,60,70]
# bins = 4
# color = any
# edgecolor = black
# grid add गर


# 🧠 Real-life use
# Exam analysis

# Income distribution
# ML feature analysis
# Data cleaning insight
# ⚠️ Bar vs Histogram (important)
# Bar Chart	Histogram
# Categories	Continuous data
# Separate bars	Joined bars
# Compare	Distribution


# 🎯 Practice (Must do)

# 👉 
# Create histogram:

Data: [10,20,20,30,40,40,40,50,60,70]
bins = 4
# Add title + labels