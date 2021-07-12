import math 
import mathFun

#first input -> num1 
#opperation -> opp
#second input -> num2
#perform calculation & result -> res
# ask for next opperation
# if "=" then print res 
# else res -> num1 
# ask num2 
# perform caluculation & result -> res  

def funCalculator():
   
    strInput = input()
    num = 0
    if strInput == "pi":
        num = float(math.pi)
    elif strInput == "e":
        num = float(math.e)
    elif strInput == "tau":
        num = float(math.tau)
    else:
        num = float(strInput)

    res = num

    while True:
        
        opp = input()
        
        if opp == "=": 
            break

        strInput = input()
        num = 0
        if strInput == "pi":
            num = float(math.pi)
        elif strInput == "e":
            num = float(math.e)
        elif strInput == "tau":
            num = float(math.tau)
        else:
            num = float(strInput)

        if opp == "+":
            res = mathFun.add(res,num)
        elif opp == "-":
            res = mathFun.subtract(res,num)    
        elif opp == "x":
            res=mathFun.multiply(res,num)
        elif opp == "/":
            res = mathFun.devide(res,num)
        elif opp == "%":
            res = mathFun.remainder(res,num)
        elif opp == "*":
            res = mathFun.exponent(res,num)
    
    print(res)
       
        
if __name__ == '__main__':
    funCalculator()
