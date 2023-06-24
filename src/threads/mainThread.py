import threading
import time

def myChild_or_MainThread():
    print("Child Thread Starting")
    time.sleep(5)
    print("Current Thread ---------- ")
    print(threading.current_thread())
    print("-----------------------")
    print("Main Thread -----------")
    if threading.current_thread() == threading.main_thread():
        print("I was called by main")
    else:
        print("I was called by child")
    print("-----------------------")
    print("Child Thread Ending")

child = threading.Thread(target=myChild_or_MainThread)
myChild_or_MainThread()
child.start()
child.join()

