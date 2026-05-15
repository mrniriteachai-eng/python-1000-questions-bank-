# 🎯 3. np.where() (Where Function in NumPy)

# 🧠 np.where() के हो?

# 👉 np.where() ले condition अनुसार value choose/replace गर्ने काम गर्छ।

# 🧠 Simple Meaning

# 👉 np.where() =
# “यदि condition True भए X, होइन भने Y”

# 🔢 Syntax (Important)

# np.where(condition, value_if_true, value_if_false)

# np.where(condition, value_if_true, value_if_false)

# 🔢 1. Basic Example

import numpy as np

a = np.array([10, 20, 30, 40])

result = np.where(a > 25, "High", "Low")
print(result)

# | Value | Condition | Result |
# | ----- | --------- | ------ |
# | 10    | False     | Low    |
# | 20    | False     | Low    |
# | 30    | True      | High   |
# | 40    | True      | High   |


# ⚡ 2. Numeric Replacement
import numpy as np
a = np.array([1, 2, 3, 4, 5])

result = np.where(a % 2 == 0, 0, a)
print(result)

# ✔ even numbers → 0 बनाइयो


# 📊 3. Only Condition (Index निकाल्ने)

import numpy as np
a = np.array([10, 20, 30, 40])

print(np.where(a > 25))

# ✔ index 2 र 3 (30, 40)


# 🔥 4. 2D Example

b = np.array([[1, 2],
              [3, 4]])

print(np.where(b > 2, 1, 0))


# | Feature | Boolean Masking | np.where() |
# | ------- | --------------- | ---------- |
# | Use     | filter          | replace    |
# | Output  | subset          | full array |

# 🎯 Why important?

# AI / Data Science मा:

# 📊 data transformation
# 🤖 labeling (High/Low, Pass/Fail)
# 📉 preprocessing
# 📈 condition-based modification
# 🧪 Practice
x = np.array([5, 15, 25, 35])

print(np.where(x > 20, "Big", "Small"))


# 👉 Guess output 😉

