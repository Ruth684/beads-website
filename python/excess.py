print("hello world")
myName = "Ruth"
myOccupation ="software"
age =76
isEmployed = True
isNotFromAfrica =False

print("my Name is", myName, myOccupation)
print("i am Ghanaian")
print("My name is" + myName)
print("My name is %s I am a %s" %(myName, myOccupation))

print(type(myName))
print(type(age))
print(type(isEmployed))
print(type(isNotFromAfrica))


def sum (first, second ):
    sum = first + second 
    return sum
 
print(sum(10, 9))

def calculate(action, firstNum, secondNum):
 if action == "multiply":
  result = firstNum * secondNum
  return result

 elif action =="division" :
  result = firstNum / secondNum
  return result

  
calcResult =calculate("multiply",7 , 6)
calcResult = calculate("division", 10, 5)
print("the result is: ",calcResult)

number =1
while number <= 20 :
    print("number:", number)
    number = number + 1

for number in range(1, 20, 2):
    print("Number:", number)


names = ["Ruth", "akua", "martey"]
for name in names:
 print("Name is:", name)

print("our loop is done!")
