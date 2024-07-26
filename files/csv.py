import pandas


with open("weather_data.csv") as csvFile:
    list = csvFile.readlines()
    print(type(list))
    for row in list:
        print(f"{row} => {row[0]}")
        

pandas.read_csv("weather_data.csv")










        