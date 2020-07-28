position = -1

def Search(list,n):
    i=0

    # while i < len(list):
    #     if list[i] == n:
    #         globals()['position'] = i
    #         return True
    #     i = i + 1 
    # return False
    
    for i in range(len(list)):
        if list[i] == n:
            globals()['position'] = i
            return True
    return False


list = [5,8,6,9,2]
n = 9

if Search(list,n):

    print('Found at position ', position)
else:
    print("Not Found")
