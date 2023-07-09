import time

# 내가 쓴 코드
start_time = time.time()
N, M, K = input().split()
l = [N, M, K] # 5 8 3

data = []
data = input().split() # 2 4 5 4 6
max_data = max(data)

sum = 0;
count = 0;
bool = 0

for i in range(int(l[1])) :
    if(count == int(l[2])) :
        if(bool == 0):
            count = int(l[2]) - 1
            data.remove(max(data))
            bool = 1
        elif(bool == 1):
            count = 0
            bool = 0
            data.append(max_data)
    count += 1
    print(sum, "+", int(max(data)))
    sum += int(max(data))

end_time = time.time()
print(sum, end_time - start_time)

# 정답 : 반복문 없이