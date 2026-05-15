# 🔄 4. Vectorization in NumPy


# 🧠 Vectorization के हो?

# 👉 Vectorization भनेको loop (for loop) बिना array मा direct operation गर्नु हो।

# 🧠 Simple Meaning

# 👉 Vectorization =
# “loop नलेखी सबै elements मा एकैचोटि काम गर्नु”


# 🔢 Example 1 (Without Vectorization ❌)
a = [1, 2, 3, 4]

result = []
for i in a:
    result.append(i * 2)

print(result)

# 🔢 Example 2 (With Vectorization ✔)
import numpy as np

a = np.array([1, 2, 3, 4])

print(a * 2)


# | Method        | Code  | Speed   |
# | ------------- | ----- | ------- |
# | Loop          | long  | slow    |
# | Vectorization | short | fast 🚀 |


# ⚡ More Examples
# ➕ Addition


a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

print(a + b)

[11 22 33]
# 🔢 Square
print(a ** 2)



# 📊 Math Functions
# print(np.sqrt(a))
# 🎯 Why Vectorization important?

# AI / Data Science मा:

# ⚡ faster computation
# 💾 optimized memory use
# 📊 large datasets handle गर्न सजिलो
# 🤖 ML algorithms fast हुन्छ
# 🔥 Real Insight

# 👉 NumPy internally C language use गर्छ
# 👉 त्यसैले vectorized operations धेरै fast हुन्छ

# 🧪 Practice
x = np.array([5, 10, 15])

print(x + 5)
print(x * 3)

# 👉 Guess output 😉