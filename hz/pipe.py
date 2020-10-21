#
#

class Pipe(object):
    """
    decorator for code executed each frame

    Concept Frame:
    ----------------------
    This implies to each timestamp with a message entity in the bag

    Class Var:
    ______________________
    raw_registry: keep record

    Instance Var:
    ______________________
    func

    Interface:
    ______________________
    meta_func:
        user end: "decro_func.meta_func(msg1, msg2)"

    """
    raw_registry = {}

    def __init__(self, node_func):
        self.raw_registry[node_func.__name__] = node_func
        # self.raw_func_body = node_func
        self.func = LoopMetaFunction(node_func)

    def __call__(self, *args, **kwargs):
        # parsing and modifying funcion code
        # saving some registor variable
        # regist this computation meta to global machine

        # Throw warning if used as normal decorator call!
        print("Pipe decorator is grammar for the hz meta computation operation, ",
              "it should not be used as normal decorater!")

    @property
    def meta_func(self):
        return self.func

    @meta_func.setter
    def meta_func(self, anything):
        print("setting ignored")


class LoopMetaFunction:
    """
    object to store raw code and compiled code

    Instance Var
    ________________________
    exec_code: should be a code object:
    ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__',
    '__hash__', '__init__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
     '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'co_argcount', 'co_cellvars', 'co_code', 'co_consts',
     'co_filename', 'co_firstlineno', 'co_flags', 'co_freevars', 'co_kwonlyargcount', 'co_lnotab', 'co_name',
     'co_names', 'co_nlocals', 'co_stacksize', 'co_varnames']

    """
    def __init__(self, func_obj):
        self.raw_code = func_obj

    def compile(self):
        # turn raw code into executable
        code = self.raw_code
        return "pass"

    def __call__(self, *args, **kwargs):
        # lazy compile
        self.exec_code = self.compile(self.raw_code)
        # add args to exec_code function closures
        exec(self.exec_code)
