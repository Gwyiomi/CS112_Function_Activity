# to add and multiply

print("* " * 20)
print("*{:^46}*".format("\033[95mLABORATORY ACTIVITY\033[0m"))
print("* " * 20, "\n", "By: Galleros and Luna\n")

first_number = int(input("Enter 1st integer number: "))
second_number = int(input("Enter 2nd integer number: "))
third_number = int(input("Enter 3rd integer number: "))


def add_or_multiply():
    if first_number == second_number == third_number:
        multiply_numbers = first_number * second_number * third_number
        print(f"The product of {first_number}, {second_number}, and {third_number} is {multiply_numbers}")
    elif first_number == second_number:
        multiply_numbers = first_number * second_number + third_number
        print(f"The result of {first_number}, {second_number}, and {third_number} is {multiply_numbers}")
    elif first_number == third_number:
        multiply_numbers = (first_number * third_number) + second_number
        print(f"The product of {first_number}, {second_number}, and {third_number} is {multiply_numbers}")
    elif second_number == third_number:
        multiply_numbers = (second_number * third_number) + first_number
        print(f"The product of {first_number}, {second_number}, and {third_number} is {multiply_numbers}")
    else:
        add_numbers = first_number + second_number + third_number
        print(f"The sum of {first_number}, {second_number}, and {third_number} is {add_numbers}")


add_or_multiply()
