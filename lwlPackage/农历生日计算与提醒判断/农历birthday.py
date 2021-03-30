# borax==3.3.1

from borax.calendars.lunardate import LunarDate
from 农历生日计算与提醒判断 import facade

list = [
    '12-26', # 农历生日
]

# 获取今天的农历日期
today = LunarDate.today()
today_string = today.strftime('%m-%d')

year = today.year
month = today.month
day = today.day

for i in list:
    i = i.split('-')
    tmpMonth = int(i[0])
    tmpDay = int(i[1])
    tmpNow = LunarDate(year, tmpMonth, tmpDay)
    # print(tmpNow)
    dis = today - tmpNow
    dis = dis.days
    message = None
    if  dis == 0:
        message = '今天'
    elif dis == -1:
        message = '明天'
    elif dis == -2:
        message = '后天'
    elif dis == -3:
        message = '大后天'


    # 若在范围内
    if message:
        facade.update(message, flag= True)
        # 转化为公历
        solarDay = tmpNow.to_solar_date()

    else:
        facade.update(message='该生日今天不需要通知')

