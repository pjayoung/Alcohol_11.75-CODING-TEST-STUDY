import sys
input = sys.stdin.readline

n = int(input())
A = []
mystack = []

for _ in range(n):
    A.append(int(input()))

num = 1
result = True
answer = ""

for i in range(n):
    if A[i] >= num:
        while A[i] >= num:
            mystack.append(num)
            num += 1
            answer += "+\n"
        mystack.pop()
        answer += "-\n"
    else:
        n = mystack.pop()
        if n > A[i]:
            print("NO")
            result = False
            break
        else:
            answer += "-\n"

if result:
    print(answer)