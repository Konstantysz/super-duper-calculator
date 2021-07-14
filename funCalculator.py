import math 
import mathFun 

def funCalculator():
    mem = 0 
    res = 0
    while True:
        mem = res
        strInput = input()
        res = 0
        if strInput == "pi":
            res = float(math.pi)
        elif strInput == "e":
            res = float(math.e)
        elif strInput == "tau":
            res = float(math.tau)
        else:
            res = float(strInput)

        while True:
            
            opp = input()
            
            if opp == "=": 
                break
            elif opp == "squared":
                res = mathFun.square(res)
                break
            elif opp == "inverse":
                res = mathFun.inverse(res)
                break
            elif opp == "squrt":
                res = mathFun.squrt(res)
                break

            strInput = input()
            num = 0
            if strInput == "pi":
                num = float(math.pi)
            elif strInput == "e":
                num = float(math.e)
            elif strInput == "tau":
                num = float(math.tau)
            elif strInput == "mem":
                num = mem
            else:
                num = float(strInput)

            if opp == "+":
                res = mathFun.add(res, num)
            elif opp == "-":
                res = mathFun.subtract(res, num)    
            elif opp == "x":
                res=mathFun.multiply(res, num)
            elif opp == "/":
                res = mathFun.devide(res, num)
            elif opp == "%":
                res = mathFun.remainder(res, num)
            elif opp == "^":
                res = mathFun.exponent(res, num)

        print(res)
       
        
if __name__ == '__main__':
    funCalculator()
