# 📊 6. Linear Algebra in NumPy (AI का लागि 🔥)


# 🧠 Linear Algebra के हो?

# 👉 matrices (2D arrays) मा हुने math operations लाई linear algebra भनिन्छ।

# 🧠 Simple Meaning

# 👉 Linear Algebra =
# “matrix (array) प्रयोग गरेर calculation गर्ने system”


# 🔢 1. Matrix Multiplication (np.dot())


import numpy as np

a = np.array([[1,2,3],
              [4,5,6]])

b = np.array([[7,8],
              [9,10],
              [11,12]])
print(a.nbytes)

print(np.dot(a, b))

#### row and colum same hunu paryo 

# 🔢 Result = a · b


# 👉 First row × first column:
# (1×7) + (2×9) + (3×11)
# = 7 + 18 + 33 = 58


# 👉 First row × second column:
# (1×8) + (2×10) + (3×12)
# = 8 + 20 + 36 = 64

# 👉 Second row × first column:
# (4×7) + (5×9) + (6×11)
# = 28 + 45 + 66 = 139

# 👉 Second row × second column:
# (4×8) + (5×10) + (6×12)
# = 32 + 50 + 72 = 154

import numpy as np

a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])

print(np.dot(a, b))

# 🧠 Rule (Important)

# 👉 multiplication possible हुन्छ यदि:

# columns of A = rows of B


# 🔄 2. Transpose (.T)
# print(a.T)

# 👉 rows ↔ columns swap

import numpy as np

a = np.array([[1, 2],
              [3, 4]])


print(a.T)

import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])

print(a.T)


# 🧠 What happened?
# Before:
# 1  2  3
# 4  5  6

# 👉 Shape = (2, 3)

# After .T:
# 1  4
# 2  5
# 3  6

# 👉 Shape = (3, 2)

# ✔ rows → columns
# ✔ columns → rows

# 📊 Shape Check
print(a.shape)     # (2, 3)
print(a.T.shape)   # (3, 2)


# ⚠️ 1D Array Case (Important)
b = np.array([1, 2, 3])
print(b.T)



# ✔ 1D मा transpose गर्दा change देखिँदैन

# 🔥 Why important?
# 🤖 Matrix multiplication
# 📊 Linear algebra
# 📈 Data transformation
# 🧠 Neural networks
# 🧪 Practice
x = np.array([[10, 20],
              [30, 40],
              [50, 60]])

print(x.T)

# 👉 Try guess output 😉



# 🔁 3. Matrix Inverse (np.linalg.inv())


# 🧠 Matrix Inverse के हो?
# 👉 Matrix inverse भनेको division जस्तै concept हो (numbers मा जस्तो 1/x1/x1/x, matrix मा inverse हुन्छ)

# 🧠 Simple Meaning
# 👉 Inverse =
# “matrix लाई यस्तो बनाउने कि original matrix सँग multiply गर्दा identity matrix आउँछ”

# 📐 Identity Matrix Idea
# 👉
# A⋅A−1=I

# जहाँ I = identity matrix


# जहाँ III = identity matrix


# EXAMPLE

import numpy as np

a = np.array([[1,2],
             [4,5]])

inv = np.linalg.inv(a)

print(inv)

# 📐 Inverse formula (for 2×2 matrix):

# a inverse = 



# A−1 = 1/ad−bc[d,-b]
#              [-c,a]

import numpy as np

a = np.array([[1, 2],
              [3, 4]])

inv = np.linalg.inv(a)

print(inv)

print(a @ inv)


# | Operation   | 2×3 matrix     |
# | ----------- | -------------- |
# | determinant | ❌ not possible |
# | inverse     | ❌ not possible |
# | adjoint     | ❌ not possible |
# | transpose   | ✅ possible     |
# | reshape     | ✅ possible     |


# ⚠️ Important Rule

# 👉 सबै matrix को inverse हुँदैन ❗

# ✔ Condition:

# 👉 determinant ≠ 0 हुनुपर्छ

# ❌ Example (No Inverse)
import numpy as np
b = np.array([[1, 2],
              [2, 4]])

print(np.linalg.inv(b))

# 👉 Error आउँछ ❗
# ✔ किन? determinant = 0

# 🧠 Why important?

# AI / Data Science मा:

# 📊 Linear equations solve गर्न
# 🤖 Machine learning algorithms
# 📈 optimization problems
# 🧠 neural networks math
# 🧪 Practice
x = np.array([[2, 0],
              [0, 2]])

print(np.linalg.inv(x))

# 👉 Guess output 😉




# 📐 4. Determinant (np.linalg.det())



# 🧠 Determinant के हो?

# 👉 Determinant भनेको matrix को एक special number (scalar value) हो जसले matrix को property (जस्तै invertible छ कि छैन) बताउँछ।

# 🧠 Simple Meaning

# 👉 Determinant =
# “matrix कस्तो छ (valid/invertible कि छैन) भनेर check गर्ने value”

# 🔢 Example

import numpy as np

a = np.array([[1,2],
              [3,4]])

det = np.linalg.det(a)
print(det)



# 🧠 Formula (2×2 matrix)

# यदि


# A= [a  ​b​]
#    [c  d]



# 👉 determinant:

# ad−bc

# ✔ यहाँ:

# (1×4)−(2×3)=4−6=−2

###

import numpy as np

a = np.array([[6, 2],
              [8, 4]])

print(np.linalg.det(a))


# | Determinant | Meaning                |
# | ----------- | ---------------------- |
# | ≠ 0         | ✔ inverse possible     |
# | = 0         | ❌ inverse possible छैन |


# ❌ Example (No Inverse)
import numpy as np
b = np.array([[1, 2],
              [2, 4]])

print(np.linalg.det(b))



# 🔗 Connection with Inverse

# 👉

# det ≠ 0 → np.linalg.inv() काम गर्छ
# det = 0 → error आउँछ


# 🎯 Why important?

# AI / Data Science मा:

# 📊 matrix valid छ कि छैन check
# 🤖 solving linear equations
# 📈 optimization problems
# 🧠 linear algebra base
# 🧪 Practice
x = np.array([[2, 0],
              [0, 2]])

print(np.linalg.det(x))

# 👉 Guess output 😉



# 🎯 5. Eigenvalues (Advanced 🔥)
