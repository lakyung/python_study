# 함수 고급
# 튜플(tuple)은 리스트와 비슷한 자료형. 한번 결정된 요소를 바꿀 수 없다!
tuple_test = (10,20,30)  # 요소 하나만 가지는 튜플 선언은 숫자뒤에 콤마 붙여야함. ex)  tuple_test=(10,)
print(tuple_test[0],",",tuple_test[1],",",tuple_test[2])
# tuple_test[0]=1 # TypeError

#괄호가 없는 튜플
tuple_test = 10,20,30,40
print("#괄호가 없는 튜플의 값과 자료형 출력")
print("tuple_test:",tuple_test)
print("type(tuple_test):",type(tuple_test))
print()

#괄호가 없는 튜플 활용
a,b,c = 10,20,30
print("#괄호가 없는 튜플을 활용한 할당")
print("a:",a)
print("b:",b)
print("c:",c)

#값을 교환
a,b=c,50
print("a:",a)
print("b:",b)

#튜플은 함수의 리턴에 많이 사용
#여러 개의 값 리턴하기```
def test():
    return (10,20)

print("tuple return : ", test())

#튜플을 리턴하는 함수의 예
for i,value in enumerate([1,2,3,4,5,6]):
    print("{}번째 요소는 {}입니다.".format(i,value))

print(divmod(97,40))

#람다 
#함수의 매개 변수로 함수 전달하기
def call_10_times(func):
    for i in range(10):
        func()

def print_hello():
    print("안녕하세요")

call_10_times(print_hello)

#함수를 매개변수로 전달하는 대표적인 표준함수 : map(), filter()
def power(item):
    return item*item
def under_3(item):
    return item<3
list_input_a=[1,2,3,4,5]

#map(함수, 리스트) 함수를 사용
output_a = map(power, list_input_a)
print("# map() 함수의 실행결과")
print("map(power, list_input_a):",output_a)
print("map(power, list_input_a):",list(output_a))
print()

#filter(함수, 리스트) 함수를 사용
output_b = filter(under_3,list_input_a)
print("# filter() 함수의 실행결과")
print("filter(under_3, list_input_b):",output_b)
print("filter(under_3, list_input_b):",list(output_b))
print()

print("========lambda")
# lambda 매개변수 : 리턴값                    // 매개변수 여러개는 콤마로 구분
lambda_power = lambda x: x * x
lambda_under_3=lambda x:x<3
list_a=[1,2,3,4,5]
#map(함수, 리스트) 함수를 사용
output_a = map(lambda_power, list_a)
print("# map() 함수의 실행결과")
print("map(power, list_a):",output_a)
print("map(power, list_a):",list(output_a))
print()

#filter(함수, 리스트) 함수를 사용
output_b = filter(lambda_under_3,list_a)
print("# filter() 함수의 실행결과")
print("filter(under_3, list_input_b):",output_b)
print("filter(under_3, list_input_b):",list(output_b))
print()

#인라인 람다 : 매개변수에 바로 넣기
print("인라인 람다----------------")
in_lambda_output_a = map(lambda x:x*x, list_a)
print("# map() 함수의 실행결과")
print("map(power, list_a):",in_lambda_output_a)
print("map(power, list_a):",list(in_lambda_output_a))

in_lambda_output_b= filter(lambda x:x<3, list_a)
print("# filter() 함수의 실행결과")
print("filter(under_3, list_input_b):",in_lambda_output_b)
print("filter(under_3, list_input_b):",list(in_lambda_output_b))