"""Numeric operators practice."""

__author__ = "730336784"

number_one: int = int(input("Pick a number ")) 
number_two: int = int(input("Pick another number "))
number_one_plus_number_two: int = number_two + number_one 
number_one_times_number_two: int = number_two * number_one
number_two_to_the_power_of_number_one: int = number_two ** number_one 
number_one_minus_number_two: int = number_one - number_two
print(str(number_one) + " + " + str(number_two) + " is " + str(number_one_plus_number_two))
print(str(number_one) + " * " + str(number_two) + " is " + str(number_one_times_number_two))
print(str(number_two) + " ** " + str(number_one) + " is " + str(number_two_to_the_power_of_number_one))
print(str(number_one) + " - " + str(number_two) + " is " + str(number_one_minus_number_two))
