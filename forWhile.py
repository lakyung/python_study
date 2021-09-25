import time
''' 
range(A)  0부터 A-1 까지 정수 범위
range(A,B) A부터 B-1까지 정수 범위
range(A,B,C) A부터 B-1까지의 정수 범위를 만드는데, 앞뒤의 숫자가 C만큼의 차이 가짐

'''
a=range(5)
print(a)
list(range(0,10,2)) # 0부터 2씩 증가하면서 범위 만듬
list(range(0,10+1)) #10을 반드시 포함해야 하는 것을 강조

n=10
# a= range(0, n/2)   // 나눗셈 사용시 TypeError에러발생~ range함수 매개변수로는 반드시 정수 입력해야 함.
a= range(0,int(n/2))  # 실수를 정수로 바꾸면 오류 안나지만
a= range(0, n // 2)   # 정수 나누기 연산자를 많이 사용한다. "//" <- 정수 나누기 연산자
array=[12,13,14,15]
for i in range(len(array)):
    print("{}번째 반복:{}".format(i,array[i]))

# 반대로 반복하기
for i in range(len(array)-1,-1,-1):
    print("{}번째 반복:{}".format(i,array[i]))

# reversed() 함수 이용하여 반대로 반복하기
for i in reversed(range(len(array))):
	print("{}번째 값:{}".format(i,array[i]))

#while반복문 - for 반복문처럼 사용하기
i=0
while i<10:
    print("{}번째 반복입니다.".format(i))
    i+=1

#해당하는 값 모두 제거
list_test=[1,2,1,2]
value=2
while value in list_test:
    list_test.remove(value)

print(list_test)

#무한반복 - 강제 종료시 ctrl+c
'''while True:
    print(".",end="")
    '''

print(time.time())
# 5초동안 반복하기
number=0
target_tick = time.time()+5
while time.time()<target_tick:
	number+=1
print("5초 동안 {}번 반복했습니다.".format(number))

# break키워드/ continue 키워드
i=0
while True:
    print("{}번째 반복문입니다.".format(i))
    i=i+1
    input_text=input(">종료하시겠습니까?y/n):")
    if input_text in ["y","Y"]:
        print("반복을 종료합니다.")
        break

numbers=[5,15,6,20,7,25]
for number in numbers:
    if number<10:
        continue
    print(number)


