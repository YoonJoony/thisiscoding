# 처음 짠 코드
N = 1260

coins = [500, 100, 50, 10]

count =0
for i in coins:
	count = count + int(N / i)
	N = N % i

print(count)

# 정답
N = 1260

coins = [500, 100, 50, 10]

count =0
for i in coins:
	count += N // i
	N = N % i

print(count)

