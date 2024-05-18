import sys
input = sys.stdin.readline

n = int(input())
A = []

for i in range(n):
    A.append((int(input()),i))

max = 0
A.sort()

for j in range(n):
    
    if max < A[j][1] - j:
        max = A[j][1] - j

print(max+1)