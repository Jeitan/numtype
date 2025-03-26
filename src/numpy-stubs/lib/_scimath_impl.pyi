from typing import TypeAlias, overload

import numpy as np
from _numtype import (
    Array,
    CanArray0D,
    CoComplex_0d,
    CoComplex_1nd,
    CoComplex_nd,
    CoFloating_0d,
    CoFloating_1nd,
    CoFloating_nd,
    CoInt8_0d,
    CoInt8_1nd,
    CoInt8_nd,
    CoInteger_0d,
    CoInteger_1nd,
    CoInteger_nd,
    CoUInt8_0d,
    CoUInt8_1nd,
    CoUInt8_nd,
    CoUInt64_0d,
    CoUInt64_1nd,
    CoUInt64_nd,
    JustInt,
    ToBool_0d,
    ToBool_1nd,
    ToCLongDouble_0d,
    ToCLongDouble_1nd,
    ToComplex64_0d,
    ToComplex64_1nd,
    ToComplex128_0d,
    ToComplex128_1nd,
    ToComplex_0d,
    ToComplex_1nd,
    ToComplex_nd,
    ToFloat16_0d,
    ToFloat16_1nd,
    ToFloat32_0d,
    ToFloat32_1nd,
    ToFloat64_0d,
    ToFloat64_1nd,
    ToFloating_0d,
    ToFloating_1nd,
    ToFloating_nd,
    ToInt8_0d,
    ToInt8_1nd,
    ToInt16_0d,
    ToInt16_1nd,
    ToLongDouble_0d,
    ToLongDouble_1nd,
    ToSInteger_0d,
    ToSInteger_1nd,
    ToSInteger_nd,
    ToUInt8_0d,
    ToUInt8_1nd,
    ToUInt16_0d,
    ToUInt16_1nd,
    ToUInteger_0d,
    ToUInteger_1nd,
    ToUInteger_nd,
    _ToArray2_1nd,
    _ToArray_1nd,
    integer8,
    integer16,
    integer32,
    integer64,
)

__all__ = ["arccos", "arcsin", "arctanh", "log", "log2", "log10", "logn", "power", "sqrt"]

###

_ToScalar_u4_u8: TypeAlias = CanArray0D[np.uint32 | np.uint64]
_ToScalar_i4_i8: TypeAlias = CanArray0D[np.int32 | np.int64] | JustInt

_ToArray_u4_u8: TypeAlias = _ToArray_1nd[np.uint32 | np.uint64]
_ToArray_i4_i8: TypeAlias = _ToArray2_1nd[np.int32 | np.int64, JustInt]

###

# NOTE: This module is publically re-exported as `numpy.emath`
# NOTE: All signatures are weird: https://github.com/numpy/numpy/issues/28367
# NOTE: The signatures of sqrt, log, log2, and log10 are identical
# NOTE: all ignored mypy [overload-overlap] errors are false positives (meet vs join)

