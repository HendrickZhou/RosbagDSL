# python3.7
import rosbag
 

class _Register:
    """
    singleton object
    register for all pipe agent and function call
    register(str_literal) -> run_all[pre_check(bag, topic) -> get bag iter and start loop
    -> check msg on the fly]
    """
    registration = []

    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        # run for all registration

    def register(self, pipe_node):
        # mapping msg to pipe, without checking legality


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
def save(*args):
    '''
    main entry for the operation
    :return:
    '''
    target_msg
    deeandency_msg_signature
    # additively register the bag, topic, msg info, pipe we need
    registry.register()
    # compile corresponding pipe function
    # pre-loop checking(if exist, if on the same topic) and recovery

    # create mapping relationship, give the variable to pipe operand


