#in day so fibo vao so fibo thu n
n=int(input('nhap day so:'))
sotruoc=0
sosau=1
for i in range(n):
    sotruoc,sosau=sosau,sotruoc+sosau
    print(sotruoc)
print('so fibo thu n gia tri la',sotruoc)
#kiem tra so fibo
s=int(input('nhap so:'))
while sotruoc<=s:
    if sotruoc==n:
        print('la so fibo')
        break
    sotruoc,sosau=sosau,sotruoc+sosau
else:
    print('ko phai sofibo')


#dùng đệ quy
def fibo(n):
    if n==0 or n==1:
        return 1
    return fibo(n-1)+fibo(n-2)
if __name__=='__main__':
    n=int(input('số fibo lần thứ :'))
    for i in range(n):
        print(fibo(i))