#
@overload
def sqrt(x: ToBool_0d) -> np.float16: ...
@overload
def sqrt(x: _ToScalar_u4_u8) -> np.float64: ...
@overload
def sqrt(x: ToUInt16_0d) -> np.float32: ...
@overload
def sqrt(x: ToUInt8_0d) -> np.float16: ...
@overload
def sqrt(x: CoUInt64_0d) -> np.floating: ...
@overload
def sqrt(x: _ToScalar_i4_i8) -> np.float64 | np.complex128: ...
@overload
def sqrt(x: ToInt16_0d) -> np.float32 | np.complex64: ...
@overload
def sqrt(x: ToInt8_0d) -> np.float16 | np.complex64: ...
@overload
def sqrt(x: ToFloat64_0d) -> np.float64 | np.complex128: ...
@overload
def sqrt(x: ToLongDouble_0d) -> np.longdouble | np.complex128: ...
@overload
def sqrt(x: ToFloat32_0d) -> np.float32 | np.complex64: ...
@overload
def sqrt(x: ToFloat16_0d) -> np.float16 | np.complex128: ...
@overload
def sqrt(x: ToComplex128_0d) -> np.complex128: ...
@overload
def sqrt(x: ToCLongDouble_0d) -> np.complex128 | np.clongdouble: ...
@overload
def sqrt(x: ToComplex64_0d) -> np.complex64: ...
@overload
def sqrt(x: ToComplex_0d) -> np.complexfloating: ...
@overload
def sqrt(x: CoComplex_0d) -> np.inexact: ...
@overload
def sqrt(x: ToBool_1nd) -> Array[np.float16]: ...
@overload
def sqrt(x: _ToArray_u4_u8) -> Array[np.float64]: ...
@overload
def sqrt(x: ToUInt16_1nd) -> Array[np.float32]: ...
@overload
def sqrt(x: ToUInt8_1nd) -> Array[np.float16]: ...
@overload
def sqrt(x: CoUInt64_1nd) -> Array[np.floating]: ...
@overload
def sqrt(x: _ToArray_i4_i8) -> Array[np.float64 | np.complex128]: ...
@overload
def sqrt(x: ToInt16_1nd) -> Array[np.float32 | np.complex64]: ...
@overload
def sqrt(x: ToInt8_1nd) -> Array[np.float16 | np.complex64]: ...
@overload
def sqrt(x: ToFloat64_1nd) -> Array[np.float64 | np.complex128]: ...
@overload
def sqrt(x: ToLongDouble_1nd) -> Array[np.longdouble | np.complex128]: ...
@overload
def sqrt(x: ToFloat32_1nd) -> Array[np.float32 | np.complex64]: ...
@overload
def sqrt(x: ToFloat16_1nd) -> Array[np.float16 | np.complex128]: ...
@overload
def sqrt(x: ToComplex128_1nd) -> Array[np.complex128]: ...
@overload
def sqrt(x: ToCLongDouble_1nd) -> Array[np.complex128 | np.clongdouble]: ...
@overload
def sqrt(x: ToComplex64_1nd) -> Array[np.complex64]: ...
@overload
def sqrt(x: ToComplex_1nd) -> Array[np.complexfloating]: ...
@overload
def sqrt(x: CoComplex_1nd) -> Array[np.inexact]: ...

# signature is equivalent to `sqrt`
@overload
def log(x: ToBool_0d) -> np.float16: ...
@overload
def log(x: _ToScalar_u4_u8) -> np.float64: ...
@overload
def log(x: ToUInt16_0d) -> np.float32: ...
@overload
def log(x: ToUInt8_0d) -> np.float16: ...
@overload
def log(x: CoUInt64_0d) -> np.floating: ...
@overload
def log(x: _ToScalar_i4_i8) -> np.float64 | np.complex128: ...
@overload
def log(x: ToInt16_0d) -> np.float32 | np.complex64: ...
@overload
def log(x: ToInt8_0d) -> np.float16 | np.complex64: ...
@overload
def log(x: ToFloat64_0d) -> np.float64 | np.complex128: ...
@overload
def log(x: ToLongDouble_0d) -> np.longdouble | np.complex128: ...
@overload
def log(x: ToFloat32_0d) -> np.float32 | np.complex64: ...
@overload
def log(x: ToFloat16_0d) -> np.float16 | np.complex128: ...
@overload
def log(x: ToComplex128_0d) -> np.complex128: ...
@overload
def log(x: ToCLongDouble_0d) -> np.complex128 | np.clongdouble: ...
@overload
def log(x: ToComplex64_0d) -> np.complex64: ...
@overload
def log(x: ToComplex_0d) -> np.complexfloating: ...
@overload
def log(x: CoComplex_0d) -> np.inexact: ...
@overload
def log(x: ToBool_1nd) -> Array[np.float16]: ...
@overload
def log(x: _ToArray_u4_u8) -> Array[np.float64]: ...
@overload
def log(x: ToUInt16_1nd) -> Array[np.float32]: ...
@overload
def log(x: ToUInt8_1nd) -> Array[np.float16]: ...
@overload
def log(x: CoUInt64_1nd) -> Array[np.floating]: ...
@overload
def log(x: _ToArray_i4_i8) -> Array[np.float64 | np.complex128]: ...
@overload
def log(x: ToInt16_1nd) -> Array[np.float32 | np.complex64]: ...
@overload
def log(x: ToInt8_1nd) -> Array[np.float16 | np.complex64]: ...
@overload
def log(x: ToFloat64_1nd) -> Array[np.float64 | np.complex128]: ...
@overload
def log(x: ToLongDouble_1nd) -> Array[np.longdouble | np.complex128]: ...
@overload
def log(x: ToFloat32_1nd) -> Array[np.float32 | np.complex64]: ...
@overload
def log(x: ToFloat16_1nd) -> Array[np.float16 | np.complex128]: ...
@overload
def log(x: ToComplex128_1nd) -> Array[np.complex128]: ...
@overload
def log(x: ToCLongDouble_1nd) -> Array[np.complex128 | np.clongdouble]: ...
@overload
def log(x: ToComplex64_1nd) -> Array[np.complex64]: ...
@overload
def log(x: ToComplex_1nd) -> Array[np.complexfloating]: ...
@overload
def log(x: CoComplex_1nd) -> Array[np.inexact]: ...

