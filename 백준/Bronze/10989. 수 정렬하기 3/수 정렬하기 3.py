import sys
n = int(input())
num = [0]*10000
for i in range(n):
    m = int(sys.stdin.readline())
    num[m-1] +=1
for i in range(10000):
    if num[i] != 0:
        for j in range(num[i]):
            print(i+1)