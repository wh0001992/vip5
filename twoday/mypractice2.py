#一、列出100以内偶数中能整除3的所有数字
# list1 = [x for x in range(1,100) if x % 2 == 0 and x%3 ==0]
# print(list1)
#二、输出100以内的所有质数（只能被1和其本身整除的数）
#1-判断一个数是质数
#第一种方法
# list1 = []
# for x in range(2,101):
#     for n in range(2,x):
#         if x % n == 0:
#             break
#     else:
#         list1.append(x)
# print(list1)
#第二种方法
# list1 = []
# for x in range(2,101):
#     if x ==2:
#         list1.append(x)
#     else:
#         for n in range(2,x):
#             if x % n == 0:
#                 break
#             elif n == x-1:
#                 list1.append(x)
# print(list1)
# m = int(input('请输入！'))
# print(type(m))
#如何求一个数是质数
# list1 = []
# for n in range(1,m+1):
#     #如果是2和1则不用判断，直接加入列表
#     if n == 2 or n == 1:
#         list1.append(n)
#     #否则（大于2）开始判断
#     else:
#         #判断一个数是否为质数-循环体
#         for i in range(2,n):
#
#             if n % i == 0:
#                 #如果条件成立说明能被整除，不是质数
#                 print(("此数%d不是质数")%(n))
#                 break
#             elif i == n-1:
#                 #否则要判断是否全部整除完毕，从2开始整除，一直到n-1代表全部整除完毕
#                 print(("此数%d是质数")%(n))
#                 list1.append(n)
#
# print(list1)
#2-循环100次
#三、求10阶乘
#1、求两个数的积
#2、加循环
# b = 1
# j = 2
# while j<11:
#     b =b*j
#     j += 1
# print(b)
#四、求100以内能被3整除的数，并将作为列表输出
#1、一个数能否被3整除
#2、100以内能被3整除的数
#3、把这些数放到列表里
# list3 = []
# for i in range(1,100):
#     if i % 3 ==0:
#         list3.append(i)
# print(list3)
#五、列表[1,2,3,4,3,4,2,5,5,8,9,7],将此列表去重，得到一个唯一元素的列表
# list1 = [1,2,3,4,3,4,2,5,5,8,9,7]
# list2 = []
# #获取这个列表的长度
# m = len(list1)
# #列表从零开始取
# for n in range(m):
#     if list2.count(list1[n])<1:
#         list2.append(list1[n])
#     else:
#         continue
# print(list2)
#六、求斐波那契数列 1 1 2 3 5 8 13 ……








