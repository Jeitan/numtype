import re
from _typeshed import Incomplete, StrOrBytesPath, StrPath
from collections.abc import Callable, Iterable, Mapping
from typing import IO, Any, Concatenate, Final, Literal as L, ParamSpec, TypeAlias, overload
from typing_extensions import Never

from .__version__ import version
from .auxfuncs import isintent_dict as isintent_dict

###

_Tss = ParamSpec("_Tss")

_VisitResult: TypeAlias = list[Any] | dict[str, Any] | None
_VisitItem: TypeAlias = tuple[str | None, _VisitResult]
_VisitFunc: TypeAlias = Callable[Concatenate[_VisitItem, list[_VisitItem], _VisitResult, _Tss], _VisitItem | None]

###

COMMON_FREE_EXTENSIONS: Final[list[str]] = ...
COMMON_FIXED_EXTENSIONS: Final[list[str]] = ...

f2py_version: Final = version
tabchar: Final[str] = "    "

f77modulename: str
pyffilename: str
sourcecodeform: L["fix", "gree"]
strictf77: L[0, 1]
quiet: L[0, 1]
verbose: L[0, 1, 2]
skipemptyends: L[0, 1]
ignorecontains: L[1]
dolowercase: L[1]

beginpattern: str | re.Pattern[str]
currentfilename: str
filepositiontext: str
expectbegin: L[0, 1]
gotnextfile: L[0, 1]
neededmodule: int
skipblocksuntil: int
groupcounter: int
groupname: dict[int, str] | str
groupcache: dict[int, dict[str, Any]] | None
grouplist: dict[int, list[dict[str, Any]]] | None
previous_context: tuple[str, str, int] | None

f90modulevars: dict[str, dict[str, Any]] = {}
debug: list[Never] = []
include_paths: list[str] = []
onlyfuncs: list[str] = []
skipfuncs: list[str] = []
skipfunctions: Final[list[str]] = []
usermodules: Final[list[dict[str, Any]]] = []

defaultimplicitrules: Final[dict[str, dict[str, str]]] = {}
badnames: Final[dict[str, str]] = {}
invbadnames: Final[dict[str, str]] = {}

beforethisafter: Final[str] = ...
fortrantypes: Final[str] = ...
groupbegins77: Final[str] = ...
groupbegins90: Final[str] = ...
groupends: Final[str] = ...
endifs: Final[str] = ...
moduleprocedures: Final[str] = ...

beginpattern77: Final[tuple[re.Pattern[str], L["begin"]]] = ...
beginpattern90: Final[tuple[re.Pattern[str], L["begin"]]] = ...
callpattern: Final[tuple[re.Pattern[str], L["call"]]] = ...
callfunpattern: Final[tuple[re.Pattern[str], L["callfun"]]] = ...
commonpattern: Final[tuple[re.Pattern[str], L["common"]]] = ...
containspattern: Final[tuple[re.Pattern[str], L["contains"]]] = ...
datapattern: Final[tuple[re.Pattern[str], L["data"]]] = ...
dimensionpattern: Final[tuple[re.Pattern[str], L["dimension"]]] = ...
endifpattern: Final[tuple[re.Pattern[str], L["endif"]]] = ...
endpattern: Final[tuple[re.Pattern[str], L["end"]]] = ...
entrypattern: Final[tuple[re.Pattern[str], L["entry"]]] = ...
externalpattern: Final[tuple[re.Pattern[str], L["external"]]] = ...
f2pyenhancementspattern: Final[tuple[re.Pattern[str], L["f2pyenhancements"]]] = ...
formatpattern: Final[tuple[re.Pattern[str], L["format"]]] = ...
functionpattern: Final[tuple[re.Pattern[str], L["begin"]]] = ...
implicitpattern: Final[tuple[re.Pattern[str], L["implicit"]]] = ...
intentpattern: Final[tuple[re.Pattern[str], L["intent"]]] = ...
intrinsicpattern: Final[tuple[re.Pattern[str], L["intrinsic"]]] = ...
optionalpattern: Final[tuple[re.Pattern[str], L["optional"]]] = ...
moduleprocedurepattern: Final[tuple[re.Pattern[str], L["moduleprocedure"]]] = ...
multilinepattern: Final[tuple[re.Pattern[str], L["multiline"]]] = ...
parameterpattern: Final[tuple[re.Pattern[str], L["parameter"]]] = ...
privatepattern: Final[tuple[re.Pattern[str], L["private"]]] = ...
publicpattern: Final[tuple[re.Pattern[str], L["public"]]] = ...
requiredpattern: Final[tuple[re.Pattern[str], L["required"]]] = ...
subroutinepattern: Final[tuple[re.Pattern[str], L["begin"]]] = ...
typespattern: Final[tuple[re.Pattern[str], L["type"]]] = ...
usepattern: Final[tuple[re.Pattern[str], L["use"]]] = ...

