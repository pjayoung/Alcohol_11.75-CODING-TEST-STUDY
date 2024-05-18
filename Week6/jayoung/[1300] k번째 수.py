import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
start = 1   # 문제에서 시작 인덱스 번호 1 로 줌
end = k
result = 0

while start <= end:    #start 가 더 커지기 전까지
    middle = int((start+end)/2)
    cnt = 0    # 중앙값보다 작은 수 저장

    for i in range(1,n+1):   #1~n까지
        cnt += min(int(middle/i), n)    # 각 행마다 중앙값보다 작은 것 구하는 과정 (개수)
    if cnt < k:  # (현재 중앙값보다 작은 수의 개수)가 k 보다 작으면 
        start = middle +1   # 중앙값 좌측 뒤는 버림
    else:  # 반대의 경우
        end = middle-1   # 중앙값 우측 뒤는 버림
        result = middle   # 이때 결과값으로 중앙값을 업데이트 -> start가 end보다 커지는 순간에 이 값이 결과값이 됨

print(result)

