import math 
print("This is a two number calculator")
print("Mathematical opperations are performed on the numbers in the order they are input") 
print("ex. to get the n-th root of the first number enter negitive n to the second number")
num1= input("Enter First Number (or 'pi', 'e', 'tau'):")
if num1=="pi":
    num1=math.pi
elif num1=="e":
    num1=math.e
elif num1=="tau":
    num1=math.tau

num2= input("Input Second Number (or 'pi', 'e', 'tau'):")
if num2=="pi":
    num2=math.pi
elif num2=="e":
    num2=math.e
elif num2=="tau":
    num2=math.tau

opp=input("Choose operation \n 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division \n 5.Remainder \n 6.Expontent \n")
print("Result:")
if opp=="1":
    print(float(num1)+float(num2))
elif opp=="2":
    print(float(num1)-float(num2))    
elif opp=="3":
    print(float(num1)*float(num2))
elif opp=="4":
    print(float(num1)/float(num2))
elif opp=="5":
    print(float(num1)%float(num2))
elif opp=="6":
    print(float(num1)**float(num2))