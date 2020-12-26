import time
from threading import *
import psutil

print(psutil.cpu_count())
runs = 500000


class Hello(Thread):
    def run(self):
        for i in range(runs):
            print("Hello")


class Hi(Thread):
    def run(self):
        for i in range(runs):
            print("Hi")


t1 = Hello()
t2 = Hi()

if __name__ == '__main__':
    start_time = time.time()
    t1.run()
    t2.run()

    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()

    print("--- %s seconds ---" % (time.time() - start_time))
