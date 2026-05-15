# 🧮 5. Mathematical Functions in NumPy

# 🧠 Mathematical Functions के हो?

# 👉 NumPy ले array भित्रका values मा direct mathematical operations (math functions) apply गर्न सक्छ।

# 🧠 Simple Meaning

# 👉 Mathematical functions =
# “array को data मा math operations एकैचोटि apply गर्नु”

# 🔢 1. Square Root (np.sqrt())
import numpy as np

a = np.array([1, 4, 9, 16])

print(np.sqrt(a))



# ✔ प्रत्येक number को square root निकाल्यो

# 🔢 2. Exponential (np.exp())

# 👉 e^x (Euler number आधारित)


import numpy as np
a = np.array([1, 2, 3])

print(np.exp(a))


# 📐 Formula:

# e ko power x
# 🧠 Element-wise working:

# e ko power 1 =2.718
# e ko power 2 =7.38
# e ko power 3 =20.085



# 🔢 3. Logarithm (np.log())

# 👉 It’s the inverse of exponential e ko power x

# 👉 natural log (ln)
# 📐 Formula:

# ln(x)
import numpy as np
a = np.array([1, 2, 3])

print(np.log(a))


import numpy as np

x = np.array([1, np.e, 10])

result = np.log(x)

print(result)


# 🧠 Understanding:
# ln(1)=0
# ln(e)=1
# ln(10)≈2.302


# ⚠️ Important rules:
# ❌ log(0) → -inf (undefined)
# ❌ log(negative) → nan
# ✅ input must be positive


# 💡 Related functions:
# np.log10(x) → log base 10
# np.log2(x) → log base 2


# 🔄 Connection with exp:
# np.log(np.exp(2))  # = 2


# 🔢 4. Absolute (np.abs())


# 👉 negative → positive बनाउने



import  numpy as np
a = np.array([-1, -5, 3])

print(np.abs(a))


# 🔢 5. Power (np.power())


import numpy as np
a = np.array([1, 2, 3])

print(np.power(a, 3))

# 🔢 6. Trigonometry Functions
import numpy as np
a = np.array([0, np.pi/2, np.pi])

print(np.tan(a))



# 📐 Concept:

# sin(x)

# NumPy computes sine using radians (not degrees ⚠️)

# 🧠 Values:
# sin(0)=0
# sin(pi/2) = 1
# sin(π)=0


# 👉 If you use degrees, convert first:

np.sin(np.deg2rad(90)) 


# 🔥 Other trig functions:
# np.cos(a)
# np.tan(a)


import numpy as np

angles = np.array([0, np.pi/4, np.pi/2])

print("sin:", np.sin(angles))
print("cos:", np.cos(angles))
print("tan:", np.tan(angles))



# 📌 Example 2: Using degrees
angles_deg = np.array([0, 30, 90])

angles_rad = np.deg2rad(angles_deg)

print(np.sin(angles_rad))

# | Quadrant        | sin | cos | tan |
# | --------------- | --- | --- | --- |
# | I (0°–90°)      | +   | +   | +   |
# | II (90°–180°)   | +   | −   | −   |
# | III (180°–270°) | −   | −   | +   |
# | IV (270°–360°)  | −   | +   | −   |

# Easy memory trick: ASTC
# A → All positive (Quadrant I)
# S → Sine positive (Quadrant II)
# T → Tangent positive (Quadrant III)
# C → Cosine positive (Quadrant IV)

# ASTC


# sin(90∘−a)=cosa



# full table
# | Angle | rad | sin  | cos  | tan       |
# | ----- | --- | ---- | ---- | --------- |
# | 0°    | 0   | 0    | 1    | 0         |
# | 30°   | π/6 | 1/2  | √3/2 | 1/√3      |
# | 45°   | π/4 | √2/2 | √2/2 | 1         |
# | 60°   | π/3 | √3/2 | 1/2  | √3        |
# | 90°   | π/2 | 1    | 0    | undefined |



# 🧠 Key Idea

# 👉 NumPy math functions = vectorized (loop बिना fast computation)

# ⚡ Why important?

# AI / Data Science मा:

# 📊 data transformation
# 🤖 machine learning preprocessing
# 📈 signal processing
# 🧠 neural networks
# 🔥 Real Example (AI Style)



# 🔥 Real-life idea:
# Used in graphics 🎮 (rotation)
# Used in physics (waves 🌊)
# Used in AI (signal processing)





marks = np.array([36, 45, 80, 90])

print(np.sqrt(marks))
print(np.log(marks))
# 🧪 Practice   
# 🧩 Unit Circle (radius = 1)
            
#          (0,1)
#               ↑
#               |   sin(θ)
#               |                                       
#               |
# (-1,0) ←------•------→ (1,0)
#               |
#               | 
#               ↓
#             (0,-1)


# x2+y2=1

# 📍 Center point (•)
# This is (0, 0)


# ➡️ Right side (1, 0)
# Angle = 0° (0 rad)
# cos(0) = 1
# sin(0) = 0



# ⬆️ Top (0, 1)
# Angle = 90° (π/2)
# cos(π/2) = 0
# sin(π/2) = 1



# ⬅️ Left (-1, 0)
# Angle = 180° (π)
# cos(π) = -1
# sin(π) = 0


# ⬇️ Bottom (0, -1)
# Angle = 270° (3π/2)
# cos(3π/2) = 0
# sin(3π/2) = -1



# 📐 Key idea:
# Center = (0, 0)
# Radius = 1
# Any point on circle =
# 👉 (cosθ, sinθ)


# 🔥 Visual with angle:


            # (0,1)
            #   ↑
            #   |\
            #   | \   ← point (cosθ, sinθ)
            #   |  \
            #   |   \ θ
            #   •----→ (1,0)


# | Angle       | Coordinates (cosθ, sinθ) |
# | ----------- | ------------------------ |
# | 0° (0 rad)  | (1, 0)                   |
# | 90° (π/2)   | (0, 1)                   |
# | 180° (π)    | (-1, 0)                  |
# | 270° (3π/2) | (0, -1)                  |


# 🧠 Important:
# cos(θ) = x-coordinate
# sin(θ) = y-coordinate



import numpy as np

theta = np.pi / 4  # 45 degrees

print("cos:", np.cos(theta))
print("sin:", np.sin(theta))

# 🚀 Why this matters:
# Helps understand sin, cos, tan
# Used in graphics, AI, physics, waves


# 🧪 Practice  
x = np.array([4, 9, 16])

print(np.sqrt(x))


# \sin^2(x) + \cos^2(x) = 1

# 👉 Guess output 😉