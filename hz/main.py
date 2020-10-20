# python3.7


class Pipe:
    """
    decorator for code executed each frame

    Concept Frame:
    ----------------------
    This implies to each timestamp with a message entity in the bag

    Instance Var:
    ______________________
    signatures

    """

    def __init__(self, node_func):
        self.func = node_func

    def __call__(self, *args, **kwargs):
        # parsing and modifying funcion code
        # saving some registor variable
        # regist this computation meta to global machine
        self.func()

    # return a function object
    def _translate(self):
        pass
 

class _Register:
    '''
    singleton object
    register for all pipe agent
    '''
    registration = []
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        # run for all registration


    def register(self, pipe_node):
        self.registration.append(pipe_node)

    def run_all(self):
        # iter1 = iter of bag one
        while True:
            topic, msg, timestamp = iter1.next()
            for msg_data in all_required_msg_from_pipe:
                real_msg_data.append(_MsgObj(msg_data))

            if topic correct and msg correct
                result = exec(pipe.function(), param1, param2)
                result_container.append(result)




class _MsgObjMeta(object):
    def __new__(cls, *args, **kwargs):
        cls.__slots__ = []

class _MsgObj(metaclass=_MsgObjMeta):
    '''
    This Class are design to be standalone msg object for python user
    If they only use this object, they're using it as a wrapper for message
    '''
    def __init__(self):
        pass

    @staticmethod
    def _get_attr(signature):
        for sig in signature:
            pass

    def __getitem__(self, item):
        '''
        overriding the original dot operation
        :param item:
        :return:
        '''
        pass

"""
interface
"""
def save():
    pass

