#字典（键-值）
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
alien_0['position'] = 0
print(alien_0)
alien_0['position'] = 100
print(alien_0)
del alien_0['position']
print(alien_0)
#遍历字典
for key, value in alien_0.items():
    print(key,value)
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
#遍历键
if 'erin' not in favorite_languages.keys():
    print('erin not in'.title())
#顺序返回
for name in sorted(favorite_languages.keys()):
    print(name.title())
#遍历值
for language in favorite_languages.values():
    print(language.title())
for language in set(favorite_languages.values()):
    print(language.title())