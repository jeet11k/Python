# Write a program to find the largest number in a list.
numbers = [3, 6, 9, 12, 20]

maximum = numbers[0]

for number in numbers:
    if number > maximum:
        maximum = number

print(maximum)       