
#1
while True:
    height: float = float(input("what's your height"))

    is_valid_height = 0.4 <= height <= 2.5

    if is_valid_height:
        print(f"your height is {height}")
        break
    else:
        print("wrong input")

#2
num1: int = int(input("enter first number"))
num2: int = int(input("enter second number"))

if num1 < num2:
    for i in range(num1, num2 + 1):
        print(i, end=" ")
else:
    for i in range(num1, num2 - 1, -1):
        print(i, end=" ")

#3
pie: float = 3.14
counter = 3
user_attempt: float = float(input("enter is pie num"))

while user_attempt != pie and counter < 3:
    print("wrong num")
    counter += 1
    user_attempt = float(input("try again"))

if user_attempt == pie:
    print("you are correct")
else:
    print(f"pie is {pie}")


#4

beers_given: int = 0
while beers_given < 10:
    age:int = int(input("whats your age?"))
    if age >= 18:
        print("take u beer")
        beers_given += 1
    else:
        print("wait for 18 y.o")

