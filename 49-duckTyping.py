
class PyCham:
    def execute(self):
        print("compliling")
        print("running")


class VScode:
    def execute(self):
        print("spell check")
        print("convetio check")
        print("compliling")
        print("running")

class Laptop:
    def code(self,ide):
        ide.execute()


# ide = PyCham()

ide = VScode()

lap1 = Laptop()

lap1.code(ide)

