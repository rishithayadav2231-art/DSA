a=int(input("enterb your frist number:"))
b=int(input("enter your second number:"))
while b!=0:
    a,b=b,a%b
print("GCD:",a)