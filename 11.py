#hàm(function)
#Tham số hình thức: Parameter
def tong(a,b):
    t=a+b
    return t
m,n=10,20
print(tong(m,n))
x,y=100,200
print(tong(x,y)) #Đối số=tham số chính thức = Argument

'''nếu không có lệnh return thì print sẽ ra none'''

'''các def cơ bản khác '''
def tong(a,b):
    t=a+b
    return t

def change(n):
    n*=2
    return n

def xinchao():
    print('hello world')
#code để chạy ctr
if __name__ == '__main__':#code , báo hiệu bắt đầu sử dụng code
   xinchao()
   xinchao()
   for i in range(1):
       xinchao()


if __name__ == '__main__':#code , báo hiệu bắt đầu sử dụng code

    '''1 dòng lệnh thông báo bắt đầu làm việc'''

def xinchao(a,b,c):
    print('XINCHAO',a,b,c)
    
if __name__=='__main__':
    xinchao(b='o',a='s',c='n') #Keyword argument
    xinchao('x','y','z') #Positional argument
    
#Default argument
def in4(name,job='developer'):
    print(name,job)
    
if __name__ == '__main__':
    in4('son','xe om')
    in4('son')
'''output:
1 : son xe om
2 : son developer
'''

#bài hàm tính giải thừa
def giaithua(a):
    t=1
    for i in range(1,a+1):
        t=t*i
        print(i)
    return t
    
if __name__ == '__main__':
    print(giaithua(36))

'''output : 1
2
3
4
5
...
35
36
371993326789901217467999448150835200000000'''

#hàm tính số mũ
def somu(a,b):
    t=a**b
    return t  
    
if __name__ == '__main__':
    print(somu(3,6))

#kiểm tra số có chia hết cho cả 3 và 5 không
def kt(a):
    if a%3==0 and a%5==0:
        print('ok')
    else:
        print('no')
        
if __name__ == '__main__':
    kt(3)

#có thể return nhiều giá trị
def tonghieu(a,b):
    tong=a+b
    hieu=a-b
    return tong,hieu
        
if __name__ == '__main__':
    t,h=tonghieu(10,20)
    print(tonghieu(10,20))

#khi in ra tuple thì có thể dùng kĩ thuật unpack
'''tức là gán a,b,c,v.v cho các đối tượng return ra 
vd như ở trên có thể gán a,b = tonghieu(a,b)
'''