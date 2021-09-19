# 리스트를 선언
list_a=[1,2,3]
list_b=[4,5,6]

#출력
print("# 리스트")
print("list_a=",list_a)
print("list_b=",list_b)
print()

#기본 연산자
print("#리스트 기본 연산자")
print("list_a + list_b", list_a + list_b) #문자열 연결
print("list_a * 3 = ", list_a * 3) #문자열 반복         
print()

#함수
print("#길이 구하기")
print("len(list_a)= ", len(list_a))
print()

print("#요소 추가하기")
#리스트에 요소 추가하기: append, insert
list_a.append(4) #리스트 뒤에 추가
print(list_a)
list_a.append(5)
print(list_a)
print()

print("리스트 중간에 요소 추가하기")
list_a.insert(2,10)
print(list_a)
print()

print("한 번에 여러 요소를 추가")
list_a.extend([6,7,8])
print(list_a)
print()

print("##요소 삭제하기")
print("인덱스로 제거하기: del, pop")
del list_a[2]
print(list_a)
list_a.pop() #마지막 요소 제거
print(list_a)
list_a.pop(0)
print(list_a)

list_b=[0,1,2,3,4,5,6]
del list_b[3:6]
print("del 3:6 = ",list_b)

print("값으로 제거하기 : remove")
list_c=[1,2,1,2]
list_c.remove(2) # 동일한 값이 있어도 가장 먼저 발견되는 하나만 제거
print(list_c)

print("모두 제거하기:clear")
list_d=[1,2,3,4,5]
list_d.clear()
print(list_d)

# 리스트 내부에 있는지 확인하기 : in/not in 연산자
list_a=[273,32,103,57,52]
print("273 in list_a = ",273 in list_a)
print("99 in list_a = ",99 in list_a)

print("273 not in list_a = ",273 not in list_a)
print("99 not in list_a = ",99 not in list_a)
 
# for 반복문
for i in range(3):
    print("출력")

for i in list_a:
    print(i)





