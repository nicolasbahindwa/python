from functools import reduce

# def is_even(n):
#     return n%2==0

# def update(n):
#     return n*2

num = [2,3,4,5,6,7,4,8,5,9]

# evens = list(filter(is_even,num))

evens = list(filter(lambda n : n%2==0, num))

#doubles =list(map(update,evens))
doubles = list(map(lambda n: n*2, evens))

sums = reduce(lambda a,b: a+b,doubles)



print(evens)
print(doubles)
print(sums)
