import sys
input =sys.stdin.readline
n, m =map(int, input().split())
numbers = list(map(int, input().split()))
A = []
S = [0]*n
C = [0]*m
temp =0

for i in numbers:
    temp = temp +i
    A.append(temp)    # 합 배열 만들기

count = 0
ex = 0
for i in range(len(A)):
    S[i] = A[i]%m
    if S[i] == 0:
        count += 1
    C[S[i]] += 1

for j in range(m):
    if C[j]>1:
        count += ((C[j]*(C[j]-1))//2)
print(count)