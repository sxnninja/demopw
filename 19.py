#Lý thuyết đồng dư
'''
(A+B)%C=((A%C)+(B%C))%C
(A-B)%C=((A%C)-(B%C))%C
(A*B)%C=((A%C)*(B%C))%C
'''
#Khi bài toán yêu cầu chia dư kết quả cho 1 số nào đó -> tính đến đâu chia dư đến đó

if __name__=='__main__':
    n=int(input('nhap n:'))
    t=1
    for i in range(1,n+1):
        t*=i
        t%=(10**9+7)    
    print(t)
        
if __name__=='__main__':
    a,b,c=map(int,input('nhap 3 so').split())
    t=1
    for i in range(b):
        t=(t*a)%c
    print(t)     
