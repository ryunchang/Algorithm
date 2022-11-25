# 유클리드 호제법 이용
def greatest_common_multiple(A, B):
    if A % B == 0:
        return B
    return greatest_common_multiple(B, A % B)

print(greatest_common_multiple(192, 162))