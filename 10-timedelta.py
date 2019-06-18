import datetime as dt

dt1 = dt.datetime.now()
dt2 = dt.datetime(dt1.year+1, 1, 1, 0, 0, 0)

dt = dt2 - dt1
print(dt)

print(dt.days)
print(dt.seconds)
print('올해는 %d일 남았습니다.' % dt.days)

result = dt.total_seconds()
print(result)

now_time = dt.datetime.now()

d = dt.timedelta(days=100, seconds=3600)
after_time = now_time + d
print(after_time.strftime('%Y-%m-%d %H:%M:%S'))




