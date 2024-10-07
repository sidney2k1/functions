def add(p,q):
    return p+q
def sub(p,q):
    return p-q
def multiply(p,q):
    return p*q
def divide(p,q):
    return p/q
print("please select your option")
print("A:Addition")
print("B:Subtraction")
print("C:Multiply")
print("D:Division")
choice=input("choose one of the four option:A/B/C/D:")
num1=int(input("Enter your number:"))
num2=int(input("Enter your number:"))
if choice=="A":
    print(num1," + ",num2," = ",add(num1,num2))
elif choice=="B":
    print(num1," - ",num2," = ",sub(num1,num2))
elif choice=="C":
    print(num1," * ",num2," = ",multiply(num1,num2))
elif choice=="D":
    print(num1," / ",num2," = ",divide(num1,num2))
else:
    print("invalid choice")