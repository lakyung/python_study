def print_3_times():
    print("안녕하세요")
    print("안녕하세요")
    print("안녕하세요")

print_3_times()

def print_n_times(value,n):
    for i in range(n):
        print(value)

print_n_times("안녕",5)
# print_n_times()   # 매개변수를 넣지 않아 오류

# 가변 매개변수 함수
def print_n_times(n, *values):
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_times(3,"안녕하세요","즐거운","파이썬 프로그래밍")
print_n_times(4)


# 기본 매개변수
def print_n_times(value, n=2):
    for i in range(n):
        print(value)

print_n_times("하이룽")
print_n_times("메롱",n=5) # n=5 처럼 매개변수 이름을 지정해서 입력하는 매개변수를 키워드 매개변수라고 부름.
#-------------------------------------------

# 여러 함수 호출 형태
def test(a,b=10,c=100):
    print(a+b+c)

# 1) 기본 형태
test(10,20,30)    

# 2) 키워드 매개변수로 모든 매개변수를 지정한 형태
test(a=10, b=100, c=200)

# 3) 키워드 매개변수로 모든 매개변수를 마구잡이로 지정한 형태
test(c=10, a=100, b=200)

# 4) 키워드 매개변수로 일부 매개변수만 지정한 형태
test(10, c=200)
#-------------------------------------------

# 리턴
def return_test():
    print("A 위치입니다.")
    return
    print("B dnlcldlqslek.")

return_test()

def return_test():
    #return 100
    return

value=return_test()
print("리턴값:{}".format(value))

def sum_all(start,end):
    output=0
    for i in range(start, end+1):
        output+=i

    return output

print("0 to 100 : ", sum_all(0,100))


def sum_all(start=0, end=100, step=1):
    output=0
    for i in range(start,end+1, step):
        output+=i

    return output

print("A. ", sum_all(0,100,10))
print("B. ", sum_all(end=20))
print("C. ", sum_all())

def mul(*values):
    output=1
    for value in values:
        output*=value

    return output


