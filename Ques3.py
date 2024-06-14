#3 Write a python program that calculates the factorial of a given number.

a=int(input("Enter number to get it's fatorial: "))
ans=1
while(a):
    ans=ans*a
    a=a-1
print(ans)
