
S = list(map(int, input()))

result = S.pop(0)

for i in S:    
    if (result < 2) or (i < 2) :
        result += i
    else : 
        result *= i

print(result)


