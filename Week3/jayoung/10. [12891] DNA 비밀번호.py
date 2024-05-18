import sys
input = sys.stdin.readline

check = [0]*4
mylist = [0]*4
secret = 0

character = ['A', 'C', 'G', 'T']

def add(c):
    global check, mylist, secret
    for i in range(0, 4):
        if c == character[i]:
            mylist[i] += 1
            if mylist[i] == check[i]:
                secret += 1

def remove(c):
    global check, mylist, secret
    for i in range(0, 4):
        if c == character[i]:
            if mylist[i] == check[i]:
                secret -= 1
            mylist[i] -= 1

S, P = map(int, input().split())
result = 0
A = list(input())
check = list(map(int, input().split()))

for i in range(4):
    if check[i] == 0:
        secret += 1

for i in range(P):
    add(A[i])

if secret == 4:
    result +=1

for i in range(P,S):
    j = i-P
    add(A[i])
    remove(A[j])
    if secret == 4:
        result += 1

print(result)



