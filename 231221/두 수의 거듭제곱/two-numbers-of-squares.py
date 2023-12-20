# 변수 선언 및 입력:
a, b = tuple(map(int, input().split()))

# a^b의 값을 반환합니다.
def power(a, b):
    cnt = 1
    for _ in range(b):
        cnt *= a

    return cnt

print(power(a, b))