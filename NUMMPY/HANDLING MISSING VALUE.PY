# 🧹 Handling Missing Values in NumPy
# 🧠 Missing Value के हो?

# 👉 dataset मा value नभएको (empty / NaN) लाई missing value भनिन्छ

# 🧠 Simple Meaning

# 👉 Missing value =
# “data हराएको वा थाहा नभएको value”


# 🔢 1. NaN (Not a Number)


import numpy as np

a = np.array([1, 2, np.nan, 4])
print(a)

print(np.isnan(a))

# 🔍 2. Missing Value Check गर्ने (NumPy)
# 🧠 Concept

# 👉 Missing values (NaN) पत्ता लगाउन NumPy मा np.isnan() प्रयोग गरिन्छ


import numpy as np

a = np.array([1, 2, np.nan, 4])

print(np.isnan(a))


# | Value | Result |
# | ----- | ------ |
# | 1     | False  |
# | 2     | False  |
# | nan   | True ✅ |
# | 4     | False  |


# ✔ True ⇒ missing value छ



# ⚡ Count Missing Values
print(np.isnan(a).sum())


# ✔ 1 वटा missing value छ

# 🔥 Check if any missing value
print(np.isnan(a).any())



# ✔ कम्तीमा 1 missing value छ

# | Function     | Meaning      |
# | ------------ | ------------ |
# | `np.isnan()` | check NaN    |
# | `.sum()`     | count        |
# | `.any()`     | any missing? |
# | `.all()`     | सबै missing? |


# 🧪 Practice
x = np.array([np.nan, 5, 10, np.nan])

print(np.isnan(x))
print(np.isnan(x).sum())

# 👉 Guess output 😉


# ❌ 3. Remove Missing Values (NumPy)
# 🧠 Concept

# 👉 Missing values (NaN) हटाउन Boolean masking प्रयोग गरिन्छ


import numpy as np

a = np.array([1, 2, np.nan, 4])

clean = a[~np.isnan(a)]
print(clean)


# Step-by-step:
# np.isnan(a)

# 👉 [False False True False]

# ~ (NOT operator)
# ~np.isnan(a)

# 👉 [True True False True]

# Apply mask

# 👉 True भएका मात्र select हुन्छन्:

# ✔ 1
# ✔ 2
# ❌ nan (remove)
# ✔ 4

# 🎯 Final Result

# 👉 clean array = [1. 2. 4.]

# ⚡ Important Idea

# 👉 ~ = NOT
# 👉 True → select
# 👉 False → ignore

# 🧪 Practice
x = np.array([10, np.nan, 20, np.nan, 30])

clean = x[~np.isnan(x)]
print(clean)

# 👉 Guess output 😉



# 🔄 4. Replace Missing Values (NumPy)

# 🧠 Concept

# 👉 Missing values (NaN) हटाउनुको सट्टा replace (fill) गर्नु धेरै case मा राम्रो हुन्छ (data loss हुँदैन)

# 🧠 Simple Meaning

# 👉 Replace =
# “missing value लाई नयाँ value ले भरिदिने”



# 🔢 1. Replace with 0
import numpy as np

a = np.array([1, 2, np.nan, 4])

a[np.isnan(a)] = 3
print(a)


# 🔢 2. Replace with Mean (Best Practice 🔥)


import numpy as np
a = np.array([1, 2, np.nan, 4])

mean = np.nanmean(a)
a[np.isnan(a)] = mean

print(a)


# 🧠 किन mean use गर्ने?

# 👉 Mean ले data को balance राख्छ
# 👉 model मा bias कम हुन्छ

# 🔢 3. Replace with Custom Value

import numpy as np
a = np.array([5, np.nan, 10])

a[np.isnan(a)] = 999
print(a)

# 📊 4. 2D Array Example
b = np.array([[1, np.nan],
              [3, 4]])

b[np.isnan(b)] = np.nanmean(b)

print(b)


# | Function          | Use                          |
# | ----------------- | ---------------------------- |
# | `np.nanmean()`    | mean ignoring NaN            |
# | `np.nanmedian()`  | median                       |
# | `np.nan_to_num()` | replace NaN with 0 or custom |

# 🔥 Shortcut
print(np.nan_to_num(a))


# | Method  | Result        |
# | ------- | ------------- |
# | Remove  | data कम हुन्छ |
# | Replace | data बच्छ ✔   |



# 🎯 Why important?

# AI / Data Science मा:

# 📊 data completeness
# 🤖 better model training
# 📉 bias reduction
# 📈 preprocessing

# 🧪 Practice
x = np.array([10, np.nan, 30])

x[np.isnan(x)] = np.nanmean(x)
print(x)

# 👉 Guess output 😉

