def hello_decorator(func):
    def inner1():
        print("Hello, this is before function execution")

        func()

        print("Hello, this is after function execution")

    return inner1


@hello_decorator
def function_to_be_used():
    print("This is inside the function!!!")


function_to_be_used()