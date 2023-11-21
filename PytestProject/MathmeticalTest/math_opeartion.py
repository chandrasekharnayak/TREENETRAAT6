d
ef add(x,y):
    return x+y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y == 0:
        raise ZeroDivisionError('Cannot divide')
    return x/y

# print(3/3)