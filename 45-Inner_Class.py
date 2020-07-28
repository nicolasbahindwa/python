

class student:

    def __init__(self,name,rolno):
        self.name = name
        self.rolno= rolno
        #from inner class
        self.pc = self.laptop()
    
    def show(self):
        print(self.name,self.rolno)
        self.pc.show()

   #inner class
    class laptop:
        def __init__(self):
            self.brand="HP"
            self.cpu ="i3"
            self.ram ="8"

        def show(self):
            print(self.brand,self.cpu,self.ram)


s1 = student("nicolas",2)
s2 = student("bahindwa",3)

s1.show()