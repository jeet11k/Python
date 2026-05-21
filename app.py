#number = int(input("Enter a number:"))

#if number % 2 == 0:
#    print(number, "is an Even number")
#else:
#    print(number, "is an Odd number")

def check_even_or_odd(number):

    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


def main():

    try:
        number = int(input("Enter a number: "))

        result = check_even_or_odd(number)

        print(f"{number} is an {result} number")

    except ValueError:
        print("Please enter a valid number")


main()