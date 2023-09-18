import math

# 1- Write a program that prints your name 100 times
# get_name = input("What's your name? : ")
# for i in range(100):
#     print(get_name)

# ******************************************************

# 2- Write a program to fill the screen horizontally and vertically with your name.

# for i in range(100):
#     print(get_name, end=' ')

# ******************************************************

# 3- Write a program that outputs 100 lines, numbered 1 to 100 , each with your name on it. The output should look like the output below 
# 
# 1 Your name
# 2 Your name
# 3 Your name
# 4 Your name
# ...
# 100 Your name 


# for i in range(1, 101):
#     print(f"{i} Bartu Akdogan")   

# ******************************************************

# 4- Write a program that prints out a list of the integers from 1 to 20 and their squares. The output should look like this:
# 1 --- 1
# 2 --- 4
# 3 --- 9
# ...
# 20 --- 400

# for i in range(1, 21):
#     print(f"{i} --- {math.pow(i, 2)}")

# ******************************************************

# 5- Write a program that uses a for loop to print the numbers 8, 11, 14, 17, 20, .... , 89.

# for i in range(8, 90, 3):
#     print(i)

# ******************************************************

# 6- Write a program that uses a for loop to print the numbers 100, 98, 96, ..... , 4, 2.

# for i in range(100, 1, -2):
#     print(i)

# ******************************************************

# 7- Write a program that uses exactly four for loops to print sequence of  letters below:

# AAAAAAAAAABBBBBBBCDCDCDCDEFFFFFFG

# for i in range(10):
#     print('A',end='')

# for i in range(7):
#     print('B', end='')

# for i in range(4):
#     print('C', end='')
#     print('D', end='')

# print('E', end='')

# for i in range(6):
#     print('F', end='')

# print('G', end='')

# ******************************************************

# 8- Write a program that asks the user for their name and how many times to print it. The program should print out the user's name the specified number of times.

# get_name = input("Enter your name: ")
# repeat = int(input("How many times do you want to repeat? (integer) : "))

# for i in range(1, repeat + 1):
#     print(get_name)

# ******************************************************

# 9- The Fibonacci numbers are the sequence below, where the first two numbers are 1, and each number thereafter is the sum of the two preceding numbers. Write a program that asks the user how many Fibonacci numbers to print and then prints that many.

# 1,1,2,3,5,8,13,21,34,55,89

# how_many = int(input("How many Fibonacci numbers do you want to print? : "))
# fibonacci_seq = []
# a, b = 1, 1
# for i in range(how_many):
#     fibonacci_seq.append(a)
#     a,b = b, a + b
#     print(fibonacci_seq, end='')
    


# *******************************************************

# 10- Use a for loop to print a box like the one below. Allow the user to specify how wide and how
# high the box should be. [Hint: print('*'*10) prints ten asterisks.]

width = int(input("Enter the width of the box: "))
height = int(input("Enter the height of the box: "))

for i in range(height):
    for j in range(width):
        print('*', end='')
    print()