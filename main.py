def add(a,b):
    return a+b

def divide(a,b):
    raise ValueError("Cannot divide by zero") #raise an error if b is zero
    return a/b