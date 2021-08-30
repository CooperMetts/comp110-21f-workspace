"""Relational operators practice."""

__author__ = "730336784"

number_one: int = int(input("Pick a number ")) 
number_two: int = int(input("Pick another number "))

number_one_greater_than_number_two: int = number_one > number_two
number_one_is_at_least_number_two: int = number_one >= number_two
number_one_equal_to_number_two: int = number_one == number_two 
number_one_is_not_equal_to_number_two: int = number_one != number_two

print(str(number_one) + " > " + str(number_two) + " is " + str(number_one_greater_than_number_two))
print(str(number_one) + " >= " + str(number_two) + " is " + str(number_one_is_at_least_number_two))
print(str(number_one) + " == " + str(number_two) + " is " + str(number_one_equal_to_number_two))
print(str(number_one) + " != " + str(number_two) + " is " + str(number_one_is_not_equal_to_number_two))
