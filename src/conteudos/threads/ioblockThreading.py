import threading
import urllib.request
import time
import os

def downloadImage(imagePath, fileName):
    print("Downloading Image from ", imagePath)
    urllib.request.urlretrieve(imagePath, fileName)
    print("Completed Download \n")

def executeThread(i):

    if not os.path.exists('temp'):
        os.makedirs('temp')

    if not os.path.exists('temp/thread'):
        os.makedirs('temp/thread')

    imageName = f"temp/thread/image-{i}.jpg"
    downloadImage("https://picsum.photos/200/300?random=1", imageName)

def main():
    t0 = time.time()
    threads = []
    for i in range(10):
        thread = threading.Thread(target=executeThread, args=(i,))
        threads.append(thread)
        thread.start()
    for i in threads:
        i.join()
    t1 = time.time()
    totalTime = t1 - t0

    with open('tempos.csv', 'a') as f:
        f.write(f"10,threads,{totalTime}\n")

    print(f"Total execution time {totalTime}")

if __name__ == '__main__':
    main()

