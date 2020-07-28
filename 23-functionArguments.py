

def update(lst):
    print(id(lst))
    

    lst[1]=25
    print(id(lst))
    print("x", lst)

lst =[10,30,40]
print(id(lst))
update(lst)
print("x", lst)
    

 