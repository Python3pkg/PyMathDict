# Reference: https://docs.python.org/2/reference/datamodel.html
# Reference: https://docs.python.org/2/library/operator.html

from __future__ import division
from collections import Mapping
from copy import deepcopy
from Helpy.SymPy import sympy_allclose
from frozendict import frozendict
from itertools import product
from operator import index, pos, neg, abs, lt, le, eq, ne, ge, gt, add, sub, mul, div, truediv, floordiv, mod, pow, xor
from pprint import pprint
from sympy import exp as e, log as ln, sqrt as square_root


class MathDict(Mapping):
    def __init__(self, *args, **kwargs):
        self.__Mapping = dict(*args, **kwargs)
        self.__Hash = None

    def __repr__(self):
        return '<MathDict %s>' % repr(self.__Mapping)

    def __len__(self):
        return len(self.__Mapping)

    def __iter__(self):
        return iter(self.__Mapping)

    def __getitem__(self, k):
        return self.__Mapping[k]

    def __setitem__(self, k, v):
        self.__Mapping[k] = v

    def __delitem__(self, k):
        del self.__Mapping[k]

    def __contains__(self, item):
        return item in self.__Mapping

    def __hash__(self):
        if self.__Hash is None:
            self.__Hash = reduce(xor, map(hash, self.iteritems()), 0)
        return self.__Hash

    # __call__: simply return __dict
    def __call__(self):
        return self.__Mapping

    def copy(self, deep=True):
        if deep:
            return MathDict(deepcopy(self.__Mapping))
        else:
            return MathDict(self.__Mapping.copy())

    def update(self, *args, **kwargs):
        self.__Mapping.update(*args, **kwargs)

    def __op__(self, op=mul, other=None, __r=False, **kwargs):
        if hasattr(other, 'keys'):
            __mapping = {}
            for item_0, item_1 in product(self.items(), other.items()):
                vars_and_values_0___frozen_dict, func_value_0 = item_0
                vars_and_values_1___frozen_dict, func_value_1 = item_1
                same_vars_same_values = True
                for var in (set(vars_and_values_0___frozen_dict) & set(vars_and_values_1___frozen_dict)):
                    same_vars_same_values &=\
                        (vars_and_values_0___frozen_dict[var] == vars_and_values_1___frozen_dict[var])
                if same_vars_same_values:
                    if __r:
                        value = op(func_value_1, func_value_0, **kwargs)
                    else:
                        value = op(func_value_0, func_value_1, **kwargs)
                    __mapping[frozendict(set(vars_and_values_0___frozen_dict.items()) |
                                      set(vars_and_values_1___frozen_dict.items()))] = value
            return MathDict(__mapping)
        elif other is None:
            return MathDict({k: op(v, **kwargs) for k, v in self.items()})
        elif __r:
            return MathDict({k: op(other, v, **kwargs) for k, v in self.items()})
        else:
            return MathDict({k: op(v, other, **kwargs) for k, v in self.items()})

    # Operations on Self alone:
    def __index__(self):
        return self.__op__(op=index)

    def __int__(self):
        return self.__op__(op=int)

    def __long__(self):
        return self.__op__(op=long)

    def __hex__(self):
        return self.__op__(op=hex)

    def __float__(self):
        return self.__op__(op=float)

    def __complex__(self):
        return self.__op__(op=complex)

    def __pos__(self):
        return self.__op__(op=pos)

    def __neg__(self):
        return self.__op__(op=neg)

    def __abs__(self):
        return self.__op__(op=abs)

    # Rich Comparisons
    def __lt__(self, other):
        return self.__op__(lt, other)

    def __le__(self, other):
        return self.__op__(le, other)

    def __eq__(self, other):
        return self.__op__(eq, other)

    def __ne__(self, other):
        return self.__op__(ne, other)

    def __ge__(self, other):
        return self.__op__(ge, other)

    def __gt__(self, other):
        return self.__op__(gt, other)

    # Bit-Wise Operations
    def __add__(self, other):
        return self.__op__(add, other)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        self += other

    def __sub__(self, other):
        return self.__op__(sub, other)

    def __rsub__(self, other):
        return (-self) + other

    def __isub__(self, other):
        self -= other

    def __mul__(self, other):
        return self.__op__(mul, other)

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        self *= other

    def __div__(self, other):
        return self.__op__(div, other)

    def __rdiv__(self, other):
        return self.__op__(div, other, __r=True)

    def __idiv__(self, other):
        self /= other

    def __truediv__(self, other):
        return self.__op__(truediv, other)

    def __rtruediv__(self, other):
        return self.__op__(truediv, other, __r=True)

    def __itruediv__(self, other):
        self /= other

    def __floordiv__(self, other):
        return self.__op__(floordiv, other)

    def __rfloordiv__(self, other):
        return self.__op__(floordiv, other, __r=True)

    def __mod__(self, other):
        return self.__op__(mod, other)

    def __rmod__(self, other):
        return self.__op__(mod, other, __r=True)

    def __imod__(self, other):
        self %= other

    def __pow__(self, power):
        return self.__op__(pow, power)

    def __rpow__(self, other):
        return self.__op__(pow, other, __r=True)

    def __ipow__(self, power):
        self **= power

    def allclose(self, other, rtol=1e-5, atol=1e-8):
        return all(self.__op__(sympy_allclose, other, rtol=rtol, atol=atol).values())

    def pprint(self):
        pprint(self())


def exp(math_dict):
    if isinstance(math_dict, MathDict):
        return math_dict.__op__(e)
    else:
        return e(math_dict)


def log(math_dict):
    if isinstance(math_dict, MathDict):
        return math_dict.__op__(ln)
    else:
        return ln(math_dict)


def sqrt(math_dict):
    if isinstance(math_dict, MathDict):
        return math_dict.__op__(square_root)
    else:
        return square_root(math_dict)
