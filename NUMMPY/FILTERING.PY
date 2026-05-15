# 🔍 Filtering Data in NumPy 

# 🧠 Filtering के हो?
# 👉 Filtering भनेको condition (शर्त) लगाएर data बाट चाहिएको elements मात्र निकाल्ने process हो।

# 🧠 Simple Meaning
# 👉 Filtering =
# “condition पुरा गर्ने data मात्र छान्ने”


# 🔢 1. Basic Filtering Example

import numpy as np

a = np.array([[10, 20, 30, 40, 50],
             [20, 30, 50, 40, 22]])


print(a[a > 25])

# 👉 Condition: a > 25

# 10 ❌
# 20 ❌
# 30 ✔
# 40 ✔
# 50 ✔

# ⚡ 2. Even Numbers Filter


import numpy as np
a = np.array([1, 2, 3, 4, 5, 6])

print(a[a % 2 == 0])
print(a[a % 2 != 0])
#  केवल even numbers मात्र select भयो✔


# 🧱 4. 2D Array Filtering


b = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
print(b[b % 2 == 0])
print(b[b % 2 != 0])


# 🧠 Important Concept

# 👉 NumPy मा filtering = Boolean indexing

# True → value select हुन्छ
# False → value ignore हुन्छ

# 🎯 Why Filtering important?

# AI / Data Science मा:

# 📊 data cleaning
# 🤖 feature selection
# 📉 outlier removal
# 📈 dataset preparation

# 🧪 Practice


x = np.array([15, 22, 35, 40, 55])

print(x[x >= 40])

# 👉 Try guess output 😉