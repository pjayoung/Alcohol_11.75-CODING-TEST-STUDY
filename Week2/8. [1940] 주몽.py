import sys
input =sys.stdin.readline

n = int(input())
m = int(input())
A = [int(x) for x in input().split()]
A.sort()
count = 0
start = 0
end = n-1

while start < end:
    if A[start]+A[end] <m:
        start +=1
    elif A[start]+A[end] >m:
        end -= 1
    else:
        count +=1
        start += 1
        end -= 1
print(count)