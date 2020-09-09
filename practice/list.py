list = ['sa','SA','bs','ca','da']
#结尾添加元素
list.append('sama')
print(list)
#插入元素
list.insert(1,'insert')
print(list)
#删除元素（不使用）
del list[1]
print(list)
#删除最后元素（可以使用）
elm = list.pop()
print(elm)
print(list)
#删除指定元素
list.move('sama')
print(list)
#排序（永久），reverse = True 反向排序
list.sort(reverse = True)
print(list)
#排序（临时）
print(sorted(list))
print(list)
#反转列表排序
list.reverse()
print(list)
#列表长度
print(len(list))