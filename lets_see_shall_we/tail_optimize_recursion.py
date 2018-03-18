"""Modified Py3.4 and extendable version of the ActiveState recipe"""

from sys import _getframe, argv
from .pudding import proof


class TailRecurseException(Exception):
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs


def _compare_code_objects(frame, prev=2):
    f_back = frame
    if prev % 2: raise RuntimeError("prev must be multiple of 2")
    for i in range(0, prev, 2):
        if f_back.f_back and f_back.f_back.f_back:
            f_back = f_back.f_back.f_back
        else:
            break
    return frame.f_code == f_back.f_code


def tail_call_optimized(g):
    """
    This function decorates a function with tail call
    optimization. It does this by throwing an exception
    if it is it's own grandparent, and catching such
    exceptions to fake the tail call optimization.

    This function fails if the decorated
    function recurses in a non-tail context.
    """

    def func(*args, **kwargs):
        frame = _getframe()
        if _compare_code_objects(frame, 4):
            raise TailRecurseException(args, kwargs)
        else:
            while True:
                try:
                    return g(*args, **kwargs)
                except TailRecurseException as e:
                    args = e.args
                    kwargs = e.kwargs

    func.__doc__ = g.__doc__
    return func


@tail_call_optimized
def factorial(n, acc=1):
    proof()
    if n == 0:
        return acc
    print(acc)
    return factorial(n - 1, n * acc)


if __name__ == '__main__':
    print(factorial(int(argv[-1])))
    print("This is a unique combination of recursion and iteration.\n"
          "We recurse a few times, specifically, we call our function, \n"
          "then attempt doing so until we reach prev calls, then cut off \n"
          "our frame shortly via blowing up cand catching our explosion far\n"
          "below the default recursion limit to copy our new args\n"
          "and recurse again for a few times. It would be interesting\n"
          "to do some testing and find the best optimization of recursion\n"
          "calls to jumps back to the beginning of a loop by playing\n"
          "around with `_compare_code_objects` prev count. Any multiple of 2\n"
          "that is higher than 0 will do, however the input size needs to be\n"
          "checked as well, such that we get a 3d result out of some function\n"
          "of both N and M, which, due to the nature of the splits, is a step function\n"
          "in the axis of N or M depending on which metric you are testing")