# 변수 선언 및 입력:
row_num, col_num = tuple(map(int, input().split()))

# n * m 크기의 사각형을 출력합니다.
def print_rect(n, m):
    for _ in range(n):
        print("1" * m)

print_rect(row_num, col_num)