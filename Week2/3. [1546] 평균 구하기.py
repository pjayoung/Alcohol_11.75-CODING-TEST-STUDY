n = int(input())
score = list(input().split())
sum = 0
m = 0
a = 0

for i in score:
    if int(i) > m:
        m = int(i)

for j in score:
    a = int(j)/m*100
    sum += a

print(sum/n)


# 교재 풀이
n = input()
mylist = list(map(int, input().split()))
mymax = max(mylist)
sum = sum(mylist)

print(sum*100/mymax/int(n))