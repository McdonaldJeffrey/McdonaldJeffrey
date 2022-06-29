print ("Enter the number :")

print ("1 as Addition")
print ("2 as Subration")
print ("3 as Multiply ")
print ("4 as Divide")
operation = input()
if operation == "1":
    num1= input("enter the number:")
    num2=input("enter the number:")
    print("Sum of the numbers :" + str(int(num1) + int(num2)))
elif operation == "2":
    num1= input("enter the number:")
    num2=input("enter the number:")
    print("Diffrence of the numbers :" + str(int(num1) - int(num2)))
elif operation == "3":
    num1= input("enter the number:")
    num2=input("enter the number:")
    print("Multiply of the numbers :" + str(int(num1) * int(num2)))
elif operation == "4":
    num1= input("enter the number:")
    num2=input("enter the number:")
    print(" Divison of the numbers :" + str(int(num1) * int(num2)))
else:
    print("invalid Numbe")







