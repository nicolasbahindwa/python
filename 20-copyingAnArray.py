from numpy import *

# arr1 = array([1,2,3,4,5])

# arr2 = array([6,2,3,4,5])

# arr3 = arr1 + arr2

# print(arr3)

#=====================================

# arr1 = array([2,1,3,4,5])

# print(sum(arr1))
# print(max(arr1))
# print(sorted(arr1))

#-----------------------------------------


# arr1 = array([2, 1, 3, 4, 5])
# arr2 = array([2, 4, 6, 9, 5])

# print(concatenate([arr1,arr2]))

#-------------------------------------------

arr1 = array([2, 1, 3, 4, 5])

#arr2 = arr1.view() #shallow copy
arr2 = arr1.copy()

print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))