# signature is equivalent to `sqrt`
@overload
def log10(x: ToBool_0d) -> np.float16: ...
@overload
def log10(x: _ToScalar_u4_u8) -> np.float64: ...
@overload
def log10(x: ToUInt16_0d) -> np.float32: ...
@overload
def log10(x: ToUInt8_0d) -> np.float16: ...
@overload
def log10(x: CoUInt64_0d) -> np.floating: ...
@overload
def log10(x: _ToScalar_i4_i8) -> np.float64 | np.complex128: ...
@overload
def log10(x: ToInt16_0d) -> np.float32 | np.complex64: ...
@overload
def log10(x: ToInt8_0d) -> np.float16 | np.complex64: ...
@overload
def log10(x: ToFloat64_0d) -> np.float64 | np.complex128: ...
@overload
def log10(x: ToLongDouble_0d) -> np.longdouble | np.complex128: ...
@overload
def log10(x: ToFloat32_0d) -> np.float32 | np.complex64: ...
@overload
def log10(x: ToFloat16_0d) -> np.float16 | np.complex128: ...
@overload
def log10(x: ToComplex128_0d) -> np.complex128: ...
@overload
def log10(x: ToCLongDouble_0d) -> np.complex128 | np.clongdouble: ...
@overload
def log10(x: ToComplex64_0d) -> np.complex64: ...
@overload
def log10(x: ToComplex_0d) -> np.complexfloating: ...
@overload
def log10(x: CoComplex_0d) -> np.inexact: ...
@overload
def log10(x: ToBool_1nd) -> Array[np.float16]: ...
@overload
def log10(x: _ToArray_u4_u8) -> Array[np.float64]: ...
@overload
def log10(x: ToUInt16_1nd) -> Array[np.float32]: ...
@overload
def log10(x: ToUInt8_1nd) -> Array[np.float16]: ...
@overload
def log10(x: CoUInt64_1nd) -> Array[np.floating]: ...
@overload
def log10(x: _ToArray_i4_i8) -> Array[np.float64 | np.complex128]: ...
@overload
def log10(x: ToInt16_1nd) -> Array[np.float32 | np.complex64]: ...
@overload
def log10(x: ToInt8_1nd) -> Array[np.float16 | np.complex64]: ...
@overload
def log10(x: ToFloat64_1nd) -> Array[np.float64 | np.complex128]: ...
@overload
def log10(x: ToLongDouble_1nd) -> Array[np.longdouble | np.complex128]: ...
@overload
def log10(x: ToFloat32_1nd) -> Array[np.float32 | np.complex64]: ...
@overload
def log10(x: ToFloat16_1nd) -> Array[np.float16 | np.complex128]: ...
@overload
def log10(x: ToComplex128_1nd) -> Array[np.complex128]: ...
@overload
def log10(x: ToCLongDouble_1nd) -> Array[np.complex128 | np.clongdouble]: ...
@overload
def log10(x: ToComplex64_1nd) -> Array[np.complex64]: ...
@overload
def log10(x: ToComplex_1nd) -> Array[np.complexfloating]: ...
@overload
def log10(x: CoComplex_1nd) -> Array[np.inexact]: ...

