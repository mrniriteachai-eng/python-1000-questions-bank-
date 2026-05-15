# ⚡ 1. Broadcasting in NumPy
# 🧠 Broadcasting के हो?

# 👉 Broadcasting भनेको NumPy ले different shape भएका arrays बीच automatic operation गराउने system हो — बिना manually same size बनाउनु।

# 🧠 Simple Meaning

# 👉 Broadcasting =
# “सानो array लाई ठूलो जस्तो बनाएर calculation गर्नु”


# 🔢 Example 1: Scalar + Array
import numpy as np

a = np.array([1, 2, 3])

print(a + 10)
# ✔ 10 सबै elements मा add भयो

# 📊 Example 2: 1D + 2D



import numpy as np
a = np.array([[1, 2, 3],
              [4, 5, 6]])

b = np.array([10, 20, 30])

print(a + b)
print(a * b)
print(a - b)

# ✔ b लाई प्रत्येक row मा apply गरियो


# 🧠 How Broadcasting Works (Rules)
# 📌 Rule 1:

# 👉 Shapes compare from right to left

# 📌 Rule 2:

# 👉 Dimensions match हुनुपर्छ वा 1 हुनुपर्छ

# 🔍 Example:
# a shape = (2, 3)
# b shape = (3,)

# 👉 NumPy internally यसरी सोच्छ:

# (2, 3)
# (1, 3)

# ✔ compatible भयो

# ❌ Invalid Example

import numpy as np
a = np.array([[1,2,3],
              [4,5,6]])

b = np.array([10,20])

print(a + b)

# 👉 Error आउँछ ❗

# ✔ किन? shape match भएन

# 🎯 Why Broadcasting important?

# AI / Data Science मा:

# ⚡ fast computation
# 🧠 less code
# 📊 large dataset handling
# 🤖 matrix operations


import numpy as np
x = np.array([[1, 2],
              [3, 4]])

y = np.array([10, 20])

print(x * y)


import numpy as np
a = np.array([[1,2,3,],
             [2,3,4,],
             [2,3,4,]])
b = np.array([[1,2,3,],
             [2,3,4,],
             [2,3,4,]])

print(a * b)

print(a.shape)


# 🧪 Practice
x = np.array([[1, 2],
              [3, 4]])

y = np.array([10, 20])

print(x + y)

# 👉 Guess output 😉
