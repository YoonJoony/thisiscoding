N, M = map(int, input().split())

board = [[0] * M for i in range(N)] # 2차원 배열 선언 함수

list_add = []

min_a = 0
min_b = 0

for i in range(N):
    list_add = list(map(int, input().split()))
    if(min_a < min(list_add)) :
        min_b = min(list_add)
    min_a = min(list_add)
    for j in range(M):
        board[i][j] = list_add[j]

print(min_b)