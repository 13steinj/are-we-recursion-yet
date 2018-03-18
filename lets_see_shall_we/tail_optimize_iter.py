from .pudding import proof
from sys import argv

class Recurse(Exception):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs


def recurse(*args, **kwargs):
    raise Recurse(*args, **kwargs)


def tail_recursive(f):
    def decorated(*args, **kwargs):
        while True:
            try:
                return f(*args, **kwargs)
            except Recurse as r:
                args = r.args
                kwargs = r.kwargs
                continue

    return decorated

@tail_recursive
def factorial(n, accumulator=1):
    proof()
    if n == 0:
        return accumulator
    recurse(n-1, accumulator=accumulator*n)

if __name__ == '__main__':
    factorial(int(argv[-1]))
    print("This isn't recursion whatsoever, it is iteration,\n"
          "that is trying very hard to pretend it is recursion\n."
          "after calling our function once from the top stack,\n"
          "we enter a frame defined by the manager for our iteration,\n",
          "so while we are indeed calling our function and code multiple times\n",
          "the previous state is completely forgotten, so this isn't recursion")