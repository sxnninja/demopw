import random
lower='qwertyuiopasdfghjklzxcvbnm'
upper='QWERTYUIOPASDFGHJKLZXCVBNM'
numbers='1234567890'
symbols='!@#$%^&*()_-+='

password=''
requiredpw=[]
fnpassword=[]
    
if __name__=='__main__':
    n=int(input('Do dai mat khau:'))
    all_chars=lower+upper+numbers+symbols
    rqpw=[random.choice(chars) for chars in [lower,upper,numbers,symbols]]
    
    lenreal=n-4
    
    pw=random.choices(all_chars,k=lenreal)
    fnpassword=rqpw + pw
    random.shuffle(fnpassword)
    PASSWORD=''.join(fnpassword)   
               
    print(PASSWORD)


'''
Các hàm áp dụng:
+random.choice(a): chọn 1 phần tử từ a (list,tuple,string)
+random.choices(a,k=n): chọn nhiều phần tử từ a, mỗi lần lấy k phần tử (list,tuple,string)
+random.shuffle: xáo trộn (list)
+''.join(): công cụ chuyển từ list/tuple sang string

'''   

#STRING sang LIST : list(),split()
#LIST sang STRING : ''.join()

#STRING sang TUPLE : tuple()
#TUPLE sang STRING : ''.join()

#LIST sang TUPLE : tuple()
#TUPLE sang LIST : list()