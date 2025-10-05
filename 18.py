#Số hoàn hảo : 28,...
#Perfect number
from math import*
def pfn(n):
    t=1
    for i in range(2,isqrt(n)+1):
        if n%i==0:
            t+=i
            if i!=n//i:
                t+=n//i
    print(t)        
    if t==n:
        return True
    else:
        return False
        
if __name__=='__main__':
    n=int(input('nhap so:'))
    print(pfn(n))


''' bài toán tìm tổng nghiệm
from math import*
def tn(n):
    t=0
    for i in range(1,isqrt(n)+1):
        if n%i==0:
            t+=i
            if i!=n//i:
                t+=n//i
    return t
if __name__=='__main__':
    n=int(input('nhap so'))
    print(tn(n))
'''

#Định lý euclid-euler 
#Nếu p là số nguyên tố và 2**p-1 cũng là số nguyên tố-> (2**p-1)*(2*(p-1))-> là số hoàn hảo
from math import*
def prime(n):
    if n<2:
        return False
    for i in range(2,isqrt(n)+1):
        if n%i==0:
            return False
    return True
def npr(n):
    for p in range(1,30):
        if prime(p):
            if prime(2**p-1):
                #print('so fibo thu:',((2**p-1)*(2**(p-1))))
                if ((2**p-1)*(2**(p-1)))==s:
                    return True
    return False           
if __name__=='__main__':
    '''n=int(input('nhap so'))'''
    s=int(input('so hoan hao can check:'))
    print(npr(s))
    