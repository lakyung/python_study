
string_a="{}".format(10)
print(string_a)
format_a="{}만 원".format(5000)
format_b="{} {} {}".format(3000,"문자열",True)
print(format_a+","+format_b)

#정수
output_a="{:d}".format(52)
output_b="{:5d}".format(52) #특정캉에 출력

# 빈칸을 0으로 채우기
output_c="{:05d}".format(52)  #양수
output_d="{:05d}".format(-52)  #음수

print("output_a : "+output_a)
print("output_b : "+output_b)
print("output_c : "+output_c)
print("output_d : "+output_d)

# 의미 없는 소수점 제거하기
output_e = 52.0
print("{:g}".format(output_e))

a = "Hello Python"
print("대문자 : " + a.upper())
print("소문자 : " + a.lower())

# 문자열 양옆의 공백 제거
input_a ="""
        안녕하세요
문자열의 함수를 알아봅시다
"""
print(input_a)
print("---------------------")
print(input_a.strip())
print(" print".isidentifier())
print("input_b".isidentifier())

# 문자열 찾기 : find()와 rfind()
aa = "안녕안녕하세요"
print(aa.find("안녕"))
print(aa.rfind("안녕"))

# 문자열과 in 연산자
print("안녕" in "안녕하세요")

# 문자열 자르기 : split()
bb = "10 20 30 40 50".split(" ")
print(bb)

