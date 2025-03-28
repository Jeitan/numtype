# NOTE: numpy.compat is deprecated since 1.26.0

from numpy._utils._inspect import formatargspec, getargspec

from .py3k import (
    Path,
    asbytes,
    asbytes_nested,
    asstr,
    asunicode,
    asunicode_nested,
    basestring,
    bytes,
    contextlib_nullcontext,
    getexception,
    integer_types,
    is_pathlib_path,
    isfileobj,
    long,
    npy_load_module,
    open_latin1,
    os_PathLike,
    os_fspath,
    pickle,
    sixu,
    strchar,
    unicode,
)

__all__ = [
    "Path",
    "asbytes",
    "asbytes_nested",
    "asstr",
    "asunicode",
    "asunicode_nested",
    "basestring",
    "bytes",
    "contextlib_nullcontext",
    "formatargspec",
    "getargspec",
    "getexception",
    "integer_types",
    "is_pathlib_path",
    "isfileobj",
    "long",
    "npy_load_module",
    "open_latin1",
    "os_PathLike",
    "os_fspath",
    "pickle",
    "sixu",
    "strchar",
    "unicode",
]
