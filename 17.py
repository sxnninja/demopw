#số thuận nghịch,đối xứng,palindrome
def palin(n):
    m=n
    a=0
    while n!=0:
        a=a*10+n%10
        n//=10
    if a==m:
        return True
if __name__=='__main__':
    n=int(input('nhap so'))
    if palin(n): print('juan')
    else: print('ahh')