# class _MsgObjMeta(object):
#     def __new__(cls, *args, **kwargs):
#         cls.__slots__ = []

#    This one doesn't interact with bag infomatin itself, if exception happens in parsing,
#    _MsgObj is just None, but itself wont' cause Exception
class _MsgObj:
    '''
    This is not a user accessible class
    this interact directly with resgister running process
    lazy checking

    * probably inherit from rosbag message in the future
    * writing to msg is not supported now
    '''
    def __init__(self, ros_msg, signature):
        """
        :param signature: list of string
        """
        self.ros_msg = ros_msg
        self.signature = signature
        self.msg_obj = self._get_attr(self.ros_msg, self.signature)
        self.bag = DTree().bag
        self.topic = DTree().topic
        self.msg_raw = DTree().msg_raw

    @staticmethod
    def _get_attr(msg, signature):
        # TODO add exception handling
        for sig in signature:
            msg = msg.__getattr__[sig]
        return msg

    def __getattr__(self, item):
        """
        overriding the original dot operation
        :param item:
        :return:
        """
        pass