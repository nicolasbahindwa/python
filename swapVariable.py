
a = 5
b = 6
#to swap the 2 numbers, first method

temp = a
a = b
b = temp

print(a)
print(b)

#second method

a = a + b
b = a - b
a =  a - b

print(a)
print(b)

#third method

a = a ^ b
b = a ^ b
a = a ^ b

print(a)
print(b)

#fourth method
a,b = b,a



