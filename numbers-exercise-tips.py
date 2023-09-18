import math
import random

# As another example, take a game with players 1 through 5. Say you have a variable player that
# keeps track of the current player. After player 5 goes, it’s player 1’s turn again. The modulo
# operator can be used to take care of this:

# player = player%5+1

# When player is 5, player%5 will be 0 and expression will set player to 1.

# from random import randint
# import math

# print(f"PI: {math.pi} ")
# print(f"sin(0) = {math.sin(0)}")

# ********************EXERCISES*********************

# 1- Write a program that generates and prints 50 random integers, each between 3 and 6.

# for i in range(50):
#     print(random.randint(3,6))


# ********************************************************

# 2- Write a program that generates a random number, x, between 1 and 50, random number y, between 2 and 5, and computes x ** y

# x = random.randint(1,50)
# y = random.randint(2,5)

# print(math.pow(x,y))


# ********************************************************

# 3- Write a program that generates a random number between 1 and 10 and prints your name that many times

# how_many = random.randint(1,10)

# for i in range(how_many):
#     print("Bartu Akdogan")

# ********************************************************

# 4- Write a program that generates a random decimal number between 1 and 10 with two decimal places of accuracy. Examples are 1.23, 3.45, 9.80 and 5.00

# a = random.uniform(1,10)

# print(f"The value: {a:.2f}")     # for decimal --> random.uniform()          for integer --> random.randint()

# ********************************************************

# 5- Write a program that generates 50 random numbers such that the first number is between 1 and 2, the second is between 1 and 3, the third is between 1 and 4, ..., the last is between 1 and 51.

# for i in range(51):
    
#     i += 1
#     print(random.randint(1,i))
    

# ********************************************************

# 6- Write a program that asks the user to enter two numbers, x and y, and computes |x - y| / (x + y)

# x = int(input("Enter the x: "))
# y = int(input("Enter the y: "))

# print(round((abs(x - y)) / (x + y), 2))


# ********************************************************

# 7- Write a program that asks the user to enter an angle between (-180°) and (+180°). Using an expression with the modulo operator, convert the angle to its equivalent between 0° and 360°.

# angle = float(input("Enter an angle between -180 and +180 degrees: "))

# Convert the angle to its equivalent between 0 and 360 degrees using the modulo operator

# equivalent_angle = angle % 360

# print(f"The equivalent angle between 0 and 360 degrees is : {equivalent_angle}")


# ********************************************************


# 8- Write a program that asks the user for a number of seconds and prints out how many minutes and seconds that is. For instance, 200 seconds is 3 minutes and 20 seconds.

# get_seconds = int(input("How many seconds do you want to convert to min-sec? : "))

# min = get_seconds // 60
# sec = get_seconds % 60

# print(f"Your input(type of seconds): {get_seconds} ||  type of Min: {min}m and Sec: {sec}s ")


# ********************************************************

# 9- Write a program that asks the user for an hour between 1 and 12 and for how many hours in the future they want to go. Print out what the hour will be many hours into the future. 

# An example is shown below.
# Enter hour: 8
# How many hours ahead? 5
# New hour: 1 o'clock

# get_hour = int(input("Enter Hour(1 and 12) : "))
# how_many_hours_ahead = int(input("How many hours ahead? : "))
# new_hour = (f"New Hour: {(get_hour + how_many_hours_ahead) % 12} o'clock.")

# print(new_hour)


# ********************************************************

# 10- Write a program that asks the user to enter a weight in kilograms. The program should convert it to pounds, printing the answer rounded to the nearest tenth of a pound

# get_kilo = int(input("Enter your weight (kilogram) : "))

# convert_to_pounds = get_kilo * 2.20462

# print(f"Your Weight(kilogram): {get_kilo}, and Your Weight(Pound): {round(convert_to_pounds)}")


# ********************************************************


# 11- Write a program that asks the user for a number and prints out the factorial of that number.

# get_num = int(input("Enter the number whose factorial you want to calculate : "))
# fact = math.factorial(get_num)

# print(f"Your number is: {get_num}, and the factorial is : {fact}")


# ********************************************************

# 12- Write a program that asks the user for a number and then prints out the sin(e), cos(e) and tangent of that number.

# get_num = int(input("Enter the number for using sin and cos : "))

# sin = math.sin(get_num)
# cos = math.cos(get_num)

# tan = sin / cos

# print(f"Sin value: {sin}, Cos value : {cos} and Tan Value: {tan}")


# ********************************************************


# 13- Write a program that asks the user to enter an angle in degrees and prints out the sine of that angle.

get_angle = int(input("Enter the angle: "))
sin_calc = math.sin(get_angle)

print(f"Angle : {get_angle} || Sin Value : {sin_calc}")


# ********************************************************
