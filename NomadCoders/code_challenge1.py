# +,-,*,/,%,-x,**
# exception  -  string, / by 0

def plus(a,b):
    return a+b
def minus(a,b):
    return a-b
def times(a,b):
    return a*b
def div(a,b):
    try: return a/b
    except: return "can't div by 0"
def mod(a,b):
    try: return a%b
    except: return "can't div by 0"
def negat(a, b):
    return -a,-b
def pow(a,b):
    return a**b
def cal(s,a,b):
    return {"+":plus(a,b),"-":minus(a,b),"*":times(a,b),"/":div(a,b),
            "%":mod(a,b),"neg":negat(a,b),"^":pow(a,b)}.get(s,"not exist operator")

while True:
    try:
        a,b = int(input("a: ")),int(input("b: "))
        break
    except:
        print("int only")
s = input("cal: ")
print(cal(s,a,b))
