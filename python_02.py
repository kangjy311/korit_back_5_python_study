number = 10
print(type(number))

# id() 주소값 확인
print(id(10))   
print(id(number))
number += 1
print(id(number))
number -= 1
print(id(number))

print(type("test"))
print(type([]))     #리스트
print(type(()))     #튜플 (상수라고 생각, 요소 변경 불가능)
print(type({}))     #딕셔너리 (JSON 비슷)

print([1,2,3,4])
print((1,2,3,4))
print({"id": 1, "name": "김준일"})

list1 = [1,2,3,4]
tp = (5,6,7,8)
dict1 = {"id": 1, "name": "김준일"}

print(list1[0])
print(tp[0])
print(dict1["id"])

list1.append(5)  # append = add
print(list1)
print(tp.index(7))
list2 = list(tp)    #형 변환 (튜플 -> 리스트)
print(list2)
print(dict1.keys())  
print(dict1.values())
print(list(dict1.items())[0])  

# True, False 대문자
print(True)     
print(False)     