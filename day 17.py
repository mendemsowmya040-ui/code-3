
def palidram_or_palidram():
    n=int(input())
    t=n
    s=0
    while n>0:
        d=n%10
        s=s*10+d
        n=n//10
    if t==s:
        print("palidram")
    else:
        print("not palidram")
    palidram_or_palidram()

def palidram_or_palidram():
    n=int(input())
    org=n
    rev=0
    while n>0:
        d=n%10
        rev=rev*10+d
        n=n//10
    if org==rev:
        print("palidram")
    else:
        print("not palidram")
    palidram_or_palidram()

def prime_number_or_not_using_while():
    n=int(input())
    s=1
    c=0
    while s<=n:
        if n%s==0:
            c=c+1
        s=s+1
    if c==2:
        print("prime number")
    else:
        print("not prime number")
    prime_number_or_not_using_while()

def perfect_number_using_forloop():
    n=int(input())
    c=0
    for i in range(1,n):
        if n%i==0:
            c=c+i
    if c==n:
        print("perfect number")
    else:
        print("not perfect number")
    perfect_number_using_forloop()
   
def perfect_number_using_whileloop():
    n=int(input())
    i=1
    sum=0
    while i<n:
        if n%i==0:
            sum=sum+i
        i=i+1
    if n==sum:
        print("perfect number")
    else:
        print("not perfect number")
perfect_number_using_whileloop()
