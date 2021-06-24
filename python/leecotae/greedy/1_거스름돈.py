
n = 1260
count = 0

array = [500, 100, 50, 10]

for i in array:
    count += n//i
    n = n%i

print(count)
