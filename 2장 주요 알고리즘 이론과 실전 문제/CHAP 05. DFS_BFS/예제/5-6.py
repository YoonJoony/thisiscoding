# 입접 행렬 방식 예제

INF = 999999999

#2차원 리스트를 이용해 인접 행렬 표현
graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

print("인접행렬 : ", graph)
print(type(graph)) # 일반 리스트와 타입은 같다.

# 행(Row)이 3개인 2차원 리스트로 인접 리스트 표현

graph =[[] for _ in range(3)]

graph[0].append((1, 7))
graph[0].append((1, 7))


graph[1].append((1, 7))


graph[2].append((1, 7))

print("인접리스트 : ", graph)
print(type(graph)) # 일반 리스트와 타입은 같다.
