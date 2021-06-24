N = int(input())
party = list(map(int, input().split()))
cnt = 0
group = 0

party.sort()

for i in party:
    cnt += 1
    if cnt == i:
        group += 1
        cnt = 0

print(group)

