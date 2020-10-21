# python3.7
#
# dot-tree syntax support
#

class DTree:
    '''
    instance var:
    ------------------
    str_literal
    '''
    def __init__(self, str_literal=None):
        self.str_literal = str_literal

    def parse(self, *args):
        # check xpath overhead
        if self.str_literal[:2] == "x:":
            pass

        # parse and save to slot signature
        _components = self.str_literal.split('.')
        return _components

# class Parser(DTree):
#     """
#     this class return the definite correct signature for msg path
#     exception handling and checking here
#     """
#     def __init__(self, str_literal, bag_context):
#         super(Parser, self).__init__(str_literal)
#
#     def parse(self, *args):
