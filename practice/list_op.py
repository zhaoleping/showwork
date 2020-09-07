#列表循环
magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician)
#range
for value in range(1,5):
    print(value)
num = list(range(1,5))
print(num)
num = list(range(1,11,2))
print(num)
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)
#简单统计计算
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))
#列表解析
squares = [value**3 + 2 for value in range(1,11)]
print(squares)
#列表切片
players = ['charles','martina','michael','florence','eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])
for player in players[-3:]:
    print(player)
#复制列表
group = players[:]
group.append('aaa')
players.append('bbb')
print(players)
