#Ethiopian Multiply

#사용자 값 받기
m = int(input("숫자를 하나 입력하세요>> ")
n = int(input("다른 숫자를 하나 더 입력하세요 >> ")

result = 0

#반복해서 왼쪽 값은 2로 나눈 후 몫을 구하고, 오른쪽 값은 2로 곱하기
while m >= 1:
    if m%2 != 0:
        result += n
    m //= 2
    n *= 2

print(result)
