#Kiểm tra số nguyên tố
from math import*
def prime(n):
    for i in range(2,isqrt(n)+1):
        if n%i==0: return False
    return True

if __name__=='__main__':
    n=int(input('nhap so'))
    if prime(n):
        print('yes')
    else:
        print('no')