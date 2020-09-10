import json
import pygal
import math
from itertools import groupby

with open('btc_close_2017.json') as f:
    btc_data = json.load(f)
# 创建5个列表，分别存储日期和收盘价

dates = []
months = []
weeks = []
weekdays = []
close = []

# 每一天的消息
for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))


def draw_line(x_data, y_data, title, y_legend):
    xy_map = []
    for x, y in groupby(sorted(zip(x_data,y_data)), key=lambda _: _[0]):
        y_list = [v for _, v in y]
        xy_map.append([x, sum(y_list) / len(y_list)])
    x_unique, y_mean = [*zip(*xy_map)]
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend, y_mean)
    line_chart.render_to_file(title + '.svg')
    return line_chart

idx_week = dates.index('2017-12-11')
wd = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekdays_int = [wd.index(w) + 1 for w in weekdays[1:idx_week]]
line_char_weekday = draw_line(weekdays_int, close[1:idx_week], '收盘价星期均值', '星期均值')
line_char_weekday.x_labels = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
line_char_weekday.render_to_file('收盘价星期均值（¥）.svg')

with open('收盘价Dashboard.html', 'w', encoding='utf8') as html_file:
    html_file.write('<html><head><title>收盘价Dashboard</title><meta charset="utf-8></head><body>\n')
    for svg in [
        '收盘价折线图（¥）.svg','收盘价对数变换折线图（¥）.svg','收盘价月日平均.svg',
        '收盘价周日平均.svg','收盘价星期均值（¥）.svg'
    ]:
        html_file.write('   <object type="image/svg+xml" data="{0}" height=500></object>\n'
                        .format(svg))
        html_file.write('</body></html>')