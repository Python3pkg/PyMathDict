from __future__ import division
from collections import defaultdict, OrderedDict, Mapping
from copy import deepcopy
from Helpy.SymPy import sympy_allclose
from frozendict import frozendict
from frozenordereddict import FrozenOrderedDict, OrderedDict as Ordered_Dict
from operator import pos, neg, abs, lt, le, eq, ne, ge, gt, add, sub, mul, div, truediv, floordiv, mod, pow


def op_if_other_has_same_keys_or_is_not_dict(op, math_dict, other=None, **kwargs):
    if other is None:
        return MathDict({k: op(v, **kwargs) for k, v in math_dict.items()})
    else:
        keys___set = set(math_dict)
        if isinstance(other, (dict, defaultdict, OrderedDict, frozendict, Ordered_Dict, FrozenOrderedDict, MathDict)) &\
                (set(other) == keys___set):
            return MathDict({k: op(math_dict[k], other[k], **kwargs) for k in keys___set})
        else:
            return MathDict({k: op(v, other, **kwargs) for k, v in math_dict.items()})


class MathDict(Mapping):
    def __init__(self, *args, **kwargs):
        self.__dict = dict(*args, **kwargs)
        self.__hash = None

    def __repr__(self):
        return '<MathDict %s>' % repr(self.__dict)

    def __len__(self):
        return len(self.__dict)

    def __iter__(self):
        return iter(self.__dict)

    def __getitem__(self, k):
        return self.__dict[k]

    def __setitem__(self, k, v):
        self.__dict[k] = v

    def __delitem__(self, k):
        del self.__dict[k]

    def __contains__(self, item):
        return item in self.__dict

    def __hash__(self):
        return None

    # __call__: simply return __dict
    def __call__(self):
        return self.__dict

    def copy(self, deep=True):
        if deep:
            return MathDict(deepcopy(self.__dict))
        else:
            return MathDict(self.__dict.copy())

    def update(self, *args, **kwargs):
        self.__dict.update(*args, **kwargs)

    # Operations on Self alone:
    def __int__(self):
        return op_if_other_has_same_keys_or_is_not_dict(int, self)

    def __float__(self):
        return op_if_other_has_same_keys_or_is_not_dict(float, self)

    def __complex__(self):
        return op_if_other_has_same_keys_or_is_not_dict(complex, self)

    def __pos__(self):
        return op_if_other_has_same_keys_or_is_not_dict(pos, self)

    def __neg__(self):
        return op_if_other_has_same_keys_or_is_not_dict(neg, self)

    def __abs__(self):
        return op_if_other_has_same_keys_or_is_not_dict(abs, self)

    # Rich Comparisons
    def __lt__(self, other):
        return op_if_other_has_same_keys_or_is_not_dict(lt, self, other)

    def __le__(self, other):
        return op_if_other_has_same_keys_or_is_not_dict(le, self, other)

    def __eq__(self, other):
        return op_if_other_has_same_keys_or_is_not_dict(eq, self, other)

    def __ne__(self, other):
        return op_if_other_has_same_keys_or_is_not_dict(ne, self, other)

    def __ge__(self, other):
        return op_if_other_has_same_keys_or_is_not_dict(ge, self, other)

    def __gt__(self, other):
        return op_if_other_has_same_keys_or_is_not_dict(gt, self, other)

    # Bit-Wise Operations
    def __add__(self, other):
        return op_if_other_has_same_keys_or_is_not_dict(add, self, other)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        self += other

    def __sub__(self, other):
        return op_if_other_has_same_keys_or_is_not_dict(sub, self, other)

    def __rsub__(self, other):
        return (-self) + other

    def __isub__(self, other):
        self -= other

    def __mul__(self, other):
        return op_if_other_has_same_keys_or_is_not_dict(mul, self, other)

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        self *= other

    def __div__(self, other):
        return op_if_other_has_same_keys_or_is_not_dict(div, self, other)

    def __rdiv__(self, other):
        keys___set = set(self)
        if isinstance(other, (dict, defaultdict, OrderedDict, frozendict, Ordered_Dict, FrozenOrderedDict, MathDict)) &\
                (set(other) == keys___set):
            return MathDict({k: other[k] / self[k] for k in keys___set})
        else:
            return MathDict({k: other / v for k, v in self.items()})

    def __idiv__(self, other):
        self /= other

    def __truediv__(self, other):
        return op_if_other_has_same_keys_or_is_not_dict(truediv, self, other)

    def __rtruediv__(self, other):
        keys___set = set(self)
        if isinstance(other, (dict, defaultdict, OrderedDict, frozendict, Ordered_Dict, FrozenOrderedDict, MathDict)) &\
                (set(other) == keys___set):
            return MathDict({k: truediv(other[k], self[k]) for k in keys___set})
        else:
            return MathDict({k: truediv(other, v) for k, v in self.items()})

    def __itruediv__(self, other):
        self /= other

    def __floordiv__(self, other):
        return op_if_other_has_same_keys_or_is_not_dict(floordiv, self, other)

    def __rfloordiv__(self, other):
        keys___set = set(self)
        if isinstance(other, (dict, defaultdict, OrderedDict, frozendict, Ordered_Dict, FrozenOrderedDict, MathDict)) &\
                (set(other) == keys___set):
            return MathDict({k: other[k] // self[k] for k in keys___set})
        else:
            return MathDict({k: other // v for k, v in self.items()})

    def __mod__(self, other):
        return op_if_other_has_same_keys_or_is_not_dict(mod, self, other)

    def __rmod__(self, other):
        keys___set = set(self)
        if isinstance(other, (dict, defaultdict, OrderedDict, frozendict, Ordered_Dict, FrozenOrderedDict, MathDict)) &\
                (set(other) == keys___set):
            return MathDict({k: other[k] % self[k] for k in keys___set})
        else:
            return MathDict({k: other % v for k, v in self.items()})

    def __imod__(self, other):
        self %= other

    def __pow__(self, power):
        return op_if_other_has_same_keys_or_is_not_dict(pow, self, power)

    def __rpow__(self, other):
        keys___set = set(self)
        if isinstance(other, (dict, defaultdict, OrderedDict, frozendict, Ordered_Dict, FrozenOrderedDict, MathDict)) &\
                (set(other) == keys___set):
            return MathDict({k: other[k] ** self[k] for k in keys___set})
        else:
            return MathDict({k: other ** v for k, v in self.items()})

    def __ipow__(self, power):
        self **= power

    def allclose(self, other, rtol=1e-5, atol=1e-8):
        return op_if_other_has_same_keys_or_is_not_dict(sympy_allclose, self, other, rtol=rtol, atol=atol)
