from threading import Thread
import time

class MyWorkerThread(Thread):

    def __init__(self):
        print("Hello World")
        Thread.__init__(self)
    
    def run(self):
        print("Thread is now running")
        print("My name:", self.name)
        print("Thread is now slepping")
        time.sleep(1)

if __name__ == '__main__':
    myThread = MyWorkerThread()
    print("Created my Thread Object")
    myThread.start()
    print("Started my thread")
    myThread.join()
    print("My Thread finished")
