from math import *
def list_prime(p):
    natural_numbers=[]
    for i in range(2,int(p**0.5)+1):
        natural_numbers.append(i)
    
    primes=natural_numbers+[]
    for k in natural_numbers:
        for c in natural_numbers:
            if c*k in primes:
                primes.remove(c*k)
    return(primes) 

def IsItPrime(m):
    if m in list_prime(m**2):
        print(m," is prime")
    else:
        print(m,"is not prime")

def BreakDown(p):
    c=list_prime(p**2+1)
    BreakDown_list=[]
    BreakDownDown_list=[]
    for i in list_prime(p**2+1):
        while p % i == 0:
            BreakDown_list.append(i)
            p = p // i
    print(BreakDown_list)
    
    while float(max(c))>float(max(BreakDown_list)):
        c.remove(float(max(c)))
    for i in c:
        t=BreakDown_list.count(i)
        BreakDownDown_list.append(t)
        while i in BreakDown_list:
            BreakDown_list.remove(i)

    print(BreakDownDown_list)