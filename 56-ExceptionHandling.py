

a = 5
b = 3

try:
    print("resource opened")
    print(a/b)
except Exception as e:
    print("You can not divide the number by zero",e)
except ValueError as e:
    print("invalid input")
except Exception as e:
    print("something went wrong")

finally:
    print("resource closed")