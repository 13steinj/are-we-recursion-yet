from .pudding import proof
from sys import argv

def factorial(n):
    result = 1
    for multiple in range(n, 0, -1):
        proof()
        result *= multiple
    proof()
    return result


if __name__== '__main__':
    factorial(int(argv[-1]))
    print("This isn't recursion whatsoever, it is iteration.\n"
          "after calling our function once from the top stack,"
          "we never enter another frame, which implies we never\n"
          "execute the same code again")