# python3.5
#
import types
import ast
import inspect
from astunparse import unparse


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
        self.topic_scope = None
        self.func = _LoopMetaFunction(node_func)

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


class _LoopMetaFunction:
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
        self.raw_func = func_obj
        self.name = None

        self.exec_code = None

        self.local_vars = None
        self.topic_vars = None
        self.extra_vars = None
        self.register_vars = None

    def compile(self):
        # turn raw code into executable

        # legal_code_obj = types.CodeType(
        # )
        self.name = self.raw_func.__qualname__

        co_literal = inspect.getsource(self.raw_func)
        co_literal = co_literal[len("@Pipe\n"):]
        _ast = ast.parse(co_literal)
        # TODO enforce the grammar check
        reg_var_list = []
        for elt in _ast.body[0].body[0].value.elts: # TODO more generic place
            reg_var_list.append(_RegVar(elt.id))
        self.register_vars = tuple(reg_var_list)

        # TODO handle the reg variable

        # get topic_vars and extra_vars mapping
        names_map = dict()
        topic_var_list = []
        extra_var_list = []
        for arg_obj in _ast.body[0].args.args:
            topic_var_list.append(arg_obj.arg)
        self.topic_vars = topic_var_list # can't make it tuple if ctx assign exists
        for kw_obj in _ast.body[0].args.kwonlyargs:
            extra_var_list.append(kw_obj.arg)
        self.extra_vars = extra_var_list

        for i, name in enumerate(self.topic_vars):
            names_map[name] = (i, "topic_vars")

        for i, name in enumerate(self.extra_vars):
            names_map[name] = (i, "extra_vars")

        new_ast = ast.fix_missing_locations(ASTModifier(names_map).visit(_ast))
        new_ast = ast.fix_missing_locations(RemoveFuncDef().visit(new_ast))
        import pdb; pdb.set_trace()
        self.exec_code = unparse(new_ast)
        import pdb; pdb.set_trace()

    def __call__(self, *args, **kwargs):
        # lazy compile?
        # self.exec_code = self.compile(self.raw_code)
        # add args to exec_code function closures
        exec(self.exec_code)


class RemoveArgsList(ast.NodeTransformer):
    def visit_arguments(self, node):
        # empty the argument list, add self to the list
        node.args = [ast.arg(arg="self", annotation=None)]
        node.kwonlyargs = []
        return node


class RemoveFuncDef(ast.NodeTransformer):
    def visit_Module(self, node):
        node.body = node.body[0].body
        return node
    # def visit_FunctionDef(self, node):
    #     # TODO: need to make sure that user_defined func exist??
    #     # if is the top level func:
    #     func_body = node.body
    #     return ast.copy_location(func_body, node)


class RemoveRegDef(ast.NodeTransformer):
    def visit_Expr(self, node):
        # find the pattern that is a register expression: Expr(Set)
        if type(node.value) is ast.Set:
            return None
        else:
            return node


class ReplaceVar(ast.NodeTransformer):
    """
    target_names should be topic_vars and extra_vars, Sequence
    """
    def __init__(self, names_map):
        self.names_map = names_map
        super().__init__()

    def visit_Name(self, node):
        if node.id in self.names_map:
            return ast.Subscript(
                value=ast.Attribute(
                    value=ast.Name(id="self", ctx=ast.Load()),
                    attr=self.names_map[node.id][1],
                    ctx=ast.Load()
                ),
                slice=ast.Index(value=ast.Num(n=self.names_map[node.id][0])),
                ctx=node.ctx  # now it supports assignment
            )
        else:
            return node


class ASTModifier(RemoveRegDef, ReplaceVar):
    """
    In-place ast modification
    """
    def __init__(self, names_map):
        super().__init__(names_map)


class _RegVar:
    def __init__(self, name):
        self.name = name
        self._notset = True
        self._default = None

    @property
    def notset(self):
        return self._notset

    @notset.setter
    def notset(self, ns):
        self._notset = ns

    @property
    def default(self):
        return self._default

    @default.setter
    def default(self, df):
        self._default = df
