
def do_stuff(stuff: str):
    """Print provided stuff to console.
    Params:
        stuff(str): stuff to print

    """
    print(stuff)
    a = 25
    b = 30
    print(f"Sum: {addition(a,b)}")

def addition (x,y):
    num = sum(x,y)
    a = num * x * y
    num = a
    return num



