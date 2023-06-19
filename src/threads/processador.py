import multiprocessing

if __name__ == '__main__':
    count = multiprocessing.cpu_count()
    print(count)