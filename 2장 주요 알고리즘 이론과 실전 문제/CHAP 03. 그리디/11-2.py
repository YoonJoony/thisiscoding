
S = str(input())

S = list(S)

sum = int(S[0])
for i in range(len(S)-1):
    if(S[i+1] != '0' and sum != 0):
        print(sum, " x ", int(S[i+1]))
        sum *= int(S[i+1])
    else:
        print(sum, " + ", int(S[i + 1]))
        sum += int(S[i+1])

 print("[", sum, "]")


