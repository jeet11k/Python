# Write a Python program that asks the user to enter their birth year and calculates their age in the year 2026. Then display the calculated age.
from datetime import datetime
birth_year = input("Birth Year: ")
x = datetime
current_year = x.now().year
age = current_year - int(birth_year)
print(age)