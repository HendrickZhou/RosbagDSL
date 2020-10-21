# python3.7
import inspect
from typing import List, Callable, Any
from collections import namedtuple
import rosbag
from .pipe import Pipe
from .msg import _MsgObj


class _Task:
    __slots__ = "meta_func", "call_mapping", "extra_args"

class _Register:
    """
    singleton object
    register for all pipe agent and function call
    register(str_literal) -> run_all[pre_check(bag, topic) -> get bag iter and start loop
    -> check msg on the fly]
    """
    registration = []

    def __init__(self):
        self.support_msgs = []
        self.extra_args = []

    def __call__(self, *args, **kwargs):
        # run for all registration

    def register(self, pipe_node: Callable, support_msgs: List[str], extra_args: List[Any]):
        for msg in support_msgs:
            self.support_msgs.append(_MsgObj(msg))
        # TODO checking topics
        self.extra_args = extra_args
        pipe_node_sig = list(inspect.signature(Pipe.raw_registry[pipe_node.__name__]).parameters)


        # mapping msg to pipe, without checking legality
        # checking if msg belongs to the same topic
        # and split into pipe based registration
        t = _Task()
        t.meta_func = pipe_node.__name__
        if len(pipe_node_sig) != len(support_msgs)+len(extra_args):
            raise Exception("pipe signature doesn't match with save")
        else:
            t.call_mapping = {a:b for a,b in zip(pipe_node_sig ,self.support_msgs)}
            t.extra_args = {a:b for a,b in zip(pipe_node_sig[len(self.support_msgs):], self.extra_args)}
        self.registration.append(t)


    def _pre_check(self):
        # check bag exists
        # check topic exist
        bag_context = rosbag.Bag(bag_name, 'r').__enter__()

    def run_all(self):
        # checking
        self._pre_check()

        bag_iter = self.bag_context.read_messages()

        while True:
            topic, msg, timestamp = iter1.next()
            for msg_data in all_required_msg_from_pipe:
                real_msg_data.append(_MsgObj(msg_data))

            if topic correct and msg correct
                result = exec(pipe.function(), param1, param2)
                result_container.append(result)


"""
interface & shortcut
"""
registry = _Register()
def save(pipe_node, msgs, args):
    '''
    main entry for the operation
    :return:
    '''
    # checking save call signature


    # additively register the bag, topic, msg info, pipe we need
    registry.register(pipe_node, msgs, args)
    # compile corresponding pipe function
    # pre-loop checking(if exist, if on the same topic) and recovery

    # create mapping relationship, give the variable to pipe operand


