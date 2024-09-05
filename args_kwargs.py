def myFun(*args, **kwargs):
    print("args:", args)
    print("kwargs", kwargs)


myFun('hello', 'hi', 'there', first='hello', second='hi', last='there')