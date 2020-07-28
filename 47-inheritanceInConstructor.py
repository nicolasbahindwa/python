class A:
    def __init__(self):
        print("in A init")

    def feature1(self):
        print("feature 1 is working")

    def feature2(self):
        print("feature 2 working")

# class B is inheriting the feature of A
class B():
    def __init__(self):
        #calling the contructor of class a (inheriting the constructor features)
        super().__init__()
        print("in B init")

    def feature3(self):
        print("feature 1=b is working")

    def feature4(self):
        print("feature 2 working")


class C(A,B):
    def __init__(self):
        super().__init__()

        print("in C init")

    def feat(self):
        super().feature2()


a1 = C()

a1.feature1()

a1.feat()
