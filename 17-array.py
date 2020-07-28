import array 
import array as arr
from array import *

vals = array('i',[5,9,8,4,2])

newArr = array(vals.typecode, (a for a in vals))

#vals.reverse()
# for i in range(len(vals)):
#     print(vals[i])

# for e in newArr :
#     print(e)

i = 0
while i< len(newArr):
    print(newArr[i])
    i+=1
