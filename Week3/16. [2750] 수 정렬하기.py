n = int(input())
A = [0]*n

for i in range(n):
    A[i] = int(input())

for a in range(n-1):
    for b in range(n-1-a):
        if A[b] > A[b+1]:
            swap = A[b]
            A[b] = A[b+1]
            A[b+1] = swap

for j in range(n):
    print(A[j])