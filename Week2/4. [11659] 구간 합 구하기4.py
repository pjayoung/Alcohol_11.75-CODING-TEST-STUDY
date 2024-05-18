'''n, m = input().split()
A = list(map(int, input().split()))

S = [0]*len(A)
for i in range(len(A)):
    if i == 0:
        S[i] = A[i]
    else:
        S[i] = S[i-1]+A[i]

C = [0]*int(m)
for j in range(0,int(m)):
    a, b = input().split()
    if int(a)-1 != 0:
        C[j] = S[int(b)-1] - S[int(a)-2]
    else:
        C[j] = S[int(b)-1]

for k in C:
    print(k)'''


# 교재 풀이
import sys
input =sys.stdin.readline
suNo, quizNo =map(int, input().split())
numbers = list(map(int, input().split()))
prefix_sum =[0]
temp =0

for i in numbers:
    temp = temp +i
    prefix_sum.append(temp)    # 합 배열 만들기

for i in range(quizNo):
    s, e = map(int, input().split())
    print(prefix_sum[e] - prefix_sum[s-1])  # 합 배열에서 구간 합 구하기