# signature is equivalent to `sqrt`
@overload
def log2(x: ToBool_0d) -> np.float16: ...
@overload
def log2(x: _ToScalar_u4_u8) -> np.float64: ...
@overload
def log2(x: ToUInt16_0d) -> np.float32: ...
@overload
def log2(x: ToUInt8_0d) -> np.float16: ...
@overload
def log2(x: CoUInt64_0d) -> np.floating: ...
@overload
def log2(x: _ToScalar_i4_i8) -> np.float64 | np.complex128: ...
@overload
def log2(x: ToInt16_0d) -> np.float32 | np.complex64: ...
@overload
def log2(x: ToInt8_0d) -> np.float16 | np.complex64: ...
@overload
def log2(x: ToFloat64_0d) -> np.float64 | np.complex128: ...
@overload
def log2(x: ToLongDouble_0d) -> np.longdouble | np.complex128: ...
@overload
def log2(x: ToFloat32_0d) -> np.float32 | np.complex64: ...
@overload
def log2(x: ToFloat16_0d) -> np.float16 | np.complex128: ...
@overload
def log2(x: ToComplex128_0d) -> np.complex128: ...
@overload
def log2(x: ToCLongDouble_0d) -> np.complex128 | np.clongdouble: ...
@overload
def log2(x: ToComplex64_0d) -> np.complex64: ...
@overload
def log2(x: ToComplex_0d) -> np.complexfloating: ...
@overload
def log2(x: CoComplex_0d) -> np.inexact: ...
@overload
def log2(x: ToBool_1nd) -> Array[np.float16]: ...
@overload
def log2(x: _ToArray_u4_u8) -> Array[np.float64]: ...
@overload
def log2(x: ToUInt16_1nd) -> Array[np.float32]: ...
@overload
def log2(x: ToUInt8_1nd) -> Array[np.float16]: ...
@overload
def log2(x: CoUInt64_1nd) -> Array[np.floating]: ...
@overload
def log2(x: _ToArray_i4_i8) -> Array[np.float64 | np.complex128]: ...
@overload
def log2(x: ToInt16_1nd) -> Array[np.float32 | np.complex64]: ...
@overload
def log2(x: ToInt8_1nd) -> Array[np.float16 | np.complex64]: ...
@overload
def log2(x: ToFloat64_1nd) -> Array[np.float64 | np.complex128]: ...
@overload
def log2(x: ToLongDouble_1nd) -> Array[np.longdouble | np.complex128]: ...
@overload
def log2(x: ToFloat32_1nd) -> Array[np.float32 | np.complex64]: ...
@overload
def log2(x: ToFloat16_1nd) -> Array[np.float16 | np.complex128]: ...
@overload
def log2(x: ToComplex128_1nd) -> Array[np.complex128]: ...
@overload
def log2(x: ToCLongDouble_1nd) -> Array[np.complex128 | np.clongdouble]: ...
@overload
def log2(x: ToComplex64_1nd) -> Array[np.complex64]: ...
@overload
def log2(x: ToComplex_1nd) -> Array[np.complexfloating]: ...
@overload
def log2(x: CoComplex_1nd) -> Array[np.inexact]: ...

# NOTE: The signatures of arccos, arcsin, and arctanh are identical

