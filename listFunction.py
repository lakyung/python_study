
list_a=[1,2,3,4,5]
print(min(list_a))
print(max(list_a))
print(sum(list_a))

"""
reversed()함수 결과는 제너레이터인데 파이썬의 특별한 기능으로
함수 결과를 여러 번 활용하지 않고 for문 내부에서 reversed() 함수를
곧바로 넣어서 사용한다.
"""
numbers=[1,2,3,4,5]
for i in reversed(numbers):
    print("첫 번째 반복문:{}".format(i))

for i in reversed(numbers):
    print("두 번째 반복문:{}".format(i))

#확장 슬라이싱으로 리스트 뒤집기
numbers=[5,4,3,2,1]
print("numbers : {}".format(numbers))
print("numbers[::-1] : {}".format(numbers[::-1]))

#enumerate() 함수와 반복문 조합하기
example_list=["요소A","요소B","요소C"]
for i,value in enumerate(example_list):
    print("{}번째 요소는 {}입니다.".format(i,value))

example_dictionary={
    "키A": "값A",
    "키B": "값B",
    "키C": "값C"
    }
print("items():",example_dictionary.items())
print()
for key,element in example_dictionary.items():
    print("dictionary[{}]={}".format(key,element))

# [리스트 내포]
# 반복문을 사용한 리스트 생성
array=[]
for i in range(0,20,2):
	array.append(i*i)

print(array)

# 위 코드 간결하게 만들기
# 리스트이름 = [표현식 for 반복자 in 반복할 수 있는 것]
array=[i*i for i in range(0,20,2)]
print(array)

array=["사과","자두","초콜릿","바나나","체리"]
output = [fruit for fruit in array if fruit !="초콜릿"]
print(output)

#괄호로 문자열 연결하기
test=(
    "이렇게 입력해도 "
    "하나의 문자열로 연결되어 "
    "생성됩니다."
    )
print(test)

number=int(input("정수 입력>"))
if number %2==0:
    print((
        "입력한 문자열은 {}입니다.\n"
        "{}는(은) 짝수입니다."
        ).format(number,number))
else:
    print((
        "입력한 문자열은 {}입니다.\n"
        "{}는(은) 홀수입니다."
        ).format(number,number))

# join()함수
print("::".join(["1","2","3","4","5"]))
number=int(input("정수 입력>"))
if number %2==0:
    print("\n".join([
        "입력한 문자열은 {}입니다.",
        "{}는(은) 짝수입니다."
        ]).format(number,number))
else:
    print("\n".join([
        "입력한 문자열은 {}입니다.",
        "{}는(은) 홀수입니다."
        ]).format(number,number))

# 1~100 사이에 숫자 중 2진수로 변환했을 때 0이 하나만 포함된 숫자 찾기
output=[i for i in range(1,100) if "{:b}".format(i).count("0")==1]
for i in output:
	print("{} : {}".format(i, "{:b}".format(i)))

print("합계 : ",sum(output))