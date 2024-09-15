

# while True:
#     height: float = float(input("what's your height"))
#
#     is_valid_height = 0.4 <= height <= 2.5
#
#     if is_valid_height:
#         print(f"your height is {height}")
#         break
#     else:
#         print("wrong input")
#

num1: int = int(input("enter first number"))
num2: int = int(input("enter second number"))

if num1 < num2:
    for i in range(num1, num2 + 1):
        print(i, end=" ")
else:
    for i in range(num1, num2 - 1, -1):
        print(i, end=" ")