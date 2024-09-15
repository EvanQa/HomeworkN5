

while True:
    height: float = float(input("what's your height"))

    is_valid_height = 0.4 <= height <= 2.5

    if is_valid_height:
        print(f"your height is {height}")
        break
    else:
        print("wrong input")


num1: int = int(input("enter first number"))
num2: int = int(input("enter second number"))

if num1 < num2:
    for i in range(num1, num2 + 1):
        print(i, end=" ")
else:
    for i in range(num1, num2 - 1, -1):
        print(i, end=" ")


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