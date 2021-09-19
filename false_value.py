print("# if 조건문에 0 넣기")
if 0:
    print("0은 True로 변환됩니다.")
else:
    print("0은 False로 변환됩니다.")

print()

print("# if 조건문에 빈 문자열 넣기")
if "":
    print("빈 문자열은 True로 변환됩니다.")
else:
    print("빈 문자열은 False로 변환됩니다.")

number=0
if number:
    print("number은 True로 변환됩니다.")
else:
    print("number은 False로 변환됩니다.")

# 나중에 구현하려고 비워 둔 구문 - pass
number2 = input("정수 입력>")
number2 = int(number2)
if number2 >0 :
    #양수일 때
    pass
else:
    #음수일 떄
    pass

print("pass 다음 라인")

# 미구현 부분 강제 오류 발생
if number2 >0 :
    #양수일 때
    raise NotImplementedError
else:
    #음수일 떄
    raise NotImplementedError

print("미구현 강제 오류 발생 다음 라인")