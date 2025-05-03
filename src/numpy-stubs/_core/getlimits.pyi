from types import GenericAlias
from typing import Final, Generic, Literal as L, Self, overload
from typing_extensions import TypeVar

import _numtype as _nt
import numpy as np

__all__ = ["finfo", "iinfo"]

###

_IntegerT_co = TypeVar("_IntegerT_co", bound=np.integer, default=np.integer, covariant=True)
_FloatingT_co = TypeVar("_FloatingT_co", bound=np.floating, default=np.floating, covariant=True)

###

class iinfo(Generic[_IntegerT_co]):
    dtype: np.dtype[_IntegerT_co]
    bits: Final[L[8, 16, 32, 64]]
    kind: Final[L["i", "u"]]
    key: Final[L["i8", "i16", "i32", "i64", "u8", "u16", "u32", "u64"]]

    @property
    def min(self, /) -> int: ...
    @property
    def max(self, /) -> int: ...

    #
    @overload
    def __init__(self, /, int_type: _IntegerT_co | _nt._ToDType[_IntegerT_co]) -> None: ...
    @overload
    def __init__(self: iinfo[np.int8], /, int_type: _nt.ToDTypeInt8) -> None: ...
    @overload
    def __init__(self: iinfo[np.uint8], /, int_type: _nt.ToDTypeUInt8) -> None: ...
    @overload
    def __init__(self: iinfo[np.int16], /, int_type: _nt.ToDTypeInt16) -> None: ...
    @overload
    def __init__(self: iinfo[np.uint16], /, int_type: _nt.ToDTypeUInt16) -> None: ...
    @overload
    def __init__(self: iinfo[np.int32], /, int_type: _nt.ToDTypeInt32) -> None: ...
    @overload
    def __init__(self: iinfo[np.uint32], /, int_type: _nt.ToDTypeUInt32) -> None: ...
    @overload
    def __init__(self: iinfo[np.int64], /, int_type: _nt.ToDTypeInt64 | int) -> None: ...
    @overload
    def __init__(self: iinfo[np.uint64], /, int_type: _nt.ToDTypeUInt64) -> None: ...

    #
    @classmethod
    def __class_getitem__(cls, item: object, /) -> GenericAlias: ...

#
class finfo(Generic[_FloatingT_co]):
    dtype: np.dtype[_FloatingT_co]
    eps: _FloatingT_co
    epsneg: _FloatingT_co
    resolution: _FloatingT_co
    smallest_subnormal: _FloatingT_co
    max: _FloatingT_co
    min: _FloatingT_co

    bits: Final[L[2, 4, 8, 12, 16]]
    iexp: Final[int]
    machep: Final[int]
    maxexp: Final[int]
    minexp: Final[int]
    negep: Final[int]
    nexp: Final[int]
    nmant: Final[int]
    precision: Final[int]

    @property
    def smallest_normal(self, /) -> _FloatingT_co: ...
    @property
    def tiny(self, /) -> _FloatingT_co: ...

    #
    @overload
    def __new__(cls, dtype: _nt.ToDTypeFloat16) -> finfo[np.float16]: ...
    @overload
    def __new__(cls, dtype: _nt.ToDTypeFloat32 | _nt.ToDTypeComplex64) -> finfo[np.float32]: ...
    @overload
    def __new__(cls, dtype: _nt.ToDTypeFloat64 | _nt.ToDTypeComplex128 | complex) -> finfo[np.float64]: ...
    @overload
    def __new__(cls, dtype: _nt.ToDTypeLongDouble | _nt.ToDTypeCLongDouble) -> finfo[np.longdouble]: ...
    @overload
    def __new__(cls, dtype: _FloatingT_co | _nt._ToDType[_FloatingT_co]) -> Self: ...

    #
    @classmethod
    def __class_getitem__(cls, item: object, /) -> GenericAlias: ...
