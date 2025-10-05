#1.Cấu trúc dữ liệu ngăn xếp 
'''
+ Dựa trên nguyên tắc LIFO : Last in First out
push : đẩy vào
pop : lấy ra
'''

#2.Stackframe
'''
+ Cơ chế quản lí bộ nhớ, thông tin của hàm con khi gọi hàm đó
'''
#Hàm đệ quy
'''
+ Là 1 hàm gọi lại chính nó
+ Khi gọi quá nhiều sẽ báo Stackoverflow
def S(n):
    if n==0:
        return 0
    else:
        return n+S(n-1) #Đệ quy
if __name__=='__main__':
    n=4
    print(S(4))
output:10
+ Phải có điểm dừng, công thức truy hồi
'''
