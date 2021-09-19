import datetime
'''
# 입력 받기
number = input("정수입력>")
# 마지막 자리 숫자를 추출
last_character = number[-1]

# 숫자로 변환하기
last_number = int(last_character)

# 짝수 확인

if last_number == 0 \
    or last_number==2:
    print("짝수입니다")

if last_character in "02468":
    print("in : 짝수입니다")

if last_number % 2 == 0:
    print("% : 짝수입니다")
else:
    print("% : 홀수입니다.")
'''

now = datetime.datetime.now()
month = now.month

if 3 <= month <= 5:
    print("현재는 봄입니다.")
elif 6 <= month <=8:
    print("현재는 여름입니다.")
elif 9 <= month <=11:
    print("현재는 가을입니다.")
else:
    print("현재는 겨울입니다.")


# 조건문에서 조건이 0, 빈문자열("")은 False
if 0 :
    print("0은 True")
else:
    print("0은 False")

if "" :
    print(" 빈문자열은 True")
else:
    print(" 빈문자열은 False")

# pass 키워드를 사용한 미구현 부분 입력
number = input("정수입력> ")
number = int(number)
if number >0:
    pass  # 아직 미구현 상태

#raise NotImplementError 미구현 부분 강제 에러 발생
if number >0:
    raise NotImplementedError

