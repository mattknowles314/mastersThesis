import numpy as np

X = np.array([  
    [0, 0, 1,7],
    [0, 1, 1,3],
    [1, 0, 0,2],
    [1, 1, 0,1],
    [1, 0, 1,7],
    [1, 1, 1,0],
])
K=3

t = np.random.random((3,3))-5
x = 5*t
print(t)
print(x)