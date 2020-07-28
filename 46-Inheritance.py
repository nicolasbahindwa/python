

class A:

    def feature1(self):
        print("feature 1 is working")

    def feature2(self):
        print("feature 2 working")

# class B is inheriting the feature of A
class B(A):

    def feature3(self):
        print("feature 1 is working")

    def feature4(self):
        print("feature 2 working")

class C(B):
    def feature5(self):
        print("feature 1 is working")

    def feature6(self):
        print("feature 2 working")

#multi pal inheritance
class D(A,B):
    def feature8(self):
        print("feature 1 is working")

    def feature9(self):
        print("feature 2 working")

     


a1 = A()

a1.feature1()
a1.feature2()

b1 = B()

b1.feature1()

C.feature1()

