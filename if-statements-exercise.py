import time
import random

# **************** EXERCISES ******************

# 1- Write a program that asks the user to enter a length in centimeters. If the user enters a negative length, the program should tell the user that the entry is invalid. Otherwise, the program should convert the length to inches and print out the result. There are 2.54 centimeters in an inch. (1 inch = 2.54cm)

# get_input = int(input("Please enter the centimeter value(must be positive!) : "))
# convert_inches = get_input / 2.54

# if (get_input < 0 ):
#     print("The Entry is INVALID! You should enter positive value.")
# else: 
#     print(f"Your centimeter value is : {get_input}  ||  The inch value is : {convert_inches}")

# **********************************

# 2- Ask the user for a temperature. Then ask them what units, Celsius or Fahrenheit, the temperature is in. Your program should convert the temperature to the other unit. (The conversions are °F = ((9/5) * °C ) + 32 and °C = (5/9) * (°F - 32))

# temperature = int(input("Please enter the temperature : "))
# unit = input("Celsius(°C) or Fahrenheit(°F) ?(C/F) :   ")

# if (unit == 'C'):
#     celsius_to_fahrenheit = ((9 * temperature) / 5) + 32
#     print("Converting....")
#     time.sleep(1)
#     print(f"Celsius Value: {temperature} °C, and Fahrenheit Value: {celsius_to_fahrenheit} °F")
# elif (unit == 'F'):
#     fahrenheit_to_celsius = (((temperature - 32) * 5) / 9)
#     print("Converting....")
#     time.sleep(1)
#     print(f"Fahrenheit Value: {temperature} °F , and Celsius Value: {fahrenheit_to_celsius} °C")


# **********************************


# 3- Ask the user to enter a temperature in Celsius. The program should print a message based on the temperature:
# If the temperature is less than -273.15, print that the temperature is absolute 0.
# If it is exactly -273.15, print that the temperature is absolute 0.
# If the temperature is between -273.15 and 0, print that the temperature is below freezing.
# If it is 0, print that the temperature is at the freezing point.
# If it is between 0 and 100, print that the temperature is in the normal range.
# If it is 100, print that the temperature is at the boiling point.
# If it is above 100, print that the temperature is above the boiling point.

# celsius_input = int(input("Enter a temperature (°C) : "))
# time.sleep(0.2)


# if (celsius_input < -273.15):
#     print("The temperature is absolute 0.")
# elif (celsius_input == -273.15):
#     print("The temperature is absolute 0.")
# elif (celsius_input > -273.15 and celsius_input < 0):
#     print("The temperature is below freezing.")
# elif (celsius_input == 0):
#     print("The temperature is at the freezing point.")
# elif (celsius_input > 0 and celsius_input < 100):
#     print("The temperature is in the normal range.")
# elif (celsius_input == 100):
#     print("The temperature is at the boiling point.")
# else:
#     print("The temperature is above the boiling point.")


# **********************************


# 4- Write a program that asks the user how many credits they have taken. If they have taken 23 or less, print that the student is a freshman. If they have taken between 24 and 53, print that they are sophomore. The range for juniors is 54 to 83, and for seniors it is 84 and over.

# credits = int(input("How many credits do you have? (integer) : "))

# if (credits <= 23):
#     print("Student is a FRESHMAN!..")
# elif (credits >= 24 and credits <= 53):
#     print("Student is a SOPHOMORE!..")
# elif (credits >= 54 and credits <= 83):
#     print("Student is a JUNIOR!..")
# elif (credits >= 84):
#     print("Student is a SENIOR!..")


# **********************************

# 5- Generate a random number between 1 and 10. Ask the user to guess the number and print a message based on whether they get it right or not.




user_input = int(input("Guess the number between 1 - 10 ? : "))
num = random.randint(1,10)

if (user_input == num):
    time.sleep(0.3)
    print(f"Congrulations! The answer is : {num}")
        
    
else:
    time.sleep(0.3)
    print(f"Wrong!..")

# *****************************

# 6- A store charges $12 per item if you buy less than 10 items. If you buy between 10 and 99 items, the cost is $10 per item. If you buy 100 or more items, the cost is $7 per item. Write a program that asks the user how many items they are buying and prints the total cost.


how_many_items = int(input("How many items do you buy? : "))