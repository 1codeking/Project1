#判断素数
# flag = False
# try:
#     num = int(input('请输入一个数字：'))
#     for i in range(2,num):
#         if num % i == 0:
#             flag = True
#             break
#     if flag:
#         print('合数')
#     else:
#         print('素数')
# except ValueError :
#     print('请输入数字！！')
from sys import flags
from wsgiref.validate import header_re


# 求阶乘
# n = int(input('请输入一个数字：'))
# result = 1
# for i in range(1,n+1):
#     result = result * i
# print(result)

#排序
# a = int(input('请输入：'))
# b = int(input('请输入：'))
# c = int(input('请输入：'))
# list = [a,b,c]
# list1 = sorted(list)
# print('顺序为：')
# for i in list1:
#     print(i,end=' ')



#找出区间内素数
# def su_Func(n):
#     flag = True
#     for i in range(2,n):
#         if n % i == 0:
#             flag = False
#             break
#     return  flag
#
# a = int(input('请输入：'))
# b = int(input('请输入：'))
# list = []
# for i in range(a,b+1):
#     if su_Func(i):
#         list.append(i)
# print(list)


#乘法口诀表
# for i in range(1,10):
#     print()
#     for j in range(1,i+1):
#         print(f'\t{j} * {i} = {j*i}',end=' ')

# 水仙花数
# for i in range(100,1000):
#     a = i // 100
#     b = (i % 100) // 10
#     c = i % 10
#     if a**3 + b**3 + c**3 == i:
#         print(f'{i}是水仙花数')

# 反向输出数字
# a = int(input('请输入一个整数：'))
# a = str(a)
# a = a[::-1]
# print(int(a))


#判断是否是字母
# a = input()
# res = a.isalpha()
# if res:
#     print(f'{a}是字母')
# else:
#     print(f'{a}不是字母')


#完数

# def wanshu_Func(n):
#     sum = 0
#     for i in range(1,n):
#         if n % i == 0:
#             sum += i
#     if sum == n:
#         print(f'{n}是完数。')
#
# for j in range(1,1000):
#     wanshu_Func(j)


#斐波那契数列
# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# print(fib(10))

# n = int(input(''))
# fib = [1,1]
# for i in range(2,n):
#     fib.append(fib[i-1] + fib[i-2])
# print(fib)

#列表的浅复制
# import copy
# # l1 = [1,2,3]
# # l2 = l1[::]
# # l3 = l1.copy()
# # l4 = copy.copy(l1)
# # print(l1,l2,l3,l4)
# # print(id(l1),id(l2),id(l3),id(l4))
# # 深复制
# l5 = [1,2,['a','b','c']]
# l6 = copy.deepcopy(l5)
# l5[-1][0] = 'xxx'
# print(l5,l6)


#栈的应用
#1.匹配（）括号
# from pythonds.basic.stack import Stack
# def parcheker(symbolstring):
#     s = Stack()
#     balance = True
#     index = 0
#     while index < len(symbolstring) and balance:
#         symbol = symbolstring[index]
#         if symbol == '(':
#             s.push(symbol)
#         else:
#             if s.isEmpty():
#                 balance = False
#             else:
#                 s.pop()
#         index += 1
#     if balance and s.isEmpty():
#         return True
#     else:
#         return False
#
# print(parcheker('(((()))()()())'))
# print(parcheker('(((()))))()(()())'))

#匹配通用括号类型
# from pythonds.basic.stack import Stack
# # def parcheker(symbolstring):
# s = Stack()
# print(type(s))
#     balance = True
#     index = 0
#     while index < len(symbolstring) and balance:
#         symbol = symbolstring[index]
#         if symbol in '([{':
#             s.push(symbol)
#         else:
#             if s.isEmpty():
#                 balance = False
#             else:
#                 top = s.pop()
#                 if not matches(top,symbol):
#                     balance = False
#         index += 1
#     if balance and s.isEmpty():
#         return True
#     else:
#         return False
# def matches(open,close):
#     opens = '([{'
#     closes = ')]}'
#     return opens.index(open) == closes.index(close)
#
# print(parcheker('{{([][])}()}'))


#2.十、二进制数转换

# from pythonds.basic.stack import Stack
# def divideBy2(decNumber):
#     numStack = Stack()
#     while decNumber > 0:
#         num = decNumber % 2
#         numStack.push(num)
#         decNumber = decNumber // 2
#     string = ''
#     while not numStack.isEmpty():
#         string += str(numStack.pop())
#     return string
# print(divideBy2(89))

