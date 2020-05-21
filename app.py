def add_operations():
    first_number = float(input("Enter first number :"))
    second_number = float(input("Enter second number :"))
    total = first_number + second_number
    print(f" {first_number} + {second_number}  is {total}")

def sub_operations():
    first_number = float(input("Enter first number :"))
    second_number = float(input("Enter second number :"))
    total = first_number - second_number
    print(f"{first_number} - {second_number}  is {total}")

def mul_operations():
    first_number = float(input("Enter first number :"))
    second_number = float(input("Enter second number :"))
    total = first_number * second_number
    print(f" {first_number} * {second_number}  is {total}")

def div_operations():
    first_number = float(input("Enter first number :"))
    second_number = float(input("Enter second number :"))
    total = first_number / second_number
    total = round(total ,2 )
    print(f" {first_number} / {second_number}  is {total}")
menu_promt = """
Select operations 
1. Add
2. Subtract
3. Multiply
4. Divide
5. Quit

Please choice (1/2/3/4/5) :
"""

user_input =input(menu_promt)
while user_input != '5' :
    if user_input == '1':
        add_operations()
    elif user_input == '2':
        sub_operations()
    elif user_input == '3':
        mul_operations()
    elif user_input == '4':
        div_operations()
    else:
        print("Enter valid input")

    user_input =input( menu_promt )
