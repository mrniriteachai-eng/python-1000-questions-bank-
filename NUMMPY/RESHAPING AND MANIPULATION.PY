# 🔁 Reshaping & Manipulating Arrays (NumPy)

# NumPy मा data लाई shape change गर्नु, arrange गर्नु, combine गर्नु आदि कामलाई reshaping & manipulation भनिन्छ।




# 📦 1. Reshaping Arrays (reshape())


# 🔁 Reshaping Arrays in NumPy: reshape()

# reshape() is used to change the shape (dimension) of an array without changing its data.

# 🧠 Meaning:

# 👉 array को shape change गर्नु (data same रहन्छ)

# 🔢 Example

import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])

b = a.reshape(2, 3)
print(b)


# 1D → 2D array बन्यो
# total elements same (6)
# ⚠️ Rule:

# 👉 reshape गर्दा elements count match हुनुपर्छ


# 🔄 flatten() in NumPy


# 🧠 Meaning

# 👉 multi-dimensional array लाई 1D (single row) मा convert गर्ने

# example

import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])

print(a.flatten())

# 🧠 What happened?

# Before (2D):

# [[1 2 3]
#  [4 5 6]]

# After (1D):

# [1 2 3 4 5 6]

# ✔ सबै rows लाई एउटै लाइनमा मिलायो

# Practice
x = np.array([[10, 20],
              [30, 40]])

print(x.flatten())

# 👉 Try guess output 😉


# 🔁 ravel() in NumPy


# 🧠 Meaning

# 👉 ravel() पनि multi-dimensional array लाई 1D मा convert गर्छ
# ✔ तर यो memory efficient (copy नबनाई view दिन्छ)


import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])

print(a.ravel())



# 🧠 What happened?

# Before (2D):

# [[1 2 3]
#  [4 5 6]]

# # After (1D):

# [1 2 3 4 5 6]

# ✔ Same as flatten() result

# ⚡ Main Difference (Very Important)

# 👉 ravel() = view (original data सँग जोडिएको)

# 🔬 Proof (Important)


b = a.ravel()
b[0] = 100

print(b)
print(a)

# | Feature         | flatten()   | ravel()    |
# | --------------- | ----------- | ---------- |
# | Memory          | copy बनाउँछ | view दिन्छ |
# | Speed           | slow        | fast       |
# | Original change | ❌ no        | ✔ yes      |


# 🎯 When to use ravel()?
# ⚡ fast operation चाहिँदा
# 💾 memory बचाउनु परेमा
# 🔄 large data handle गर्दा
# 🧪 Practice


import numpy as np
x = np.array([[10, 20],
              [30, 40]])

y = x.ravel()
y[1] = 999

print(x)

# 👉 Guess output 😉



# 🔄 4. Transpose (.T) in NumPy


# 🧠 Meaning
# 👉 .T ले array को rows र columns swap (exchange) गर्छ


# 🔢 Example (2D Array)
import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])

print(a.T)



# 🧠 What happened?
# Before:
# 2 rows × 3 columns
# 1  2  3
# 4  5  6
# After .T:
# 3 rows × 2 columns
# 1  4
# 2  5
# 3  6

# ✔ rows → columns
# ✔ columns → rows

# 📊 Shape Change (Important)
# print(a.shape)     # (2, 3)
# print(a.T.shape)   # (3, 2)


# ⚡ 1D Array Case (Tricky)
# b = np.array([1, 2, 3])
# print(b.T)



# ✔ 1D मा transpose गर्दा फरक देखिँदैन


# 🧠 Why?

# 👉 1D array मा row/column concept clear हुँदैन
# 👉 त्यसैले change हुँदैन


# 🔥 Important Use

# AI / Data Science मा:

# 🤖 Matrix multiplication
# 📊 Linear algebra
# 📈 Data transformation
# 🧠 Neural networks

# 🧪 Practice
x = np.array([[10, 20],
              [30, 40],
              [50, 60]])

print(x.T)

# 👉 Guess output 😉


# ➕ 5. Joining Arrays — concatenate() in NumPy




# 🧠 Meaning

# 👉 concatenate() ले दुई वा बढी arrays लाई जोडेर एउटा बनाउँछ

# 🔢 1. Basic Example (1D)

import numpy as np


a = np.array([1, 2])
b = np.array([3, 4])

print(np.concatenate((a, b)))

# ✔ दुई array जोडिएर एउटा भयो


# 📊 2. 2D Array Join (Very Important)


import numpy as np
x = np.array([[1, 2],
              [3, 4]])

y = np.array([[5, 6],
              [7, 8]])
# 🔹 axis = 0 (Vertical join)

print(np.concatenate((x, y), axis=0))


# ✔ rows थपियो (downward)

####

# 🔹 axis = 1 (Horizontal join)
print(np.concatenate((x, y), axis=1))


# ✔ columns थपियो (side by side)

# ⚠️ Important Rules

# 👉 concatenate गर्दा:

# axis=0 ⇒ columns same हुनुपर्छ
# axis=1 ⇒ rows same हुनुपर्छ

# ❌ mismatch भयो भने error आउँछ


# | Axis   | Meaning                  |
# | ------ | ------------------------ |
# | axis=0 | माथि–तल (vertical)       |
# | axis=1 | दायाँ–बायाँ (horizontal) |



# 🎯 Why important?

# AI / Data Science मा:

# 📊 dataset merge गर्न
# 🤖 features combine गर्न
# 📈 data preparation
# 📉 preprocessing


# 🧪 Practice

a = np.array([10, 20])
b = np.array([30, 40])

print(np.concatenate((a, b)))

# 👉 Guess output 😉




# 🔗 6. Stacking Arrays in NumPy



# 🧠 Meaning

# 👉 Stacking भनेको arrays लाई नयाँ dimension मा जोड्ने (stack गर्ने) हो

# 🧠 Simple Meaning

# 👉 Stacking =
# “array हरूलाई माथि–तल वा side-by-side राख्ने”


# 🔼 1. Vertical Stack (vstack())


# 👉 arrays लाई माथि–तल (row-wise) राख्छ

import numpy as np

a = np.array([1, 2])
b = np.array([3, 4])

print(np.vstack((a, b)))

# ✔ नयाँ row add भयो

# ➡️ 2. Horizontal Stack (hstack())

# 👉 arrays लाई side-by-side (column-wise) राख्छ

print(np.hstack((a, b)))

# 📊 3. 2D Array Example

import numpy as  np
x = np.array([[1, 2],
              [3, 4]])

y = np.array([[5, 6],
              [7, 8]])
# 🔼 Vertical Stack
print(np.vstack((x, y)))


# | Function | Meaning       |
# | -------- | ------------- |
# | vstack() | माथि–तल       |
# | hstack() | side-by-side  |
# | stack()  | new dimension |


# 🧪 Practice
a = np.array([10, 20])
b = np.array([30, 40])

print(np.vstack((a, b)))
print(np.hstack((a, b)))

# 👉 Guess output 😉