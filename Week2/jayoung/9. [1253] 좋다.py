import sys
input =sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
A.sort()

count = 0

for k in range(n):
    m = A[k]
    start = 0
    end = n-1
    while start < end:
        if A[start]+A[end] <m:
            start +=1
        elif A[start]+A[end] >m:
            end -= 1
        else:
            if start != k and end != k:
                count +=1
                break
            elif start == k:
                start += 1
            elif end ==k:
                end -= 1
print(count)