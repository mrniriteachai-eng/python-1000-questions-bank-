import numpy as np

arr_2d = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])
print(arr_2d)

## NumPy Array Propertie

import numpy as np

arr = np.array([[1,2,3],
                [4,5,6]])
print(arr)


## MULTIDIMENSIONAL ARRAY
## MATRIX

import numpy as np
matrix = np.array([[2,3,4],
                   [8,10,11]])
print(matrix)

### creating arrays from python lists

import numpy as np

arr = np.array([1,2,3,4])
print(arr)

## default value
## np.zeros(shape) (3)  fir 1d, (3,3) 

import numpy as np

a = np.array([[[1,2,3],
              [4,5,6],
              [7,8,9]]])
print(a)
print(a.ndim)




##### n array

import numpy as np
a = np.array([[[[[[[[[[[[[[[[[[[[[[[[[[1,2,3]]]]]]]]]]]]]]]]]]]]]]]]]])
print(a)
print(a.ndim)