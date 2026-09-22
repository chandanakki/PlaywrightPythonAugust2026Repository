#After Applying the Exception Handling, What can be the behavior of execution of Program:
 
def addition(x,y):
    result=(x + y)
    print("Addition Result :",result)
 
def substraction(x,y):
    result=(x - y)
    print("Substraction Result :",result)
 
def multiplication(x,y):
    result=(x * y)
    print("Multiplication Result :",result)
 
# def division(x,y):
#     try:
#         result=(x / y)
#         print("Division Result :",result)
#     except ZeroDivisionError as e:
#         print("Zero Division Error has Occured :",e)


# #Case 1: Exception class used in the Except block must match with Exception thrown by the try block then only it handles the Exception
# def division(x,y):
#     try:
#         result=(x / y)
#         print("Division Result :",result)
#     except ImportError as e:
#         print("Zero Division Error has Occured :",e)

# #Case 2: If except block has Exception class , Does it handle the exception thrown by the try block.
# #answer : Yes, Since Exception is a super class , It can handle all sub class Exceptions.
# def division(x,y):
#     try:
#         result=(x / y)
#         print("Division Result :",result)
#     except Exception as e:
#         print("Zero Division Error has Occured :",e)

# #Case 3: 3. finally Block:
# #It is an optional block, Irrespective of Exception raised or not , This block Execute always. So the cleanup code we should specify in Finally Block.

# def division(x,y):
#     try:
#         result=(x / y)
#         print("Division Result :",result)
#     except Exception as e:
#         print("Zero Division Error has Occured :",e)
#     finally:
#         print("This statement execute Always !!!!")

#Special Case : try block is directly followed by finally block (except block is missing), does it works in Python.

# def division(x,y):
#     try:
#         result=(x / y)
#         print("Division Result :",result)
#     finally:
#         print("This statement execute Always !!!!")

def verify_even_number(num):
    if(num % 2 == 0):
        print(num, " is a Even Number")
 
def verify_odd_number(num):
    if(num % 2 == 1):
        print(num, " is a Odd Number")
 
def find_factorial(num):
    fact=1
    for i in range(num,0,-1):
        fact = fact * i
    print("Factorial of ",num," is ",fact)
 
def verify_divisiable_by_9(num):
    if(num % 9 ==0):
        print(num," is Divisiable by 9")
 
# Execute All Functions 
addition(40,30)
substraction(55,15)
verify_even_number(88)
multiplication(13,10)
division(45,0)
verify_odd_number(121)
find_factorial(5)
verify_divisiable_by_9(81)