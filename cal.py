def add():
    a = int(input("enter 1st no"))
    b = int(input("enter 2nd no"))
    print(a+b)
def sub():
    a = int(input("enter 1st no"))
    b = int(input("enter 2nd no"))
    print(a-b)
def mul():
    a = int(input("enter 1st no"))
    b = int(input("enter 2nd no"))
    print(a+b)
def div():
    a = int(input("enter 1st no"))
    b = int(input("enter 2nd no"))
    print(a/b)
    
print("This is a clc")
x = input("what you want to do like +,-,*,/")
if x == "+":
    add()
elif x == "-":
    sub()
elif x == "*":
    mul()
elif x == "/":
    div()
else:
    print("wrong input please choose between +,-,*,/ only")
