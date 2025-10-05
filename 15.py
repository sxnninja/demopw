#UCLN, BCNN : euclid
'''UCLN : math.gcd(a,b)  - greatest common divisor'''
'''BCNN : math.lcm(a,b) - least common multiple'''

#GCD
def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

if __name__=='__main__':
    a,b=map(int,input('nhap 2 so:').split())
    print(gcd(a,b))

#LCM
def lcm(a,b):
    return a*b /gcd(a,b)
if __name__=='__main__':
    print(lcm(3,4))

#factorial(n)
#comb(a,b) - n!/(n!*(n-k)!)


