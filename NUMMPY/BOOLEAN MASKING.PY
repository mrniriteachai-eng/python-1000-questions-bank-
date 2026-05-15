# 🎭 2. Boolean Masking in NumPy


# 🧠 Boolean Masking के हो?

# 👉 Boolean Masking भनेको condition (True/False) प्रयोग गरेर array बाट data filter गर्ने method हो।

# 🧠 Simple Meaning
# 👉 Boolean Masking =
# “condition पूरा गर्ने data मात्र छान्ने”



# 🔢 1. Basic Example

import numpy as np

a = np.array([10, 20, 30, 40])


mask = a > 25
print(mask)

import numpy as np

n = np.array([1,2,3])

mask = n>2
print(mask)


# ✔ True/False array बन्यो (mask

# 🔍 Apply Mask

print(a[mask])

# ⚡ Direct Shortcut

import numpy as np

a = np.array([10, 20, 30, 40])
print(a[a > 25])
mask = a>25
print(mask)


# 🔥 2. Even Numbers Filter

a = np.array([1, 2, 3, 4, 5, 6])

print(a[a % 2 == 0])

# 📊 3. 2D Array Masking

b = np.array([[1, 2, 3],
              [4, 5, 6]])

print(b[b > 3])


# 🎯 4. Multiple Conditions (Important)


a = np.array([10, 20, 30, 40, 50])

print(a[(a > 20) & (a < 50)])

# | Symbol | Meaning |    |
# | ------ | ------- | -- |
# | `&`    | AND     |    |
# | `      | `       | OR |
# | `~`    | NOT     |    |



# ⚠️ Important Rule

# 👉 Python को and, or प्रयोग नगर्नु ❌
# 👉 NumPy मा &, | प्रयोग गर्नु ✔

# 🎯 Why important?

# AI / Data Science मा:

# 📊 data cleaning
# 🤖 feature selection
# 📉 outlier removal
# 📈 preprocessing

# 🧪 Practice
x = np.array([5, 15, 25, 35, 45])

print(x[x >= 25])

# 👉 Guess output 😉
