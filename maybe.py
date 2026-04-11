def decorator(func):
    def wrapper(*args):
        print('Hi')
        func(*args)
        print("Bye")
    return wrapper

@decorator
def add(a, b):
    print(a + b)

add(3, 9)


