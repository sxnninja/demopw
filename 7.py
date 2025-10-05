from math import*
#Math module
#để sử dụng hàm toán học thì dùng import math
'''sử dụng print(help(math)) để xem hướng dẫn'''
#sqrt : square root (tính căn bậc 2)
'''math.sqrt(con số)'''
'''print(math.sqrt(36))'''

#isqrt : integer square root (căn bậc 2 chỉ lấy phần nguyên)
print(isqrt(35))

#có thể dùng 'import math'(dùng lệnh toán phải thêm math dài hơn) hoặc 'from math import*' (dùng lệnh khác ngắn hơn)

#pow : power (lũy thừa)
'''print(math.pow(2,36)) #nếu dùng import math'''
print(pow(2,3.6)) # nếu dùng from math import*

#ceil : ceiling (trần nhà?-làm tròn lên(chỉ lấy nguyên))
print(ceil(2.1)) # output : 3
print(ceil(8)) # output :8
print(ceil(3.5)) # output :4

#floor : sàn nhà-làm tròn xuống(chỉ lấy nguyên)
print(floor(3.6)) # 3
print(floor(2)) # 2
print(floor(5.1)) # 5

#factorial (giai thừa) vd: 5! , 10!,...
print(factorial(5)) # 120
print(1*2*3*4*5) # 120

#gcd :greatest common divisor (UCLN)
print(gcd(36,360)) #36
print(gcd(4,2)) #2 
'''không dùng được với float'''

#build-in function
'''round phụ thuộc vào phần thập phân'''
print(round(3.6)) #4
print(round(3.4)) #3
print(round(3.5)) #4
print(round(3.6543,2)) #3.65 ",2" ở đằng sau là muốn làm tròn đến bao nhiêu số sau dấu phẩy

'''abs'''
print(abs(-2,1)) # output:2

#sum : tổng (tuple/list)
'''tuple'''
print(round(sum((1,5.2321,-5,32,3.2)),2)) #output : 36.43
'''list'''
print(sum([1,2,3,4,5])) #output : 15

'''
khác nhau giữa tuple và list
là tuple không thể thêm bớt hay chỉnh sửa
nhưng list thì có thể
vd : 
a=[1,2,3]
a.append(3)
a[0]=36
print(a)
output : [36,2,3,3]
'''



'''max và min'''
a=min(1,2,45,463,5)
b=max(4,5,72,36,7)
print(a+b)
# output : 73







'''#comb(n,k) : tổ hợp chập k của n
print(comb(10,2)) #45

#perm : hoán vị
print(perm(5)) #120

print(perm(5,3)) chỉnh hợp #60
'''
