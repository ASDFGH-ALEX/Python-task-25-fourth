'''
Author:Alex
Date:16-1-2024
Description:In this task, you’ll learn how to takemultiple inputs and use conditional
statements to perform different actions based on the user's choice.
'''
num_1=int(input("Enter the first number: "))
num_2=int(input("Enter the second number: "))
op=input("Choose the operator(+,-,*,/): ")
if(op=='+'):
    result= num_1+num_2
    print("The result is: ",result)
elif(op=='-'):
    result= num_1-num_2
    print("The result is: ",result)
elif(op=='*'):
    result= num_1*num_2
    print("The result is: ",result)
elif(op=='/'):
    result= num_1/num_2
    print("The result is: ",result)
else:
    print("Wrong calculation")