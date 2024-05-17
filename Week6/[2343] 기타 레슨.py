import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))

result = 0
start = max(A)
end = sum(A)

while start <= end: # start 가 종료보다 커지면 종료
    mid = int((start+end)/2)
    sum = 0
    count = 1
    for i in A:
        if sum + i > mid:
            count += 1
            sum = 0
        sum += i

    if count <= m:
        result = mid
        end = mid - 1
    else:
        start = mid + 1

print(result)