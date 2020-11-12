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
        return m3 * t2 -1, t2
    else:
        # each return tuple/name size must match, or grammar mistake prompts
        return t2 - a - args, None # None means it's not in array, otherwise use default value 0

# f = filter.meta_func
print(filter.meta_func([1,2,1], [1]))
print(filter.meta_func([12,2,3], [1]))

"""
This piece of code should be compiled into string like this:
--- exec_code
a = 1
if self.topic_vars[0] > self.extra_vars[0]:
    # return self.topic_vars[0] * self.topic_vars[2].value * a
    self.result = (self.topic_vars[0] * self.topic_vars[2].value * a)
else:
    # return self.topic_vars[1] - 1
    self.result_data = (self.topic_vars[1] -1)
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
    # data = meta(self.support_msgs, self.extra_args)
    
    container.append(data)
"""
