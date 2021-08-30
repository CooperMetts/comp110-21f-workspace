"""Numeric operators practice."""

__author__ = "730336784"

number_one: int = int(input("Pick a number ")) 
number_two: int = int(input("Pick another number "))
number_one_to_the_power_of_number_two: int = number_one ** number_two 
number_one_divided_by_number_two: float = number_one / number_two
number_one_int_divided_by_number_two: int = number_one // number_two 
number_one_remainder_division_number_two: int = number_one % number_two
print(str(number_one) + " ** " + str(number_two) + " is " + str(number_one_to_the_power_of_number_two))
print(str(number_one) + " / " + str(number_two) + " is " + str(number_one_divided_by_number_two))
print(str(number_one) + " // " + str(number_two) + " is " + str(number_one_int_divided_by_number_two))
print(str(number_one) + " % " + str(number_two) + " is " + str(number_one_remainder_division_number_two))
