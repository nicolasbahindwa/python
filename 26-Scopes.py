# out function
a=10
print(id(a))
def somthing():
    a = 9

    x= globals()['a']
    print(id(x))
    print('in fun',a)

    globals()['a']=15

    # global a
    # a =15
 
    #in function
   # a = 15
   

    print(a)



somthing()
print(a)
