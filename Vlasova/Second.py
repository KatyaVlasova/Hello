from re import S


def plus(c, s):
    print(c+s)
    return c+S
  
def minus(c,s):
    print(c-s)
    return(c-s)



def calc():
    c = int(input("введи c "))
    s = int(input("введи s "))
    operand = input("введи operand ")
    if operand == "+":
        print(c+s)
    elif operand =="-":
        print(c-s)
    elif operand == "*":
        print(c*s)
    elif operand == "/":
        print(c/s)            

