# to add and multiply

print("* " * 20)
print("*{:^46}*".format("\033[95mLABORATORY ACTIVITY\033[0m"))
print("* " * 20, "\n", "By: Galleros and Luna\n")

first_number = int(input("Enter 1st integer number: "))
second_number = int(input("Enter 2nd integer number: "))
third_number = int(input("Enter 3rd integer number: "))


def add_or_multiply():
    if first_number == second_number == third_number:
        result = first_number * second_number * third_number
        print(f"The product of {first_number}, {second_number}, and {third_number} is {result}")
    elif first_number == second_number:
        result = first_number * second_number + third_number
        print(f"The result of {first_number} multiplied by {second_number} plus {third_number} is {result}")
    elif first_number == third_number:
        result = (first_number * third_number) + second_number
        print(f"The result of {first_number} multiplied by {third_number} plus {second_number} is {result}")
    elif second_number == third_number:
        result = (second_number * third_number) + first_number
        print(f"The product of {second_number} multiplied by {third_number} plus {first_number} is {result}")
    else:
        result = first_number + second_number + third_number
        print(f"The sum of {first_number}, {second_number}, and {third_number} is {result}")


add_or_multiply()
