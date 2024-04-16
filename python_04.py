def add(num1, num2):
    return num1 + num2

result1 = add(10, 20)
print(result1)

def add(num1, num2, num3, num4):
    return num1 + num2, num3 +num4

result2, result3 = add(10, 20, 30, 40)
print(result2)
print(result3)

r1, r2 = (1, 2)
print(r1, r2)

nums = [5,2,7,3,1]
nums.sort()
nums.reverse()
print(nums)

# print(nums.index(10))

name = "김준일"
print(name.find("주"))  # find: 못찾으면 -1 (문자열에만) 
print(name.index("준")) # index: 못찾으면 Error

user = {
    "username": "testuser",
    "password": "1234",
    "name": "김준일",
    "email": "test@gmail.com"
}

print(user)
user.update({"phone": "010-1234-5678", "name": "김준이"})
user["age"] = 31
print(user)  