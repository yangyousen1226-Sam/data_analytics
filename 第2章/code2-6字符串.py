# 创建字符串
s1 = 'hello'
print(s1)
s2 = "hello"
print(s2)
s3 = '''2024
hello
world'''
print(s3)
s4 = "It's a beautiful day"
print(s4)
s5 = '1234\'\"6666'  # \的作用是区分取消’的特殊含义，使得能打印出所需要的’‘内容
print(s5)

s6 = '\\\\\\\\\\\\'
print(s6)

#字符串拼接
print('----------字符串拼接--------------')
print(s1 + s4 +s5)

# 注意：字符串与数字不能相加，要先转换
print('----------字符串拼接--------------')
#字符串乘法
print(s1*2)
print("happy"*8)