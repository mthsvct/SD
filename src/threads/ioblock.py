
import urllib.request
import time
import os

def downloadImage(imagePath, fileName):
    print("Downloading image from ", imagePath)
    urllib.request.urlretrieve(imagePath, fileName)

def main():

    if not os.path.exists('temp'):
        os.makedirs('temp')

    if not os.path.exists('temp/seq'):
        os.makedirs('temp/seq')

    for i in range(10):
        imageName = f"temp/seq/image-{i}.jpg"
        downloadImage("https://picsum.photos/200/300?random=1", imageName)

if __name__ == '__main__':
    t1 = time.time()
    main()

    final = time.time() - t1

    with open('tempos.csv', 'a') as f:
        f.write(f"10,sequencial,{final}\n")

    print("Spent time:", final)