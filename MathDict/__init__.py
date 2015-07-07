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
        self.Mapping = dict(*args, **kwargs)
        self.Hash = None

    def __repr__(self):
        return '<MathDict %s>' % repr(self.Mapping)

    def __len__(self):
        return len(self.Mapping)

    def __iter__(self):
        return iter(self.Mapping)

    def __getitem__(self, k):
        return self.Mapping[k]

    def __setitem__(self, k, v):
        self.Mapping[k] = v

    def __delitem__(self, k):
        del self.Mapping[k]

    def __contains__(self, item):
        return item in self.Mapping

    def __hash__(self):
        if self.Hash is None:
            self.Hash = reduce(xor, map(hash, self.iteritems()), 0)
        return self.Hash

    # __call__: simply return __dict
    def __call__(self):
        return self.Mapping

    def copy(self, deep=False):
        if deep:
            return MathDict(deepcopy(self.Mapping))
        else:
            return MathDict(self.Mapping.copy())

    def update(self, *args, **kwargs):
        self.Mapping.update(*args, **kwargs)

    def op(self, op=mul, other=None, r=False, **kwargs):
        if hasattr(other, 'keys'):
            mapping = {}
            for item_0, item_1 in product(self.items(), other.items()):
                vars_and_values_0___frozen_dict, func_value_0 = item_0
                vars_and_values_1___frozen_dict, func_value_1 = item_1
                same_vars_same_values = True
                for var in (set(vars_and_values_0___frozen_dict) & set(vars_and_values_1___frozen_dict)):
                    same_vars_same_values &=\
                        (vars_and_values_0___frozen_dict[var] == vars_and_values_1___frozen_dict[var])
                if same_vars_same_values:
                    if r:
                        value = op(func_value_1, func_value_0, **kwargs)
                    else:
                        value = op(func_value_0, func_value_1, **kwargs)
                    mapping[frozendict(set(vars_and_values_0___frozen_dict.items()) |
                                       set(vars_and_values_1___frozen_dict.items()))] = value
            return MathDict(mapping)
        elif other is None:
            return MathDict({k: op(v, **kwargs) for k, v in self.items()})
        elif r:
            return MathDict({k: op(other, v, **kwargs) for k, v in self.items()})
        else:
            return MathDict({k: op(v, other, **kwargs) for k, v in self.items()})

    # Operations on Self alone:
    def __index__(self):
        return self.op(op=index)

    def __int__(self):
        return self.op(op=int)

    def __long__(self):
        return self.op(op=long)

    def __hex__(self):
        return self.op(op=hex)

    def __float__(self):
        return self.op(op=float)

    def __complex__(self):
        return self.op(op=complex)

    def __pos__(self):
        return self.op(op=pos)

    def __neg__(self):
        return self.op(op=neg)

    def __abs__(self):
        return self.op(op=abs)

    # Rich Comparisons
    def __lt__(self, other):
        return self.op(lt, other)

    def __le__(self, other):
        return self.op(le, other)

    def __eq__(self, other):
        return self.op(eq, other)

    def __ne__(self, other):
        return self.op(ne, other)

    def __ge__(self, other):
        return self.op(ge, other)

    def __gt__(self, other):
        return self.op(gt, other)

    # Bit-Wise Operations
    def __add__(self, other):
        return self.op(add, other)

    def __radd__(self, other):
        return self + other

#    def __iadd__(self, other):
#        self += other

    def __sub__(self, other):
        return self.op(sub, other)

    def __rsub__(self, other):
        return (-self) + other

#    def __isub__(self, other):
#        self -= other

    def __mul__(self, other):
        return self.op(mul, other)

    def __rmul__(self, other):
        return self * other

#    def __imul__(self, other):
#        self = self * other

    def __div__(self, other):
        return self.op(div, other)

    def __rdiv__(self, other):
        return self.op(div, other, r=True)

#    def __idiv__(self, other):
#        self /= other

    def __truediv__(self, other):
        return self.op(truediv, other)

    def __rtruediv__(self, other):
        return self.op(truediv, other, r=True)

#    def __itruediv__(self, other):
#        self /= other

    def __floordiv__(self, other):
        return self.op(floordiv, other)

    def __rfloordiv__(self, other):
        return self.op(floordiv, other, r=True)

#    def __ifloordiv__(self, other):
#        self //= other

    def __mod__(self, other):
        return self.op(mod, other)

    def __rmod__(self, other):
        return self.op(mod, other, r=True)

#    def __imod__(self, other):
#        self %= other

    def __pow__(self, power):
        return self.op(pow, power)

    def __rpow__(self, other):
        return self.op(pow, other, r=True)

#    def __ipow__(self, power):
#        self **= power

    def allclose(self, other, rtol=1e-5, atol=1e-8):
        return all(self.op(sympy_allclose, other, rtol=rtol, atol=atol).values())

    def pprint(self):
        pprint(self())


def exp(math_dict):
    if isinstance(math_dict, MathDict):
        return math_dict.op(e)
    else:
        return e(math_dict)


def log(math_dict):
    if isinstance(math_dict, MathDict):
        return math_dict.op(ln)
    else:
        return ln(math_dict)


def sqrt(math_dict):
    if isinstance(math_dict, MathDict):
        return math_dict.op(square_root)
    else:
        return square_root(math_dict)
