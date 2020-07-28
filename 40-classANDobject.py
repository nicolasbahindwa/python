
class computer:
    #constructer of computer class
    def __init__(self, cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("config is :", self.cpu,self.ram)

#object of computer class
com1 = computer("i3",16)
com2 = computer("ryzen 3",8)

# computer.config(com1)
# computer.config(com2)

com1.config()
com2.config()

