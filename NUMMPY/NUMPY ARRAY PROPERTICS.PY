import numpy as np

arr = np.array([[1,2,3],
                [4,5,6]])
print(arr)

## NumPy Array Propertie

import numpy as np

niri = np.array([[1,2,3],
                [4,5,6]])
print(niri)


### matrix of arrays
 
import numpy as np

arr  = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])
print(arr)
###
import numpy as np

nir = np.array([[1,2,3],
                [1,3,4],
                [5,4,5]])
print(nir)

# 📊 Main Properties
# 1. .ndim (Dimension)

# 👉 array कति dimension को छ?

## yasle herxa arry kun dimension ko x vaner



import numpy as np

arr_1d = np.array([1,2,3])
arr_2d = np.array([[1,3,4],[4,5,6]])
arr_3d = np.array([[[1,2,3],[4,5,6],[7,8,9],[5,6,7]]])
print(arr_1d.ndim)
print(arr_2d.ndim)
print(arr_3d.ndim)

#### 1d array
import numpy as np

a = np.array([1,2,3])
print(a.ndim)

###

import numpy as np 

a = np.array([1,2,3,4,5])
print(a.ndim)

### 2d arrys

import numpy as np

b = np.array([[1,2,3],
              [4,5,6]])
print(b.ndim)



import numpy as np
c = np.array([[1,2,3],
              [4,5,6],
              [7,8,9],
              [10,11,12]])
print(c.ndim)


### 3d arrays
c = np.array([[[1,2,3],
               [4,5,6]]])

print(c.ndim)


# 🎯 Easy Trick
# arr type           Eg              .NDIM
# arr_1d         [1,2,3]              1
# arr_2d         [[1,2,3],[1,2,3]]    2
# arr_3d         [[[1,2,3]]]          3


import numpy as np

x = np.array([[1,2],[3,4],[5,6]])
print(x.ndim)

# 2. .shape (Shape)

# 📊 .shape के हो?

# 👉 .shape ले बताउँछ:

# array को size कस्तो छ (rows, columns, …)

# 👉 .shape =
# “यो array कति rows र columns को छ?

# example 

### 1d arrys

import numpy as np

a = np.array([1,2,3,4])
print(a.shape)

# 👉 मतलब:

# 4 वटा element छन्
# 1D array हो


### 2d arrays

import numpy as np

b = np.array([[1,2,3],
              [4,5,6]])
print(b.shape)


##
b = np.array([[1, 2, 3],
              [4, 5, 6]])

print(b.shape)

# 👉 मतलब:

# 2 rows
# 3 columns

### : 3D Array


import numpy as np
c = np.array([[[1,2,3], [4,5,6]]])
               

print(c.shape)

# 👉 मतलब:

# 1 layer
# 2 rows
# 3 columns

# | Array Type | Shape                  |
# | ---------- | ---------------------- |
# | 1D         | `(n,)`                 |
# | 2D         | `(rows, cols)`         |
# | 3D         | `(layers, rows, cols)` |



x = np.array([[1,2],
              [3,4],
              [5,6]])
print(x.shape)

# 👉 .shape ले array को structure (size) देखाउँछ।


## 3. .size (Total elements)



# 📊 .size के हो?

# 👉 .size ले बताउँछ:

# array भित्र जम्मा कति वटा elements (values) छन्

# 👉 .size =
# “कुल कति number छन्?”


# 🔢 Example 1: 1D Array


import numpy as np

a = np.array ([1,2,3])
print(a.size)

# 👉 4 वटा elements छन्

# 📊 Example 2: 2D Array

import numpy as np
b = np.array([[1, 2, 3],
              [4, 5, 6]])

print(b.size)

# 👉 2 × 3 = 6 elements

# 🧊 Example 3: 3D Array

import numpy as np
c = np.array([[[1,2,3],
               [4,5,6]]])

print(c.size)

# 👉 1 × 2 × 3 = 6 elements



# 🎯 Easy Formula

# 👉 .size = shape का सबै number multiply

# Example:

# shape = (2, 3)
# size = 2 × 3 = 6



# | Property | Meaning                |
# | -------- | ---------------------- |
# | `.shape` | structure (rows, cols) |
# | `.size`  | total elements         |

# 🧪 Practice
import numpy as np
x = np.array([[1,2],[3,4],[5,6]])
print(x.size)

# 👉 Guess answer 😄

# .size ले array भित्र कति वटा elements छन् भनेर देखाउँछ।




# 4. .dtype (Data type)


# 📊 .dtype के हो?

# 👉 .dtype ले बताउँछ:

# array भित्रको data कस्तो type को छ (int, float, string आदि)


# 👉 .dtype =
# “यो data कुन type को हो?”

# 🔢 Example 1: Integer Array

import numpy as np

a = np.array([1, 2, 3])
print(a.dtype)


import numpy as np

n = np.array([1,3,5])
print(n.dtype)

# int64   (system अनुसार int32 पनि हुन सक्छ)

