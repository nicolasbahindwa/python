from abc import ABC, abstractmethod

class computer(ABC):
    #abstract method
    @abstractmethod
    def process(self):
        pass

class Laptop(computer):
    def process(self):
        print("running")


class whiteboard:
    def write(self):
        print("writing ...")


class programmer:
    def work(self,com):
        print("solving bugs")
        com.process()


# com = computer()
com1 = Laptop()
prog1 = programmer()
prog1.work(com1)
com1.process()
# com.process()
