print("hello world!!!")

# 我是注释
"""我也是注释"""

money = 50

print("钱包还有：", money)

# 买了一个冰淇淋
money -= 10

print(money)

ans = "woc"
print(ans)

a = 151.555

ans_type = type(ans)
print(ans_type)

# python中变量没有类型 究极无敌逆天！！！
# 强转
wod = str(11)

nimade = float(10086.44)

# 算术
a = 5
b = 66
print(a + b)
print(b // a)  # b中有几个a
print(b / a)
b %= a
b //= a
print(b)

a **= a
# 幂赋值运算符


c = 50
d = 6
c **= d
print(c)

# 字符串定义法 有" "  ' ' """ """

x = 10
y = 50
z = 60
if x < y < z:
    print("yes")

nameme = "666"
message = "woc %s" % nameme
print(message)

condition = 0
while condition < 10:
    condition += 1
    print(condition)

print(condition)

listt = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in listt:
    print(i)

for i in range(1, 10, 2):  # 从1到9 第三个是步长 也就是每个数的间隔
    print(i)

x = 4
y = 5
z = 6
if x > 1:
    print(x)
elif x < 5:
    # else if
    print(y)
else:
    print(z)


def func():
    z = x + y
    print(z)


func()


def action(a, b, g=5):  # 默认参数和c++顺序一样
    d = a * b  # 局部变量
    global cc
    cc = 100
    print(d, g)
    return "ans"


action(x, y)

print(action(1, 2))

AK = 47  # 全局变量

print(cc)

import numpy as num

print("\nshit")

my_file = open('mytext.txt', 'w')  # 'r'只读
my_file.write('101')
my_file.close()

# 追加 'a'
file = open('mytext.txt', 'r')
content = file.readline()
print(content)


class Calculator:
    name = "hey"

    def __init__(self, name):
        self.name = name

    def add(self, x, y):
        result = x + y
        print(result)
        print(self.name)


calcul = Calculator("wuwu")
calcul.add(10, 11)

input_p = int(input('num:'))
print('you give:', input_p)
if input_p == 0:
    print('你是0！')

a = [1, 2, 3, 4, 5, 6, 1]
a.insert(2, 3)
a.remove(2)  # 去掉2的值
a.count(3)
k = a.index(6)
a.sort()
a.sort(reverse=True)
print(a)

# 分割线 #


multi_arraywo = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(multi_arraywo[0][2])

dictionary = {'wo': 1, 'shi': 2, 'sha': {1: 'wo', 2: [7, 7]}, 'bi': 4}
print(dictionary['wo'])  # 只能将左侧值作为索引 左侧可为数字

del dictionary['wo']
dictionary['b'] = 10
print(dictionary['sha'][2][0])  # 无限套娃

import time

print(time.localtime())

from time import time, localtime

print(localtime())

from time import *  # 代表引入所有功能

import myPack as printer

printer.printdata(dictionary)

con = True
while con:
    b = input('get cin:')
    if b == '114':
        break
    else:
        continue

try:
    file = open("eeee.txt", 'r')
except Exception as e:
    print(e)
    print("错误如上")
else:
    print("成功打开")
    file.close()

zip1 = [1, 2, 3]
zip2 = [3, 4, 5]
print(zip(zip1, zip2))
for i, j in zip(zip1, zip2):
    print(i / 2, j * 2)

funwo = lambda x, y: print(x + y)

funwo(5, 7)

print(list(map(funwo,[2,4],[4,6])))

import copy
a[2] = [1, 2]
b = a
b = copy.copy(a)

c = copy.deepcopy(a)
a[0] = 3
print(b)
print(c)

# 多线程
# 多核
# tkinter 可视化

import pickle

filed = open ('pick', 'wb')
pickle.dump(dictionary,filed)
filed.close()

with open('pick', 'rb') as filed:
    key = pickle.load(filed)

print(key)

char_list =['a', 'a', 'b', 'b', 'v']
print(set(char_list))
print(set(char_list))
# 只能一个一个加元素


# 正值表达式
# 待学习