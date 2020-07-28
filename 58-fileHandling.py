
#f= open('FileHandling.txt','r')
#read from file
# print(f.read())
# print(f.readline(),end="")
# print(f.readline(4), end="")

#writing files and create of not available

# f= open('FileHandling.txt','r')
# f.write("my name is nicolas bahindwa ")

#open file and append 
# f = open('abc.txt', 'a')
# f.write(" nice to meet you!")

#copy from file to file
# f = open('FileHandling.txt','r')
# f1 = open('abc.txt','w')

# for data in f:
#     # print(data)
#     f1.write(data)

# read an binary file

f2 = open('nicolas.jpeg','rb')
# for data in f2:
#     print(data)

#write a binary file
f3 = open('nicolasWR.jpg', 'wb')

for data in f2:
    f3.write(data)

