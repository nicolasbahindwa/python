

name = ("nicolas","bahindwa","kobe")
comps = ("dell","apple","ms")

zipped = list(zip(name,comps))
Set = set(zip(name, comps))
Dict = dict(zip(name, comps))



print(zipped)
print(Set)
print(Dict)

for (a,b) in zipped:
    print(a,b)
