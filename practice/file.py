with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
#写入文件
with open('pi_digits.txt','w') as file_object:
    file_object.write("I love programing13.\n")
    file_object.write("I love programing144.\n")
#附加模式a
with open('pi_digits.txt','a') as file_object:
    file_object.write(r"I love programing12222222222.\n")
name = ''

while name != 'q':
    name = input("输入姓名")
    with open('pi_digits.txt', 'a') as file_object:
        file_object.write(name + '\n')