#
@overload
def arccos(x: ToBool_0d) -> np.float16 | np.complex64: ...
@overload
def arccos(x: CanArray0D[integer64 | integer32] | JustInt) -> np.float64 | np.complex128: ...
@overload
def arccos(x: CanArray0D[integer16]) -> np.float32 | np.complex64: ...
@overload
def arccos(x: CanArray0D[integer8]) -> np.float16 | np.complex64: ...
@overload
def arccos(x: ToFloat64_0d) -> np.float64 | np.complex128: ...
@overload
def arccos(x: ToLongDouble_0d) -> np.longdouble | np.complex128: ...
@overload
def arccos(x: ToFloat32_0d) -> np.float32 | np.complex64: ...
@overload
def arccos(x: ToFloat16_0d) -> np.float16 | np.complex128: ...
@overload
def arccos(x: ToComplex128_0d) -> np.complex128: ...
@overload
def arccos(x: ToCLongDouble_0d) -> np.complex128 | np.clongdouble: ...
@overload
def arccos(x: ToComplex64_0d) -> np.complex64: ...
@overload
def arccos(x: ToComplex_0d) -> np.complexfloating: ...
@overload
def arccos(x: CoComplex_0d) -> np.inexact: ...
@overload
def arccos(x: ToBool_1nd) -> Array[np.float16 | np.complex64]: ...
@overload
def arccos(x: _ToArray2_1nd[integer64 | integer32, JustInt]) -> Array[np.float64 | np.complex128]: ...
@overload
def arccos(x: _ToArray_1nd[integer16]) -> Array[np.float32 | np.complex64]: ...
@overload
def arccos(x: _ToArray_1nd[integer8]) -> Array[np.float16 | np.complex64]: ...
@overload
def arccos(x: ToFloat64_1nd) -> Array[np.float64 | np.complex128]: ...
@overload
def arccos(x: ToLongDouble_1nd) -> Array[np.longdouble | np.complex128]: ...
@overload
def arccos(x: ToFloat32_1nd) -> Array[np.float32 | np.complex64]: ...
@overload
def arccos(x: ToFloat16_1nd) -> Array[np.float16 | np.complex128]: ...
@overload
def arccos(x: ToComplex128_1nd) -> Array[np.complex128]: ...
@overload
def arccos(x: ToCLongDouble_1nd) -> Array[np.complex128 | np.clongdouble]: ...
@overload
def arccos(x: ToComplex64_1nd) -> Array[np.complex64]: ...
@overload
def arccos(x: ToComplex_1nd) -> Array[np.complexfloating]: ...
@overload
def arccos(x: CoComplex_1nd) -> Array[np.inexact]: ...

# signature is equivalent to `arccos`
@overload
def arcsin(x: ToBool_0d) -> np.float16 | np.complex64: ...
@overload
def arcsin(x: CanArray0D[integer64 | integer32] | JustInt) -> np.float64 | np.complex128: ...
@overload
def arcsin(x: CanArray0D[integer16]) -> np.float32 | np.complex64: ...
@overload
def arcsin(x: CanArray0D[integer8]) -> np.float16 | np.complex64: ...
@overload
def arcsin(x: ToFloat64_0d) -> np.float64 | np.complex128: ...
@overload
def arcsin(x: ToLongDouble_0d) -> np.longdouble | np.complex128: ...
@overload
def arcsin(x: ToFloat32_0d) -> np.float32 | np.complex64: ...
@overload
def arcsin(x: ToFloat16_0d) -> np.float16 | np.complex128: ...
@overload
def arcsin(x: ToComplex128_0d) -> np.complex128: ...
@overload
def arcsin(x: ToCLongDouble_0d) -> np.complex128 | np.clongdouble: ...
@overload
def arcsin(x: ToComplex64_0d) -> np.complex64: ...
@overload
def arcsin(x: ToComplex_0d) -> np.complexfloating: ...
@overload
def arcsin(x: CoComplex_0d) -> np.inexact: ...
@overload
def arcsin(x: ToBool_1nd) -> Array[np.float16 | np.complex64]: ...
@overload
def arcsin(x: _ToArray2_1nd[integer64 | integer32, JustInt]) -> Array[np.float64 | np.complex128]: ...
@overload
def arcsin(x: _ToArray_1nd[integer16]) -> Array[np.float32 | np.complex64]: ...
@overload
def arcsin(x: _ToArray_1nd[integer8]) -> Array[np.float16 | np.complex64]: ...
@overload
def arcsin(x: ToFloat64_1nd) -> Array[np.float64 | np.complex128]: ...
@overload
def arcsin(x: ToLongDouble_1nd) -> Array[np.longdouble | np.complex128]: ...
@overload
def arcsin(x: ToFloat32_1nd) -> Array[np.float32 | np.complex64]: ...
@overload
def arcsin(x: ToFloat16_1nd) -> Array[np.float16 | np.complex128]: ...
@overload
def arcsin(x: ToComplex128_1nd) -> Array[np.complex128]: ...
@overload
def arcsin(x: ToCLongDouble_1nd) -> Array[np.complex128 | np.clongdouble]: ...
@overload
def arcsin(x: ToComplex64_1nd) -> Array[np.complex64]: ...
@overload
def arcsin(x: ToComplex_1nd) -> Array[np.complexfloating]: ...
@overload
def arcsin(x: CoComplex_1nd) -> Array[np.inexact]: ...

