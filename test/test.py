import numpy as np

arr = np.array([1, 1, 1, 1, 1, 0])
res = arr + (arr[:] != 0)

print(res)
