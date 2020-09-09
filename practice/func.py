#带默认值形参必须在不带默认值的形参后面
#function_name(list_name):会修改列表list_name内部内容
#function_name(list_name[:]):保留原来列表
magicians = ['allin', 'ada', 'yuki']
def show_magicians(magicians):
    for magician in magicians:
        print(magician)
def make_great(magicians):
    i = 0
    while i < len(magicians):
        magicians[i] = 'the Great ' + magicians[i]
        i += 1
    return magicians
show_magicians(make_great(magicians[:]))
show_magicians(magicians)
#未知数量实参*arg
#def function_name(*arg)
#def function_name(known_arg, *arg)

#任意数量关键字实参
def build_profile(first,last,**user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('albert', 'einstein', location = 'princeton', field = 'physics')
print(user_profile)
