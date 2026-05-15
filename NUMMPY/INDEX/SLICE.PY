## INDEXING 
# 🧠 Indexing के हो?

# 👉 Indexing भनेको array भित्रको specific (ठ्याक्कै) element access गर्नु हो।

import numpy as np

a = np.array([1,2,3,4])

print(a[0])
print(a[2])

import numpy as np

nir = np.array([1,2,3,4,5,6])
print(nir[3])

# 🔢 1. 1D Array Indexing
# 📌 Example

import numpy as np

a = np.array([10, 20, 30, 40])

print(a[0])
print(a[2])

# | Index | Value |
# | ----- | ----- |
# | 0     | 10    |
# | 1     | 20    |
# | 2     | 30    |
# | 3     | 40    |


0

# 📊 2. Negative Indexing (Important)


import numpy as np

a = np.array([1,2,3,4])
print(a[-1])
print(a[-2])

#####

import numpy as np
a = np.array([1,2,3,4])
print(a[-2])
print(a[-1])


# 🧠 Meaning:
# Index	Meaning
# -1	last element
# -2	second last

# 🧱 3. 2D Array Indexing (Matrix)

import numpy as np
b = np.array([[1, 2, 3],
              [4, 5, 6]])
# 📌 Access element
print(b[0, 1])


#### 
import numpy as np
a = np.array([[1,3,4,5,6,7,8],
              [3,4,5,6,7,9,10]])
print(a[0,2])

# | Position | Value |
# | -------- | ----- |
# | b[0,0]   | 1     |
# | b[0,1]   | 2     |
# | b[1,2]   | 6     |


# Row 0 →  1   2   3
# Row 1 →  4   5   6
#            ↑
#         b[1,1] = 5


# 🎯 Key Points

# ✔ Indexing = single element access
# ✔ Starts from 0
# ✔ Negative indexing possible
# ✔ 2D मा = [row, column]

# 🧪 Practice

x = np.array([100, 200, 300, 400])

print(x[1])
print(x[-1])

# 👉 Try guess output 😉


import numpy as np
a = np.array([[[1,2,3],
               [4,5,6],
               [9,7,6]]])
print(a[0,1,2])

  #### SLICING

# ✂️ Slicing in NumPy (Easy Explanation)
# 🧠 Slicing के हो?

# 👉 Slicing भनेको array भित्रबाट धेरै elements (part) निकाल्ने process हो।

# 📌 Basic Syntax
# array[start : end : step]

# | Part  | Meaning                   |
# | ----- | ------------------------- |
# | start | कहाँबाट सुरु गर्ने           |
# | end/STOP| कहाँसम्म (include हुँदैन) |
# | step  | कति कति skip गर्ने        |


# 🔢 1. 1D Slicing Example
import numpy as np

a = np.array([10, 20, 30, 40, 50])

print(a[1:4])##index 1 to 4
print(a[:4])## index o to 3
print(a[::2])## every second element
print(a[-1])

import numpy as np
a = np.array([1,2,3,4])
print(a[1:3])
print()


#3#3

import numpy as np

a = np.array([[1,3,4,5,6,7,8],
              [3,4,5,6,7,9,10]])
# a[row_start:row_end , col_start:col_end]
print(a[0, :])
print(a[1, :])

# 🧠 Explanation:
# start = 1 → 20
# end = 4 (NOT included) → 50 सम्म जाँदैन


# ⚡ 2. Step Slicing

print(a[0:5:2])


# | Code      | Meaning           |
# | --------- | ----------------- |
# | `a[:]`    | सबै elements      |
# | `a[:3]`   | start → 3 सम्म    |
# | `a[2:]`   | 2 देखि अन्त्यसम्म |
# | `a[::2]`  | every 2nd element |
# | `a[::-1]` | reverse array     |

# 🔄 Example: Reverse


print(a[::-1])


# 📊 2D Array Slicing (Important)

b = np.array([[1, 2, 3],
              [4, 5, 6]])
# 🔹 Example 1: Row slicing
print(b[0, :])

##########

import numpy as np

a = np.array([[1, 3, 4, 5],
              [6, 7, 8, 9]])
print(a[0, :])



# ✔ row 0 पूरा

# 🔹 Example 2: Column slicing

print(b[:, 1])


# ✔ column 1 पूरा

# 🧠 Easy Trick
# Concept	Meaning
# Indexing	one element
# Slicing	multiple elements
# 🎯 Why Slicing important?

# AI / Data Science मा:

# 📊 data filtering
# 🤖 feature selection
# 📉 dataset cleaning
# 📈 model input preparation

# 🧪 Practice
x = np.array([5, 10, 15, 20, 25, 30])

print(x[2:5])
print(x[::2])

# 👉 Try guess output 😉

# 👉 Slicing = array बाट भाग (subset) निकाल्ने method

# Fancy Indexing in NumPy 

# 🧠 Fancy Indexing के हो?

# 👉 Fancy indexing भनेको array बाट चाहिएको specific elements लाई list वा array प्रयोग गरेर निकाल्ने method हो।

# 🧠 Simple Meaning

# 👉 Fancy indexing =
# “random positions बाट multiple elements select गर्नु”


# 🔢 1. Basic Example

import numpy as np

a = np.array([10, 20, 30, 40, 50])

print(a[[0, 2, 4]])

print(a[[4, 0, 2]])

# 👉 हामीले index list दिएका छौं:

# 0 → 10
# 2 → 30
# 4 → 50

# ✔ random selection भयो

# ✔ order आफूले control गर्न सक्छौ

# 🧱 3. 2D Fancy Indexing


b = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
print(b[[0, 2]])

# ✔ row 0 र row 2 select भयो

# 🔥 Column Fancy Indexing

print(b[:, [0, 2]])

# ✔ column 0 र 2 select भयो


# | Type           | Meaning                  |
# | -------------- | ------------------------ |
# | Indexing       | single element           |
# | Slicing        | continuous part          |
# | Fancy Indexing | random multiple elements |


# 🎯 Why Fancy Indexing important?

# AI / Data Science मा:

# 📊 specific data selection
# 🤖 feature selection
# 📉 filtering dataset
# 📈 model training input control
# 🧪 Practice

x = np.array([100, 200, 300, 400, 500])

print(x[[1, 3]])

# 👉 Try guess output 😉


import numpy as np
a = np.array([[[1,2,3],
              [9,4,5],
              [3,4,5]]])
print(a[:,0:2])

########
import numpy as np

a = np.array([[1, 3, 4, 5],
              [6, 7, 8, 9]])
print(a[:,0:2])


# ✂️ 2D Slicing Formula

# a[row_start:row_end , col_start:col_end]


import numpy as np

a = np.array([[1, 3, 4, 5],
              [6, 7, 8, 9]])
print(a[0:2, 1:3])
