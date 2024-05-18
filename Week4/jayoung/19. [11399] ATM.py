import sys
input = sys.stdin.readline

n = int(input())
P = list(map(int,input().split()))
S = [0]*n

for i in range(1,n):   #정렬 중인 번호(얘보다 작은 값을 찾아서 그 앞에 삽입)
    insert_point = i    #삽입할 포인트 (밑에서 구할 거니까 일단 i로 초기화)
    insert_value = P[i]   #삽입하고 싶은 값
    for j in range(i-1, -1, -1):   #i와 비교할 애들(i보다 앞쪽에 있는 인덱스들만 봄!, 거꾸로 가면서 확인)
        if P[j]<P[i]:   #i보다 작은 값 찾으면!
            insert_point = j+1    #그거보다 한 칸 앞에! 삽입되면 된다!(삽입할 포인트 업데이트)
            break   #찾았으니까 일단 끝내고
        if j == 0:   #j가 0이라는 건, 다 정렬이 되어있다는 뜻
            insert_point = 0
    for k in range(i, insert_point, -1):   #만약에 i와 insert_point가 같으면 shift 안 일어남!
        P[k] = P[k-1]
    P[insert_point] = insert_value

S[0] = P[0]
result = S[0]

for i in range(1,n):
    S[i] = S[i-1] + P[i]
    result += S[i]

print(result)