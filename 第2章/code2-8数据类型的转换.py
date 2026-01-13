# 转换为整数int
# 1.字符串str--->整数int
# (字符串里的内容只能是纯整数的字符串才行，小数和带有其他的不行)
s = "2024"
n = int(s)
print(n)
print(type(s), type(n))
print("分隔----------------------------分隔")
s1 = 'aaa223'
# print(int(s1))  不行，会报错，字符串里只能是纯整数

# 2.浮点数float--->整数int
s1 =2.23
print(int(s1))  #2

# 3. 布尔bool--->整数int
s2, s3 =True, False
print(int(s2), int(s3))   #输出1 0




# 转换为浮点数float
# 1.str-->float字符串里的数字都能转换为浮点数（有没有小数点都行，带字母就不行）
print(float(s))  #输出2024.0
# 2.int-->float
n = 2024
print(float(n))  #输出2024.0
# 3.bool-->float
print(float(s2), float(s3))  #输出1.0  0.0




# 转换为布尔bool
# 1.str-->bool
g = 'sdw323'
print(bool(g))  #输出为True。bool是判断真假，只要变量里有内容就行
g1 = ""
print(bool(g1))  #输出为False
# 2.int-->bool
n = 1
print(bool(n))  #输出为True
n = 0
print(bool(n))  #输出为False
# float-->bool
f = 3.0
print(bool(f))  #输出为True
f1 = 0.0
print(bool(f1))  #输出为False





# 转换为字符串str
# 1.int-->str
k = 5
print(str(k))
print(type(str(k)))
# 2.float-->str
y = 5.3
print(str(y))
print(type(str(y)))
# 3.bool-->str
b = True
print(type(b))
print(str(b))
print(type(str(b)))

print("分隔----------------------------分隔")



# 进制的转换
q = '1010'
print(int(q, 2))  #输出为10，因为这里规定了q为2进制数，所以输出10进制数为10
