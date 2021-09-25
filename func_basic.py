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