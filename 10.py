#while
'''in các số từ 1 đến 20'''
i=1
while i<=20:
    print(i)
    i+=1

'''chỉ được nhập số dương'''
while True:
    i=float(input('nhap so duong'))
    if i>0:
        print('ok')
        break
    elif i==0:
        print('nhap so duong di th l')
    else:
        print('nhap so am cai dcmm a')

'''bai tap: tinh tong chu so,dem chu so,tong chu so chan,tong chu so le'''

'''lật số thuận nghịch'''
n=int(input('nhap so'))
T=0
while n!=0:
    T=T*10+n%10
    n//=10
print(T)

#đếm số chữ số có thể dùng hàm len
n=int(input())
print(len(str(n)))

'''đếm chữ số'''
n=int(input('nhap so'))
dem=0
if n==0:
    dem+=1
while n!=0:
     n=abs(n)
     n//=10
     dem+=1
print('so chu so cua n:',dem)

'''tính tổng chữ số'''
n=int(input('nhap so'))
t=0
while n!=0:
    n=abs(n)
    t=t+n%10
    n//=10
print(t)

'''tính tổng chữ số chẵn'''
n=int(input('nhap so'))
t=0
while n!=0:
    if n%2==0:
        t=t+n%10
    n//=10
print(t)

'''tính tổng chữ số lẻ'''
n=int(input('nhap so'))
t=0
while n!=0:
    if n%2!=0:
        t=t+n%10
    n//=10
print(t)

