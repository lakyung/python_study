# 반복문으로 팩토리얼 구하기
def factorial(n):
    output=1
    for i in range(1,n+1):
       # print(i)
        output *= i

    return output

#print("1! : ",factorial(1))
#print("2! : ",factorial(2))
#print("3! : ",factorial(3))
print("4! : ",factorial(4))

# 재귀 함수를 사용해 팩토리얼 구하기
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print("재귀함수 4! : ",factorial(4))