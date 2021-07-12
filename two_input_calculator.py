import math 
print("This is a two number calculator")
print("Mathematical opperations are performed on the numbers in the order they are input") 

print("ex. to get the n-th root of the first number enter negitive n to the second number")
in1= input("Enter First Number (or 'pi', 'e', 'tau'):")
if in1=="pi":
    num1=float(math.pi)
elif in1=="e":
    num1=float(math.e)
elif in1=="tau":
    num1=float(math.tau)
else:
    num1=float(in1)

in2= input("Enter Second Number (or 'pi', 'e', 'tau'):")
if in2=="pi":
    num2=float(math.pi)
elif in2=="e":
    num2=float(math.e)
elif in2=="tau":
    num2=float(math.tau)
else:
    num2=float(in2)

opp=input("Choose operation \n 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division \n 5.Remainder \n 6.Expontent \n")
print("Result:")
if opp=="1":
    print(num1+num2)
elif opp=="2":
    print(num1-num2)
elif opp=="3":
    print(num1*num2)
elif opp=="4":
    print(num1/num2)
elif opp=="5":
    print(num1%num2)
elif opp=="6":
    print(num1**num2)
else:
    print("Invalid Opperation")