from sympy import *
from sympy.abc import *
from random import *
filters = ["import", "open", "__", "eval", "exec", "\\", "dir", "sleep", 'add', 'class', 'contains', 'system', 'exit', 'calc', 'ans',
           'delattr', 'dir', 'doc', 'eq', 'format', 'getattribute', 'getitem',
           'getnewargs', 'gt', 'hash', 'init', 'init_subclass', 'iter',
           'len', 'lt', 'mod', 'mul', 'new',
           'reduce', 'repr',
           'rmod', 'rmul', 'setattr', 'sizeof', 'str', 'subclasshook', 'capitalize', 'casefold',
           'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha',
           'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper',
           'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit',
           'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']


def calc(str_):
    for filter in filters:
        if filter in str_:
            print(filter)
            return "别想注入！"
    print(str_)
    str_ = str_.replace("&#91;", "[")
    str_ = str_.replace("&#93;", "]")
    ans_ = str(eval(str_))
    # print(ans_)
    if len(ans_) > 150:
        return "我会写，但这里地方太小，写不下"
    return str(eval(str_))
