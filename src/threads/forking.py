import os

def child():
    print(f"We are in the child process with PID = {os.getpid()}")

def parent():
    print(f"We are in the parent process with PID={os.getpid()}")
    newRef = os.fork()
    if newRef == 0:
        child()
    else:
        print(f"We are in the parent process and our child process has PID = {newRef}")

if __name__ == "__main__":
    parent()