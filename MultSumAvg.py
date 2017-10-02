import time

def odd1To1k():
    for i in range (1, 1000, 2):
        print i

def multiples():
    for i in range(5, 1000000, 5):
        print i

def sumList(arr):
    sum = 0
    for i in arr:
        sum += i
    print i

def avgList(arr):
    sum = 0
    for i in arr:
        sum += i
    print sum / len(arr)

odd1To1k()
time.sleep(5)
multiples()
time.sleep(5)
sumList([1, 2, 5, 10, 255, 3])
avgList([1, 2, 5, 10, 255, 3])