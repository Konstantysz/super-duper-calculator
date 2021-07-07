import math 
def twoInputCalculator():
    print("This is a two number calculator")
    print("Mathematical opperations are performed on the numbers in the order they are input") 
    print("ex. to get the n-th root of the first number enter negitive n to the second number")

    strInput = input("Enter First Number (or 'pi', 'e', 'tau'):")
    num1 = 0
    if strInput == "pi":
        num1 = math.pi
    elif strInput == "e":
        num1 = math.e
    elif strInput == "tau":
        num1 = math.tau
    else:
        num1 = float(strInput)

    strInput = input("Input Second Number (or 'pi', 'e', 'tau'):")
    num2 = 0
    if strInput == "pi":
        num2 = math.pi
    elif strInput == "e":
        num2 = math.e
    elif strInput == "tau":
        num2 = math.tau
    else:
        num2 = float(strInput)

    strInput = input("Choose operation \n 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division \n 5.Remainder \n 6.Expontent \n")
    print("Result:")
    if strInput == "1":
        print(float(num1) + float(num2))
    elif strInput == "2":
        print(float(num1) - float(num2))    
    elif strInput == "3":
        print(float(num1) * float(num2))
    elif strInput == "4":
        print(float(num1) / float(num2))
    elif strInput == "5":
        print(float(num1) % float(num2))
    elif strInput == "6":
        print(float(num1) ** float(num2))

if __name__ == '__main__':
    twoInputCalculator()