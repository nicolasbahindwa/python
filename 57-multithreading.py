from time import *
from threading import *

class hello(Thread):
    def run(self):
        for i in range(5):
            print("hello")
            sleep(1)


class hi(Thread):
    def run(self):
        for i in range(5):
            print("hi")
            sleep(1)

t1 = hello()
t2 = hi()

# t1.run()
t1.start()
sleep(0.2)
t2.start()
# t2.run()
t1.join()
t2.join()

print("bye")