#Jaunel Deans 
#October 12, 2023
#This program will define four subroutines - add, subtract, multiply, divide that add multiply. Two numbers and return the result. Each should have two integer number arguments. The user is asked to input two numbers. These numbers will be passed as arguments into one of the subroutines. The user is asked to input 1 to add, 2 to subtract. If they input 1, call the ‘add’ subroutine, input 2 calls the ‘subtract’ subroutine. Output the returned result as part of a sentence.

number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))
opeartion = input("What math opeartion would you like to perform. Type in 1 for Addition, 2 for Subtraction, 3 for Multiplication or 4 for Divison:  ")

def add(num1, num2):
    result = num1 + num2
    return result

def sub(num1,num2):
    result = num1 - num2
    return result

def multi(num1,num2):
    result = num1 * num2
    return result

def div(num1,num2):
    result = num1 / num2
    return result

if opeartion == "1":
  print(add(number1,number2) , "is the sum of " + str(number1) + " and " + str(number2))

elif opeartion == "2":
  print(sub(number1,number2) , "is the difference of " + str(number1) , "and " + str(number2))

elif opeartion == "3":
  print(multi(number1,number2) , "is the product of " + str(number1) , "and" , str(number2))

elif opeartion == "4":
  print(div(number1,number2) , "is the quotient of " + str(number1) , "and" , str(number2))

else:
  print("Invalid Input")