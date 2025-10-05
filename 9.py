#for and range(start,stop,step)
a=str(input('nhap so'))
for i in range(int(a)+1):
    if i%2==0:
        print(i,end=' ')
'''đếm lùi thì dùng step âm'''

#tính tổng các số từ 1 đến 10
s=0
n=10
for i in range(1,n+1):
    s+=i
    print(s)
else:
    print('done')

#từ số 1 đến 10 nếu có số 7 thì dừng
for i in range(1,10):
    print(i)
    if i%7==0:
        break
        

#continue
for i in range(5):
    print('sonpy')
    continue #quay lại chạy tiếp kệ thằng sau
    print('py')
'''output : 5 thằng sonpy còn py thì vứt đéo quan tâm'''    
     
#for lồng nhau và hàm range()
for i in range(10):
    for z in range(10):
        i+=z
        print(i)
'''giải thích bài code for lồng ở trên:
bắt đầu với dòng for ở ngoài, khi i=0(bắt đầu chạy lần 1),sẽ thực hiện tiếp vòng for bên trong với i ban đầu =0 và z chạy từ 0 đến 10 và đưa ra tổng cuối
thì tiếp tục dòng for ở ngoài với i=1(chạy lần 2),sẽ thực hiện tiếp vòng for bên trong với i ban đầu=1 và z chạy từ 0 đến 10 và đưa ra tổng cuối
LIÊN TỤC cho đến lúc i của dòng for ở ngoài =9(lần chạy cuối) thì tiếp tục vòng for bên trong với i bắt đầu=9 và z chạy từ 0 đến 10, đưa ra tổng cuối rồi kết thúc.
'''
        
#kết luận
'''
range
break,continue
nested loop : vòng for lồng nhau
'''

#nếu step=0 thì range sẽ không chạy do không có bước nhảy