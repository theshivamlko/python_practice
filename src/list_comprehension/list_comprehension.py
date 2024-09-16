from numpy.ma.core import count

list=[]
for i in range(10):
    list.append(i)
print(list)

# item is the value being manipulated and then add 1 by 1
list2= [item for item in list]
print(list2)

# comprehension with condition
list2= [item for item in list if item%2==0]
print(list2)


dict={"A":[1,2,3],"B":[4,5,6],"C":[7,8,9,10]}

newDict = {k:v for (k,v) in dict.items()  if count(v)>3}
print(newDict)

newDict = {k:v for (k,v) in dict.items()  if {v1 for v1 in v  if v1%5==0}}
print(newDict)

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {k:((v * 9/5) + 32) for (k,v) in weather_c.items()}

print(weather_f)


