def gcd(a,b):
    
    if (b==0):
        return a
    else:
        return gcd(b,a%b)
a=78
b=44
result=gcd(a,b)
print(result)

'''a=int(input('Enter the value of a:'))
b=int(input('Enter the value of b:'))

result=gcd(a,b)
print(result)'''

'''def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
GCD=gcd(a,b)
print("GCD is: ",GCD)'''