#十进制转换其他任意进制数
# from pythonds.basic.stack import Stack
# digitals = '0123456789ABCDEF'
# def divide_By_N(decNumber,n):
#     numStack = Stack()
#     while decNumber > 0:
#         num = decNumber % n
#         numStack.push(num)
#         decNumber = decNumber // n
#     string = ''
#     while not numStack.isEmpty():
#         string += digitals[numStack.pop()]
#     return string
# print(divide_By_N(890,16))


#中缀表达式转换后缀表达式
# from pythonds.basic.stack import Stack
# def infixTopostfix(infixexper):
#     prec = {}
#     prec['*'] = 3
#     prec['/'] = 3
#     prec['+'] = 2
#     prec['-'] = 2
#     prec['('] = 1
#     postfix_list = []
#     s = Stack()
#     tokenlist = infixexper.split()
#     for token in tokenlist:
#         if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789':
#             postfix_list.append(token)
#         elif token == '(':
#             s.push(token)
#         elif token == ')':
#             top = s.pop()
#             while top != '(':
#                 postfix_list.append(top)
#                 top = s.pop()
#         else:
#             while (not s.isEmpty()) and prec[s.peek()] >= prec[token]:
#                 postfix_list.append(s.pop())
#             s.push(token)
#     while not s.isEmpty():
#         postfix_list.append(s.pop())
#     return ''.join(postfix_list)
#
# print(infixTopostfix('( A + B ) * ( C + D )'))


#后缀表达式求值
# from pythonds.basic.stack import Stack
# def postfixequal(postfixexper):
#     opStack = Stack()
#     postfixlist = postfixexper.split()
#     for token in postfixlist:
#         if token in '0123456789':
#             opStack.push(int(token))
#         else:
#             opnum2 = opStack.pop()
#             opnum1 = opStack.pop()
#             res = domatch(token,opnum1,opnum2)
#             opStack.push(res)
#     return opStack.pop()
# def domatch(op,op1,op2):
#     if op == '+':
#         return op1 + op2
#     elif op == '-':
#         return op1 - op2
#     elif op == '*':
#         return op1 * op2
#     else:
#         return op1 // op2
# print(postfixequal('3 2 + 2 5 + * '))



#队列Queue及其应用
#热土豆问题
# from pythonds.basic.queue import Queue
# def hotpotato(namelist,num):
#     namequeue = Queue()
#     for name in namelist:
#         namequeue.enqueue(name)
#     while namequeue.size() > 1:
#         for i in range(num):
#             namequeue.enqueue(namequeue.dequeue())
#         namequeue.dequeue()
#     return namequeue.dequeue()
# print(hotpotato(['Bill','David','Susan','Jane','Kent','Brad'],7))




#打印机问题
# from pythonds.basic.queue import Queue
# import random
# class printer:
#     def __init__(self,ppm):
#         '''ppm:打印速度，单位 页/分 '''
#         self.pagerate = ppm
#         self.currenttask = None
#         self.timeRemaining = 0
#
#     def tick(self):
#         if self.currenttask != None:
#             self.timeRemaining -= 1
#             if self.timeRemaining <= 0:
#                 self.currenttask = None
#
#     def busy(self):
#         if self.currenttask == None:
#             return False
#         else:
#             return True
#
#     def startNext(self,newtask):
#         self.currenttask = newtask
#         self.timeRemaining = newtask.getpages() * 60/self.pagerate
#
# class Task:
#     def __init__(self,time):
#         self.timestamp = time
#         self.pages = random.randrange(1,21)
#
#     def getStamp(self):
#         return self.timestamp
#
#     def getpages(self):
#         return self.pages
#
#     def waittime(self,currenttime):
#         return currenttime - self.timestamp
#
# def newPrintTask():
#     num = random.randrange(1,181)
#     if num == 180:
#         return True
#     else:
#         return False
#
# def simulation(numseconds,pagesperminute):
#     labprinter = printer(pagesperminute)
#     printqueue = Queue()
#     waittingtimes = []
#     for currentSecond in range(numseconds):
#         if newPrintTask():
#             task = Task(currentSecond)
#             printqueue.enqueue(task)
#         if (not labprinter.busy()) and (not printqueue.isEmpty()):
#             nextTask = printqueue.dequeue()
#             waittingtimes.append(nextTask.waittime(currentSecond))
#             labprinter.startNext(nextTask)
#         labprinter.tick()
#     averrageWait = sum(waittingtimes)/len(waittingtimes)
#     print(f'Average wait {averrageWait:6.2f} secs and {printqueue.size():2d} tasks remaining.')
#
# for i in range(10):
#     simulation(3600,5)


