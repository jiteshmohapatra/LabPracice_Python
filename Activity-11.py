#Q)Write a Python program to get the least common multiple (LCM) of two positive integers using if else and while commands.

def calculate(x,y):
    if x>y:
        z=x
    else:
        z=y
    while(True):
        if((z%x==0)and(z%y==0)):
            calculate=z
            break
        z+=1
    return calculate
print(calculate(4,6))
print(calculate(15,17))