# signature is equivalent to `arccos`
@overload
def arctanh(x: ToBool_0d) -> np.float16 | np.complex64: ...
@overload
def arctanh(x: CanArray0D[integer64 | integer32] | JustInt) -> np.float64 | np.complex128: ...
@overload
def arctanh(x: CanArray0D[integer16]) -> np.float32 | np.complex64: ...
@overload
def arctanh(x: CanArray0D[integer8]) -> np.float16 | np.complex64: ...
@overload
def arctanh(x: ToFloat64_0d) -> np.float64 | np.complex128: ...
@overload
def arctanh(x: ToLongDouble_0d) -> np.longdouble | np.complex128: ...
@overload
def arctanh(x: ToFloat32_0d) -> np.float32 | np.complex64: ...
@overload
def arctanh(x: ToFloat16_0d) -> np.float16 | np.complex128: ...
@overload
def arctanh(x: ToComplex128_0d) -> np.complex128: ...
@overload
def arctanh(x: ToCLongDouble_0d) -> np.complex128 | np.clongdouble: ...
@overload
def arctanh(x: ToComplex64_0d) -> np.complex64: ...
@overload
def arctanh(x: ToComplex_0d) -> np.complexfloating: ...
@overload
def arctanh(x: CoComplex_0d) -> np.inexact: ...
@overload
def arctanh(x: ToBool_1nd) -> Array[np.float16 | np.complex64]: ...
@overload
def arctanh(x: _ToArray2_1nd[integer64 | integer32, JustInt]) -> Array[np.float64 | np.complex128]: ...
@overload
def arctanh(x: _ToArray_1nd[integer16]) -> Array[np.float32 | np.complex64]: ...
@overload
def arctanh(x: _ToArray_1nd[integer8]) -> Array[np.float16 | np.complex64]: ...
@overload
def arctanh(x: ToFloat64_1nd) -> Array[np.float64 | np.complex128]: ...
@overload
def arctanh(x: ToLongDouble_1nd) -> Array[np.longdouble | np.complex128]: ...
@overload
def arctanh(x: ToFloat32_1nd) -> Array[np.float32 | np.complex64]: ...
@overload
def arctanh(x: ToFloat16_1nd) -> Array[np.float16 | np.complex128]: ...
@overload
def arctanh(x: ToComplex128_1nd) -> Array[np.complex128]: ...
@overload
def arctanh(x: ToCLongDouble_1nd) -> Array[np.complex128 | np.clongdouble]: ...
@overload
def arctanh(x: ToComplex64_1nd) -> Array[np.complex64]: ...
@overload
def arctanh(x: ToComplex_1nd) -> Array[np.complexfloating]: ...
@overload
def arctanh(x: CoComplex_1nd) -> Array[np.inexact]: ...

#
@overload
def logn(n: CoUInt8_0d, x: CoUInt8_0d) -> np.float16: ...
@overload
def logn(n: CoUInt64_0d, x: CoUInt64_0d) -> np.floating: ...
@overload
def logn(n: ToComplex_0d, x: CoComplex_0d) -> np.complexfloating: ...
@overload
def logn(n: CoComplex_0d, x: ToComplex_0d) -> np.complexfloating: ...
@overload
def logn(n: CoComplex_0d, x: CoComplex_0d) -> np.inexact: ...
@overload
def logn(n: CoUInt8_nd, x: CoUInt8_1nd) -> Array[np.float16]: ...
@overload
def logn(n: CoUInt8_1nd, x: CoUInt8_nd) -> Array[np.float16]: ...
@overload
def logn(n: CoUInt64_nd, x: CoUInt64_1nd) -> Array[np.floating]: ...
@overload
def logn(n: CoUInt64_1nd, x: CoUInt64_nd) -> Array[np.floating]: ...
@overload
def logn(n: ToComplex_nd, x: CoComplex_1nd) -> Array[np.complexfloating]: ...
@overload
def logn(n: ToComplex_1nd, x: CoComplex_nd) -> Array[np.complexfloating]: ...
@overload
def logn(n: CoComplex_nd, x: ToComplex_1nd) -> Array[np.complexfloating]: ...
@overload
def logn(n: CoComplex_1nd, x: ToComplex_nd) -> Array[np.complexfloating]: ...
@overload
def logn(n: CoComplex_nd, x: CoComplex_1nd) -> Array[np.inexact]: ...
@overload
def logn(n: CoComplex_1nd, x: CoComplex_nd) -> Array[np.inexact]: ...

