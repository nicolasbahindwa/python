
def sort(arr):

    
    for i in range(len(arr)-1):
        minval = i
        for j in range(i + 1,len(arr)-1):
            if arr[j] < arr[minval]:
                minval = j
        arr[i],arr[minval] = arr[minval ],arr[i]
#print(arr)
                


arr = [3,6,4,1,9,10,8]
sort(arr)
print(arr)
 

