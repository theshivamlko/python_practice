import tkinter


class Car:
    def __init__(self,**kargs):
        self.make=kargs["make"]
        self.model=kargs.get("model") # return None if key not found

window=tkinter.Tk()
window.title("*args and **kawrgs")
window.minsize(width=400, height=400)


myLabel=tkinter.Label(window, text="Hello World",font=("OpenSans",24), fg="red", bg="white")
myLabel.pack(side="left") # pack labels onto screen


def myFunc(a ,b=2,c=3):
    print(a,b,c)


myFunc(1)
myFunc(a=10,c=1)


def myArgFunc(*args):
    print(args)
    print(args[0])
    print(type(args))
    for arg in args:
        print(arg,type(arg))

myArgFunc(1,[1,2])

def myKArgFunc(n,**kargs):
    print(kargs)
    print(type(kargs))
    print(kargs["add"])
    for key in kargs:
        print(key,kargs[key])

myKArgFunc( add=1,sub=2,divide=3,n=1)
myKArgFunc(1, add=1,sub=2,divide=3) # both are same

car =Car(make="Nissan")
print("car",car,car.make,car.model)

window.mainloop()


