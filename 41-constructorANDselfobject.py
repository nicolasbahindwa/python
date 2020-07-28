
class computer:
    def __init__(self):
        self.name="nicolas"
        self.age = 30

    def update(self):
        self.age=30
    
    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False



c1 = computer() 
c2 = computer()

#set name of a variable
c1.name="bahindwa" 
c1.update()

if c1.compare(c2):
     print("same age")
else:
    print("not same age")

print(c1.name)
print(c2.name)

print(id(c1))
