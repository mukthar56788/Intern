#Mukthar
# Sample Python Program: Guess the Number Game

import random

def guess_the_number():
    number_to_guess = random.randint(1, 10)
    attempts = 0

    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 10.")

    while True:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low. Try again.")
            elif guess > number_to_guess:
                print("Too high. Try again.")
            else:
                print(f"🎉 Correct! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

# Run the game
guess_the_number()





#Rohini 
# Leetcode 2sum
class Solution(object):

    def twoSum(self, nums, target):
        l2=[]

        for i in range(len(nums)):
            for j in range(i):
                if target==nums[i]+nums[j]:
                   l2.append(i)
                   l2.append(j)
        return l2

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

l1=[2,7,11,15]
tar=9
s1=Solution()
r=s1.twoSum(l1,tar)
print(r)

# Susan 

#Calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero!"
    return x / y

print("Simple Calculator")
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

if choice in ['1', '2', '3', '4']:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
    else:
        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
else:
    print("Invalid choice.")
<<<<<<< HEAD


#Mileena
#Palindrome or not
def is_palindrome(value):
    # Convert to string to handle both numbers and strings
    value = str(value)
    return value == value[::-1]

# Example usage:
user_input = input("Enter a string or number: ")

if is_palindrome(user_input):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")

=======
	
	
#Noel 


n = 10
a = 0
b = 1
next = b  
count = 1

while count <= n:
    print(next, end=" ")
    count += 1
    a, b = b, next
    next = a + b
print()
>>>>>>> 6c72b9914572d544e454bc0df432140b5dc886fa
