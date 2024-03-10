from math import *
def analysis(n,p):
    y=0
    y=n
    a_value=1
    powers_list=[]
    while a_value<=n:
        a_value=p*a_value
    print("n is in between",a_value,"and",a_value/p)
    while n > 0:
        while a_value>n:
            a_value=a_value/p
        powers_list.append(round(log(a_value,p),1))
        n=n-a_value
    print("to obtain",y,"you need to take the sum  of the followings powers of ",p,":",powers_list)
    base_list=[]
    max_value=int(max(powers_list))
    for i in range(max_value+1):
        base_list.append(powers_list.count(i))
    base_list.reverse()
    print("so in base",p,",n=",base_list)   