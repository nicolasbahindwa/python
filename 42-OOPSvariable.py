

class car:
    #class variable
    wheels = 4

    def __init__(self):
        #instance variable
        self.millage = 10
        self.maker = "bmw"

c1 = car()
c2 = car()
#to modify the instance variable
c1.millage=100

#to modify the class variable
car.wheels = 5

print(c1.millage, c1.maker,c1.wheels)
print(c2.millage, c2.maker,c2.wheels)
