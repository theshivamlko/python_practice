
try:
    str="Hello"
    print(str[5])

except IndexError as e1:
    print("IndexError ",e1)
except Exception as e2:
    print("Exception",e2)
else: # if no exception in try block
    print("No Exception", len(str))
finally:
    print("Run anyway")
    raise KeyError("Intensional dev exception") # throw exception

