import numpy as np

arr= np.array([10,20,30])

print(arr + 5)
print(arr * 2)
print(arr ** 2)



# 🔢 Common Aggregation Functions

# 1. ➕ sum()

# 👉 सबै elements जोड्छ

import numpy as np

arr = np.array([1,2,3])
print(arr.sum())



import numpy as np
n = np.array([1,4,5])
print(arr.sum())

# 2. 📈 mean()

# 👉 average निकाल्छ
## bich ko 

import numpy as np

a = np.array([1,2,3])
print(a.mean())

# 3. 🔝 max()

# 👉 सबैभन्दा ठूलो value


import numpy as np

a = np.array([1,2,3])
print(a.max())



# 4. 🔻 min()

# 👉 सबैभन्दा सानो value

import numpy as np

a = np.array([1,2,3])
print(a.min())

# 5. 📏 std() (Standard Deviation)

# 👉 data कति फैलिएको छ

import numpy as np

a = np.array([1,2,3])
print(a.std())

# 🧠 यसलाई बुझ्ने तरिका
# Step 1: Mean निकाल्ने
# (1+2+3)/3=2
# Step 2: प्रत्येक value mean बाट कति टाढा छ?
# 1 → 1 unit टाढा
# 2 → 0
# 3 → 1 unit टाढा

# 👉 data धेरै टाढा छैन ⇒ std सानो हुन्छ

# 🎯 Key Idea
# Situation	Standard Deviation
# data close together	🔹 small std
# data धेरै फरक फरक	🔥 large std
# 📊 Example 2 (Better Understanding)

b = np.array([10, 10, 10])
print(b.std())



# ✔ किन?
# सबै value एउटै छन् ⇒ कुनै variation छैन

# 📊 Example 3 (Spread data)

c = np.array([1, 10, 20])
print(c.std())



# ✔ धेरै फरक values ⇒ std ठूलो

# 🧠 Formula (simple idea)

# Standard Deviation:
# 👉 mean बाट distance को average spread

# 🎯 Why important?

# AI / Data Science मा:

# 📊 data variability बुझ्न
# 🤖 model accuracy analysis
# 📉 noise detect गर्न
# 📈 pattern understand गर्न


# 6. 📊 var() (Variance)


# 👉 spread measure गर्छ

import numpy as np

a = np.array([1, 2, 3])
print(a.var())

# 🧠 कसरी काम गर्छ?
# Step 1: Mean निकाल्ने
# (1+2+3)/3=2
# Step 2: difference निकाल्ने
# 1 - 2 = -1
# 2 - 2 = 0
# 3 - 2 = 1
# Step 3: square गर्ने
# (-1)² = 1
# 0² = 0
# 1² = 1
# Step 4: average
# (1+0+1)/3=0.666...


# 🎯 Final Idea

# 👉 Variance = average squared distance from mean

# 🧠 Variance vs Standard Deviation

# Concept	Meaning
# var()	squared spread
# std()	real spread
# 🔥 Relation (Important)

# 👉

# std = root of variance
# 	​

# 🎯 Why important?

# AI / Data Science मा:

# 📊 data distribution बुझ्न
# 🤖 model stability check गर्न
# 📉 noise detect गर्न
# 📈 feature scaling (very important)
# 🔥 Final Line

# 👉 var() = data कति फैलिएको छ भनेर squared form मा measure गर्ने function