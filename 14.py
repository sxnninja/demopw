#Phân tích thừa số nguyên tố của 1 số
import math
def pt(n):
    for i in range(2,math.isqrt(n)+1):
        if n%i==0:
            while n%i==0:
                print(i,end=' ')
                n//=i
    if n>1:
        print(n)
if __name__=='__main__':
    n=int(input('nhap so:'))
    pt(n)
    
'''có thể suy ra được ước của số đó
vd: 12=2x2x3
(2+1)x(1+1)=6 -> 6 nghiệm
'''