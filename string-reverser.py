import time

print("Welcome to our String Reverser Generator.....")

#Take an input

your_str = input("Please enter your text: ")

#Reverse the string and print it out.

list_of_chars = list(your_str)
list_of_chars.reverse()
reversed_string = ''.join(list_of_chars)

time.sleep(0.3)
print(f"Your String is: {your_str} and reversed version is: {reversed_string}...")