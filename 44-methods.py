class student:
    school = "tokyo college"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    
    def average(self):
        return(self.m1 + self.m2 + self.m3)/3
    
    @classmethod
    def getSchool(cls):
        return cls.school
    
    @staticmethod
    def info():
        print("this is student class.. in abc module")

    #accessor
    # def get_m1(self):
    #     return self.m1 
    
    #mutators
    # def set_m1(self,value):
    #     self.m1 = value
    

s1 = student(24,67,32)
s2 = student(82,32,12)

print(s1.average())
print(student.getSchool())
student.info()
