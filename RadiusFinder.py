import math


def rad(x):
    return x / (math.pi * 2)


def cir(x):
    return 2 * math.pi * x


def area(x):
    return math.pi * x * x


while True:
    print("Radius Finder")
    print("")
    print("[A] Radius")
    print("[B] Circumference")
    print("[C] Area")
    print("[E] Exit")
    user_input = input(": ")

    if user_input == 'E':
        break
    elif user_input in ('A',):
        num1 = float(input("Enter the Circumference to find radius : "))
    elif user_input in ('B',):
        num2 = float(input("Enter the Radius to find Circumference : "))
    elif user_input in ('C',):
        num3 = float(input("Enter the Radius to find Area : "))

    if user_input == 'A':
        print("Result:", rad(num1))
    elif user_input == 'B':
        print("Result:", cir(num2))

    elif user_input == 'C':
        print("Result:", area(num3))
    else:
        print("Invalid input. Please enter a valid operation")
