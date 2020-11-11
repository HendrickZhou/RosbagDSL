from pipe import Pipe

# @Pipe
# def compute(m1, *, extra_arg):
#     {reg1}
#     a = 1
#     return m1

@Pipe
def filter(m3, t1, t2, *, args):
    {reg1, reg2}
    a = 1
    if m3 > t1:
        return m3 * t2 -1
    else:
        return t2 - a
filter.meta_func.compile()

"""
This piece of code should be compiled into string like this:
--- exec_code
a = 1
if topic_vars[0] > extra_vars[0]:
    return topic_vars[0] * topic_vars[2].value * a
else:
    return topic_vars[1] - 1
--- topic_vars
(m1, m2, m3) -> _MsgObj
--- extra_vars
(arg1) -> Any
--- register_vars
(reg1:{"notset":True, "default":None}) -> dict-like
--- local_vars
not for now
--

in the while loop(topic mapping is done)
while:
    ...
    ...
    # find meta for corresponding topic: meta = pipe_node.meta_func
    data = meta(m1, m2, m3, extra_arg)
    
    container.append(data)
"""
