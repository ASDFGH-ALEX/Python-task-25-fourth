'''
Author:Alex Sabu
Date:25-10-2024
Description:Write a Python program to convert temperature values back and forth between Celsius and Fahrenheit.
 The user should be able to input a temperature in Celsius or Fahrenheit,
 and the program should convert it to the other unit using the formula:
'''
temperature=int(input("Enter the temperature"))
scale=input("Is this (C)celsius or (F)Fahrenheit ")
if scale=="C":
    Fahrenheit=(9/5*temperature)+32
    print(temperature,"celsius is",Fahrenheit,"Fahrenheit")
elif scale=="F":
    Celsius=(5/9*(temperature-32))
    print(temperature,"Fahrenheit is",Celsius,"Celsius")
else:
    print("Wrong temperature code")