# 👉 मतलब: integer values

# 🔵 Example 2: Float Array

import numpy as np
b = np.array([1.5, 2.5, 3.5])
print(b.dtype)

# 👉 मतलब: decimal values

# 🔤 Example 3: String Array

import numpy as np

a = np.array(["nirmal","saud"])

print(a.dtype)



# ⚡ Mixed Data (Important)

import numpy as np

a = np.array([1,1.4,"nirmal"])
print(a.dtype)


####
x = np.array([1, 2.5, 3])
print(x.dtype)



# 👉 NumPy automatically convert गर्छ (upcasting)


# | Type                | Meaning    |
# | ------------------- | ---------- |
# | `int32 / int64`     | integer    |
# | `float32 / float64` | decimal    |
# | `bool`              | True/False |
# | `<U`                | string     |



# 🔧 Force Data Type

# 👉 तिमी आफैले type set गर्न सक्छौ:

import numpy as np

a = np.array([1,2,1.4]) , dtype = float

print(a.dtype)


###
import numpy as np
a = np.array([1,2,3], dtype= str)
print(a.dtype)

# 🧪 Practice
x = np.array([10, 20, 30])
print(x.dtype)

# 👉 Guess answer 😄




# 5. .itemsize (Item size in NumPy)

# .itemsize le NumPy array ko each element le kati bytes memory occupy गर्छ भन्ने देखाउँछ।

import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr.itemsize)

# यहाँ output 4 भनेको प्रत्येक element ले 4 bytes memory लिन्छ भन्ने हो।
# यो value array को data type (dtype) मा depend गर्छ:
# int32 → 4 bytes
# int64 → 8 bytes
# float64 → 8 bytes


# 💾 6. .nbytes (Total Memory Usage in NumPy)

# 👉 .nbytes के हो?

# .nbytes ले बताउँछ:
# 👉 पूरै array ले कति bytes memory use गरेको छ

# 🧠 Simple Meaning

# 👉 .nbytes =
# “पूरै data ले कति memory खाएको छ?”

# 🔢 Formula (Very Important)

# 👉 .nbytes = itemsize × number of elements


import numpy as np

a = np.array([1, 2, 3, 4])
print(a.nbytes)




# 🔍 Why 16 bytes?
# Each element = 4 bytes (int32)
# Total elements = 4

# 👉 4 × 4 = 16 bytes

# 🔢 Example 2 (Float array)

import numpy as np
b = np.array([1.5, 2.5, 3.5])
print(b.nbytes)

# float64 = 8 bytes
# 3 elements → 3 × 8 = 24 bytes

# | Property    | Meaning           |
# | ----------- | ----------------- |
# | `.itemsize` | 1 element memory  |
# | `.size`     | total elements    |
# | `.nbytes`   | total memory used |


# ⚡ Quick Formula Chain

# 👉 .nbytes = .size × .itemsize



import numpy as np
x = np.array([10, 20, 30, 40, 50])

print(x.size)      # 5 elements
print(x.itemsize)  # 4 bytes (int32)
print(x.nbytes) 
print(x.any)   # 20 bytes

# 🎯 Why .nbytes important?

# AI / Data Science मा:

# 💾 Memory tracking
# 🚀 Big dataset optimization
# ⚡ Faster processing
# 📉 Reducing resource usage

# 🧪 Practice Question

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
print(arr.nbytes)


# 🔄 7. .T (Transpose in NumPy)

# 👉 .T के हो?
# .T ले NumPy array को rows र columns उल्टाइदिन्छ (swap गर्छ)।

# 🧠 Simple Meaning
# 👉 .T =
# “rows ↔ columns change गर”

# 📊 Example 1: 2D Array

import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])

print(a.T)

##### example


import numpy as np

a= np.array([[1,2,3,8],
             [4,5,6,7]])
print(a.T)
# 🔍 What happened?

# Original shape:

# 2 rows × 3 columns

# After transpose:

# 3 rows × 2 columns

# ✔ Rows → Columns
# ✔ Columns → Rows

# 🧠 Visual Understanding
# Before .T
# 1  2  3
# 4  5  6
# After .T
# 1  4
# 2  5
# 3  6

b = np.array([[10, 20],
              [30, 40],
              [50, 60]])

print(b.shape)
print(b.T.shape)



# ⚡ Important Rule

# 👉 .T works mainly on:

# 2D arrays (matrices)
# Higher dimension arrays too



# 🎯 Why .T important?

# AI / Machine Learning मा:

# 🤖 Matrix operations
# 📊 Linear algebra
# 🧠 Neural networks
# 🔄 Feature transformation
# 🔥 Shortcut idea

# 👉 .T = transpose(matrix)

# 🧪 Practice
x = np.array([[1, 2],
              [3, 4],
              [5, 6]])

print(x.T)

# 👉 Try guess the output shape 😉


# 👉 .T = array को rows ↔ columns swap गर्ने tool (transpose)

