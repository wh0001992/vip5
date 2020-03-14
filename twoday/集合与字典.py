

#分别定义一个集合和一个字典

'''
a = {1,4,9}
dict1 = {'b':1,'c':2}
'''
#为集合和字典分别插入元素：55（d：55）

'''a = {1,4,9}
dict1 = {'b':1,'c':2}
a.add(55)
dict1['d']=55
'''
#分别删除集合和字典内的一个元素
a = {1,4,9}
dict1 = {'b':1,'c':2}
a.remove(1)
del dict1['b']
#取出字典内的所有值（value）和集合组合一个列表

'''
a = {1,4,9}
dict1 = {'b':1,'c':2}
e=list(dict1.values())
f=list(a)
e.extend(f)
print(e)
'''