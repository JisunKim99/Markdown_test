import datetime as dt

someday = dt.datetime(2018, 8, 30, 13, 26, 55)

print(someday.strftime('%y/%m/%d %H:%M:%S'))

date_str = '2017년 02월 01일 14시 33분'
oldday = dt.datetime.strptime(date_str, '%Y년 %m월 %d일 %H시 %M분')
print(oldday.strftime('%y/%m/%d %H:%M:%S'))

change_date = oldday.replace(year=2018, day=16, hour=15)
print(change_date.strftime('%y/%m/%d %H:%M:%S'))

d = dt.date(2017, 4, 15)
t = dt.time(12, 23, 38)

print(d)
print(t)

result = dt.datetime.combine(d, t)
print(result)






