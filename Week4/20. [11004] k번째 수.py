N, K = (map(int,input().split()))
lists = list(map(int,input().split()))

def solution(N,K,lists):
    answer = 0
    quicksort(0,N-1,K-1)
    answer = lists[K-1]
    return answer

def quicksort(S,E,K):   #k 찾기니까 불필요한 곳까지 정렬하지 않는다.
    global lists
    if (S < E):

        pivot = partition(S,E)

        if (pivot < K):
            quicksort(pivot+1,E,K)
        elif (K < pivot):
            quicksort(S,pivot-1,K)
        else:
            return


def partition(S,E):
    global lists

    #데이터가 2개인 경우 바로 비교해서 정렬
    if(S+1 == E): # 시작 +1 == 끝 이면 크기 2라는 소리
        if lists[S] > lists[E]:
            swap(S,E)
        return E

    pivot = (S+E)//2
    swap(S,pivot)   #i, j 설정하기 편하게 하려고 피벗을 제일 왼쪽으로 이동시켜놓음
    pivot = S
    i = S + 1
    j = E
    while(i<=j):
        #피벗보다 큰 수가 나올 때 까지 i 증가
        while lists[pivot]> lists[i] and i<len(lists)-1:
            i+=1
        #피벗보다 작은 수가 나올때 까지 j 감소
        while(lists[pivot] < lists[j] and j>0):
            j-=1
        if i <= j:
            swap(i, j)
            i += 1
            j -= 1  
    temp = lists[pivot]
    lists[S] = lists[j]
    lists[j] = temp
    return j   #피벗에 있던 값 출력



def swap(a,b):
    global lists
    lists[a], lists[b] = lists[b], lists[a]


print(solution(N,K,lists))