#Tính tổng ước và đếm ước của 1 số (tối ưu)
from math import*
def dem_uoc(n):
    cnt=0
    for i in range(1,isqrt(n)+1):
        if n%i==0:
            cnt+=1
            if i!=n//i:
                cnt+=1               
    return cnt

def tong_uoc(n):
    tong=0
    for i in range(1,isqrt(n)+1):
        if n%i==0:
            tong+=i
            if i!=n//i:
                tong+=n//i
    return tong

if __name__=='__main__':
    n=int(input('nhap so'))
    print(tong_uoc(n))
    print(dem_uoc(n))