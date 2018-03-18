from collections import OrderedDict
from inspect import stack
import pprint

def proof():
    # let's break down what's going on here. Firstly, the stack returns
    # frame records, which are:
    # tuple (frame object, filename, current_line_no, function name,
    #        context_lines, context_lines.index(current_line))
    # Secondly, we cut off the first two frames from stack() via [2:].
    # This is because they will always be the frame of this function,
    # up to this line and the frame defined as "up to the call of the
    # function which controls this frame", so, the frame of the next
    # line and the frame of proof. We don't care about those. Second,
    # all modules in this package are meant to be called via
    # `python3 -m lets_see_shall_we.module n`, n being the the n we want
    # to get n! for. which means the last two frames are the frames to
    # run the module given it's globals and the module as if it's the
    # top level env, we don't care about those, and slice them off via [:-2].
    #
    # Now down to dealing with frames. In Python frames aren't generally reused,
    # and in that sense they don't give a good sense of detecting recursion.
    # But, we have access to the code object of the frame. While it's repr is
    # ugly and hard to read, we just need it's location in memory. We also
    # want to differentiate the module record from the rest of the stack
    readable_stack = stack()[2:-2]
    readable_stack = [(frame_tuple[0], id(frame_tuple[0].f_code))
                      for frame_tuple in readable_stack]
    module_record = readable_stack and readable_stack.pop() or None
    pprint.pprint(OrderedDict(top=module_record, stack=readable_stack))
