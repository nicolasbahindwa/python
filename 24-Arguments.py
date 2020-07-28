

def person(name,age=18):
    print(name)
    print(age)

person('nicolas',29)
person(age=20, name='nicolas')

#tuple arguments
def sum(a, *b):
    c = a

    for i in b:
        c= c+i

    print(c)

sum(5,6,7,34)
