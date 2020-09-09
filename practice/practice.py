from _collections import OrderedDict
favorite_language = {}
favorite_language['1'] = 1123
favorite_language['4'] = 1121
favorite_language['3'] = 1125
for key,value in favorite_language.items():
    print(key,value)
list1 = ['text', 'rowA', 'colA']
list2 = ['text', 'rowA', 'colB']
list3 = ['file', 'rowA', 'colC']


class ret_parent():
    """JSON输出"""
    def __init__(self,str):
        self.str = str

    def get_parent(self):
        obj = {}
        self.str[0]






def ret_parent(full_list):
    result = {}
    result['label'] = full_list[0]
    if len(full_list[1:]) >= 1:
        result['children'] = ret_parent(full_list[1:])
    return result

result = ret_parent(list1)


print(ret_parent(list1))