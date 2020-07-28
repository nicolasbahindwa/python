from numpy import *

# arr1 = array([

#               [1,2,3,7,8,9],
#               [4,5,6,5,4,3]

#               ])
# arr2 = arr1.flatten()

# #arr3 = arr2.reshape(3,4)
# arr3 = arr2.reshape(2,2,3)

# print(arr1)
# print(arr1.ndim)
# print(arr1.shape)
# print(arr1.size)

# print(arr2)

# print(arr3)

## ================ MATRIX ================================

# arr1 = array([

#               [1,2,3,7],
#               [4,5,6,5]

#             ])

# m = matrix(arr1)
# print(m)

# n = matrix ('1,2,3;4,5,7;4,6,8')
# print(n)
# print(diagonal(n))

m1 = matrix('1,2,3;6,4,5;1,6,7')
m2 = matrix('1,2,3;6,4,5;1,6,7')

m3 = m1 * m2;

print(m3)



