a=0
b=1
n=int(input("Enter number of terms to print in the fibonacci series:"))
i=0
print(a)
print(b)
while(i<n-2):
    c=a+b
    print(a+b)
    a=b
    b=c
    i+=1
