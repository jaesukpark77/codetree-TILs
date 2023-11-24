import sys

INT_MIN = -sys.maxsize

# 변수 선언 및 입력
binary = list(map(int, list(input())))
length = len(binary)

ans = INT_MIN
for i in range(length):
	# i번째 자릿수를 바꿉니다.
	binary[i] = 1 - binary[i]
	
	# 십진수로 변환합니다.
	num = 0
	for j in range(length):
		num = num * 2 + binary[j]
	
	ans = max(ans, num)
	
	# i번째 자릿수를 원래대로 돌려놓습니다.
	binary[i] = 1 - binary[i]

# 출력
print(ans)