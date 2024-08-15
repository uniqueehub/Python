##Exceptions are errors detected at the time of program execution
#print(1/0)
#error == ZeroDivisionError: division by zero
#print('abc'+2)
#TypeError: can only concatenate str (not "int") to str
"""
x=input("Enter number1: ")
y=input("Enter number2: ")
try:
    z=int(x) / int(y)
except Exception as e:
    print("exception occured: ",e)
    z=None
print("Division is: ",z)
"""
x=input("Enter number1: ")
y=input("Enter number2: ")
try:
    z=x / int(y)
except Exception as e:
    print("exception occured: ",type(e).__name__)
    z=None
print("Division is: ",z)
