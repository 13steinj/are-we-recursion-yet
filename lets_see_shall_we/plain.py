from .pudding import proof
from sys import argv

def factorial(n, prev=1):
    proof()
    if n == 0:
        return prev
    return factorial(n - 1, n * prev)

if __name__== '__main__':
    factorial(int(argv[-1]))
    print("This is actual recursion.\n"
          "we directly call again and again until\n"
          "we reach a terminating condition.")