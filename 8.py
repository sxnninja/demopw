#cấu trúc rẽ nhánh
'''
if kết hợp cùng and và or 
'''
#
n=int(input(''))
if (n!=0) and (n%2==0):
    print('la so chan')
elif n==0:
    print('day la so 0')
else:
    print('la so le')
#
n=int(input())
a,b=3.6,36
if n>=3.6 and n<=36:
    print('in range')
else:
    print('not in range')

#else,elif(else if)  bắt buộc phải có if đi trước
n=int(input())
if n%3==0 or n%5==0:
    print('ok')
elif n%4==0:
    print('quite ok')
else:
    print('not ok')
#
t=int(input('nhập tháng'))
if t<1 or t>12:
    print('làm đéo có')
if 1<=t<=12:
    if t==1 or t==3 or t==5 or t==7 or t==8 or t==10 or t==12:
        print('có 31 ngày')
    elif t==2:
        print('có 28 ngày')
    else:
        print('có 30 ngày')

#shorthandif (viết luôn điều được in ra cùng dòng if)
a=int(input('nhập số'))
b=int(input('nhập số'))
if a>b: print('a>b');print('test code')

#shorthandif và toán tử ba ngôi
a=int(input('nhập số 1:'))
b=int(input('nhập số 2:'))
test='chim' if a<b else 'lợn'
print(test)

#if lồng nhau (hạn chế)