# 双端队列
# 判断回文字符
# from collections import deque
# def palcheker(string):
#     chardeque = Deque()
#     for ch in string:
#         chardeque.addRear(ch)
#     flag = True
#     while chardeque.size() > 1 and flag == True:
#         first = chardeque.removeFront()
#         last = chardeque.removeRear()
#         if first != last:
#             flag = False
#     return flag
# print(palcheker('abcdcba'))
# print(palcheker('abcddcba'))


#链表
#实现节点
# class Node:
#     def __init__(self,initdata):
#         self.data = initdata
#         self.next = None
#     def getdata(self):
#         return self.data
#     def getnext(self):
#         return self.next
#     def setdata(self,newdata):
#         self.data = newdata
#     def setnext(self,newnext):
#         self.next = newnext
#     def add(self,item):
#         current = self.head
#         previous = None
#         stop = False
#         while current != None and not stop:
#             if current.getdata() > item:
#                 stop = True
#             else:
#                 current = current.getnext()
#                 previous = current
#         temp = Node(item)
#         if previous == None:
#             temp.setnext(self.head)
#             self.head = temp
#         else:
#             temp.setnext(current)
#             previous.setnext(temp)
#
#         temp = Node(item)
#         temp.setnext(self.head)
#         self.head = temp
#     def size(self):
#         current = self.head
#         count = 0
#         while current != None:
#             count += 1
#             current = current.getnext()
#         return count
#     def search(self,item):
#         current = self.head
#         found = False
#         while current != None and not found:
#             if current.getdata() == item:
#                 found = True
#             else:
#                 current = current.getnext()
#             return found
#     def remove(self,item):
#         current = self.head
#         previous = None
#         found = False
#         while not found:
#             if current.getdata() == item:
#                 found = True
#             else:
#                 previous = current
#                 current = current.getnext()
#         if previous == None:
#             self.head = current.getnext()
#         else:
#             previous.setnext(current.getnext())


#无序表
#链表
# class UnorderedList():
#     def __init__(self):
#         self.head = None
#
#     def add(self,item):
#        temp = Node(item)
#
# mylist = UnorderedList()
# print(mylist.head)
#
#

#递归——海龟图
# import turtle
# t = turtle.Turtle()
# def drawing(t,linelenth):
#     if linelenth > 0:
#         t.forward(linelenth)
#         t.right(90)
#         drawing(t,linelenth - 5)
# drawing(t,100)
# turtle.done()


#二叉树
# import turtle
# def tree(branch_len):
#     if branch_len > 5:
#         t.forward(branch_len)
#         t.right(20)
#         tree(branch_len - 15)
#         t.left(40)
#         tree(branch_len -15)
#         t.right(20)
#         t.backward(branch_len)
# t = turtle.Turtle()
# t.left(90)
# t.penup()
# t.backward(100)
# t.pendown()
# t.pencolor('green')
# t.pensize(2)
# tree(75)
# t.hideturtle()
# turtle.done()

#谢尔宾斯基三角形
import turtle
t = turtle.Turtle()
def sierpinski(degree,points):
    colormap = ['blue','red','green','white','yellow','orange']
    drawTriangle(points,colormap[degree])
    if degree > 0:
        sierpinski(degree - 1,
                   {'left':points['left'],
                    'top':getmid(points['left'],points['top']),
                    'right':getmid(points['left'],points['right'])})
        sierpinski(degree - 1,
                   {'left': getmid(points['left'],points['top']),
                    'top': points['top'],
                    'right': getmid(points['top'], points['right'])})
        sierpinski(degree - 1,
                   {'left': getmid(points['left'], points['right']),
                    'top': getmid(points['top'],points['right']),
                    'right': points['right']})
def drawTriangle(points,color):
    t.fillcolor(color)
    t.penup()
    t.goto(points['top'])
    t.pendown()
    t.begin_fill()
    t.goto(points['left'])
    t.goto(points['right'])
    t.goto(points['top'])
    t.end_fill()
def getmid(p1,p2):
    return ((p1[0] + p2[0]) /2 , (p1[1] + p2[1]) /2)
points = {'left':(-200,-100),'top':(0,200),'right':(200,-100)}
sierpinski(5,points)
turtle.done()