analyzeargs_re_1: Final[re.Pattern[str]] = ...
callnameargspattern: Final[re.Pattern[str]] = ...
charselector: Final[re.Pattern[str]] = ...
crackline_bind_1: Final[re.Pattern[str]] = ...
crackline_bindlang: Final[re.Pattern[str]] = ...
crackline_re_1: Final[re.Pattern[str]] = ...
determineexprtype_re_1: Final[re.Pattern[str]] = ...
determineexprtype_re_2: Final[re.Pattern[str]] = ...
determineexprtype_re_3: Final[re.Pattern[str]] = ...
determineexprtype_re_4: Final[re.Pattern[str]] = ...
determineexprtype_re_5: Final[re.Pattern[str]] = ...
getlincoef_re_1: Final[re.Pattern[str]] = ...
kindselector: Final[re.Pattern[str]] = ...
lenarraypattern: Final[re.Pattern[str]] = ...
lenkindpattern: Final[re.Pattern[str]] = ...
namepattern: Final[re.Pattern[str]] = ...
nameargspattern: Final[re.Pattern[str]] = ...
operatorpattern: Final[re.Pattern[str]] = ...
real16pattern: Final[re.Pattern[str]] = ...
real8pattern: Final[re.Pattern[str]] = ...
selectpattern: Final[re.Pattern[str]] = ...
typedefpattern: Final[re.Pattern[str]] = ...
typespattern4implicit: Final[re.Pattern[str]] = ...
word_pattern: Final[re.Pattern[str]] = ...

post_processing_hooks: Final[list[_VisitFunc[...]]] = []

#
def outmess(line: str, flag: int = 1) -> None: ...
def reset_global_f2py_vars() -> None: ...

#
def rmbadname1(name: str) -> str: ...
def undo_rmbadname1(name: str) -> str: ...
def rmbadname(names: Iterable[str]) -> list[str]: ...
def undo_rmbadname(names: Iterable[str]) -> list[str]: ...

#
def openhook(filename: StrPath, mode: str) -> IO[Any]: ...
def is_free_format(fname: StrPath) -> bool: ...
def readfortrancode(
    ffile: StrOrBytesPath | Iterable[StrOrBytesPath],
    dowithline: Callable[[str, int], object] = ...,
    istop: int = 1,
) -> None: ...

#
def split_by_unquoted(line: str, characters: str) -> tuple[str, str]: ...

#
def crackline(line: str, reset: int = 0) -> None: ...
def markouterparen(line: str) -> str: ...
def markoutercomma(line: str, comma: str = ",") -> str: ...
def unmarkouterparen(line: str) -> str: ...
def appenddecl(
    decl: Mapping[str, Incomplete] | None,
    decl2: Mapping[str, Incomplete] | None,
    force: int = 1,
) -> dict[str, Incomplete]: ...

#
def parse_name_for_bind(line: str) -> tuple[str, str | None]: ...
def analyzeline(m: re.Match[str], case: str, line: str) -> None: ...
def appendmultiline(group: dict[str, Incomplete], context_name: str, ml: str) -> None: ...
def cracktypespec0(typespec: str, ll: str | None) -> tuple[str, str | None, str | None, str | None]: ...

#
def removespaces(expr: str) -> str: ...
def markinnerspaces(line: str) -> str: ...
def updatevars(typespec: str, selector: str | None, attrspec: str, entitydecl: str) -> str: ...
def cracktypespec(typespec: str, selector: str | None) -> tuple[dict[str, str] | None, dict[str, str] | None, str | None]: ...

