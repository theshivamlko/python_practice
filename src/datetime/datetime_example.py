
import  datetime as dt


now= dt.datetime.now()
print(now)

print(dt.datetime.__format__(now, "%Y-%m-%d %H:%M:%S"))

dob=dt.datetime(year=1992,month=12,day=20,hour=13,minute=35,second=12)
print(dob)
print(dt.datetime.__format__(dob, "%d-%m-%Y"))

