    # ARITHMETIC__CALCULATOR
num1=float(input("Enter a first number:"))
num2=float(input("Enter a second number:"))
print("Press 1 for Addition")
print("Press 2 for Subtraction")
print("Press 3 for Multiplication")
print("Press 4 for Division")
 
Choice=int(input("Enter a choice here:"))

if(Choice == 1):
    print(num1+num2)
elif(Choice == 2):
    print(num1-num2)
elif(Choice == 3):
    print(num1*num2)
elif(Choice == 4):
    print(num1/num2)
