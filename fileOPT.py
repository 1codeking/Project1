#打开文件 open
# 指定编码类型UTF-8，
# fobj = open('test.txt','w')
# # #写入数据,默认编码类型是gbk，表示中文编码
# fobj.write('在苍茫的大海上\n')
# fobj.write('狂风卷积着乌云\n')
# fobj.write('在乌云和大海之间\n')
# fobj.write('有一只海燕在高傲的飞翔')
# fobj.close()

#以二进制形式去写入，wb只能写入字节
# fobj = open('test.txt','wb')
# fobj.write('在苍茫的大海上'.encode('utf-8'))
# fobj.write('狂风卷积着乌云'.encode('utf-8'))
# fobj.close()

# 模式a 用于追加，只能写入字符串
# fobj = open('test1.txt','a')
# fobj.write('有一只海燕')
# fobj.close()


#文件读取
# content = open('test.txt','rb')
# data = content.read()
# print(data)
# print(data.decode('gbk'))
# content.close()

#with 上下文管理，自动释放打开关联的对象
# with open('test.txt','r') as co:
#     print(co.read())


#文件定位 tell:返回指针当前所在位置
# truncate（）:保留前（）个字符
#seek 控制光标位置，从当前、初始、末尾位置进行计数；打开文件模式只能用'rb'形式打开！！！

#os 模块 rename 重命名 remove 删除  mkdir 创建文件夹，不允许创建多级  rmdir 删除文件夹，只能删除空目录
# makedirs 创建多级目录  shutil.rmtree（） #删除非空目录
#获取当前目录 os.getcwd（） 拼接路径  os.path.join(path1,path2)

# pickle 模块  序列化（dump）和反序列化（load）
# pickle(str,f1)

# import pickle
# str = 'i love python'
# list1 = [0,1,2,3]
# dict = {'file_name':'testy1.txt','bites':'25kb'}
# # f1 = open('test2.pkl','wb')
# a = pickle.dumps(str)
# b = pickle.dumps(list1)
# c = pickle.dumps(dict)
# # f1.close()
# # with open('test2.pkl','rb') as f1:
# a = pickle.loads(a)
# b = pickle.loads(b)
# c = pickle.loads(c)
# print(a)
# print(b)
# print(c)
# f1.close()

# -*- coding: utf-8 -*-
# @Time    : 2024-09-14 10:31
# @Author  : AmoXiang
# @File: json_demo.py
# @Software: PyCharm
# @Blog: https://blog.csdn.net/xw1680


import json

data1 = [{"a": "Amo", "b": (9, 99), "c": 6.6, "d": 11}]
with open("./test3.json", "w", encoding='utf8') as file:
    json.dump(data1, file, allow_nan=False, sort_keys=True, indent=4)

with open("./test3.json", "r", encoding='utf8') as file:
    data2 = json.load(file)  # 注意转换之后得类型 至于json.load文章后面会讲
    print(data2)  # [{'a': 'Amo', 'b': [9, 99], 'c': 6.6, 'd': 11}] 'b'对应的数据类型都改变了
    print(data1 == data2)
    print(type(data1),type(data2))



