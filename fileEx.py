'''
    파일객체 = open(문자열:파일경로,문자열:읽기모드)
    모드(w: write(새로쓰기), a: append(뒤에 이어서 쓰기), r: read(읽기))
    파일객체.close()
    
    파일을 열고 닫지 않는 경우 방지하기 위해 with키워드 사용
    with open(파일경로, 모드) as 파일객체:
        문장
'''

#파일열고닫기
file = open("basic.txt","w")
file.write("Hello Python Programming....!")
#file.close()

#with 구문이 종료될 때 자동으로 파일 닫힘.
with open("basic2.txt","w") as file:
    file.write("Hello~~~")

with open("basic.txt","r") as file:
    contents = file.read()

print(contents)
