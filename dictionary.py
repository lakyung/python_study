# 딕셔너리는 '키를 기반으로 값을 저장하는 것'

dict_a={
    "name":"어벤저스 엔드게임",
    "type":"히어로 무비",
    "director":["안소니 루소","조 루소"]
    }
print(dict_a["name"])
print(dict_a["director"][0])
dict_a["name"]="어벤저스"
print(dict_a["name"])
dict_a["새로운키"]="새로운 값"
print(dict_a)
del dict_a["새로운키"]
print(dict_a)

key = input("> 접근하고자 하는 키 : ")
if key in dict_a:
    print(dict_a[key])

value = dict_a.get("aa")
print(value)
if value == None:
    print("존재하지 않는 키에 접근")

print("[for 반복문 :딕셔너리와 함께 사용하기]")
for key in dict_a:
    print(key,":",dict_a[key])