#
def setattrspec(decl: dict[str, list[str]], attr: str | None, force: int = 0) -> dict[str, list[str]]: ...
def setkindselector(decl: dict[str, dict[str, str]], sel: dict[str, str], force: int = 0) -> dict[str, dict[str, str]]: ...
def setcharselector(decl: dict[str, dict[str, str]], sel: dict[str, str], force: int = 0) -> dict[str, dict[str, str]]: ...
def getblockname(block: Mapping[str, Any], unknown: str = "unknown") -> str: ...
def setmesstext(block: Mapping[str, Any]) -> None: ...
def get_usedict(block: Mapping[str, Any]) -> dict[str, str]: ...
def get_useparameters(block: Mapping[str, Any], param_map: Mapping[str, str] | None = None) -> dict[str, str]: ...

#
@overload
def postcrack2(
    block: dict[str, Any],
    tab: str = "",
    param_map: Mapping[str, str] | None = None,
) -> dict[str, str | Incomplete]: ...
@overload
def postcrack2(
    block: list[dict[str, Any]],
    tab: str = "",
    param_map: Mapping[str, str] | None = None,
) -> list[dict[str, str | Incomplete]]: ...

#
@overload
def postcrack(
    block: dict[str, Any],
    args: Mapping[str, str] | None = None,
    tab: str = "",
) -> dict[str, Incomplete]: ...
@overload
def postcrack(
    block: list[dict[str, str]],
    args: Mapping[str, str] | None = None,
    tab: str = "",
) -> list[dict[str, Incomplete]]: ...

#
def sortvarnames(vars: Mapping[str, Any]) -> list[str]: ...
def analyzecommon(block: Mapping[str, Any]) -> dict[str, Incomplete]: ...
def analyzebody(block: Mapping[str, Any], args: Mapping[str, str], tab: str = "") -> list[dict[str, Incomplete]]: ...
def buildimplicitrules(block: Mapping[str, Any]) -> tuple[dict[str, dict[str, str]], dict[str, str]]: ...
def myeval(e: str, g: Incomplete | None = None, l: Incomplete | None = None) -> float: ...

#
def getlincoef(e: str, xset: set[str]) -> tuple[float | None, float | None, str | None]: ...

#
def get_sorted_names(vars: Mapping[str, Mapping[str, str]]) -> list[str]: ...
def get_parameters(vars: Mapping[str, Mapping[str, str]], global_params: dict[str, str] = {}) -> dict[str, str]: ...

#
def analyzevars(block: Mapping[str, Any]) -> dict[str, dict[str, str]]: ...

#
def param_eval(v: str, g_params: dict[str, Any], params: Mapping[str, Any], dimspec: str | None = None) -> dict[str, Any]: ...
def param_parse(d: str, params: Mapping[str, str]) -> str: ...
def expr2name(a: str, block: Mapping[str, Any], args: list[str] = []) -> str: ...
def analyzeargs(block: Mapping[str, Any]) -> dict[str, Any]: ...

#
def determineexprtype(expr: str, vars: Mapping[str, Any], rules: dict[str, Any] = {}) -> dict[str, Any]: ...
def crack2fortrangen(block: Mapping[str, Any], tab: str = "\n", as_interface: bool = False) -> str: ...
def common2fortran(common: Mapping[str, Any], tab: str = "") -> str: ...
def use2fortran(use: Mapping[str, Any], tab: str = "") -> str: ...
def true_intent_list(var: dict[str, list[str]]) -> list[str]: ...
def vars2fortran(
    block: Mapping[str, Mapping[str, Any]],
    vars: Mapping[str, Any],
    args: Mapping[str, str],
    tab: str = "",
    as_interface: bool = False,
) -> str: ...

#
def crackfortran(files: StrOrBytesPath | Iterable[StrOrBytesPath]) -> list[dict[str, Any]]: ...
def crack2fortran(block: Mapping[str, Any]) -> str: ...

#
def traverse(
    obj: tuple[str | None, _VisitResult],
    visit: _VisitFunc[_Tss],
    parents: list[tuple[str | None, _VisitResult]] = [],
    result: list[Any] | dict[str, Any] | None = None,
    *args: _Tss.args,
    **kwargs: _Tss.kwargs,
) -> _VisitItem | _VisitResult: ...

#
def character_backward_compatibility_hook(
    item: _VisitItem,
    parents: list[_VisitItem],
    result: object,  # ignored
    *args: object,  # ignored
    **kwargs: object,  # ignored
) -> _VisitItem | None: ...

# namespace pollution
c: str
n: str
