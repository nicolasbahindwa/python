
def div(a,b):
    if a<b:
        a,b = b,a
    print(a/b)

def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)

    return inner
div1 = smart_div(div)
print(type(div1))
div1(2,4)