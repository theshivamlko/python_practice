import pandas as pd
 


with open("weather_data.csv") as csvFile:
    list = csvFile.readlines()
    print(type(list))
    for row in list:
        print(f"{row} => {row[0]}")
        

data1=pd.read_csv("weather_data.csv")
print("============")
print(data1)
print(data1["temp"])
print(type(data1))
print(type(data1["temp"]))

dataDict=data1.to_dict();
print(dataDict)
print(dataDict["day"][1])
print(data1["day"].to_list())












        