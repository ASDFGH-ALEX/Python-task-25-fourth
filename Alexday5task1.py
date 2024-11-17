'''
Author:Alex
Date:16-11-2024
Description:An even number is divisible by 2, while an odd number is not.
This task will help you practice using the modulus operator (%) and conditional statements.
'''
num1=int(input("Enter a whole number: "))
if(num1%2==0):
    print("The number is even")
elif(num1%2!=0):
    print("The number is odd")
else:
    print("invalid Entry")


