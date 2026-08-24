n=int(input("enter your number:"))
sum1=0
sum2=0
for i in range(1,n+1):
    if i%2==0:
        sum1+=i
else:
    sum2+=1
print("the even numbers are",sum1)
print("the odd numbers are",sum2)
print("the sum of even numbers is",sum1+sum2)