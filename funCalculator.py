import math 
import mathFun

def funCalculator():
   
    strInput = input()
    num1 = 0
    if strInput == "pi":
        num1 = float(math.pi)
    elif strInput == "e":
        num1 = float(math.e)
    elif strInput == "tau":
        num1 = float(math.tau)
    else:
        num1 = float(strInput)

    opp = input()

    strInput = input()
    num2 = 0
    if strInput == "pi":
        num2 = float(math.pi)
    elif strInput == "e":
        num2 = float(math.e)
    elif strInput == "tau":
        num2 = float(math.tau)
    else:
        num2 = float(strInput)

    res = 0

    if opp == "+":
        res = mathFun.add(num1,num2)
    elif opp == "-":
        res = mathFun.subtract(num1,num2)    
    elif opp == "x":
        res=mathFun.multiply(num1,num2)
    elif opp == "/":
        res = mathFun.devide(num1,num2)
    elif opp == "%":
        res = mathFun.remainder(num1,num2)
    elif opp == "*":
        res = mathFun.exponent(num1,num2)

    while True:
        
        opp = input()
        
        if opp == "=": 
            break

        num1 = res

        strInput = input()
        num2 = 0
        if strInput == "pi":
            num2 = float(math.pi)
        elif strInput == "e":
            num2 = float(math.e)
        elif strInput == "tau":
            num2 = float(math.tau)
        else:
            num2 = float(strInput)

        res = 0

        if opp == "+":
            res = mathFun.add(num1,num2)
        elif opp == "-":
            res = mathFun.subtract(num1,num2)    
        elif opp == "x":
            res=mathFun.multiply(num1,num2)
        elif opp == "/":
            res = mathFun.devide(num1,num2)
        elif opp == "%":
            res = mathFun.remainder(num1,num2)
        elif opp == "*":
            res = mathFun.exponent(num1,num2)
    
    print(res)
       
        
if __name__ == '__main__':
    funCalculator()
