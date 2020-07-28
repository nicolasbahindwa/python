
def person(name, **data):

    print(name)

    for i,j in data.items():
        print(i,j)


person('nicolas',age= 29,city='saitama', tel=988332)

