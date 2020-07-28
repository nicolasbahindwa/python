
postition = -1

def Search(list,n):
    lowerbound = 0
    upperbound = len(list)-1

    while lowerbound <= upperbound:
        mid = (lowerbound + upperbound)//2

        if list[mid] == n:
            globals()['position'] =mid
            return True
        else:
            if list[mid] < n:
                lowerbound = mid + 1
            else:
                upperbound = mid - 1
    return False


list = [4,7,8,12,45,99]
n = 10

if Search(list, n):

    print('Found at position ', position)
else:
    print("Not Found")
