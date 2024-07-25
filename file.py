
file=open("temp.txt")
print(file)

contents=file.read()
print(contents)
file.close() # manually close


with open("config.json") as fileJson: # auto close after read
    contentsJson=fileJson.read()
    print(contentsJson)
    