#
@overload
def power(x: CoInt8_0d, p: CoInt8_0d) -> np.int8: ...
@overload
def power(x: ToUInteger_0d, p: CoUInt64_0d) -> np.unsignedinteger: ...
@overload
def power(x: CoUInt64_0d, p: ToUInteger_0d) -> np.unsignedinteger: ...
@overload
def power(x: CoUInt64_0d, p: ToSInteger_0d) -> np.signedinteger | np.float64: ...
@overload
def power(x: CoUInt64_0d, p: ToFloating_0d) -> np.floating: ...
@overload
def power(x: ToSInteger_0d, p: CoUInt64_0d) -> np.signedinteger | np.complexfloating: ...
@overload
def power(x: ToSInteger_0d, p: CoInteger_0d) -> np.signedinteger | np.inexact: ...
@overload
def power(x: ToFloating_0d, p: CoFloating_0d) -> np.inexact: ...
@overload
def power(x: CoFloating_0d, p: ToFloating_0d) -> np.inexact: ...
@overload
def power(x: ToComplex_0d, p: CoComplex_0d) -> np.complexfloating: ...
@overload
def power(x: CoComplex_0d, p: ToComplex_0d) -> np.complexfloating: ...
@overload
def power(x: CoInt8_nd, p: CoInt8_1nd) -> Array[np.int8]: ...
@overload
def power(x: CoInt8_1nd, p: CoInt8_nd) -> Array[np.int8]: ...
@overload
def power(x: ToUInteger_1nd, p: CoUInt64_nd) -> Array[np.unsignedinteger]: ...
@overload
def power(x: CoUInt64_1nd, p: ToUInteger_nd) -> Array[np.unsignedinteger]: ...
@overload
def power(x: CoUInt64_1nd, p: ToSInteger_nd) -> Array[np.signedinteger | np.float64]: ...
@overload
def power(x: CoUInt64_nd, p: ToSInteger_1nd) -> Array[np.signedinteger | np.float64]: ...
@overload
def power(x: CoUInt64_1nd, p: ToFloating_nd) -> Array[np.floating]: ...
@overload
def power(x: CoUInt64_nd, p: ToFloating_1nd) -> Array[np.floating]: ...
@overload
def power(x: ToUInteger_nd, p: CoUInt64_1nd) -> Array[np.unsignedinteger]: ...
@overload
def power(x: CoUInt64_nd, p: ToUInteger_1nd) -> Array[np.unsignedinteger]: ...
@overload
def power(x: ToSInteger_1nd, p: CoUInt64_nd) -> Array[np.signedinteger | np.complexfloating]: ...
@overload
def power(x: ToSInteger_nd, p: CoUInt64_1nd) -> Array[np.signedinteger | np.complexfloating]: ...
@overload
def power(x: ToSInteger_1nd, p: CoInteger_nd) -> Array[np.signedinteger | np.inexact]: ...
@overload
def power(x: ToSInteger_nd, p: CoInteger_1nd) -> Array[np.signedinteger | np.inexact]: ...
@overload
def power(x: ToFloating_1nd, p: CoFloating_nd) -> Array[np.inexact]: ...
@overload
def power(x: ToFloating_nd, p: CoFloating_1nd) -> Array[np.inexact]: ...
@overload
def power(x: CoFloating_1nd, p: ToFloating_nd) -> Array[np.inexact]: ...
@overload
def power(x: CoFloating_nd, p: ToFloating_1nd) -> Array[np.inexact]: ...
@overload
def power(x: CoComplex_nd, p: ToComplex_1nd) -> Array[np.complexfloating]: ...
@overload
def power(x: CoComplex_1nd, p: ToComplex_nd) -> Array[np.complexfloating]: ...
@overload
def power(x: ToComplex_nd, p: CoComplex_1nd) -> Array[np.complexfloating]: ...
@overload
def power(x: ToComplex_1nd, p: CoComplex_nd) -> Array[np.complexfloating]: ...
