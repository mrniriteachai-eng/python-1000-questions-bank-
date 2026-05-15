# 🚀 What is NumPy?

# NumPy (Numerical Python) is a library used for:

# Fast math operations
# Working with arrays (like lists but much more powerful)
# Linear algebra (very important for AI)
# ⚙️ Step 1: Install NumPy

# Open terminal / command prompt:

# pip install numpy
# 🧠 Step 2: Import NumPy
# import numpy as np

# 👉 np is just a shortcut (everyone uses this)

# 🔢 Step 3: Create Arrays

# NumPy uses arrays instead of lists

# import numpy as np

# arr = np.array([1, 2, 3, 4])
# print(arr)
# Output:
# [1 2 3 4]
# 📊 Step 4: 2D Arrays (Matrix)
# matrix = np.array([[1, 2, 3],
#                    [4, 5, 6]])

# print(matrix)
# ⚡ Step 5: Basic Operations (VERY IMPORTANT)
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])

# print(a + b)   # addition
# print(a * b)   # element-wise multiplication
# Output:
# [5 7 9]
# [4 10 18]
# 🎯 Step 6: Useful Functions
# 1. Zeros
# np.zeros((2, 3))
# 2. Ones
# np.ones((2, 2))
# 3. Range
# np.arange(0, 10)
# 📐 Step 7: Shape & Size
# arr = np.array([[1, 2], [3, 4]])

# print(arr.shape)   # rows & columns
# print(arr.size)    # total elements
# 🧮 Step 8: Math Operations
# arr = np.array([1, 2, 3, 4])

# print(np.mean(arr))   # average
# print(np.sum(arr))    # sum
# print(np.max(arr))    # max
# 🧩 Step 9: Indexing
# arr = np.array([10, 20, 30])

# print(arr[0])  # first element

# 2D:

# matrix = np.array([[1, 2], [3, 4]])

# print(matrix[0, 1])  # row 0, column 1
# 🧠 Why NumPy for AI?

# Because:

# Handles vectors & matrices (core of machine learning)
# Faster than Python lists
# Used in libraries like:
# TensorFlow
# PyTorch
# Scikit-learn
# 🧪 Practice Questions (Try Now)
# Create array [5, 10, 15, 20]
# Find sum and mean
# Create 3×3 matrix
# Multiply two arrays
# Print shape of matrix