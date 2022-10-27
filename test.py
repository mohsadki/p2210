#coding:utf-8
from inspect import stack
import json


i = 0;
while i < 10:
    print ("Hi World !",i)
    i=i+1
print(list(range(1,10,2)))

stack =[3,2,4,5]
stack.append(10)
print(stack)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack)
json.dumps(stack)