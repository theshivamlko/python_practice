
file=open("./temp.txt")
print(file)
contents=file.read()
print(contents)
file.close() # manually close

file2=open("temp.txt",mode="a")
for i in range(10):
    file2.write(f"{i}. YO\n")
#file2.append("\n======")


with open("config.json") as fileJson: # auto close after read
    contentsJson=fileJson.read()
    print(contentsJson)
    print(type(contentsJson))
    
    
    