import numpy as np

a = np.array([1, 2, np.nan, 4])

a[np.isnan(a)] = 3
print(a)