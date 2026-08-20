---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Machine-Modes.html
archived_at: '2026-07-15T07:31:02.308173Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Constants](Constants.md#apple-inxw443umfxhi4y),
Previous: [Flags](Flags.md#apple-izwgcz3t),
Up: [RTL](RTL.md#apple-kjkey)

---

### 12.6 Machine Modes

A machine mode describes a size of data object and the representation used
for it. In the C code, machine modes are represented by an enumeration
type, `enum machine_mode`, defined in `machmode.def`. Each RTL
expression has room for a machine mode and so do certain kinds of tree
expressions (declarations and types, to be precise).

In debugging dumps and machine descriptions, the machine mode of an RTL
expression is written after the expression code with a colon to separate
them. The letters ``mode`' which appear at the end of each machine mode
name are omitted. For example, `(reg:SI 38)` is a `reg`
expression with machine mode `SImode`. If the mode is
`VOIDmode`, it is not written at all.

Here is a table of machine modes. The term “byte” below refers to an
object of `BITS_PER_UNIT` bits (see [Storage Layout](Storage-Layout.md#apple-kn2g64tbm5ss2tdbpfxxk5a)).

**`BImode`**
: “Bit” mode represents a single bit, for predicate registers.

**`QImode`**
: “Quarter-Integer” mode represents a single byte treated as an integer.

**`HImode`**
: “Half-Integer” mode represents a two-byte integer.

**`PSImode`**
: “Partial Single Integer” mode represents an integer which occupies
four bytes but which doesn't really use all four. On some machines,
this is the right mode to use for pointers.

**`SImode`**
: “Single Integer” mode represents a four-byte integer.

**`PDImode`**
: “Partial Double Integer” mode represents an integer which occupies
eight bytes but which doesn't really use all eight. On some machines,
this is the right mode to use for certain pointers.

**`DImode`**
: “Double Integer” mode represents an eight-byte integer.

**`TImode`**
: “Tetra Integer” (?) mode represents a sixteen-byte integer.

**`OImode`**
: “Octa Integer” (?) mode represents a thirty-two-byte integer.

**`QFmode`**
: “Quarter-Floating” mode represents a quarter-precision (single byte)
floating point number.

**`HFmode`**
: “Half-Floating” mode represents a half-precision (two byte) floating
point number.

**`TQFmode`**
: “Three-Quarter-Floating” (?) mode represents a three-quarter-precision
(three byte) floating point number.

**`SFmode`**
: “Single Floating” mode represents a four byte floating point number.
In the common case, of a processor with IEEE arithmetic and 8-bit bytes,
this is a single-precision IEEE floating point number; it can also be
used for double-precision (on processors with 16-bit bytes) and
single-precision VAX and IBM types.

**`DFmode`**
: “Double Floating” mode represents an eight byte floating point number.
In the common case, of a processor with IEEE arithmetic and 8-bit bytes,
this is a double-precision IEEE floating point number.

**`XFmode`**
: “Extended Floating” mode represents an IEEE extended floating point
number. This mode only has 80 meaningful bits (ten bytes). Some
processors require such numbers to be padded to twelve bytes, others
to sixteen; this mode is used for either.

**`SDmode`**
: “Single Decimal Floating” mode represents a four byte decimal
floating point number (as distinct from conventional binary floating
point).

**`DDmode`**
: “Double Decimal Floating” mode represents an eight byte decimal
floating point number.

**`TDmode`**
: “Tetra Decimal Floating” mode represents a sixteen byte decimal
floating point number all 128 of whose bits are meaningful.

**`TFmode`**
: “Tetra Floating” mode represents a sixteen byte floating point number
all 128 of whose bits are meaningful. One common use is the
IEEE quad-precision format.

**`CCmode`**
: “Condition Code” mode represents the value of a condition code, which
is a machine-specific set of bits used to represent the result of a
comparison operation. Other machine-specific modes may also be used for
the condition code. These modes are not used on machines that use
`cc0` (see see [Condition Code](Condition-Code.md#apple-inxw4zdjoruw63rninxwizi)).

**`BLKmode`**
: “Block” mode represents values that are aggregates to which none of
the other modes apply. In RTL, only memory references can have this mode,
and only if they appear in string-move or vector instructions. On machines
which have no such instructions, `BLKmode` will not appear in RTL.

**`VOIDmode`**
: Void mode means the absence of a mode or an unspecified mode.
For example, RTL expressions of code `const_int` have mode
`VOIDmode` because they can be taken to have whatever mode the context
requires. In debugging dumps of RTL, `VOIDmode` is expressed by
the absence of any mode.

**`QCmode, HCmode, SCmode, DCmode, XCmode, TCmode`**
: These modes stand for a complex number represented as a pair of floating
point values. The floating point values are in `QFmode`,
`HFmode`, `SFmode`, `DFmode`, `XFmode`, and
`TFmode`, respectively.

**`CQImode, CHImode, CSImode, CDImode, CTImode, COImode`**
: These modes stand for a complex number represented as a pair of integer
values. The integer values are in `QImode`, `HImode`,
`SImode`, `DImode`, `TImode`, and `OImode`,
respectively.

The machine description defines `Pmode` as a C macro which expands
into the machine mode used for addresses. Normally this is the mode
whose size is `BITS_PER_WORD`, `SImode` on 32-bit machines.

The only modes which a machine description _must_ support are
`QImode`, and the modes corresponding to `BITS_PER_WORD`,
`FLOAT_TYPE_SIZE` and `DOUBLE_TYPE_SIZE`.
The compiler will attempt to use `DImode` for 8-byte structures and
unions, but this can be prevented by overriding the definition of
`MAX_FIXED_MODE_SIZE`. Alternatively, you can have the compiler
use `TImode` for 16-byte structures and unions. Likewise, you can
arrange for the C type `short int` to avoid using `HImode`.

Very few explicit references to machine modes remain in the compiler and
these few references will soon be removed. Instead, the machine modes
are divided into mode classes. These are represented by the enumeration
type `enum mode_class` defined in `machmode.h`. The possible
mode classes are:

**`MODE_INT`**
: Integer modes. By default these are `BImode`, `QImode`,
`HImode`, `SImode`, `DImode`, `TImode`, and
`OImode`.

**`MODE_PARTIAL_INT`**
: The “partial integer” modes, `PQImode`, `PHImode`,
`PSImode` and `PDImode`.

**`MODE_FLOAT`**
: Floating point modes. By default these are `QFmode`,
`HFmode`, `TQFmode`, `SFmode`, `DFmode`,
`XFmode` and `TFmode`.

**`MODE_DECIMAL_FLOAT`**
: Decimal floating point modes. By default these are `SDmode`,
`DDmode` and `TDmode`.

**`MODE_COMPLEX_INT`**
: Complex integer modes. (These are not currently implemented).

**`MODE_COMPLEX_FLOAT`**
: Complex floating point modes. By default these are `QCmode`,
`HCmode`, `SCmode`, `DCmode`, `XCmode`, and
`TCmode`.

**`MODE_FUNCTION`**
: Algol or Pascal function variables including a static chain.
(These are not currently implemented).

**`MODE_CC`**
: Modes representing condition code values. These are `CCmode` plus
any `CC_MODE` modes listed in the `machine-modes.def`.
See [Jump Patterns](Jump-Patterns.md#apple-jj2w24bnkbqxi5dfojxhg),
also see [Condition Code](Condition-Code.md#apple-inxw4zdjoruw63rninxwizi).

**`MODE_RANDOM`**
: This is a catchall mode class for modes which don't fit into the above
classes. Currently `VOIDmode` and `BLKmode` are in
`MODE_RANDOM`.

Here are some C macros that relate to machine modes:

**`GET_MODE (`x`)`**
: Returns the machine mode of the RTX x.

**`PUT_MODE (`x`,` newmode`)`**
: Alters the machine mode of the RTX x to be newmode.

**`NUM_MACHINE_MODES`**
: Stands for the number of machine modes available on the target
machine. This is one greater than the largest numeric value of any
machine mode.

**`GET_MODE_NAME (`m`)`**
: Returns the name of mode m as a string.

**`GET_MODE_CLASS (`m`)`**
: Returns the mode class of mode m.

**`GET_MODE_WIDER_MODE (`m`)`**
: Returns the next wider natural mode. For example, the expression
`GET_MODE_WIDER_MODE (QImode)` returns `HImode`.

**`GET_MODE_SIZE (`m`)`**
: Returns the size in bytes of a datum of mode m.

**`GET_MODE_BITSIZE (`m`)`**
: Returns the size in bits of a datum of mode m.

**`GET_MODE_MASK (`m`)`**
: Returns a bitmask containing 1 for all bits in a word that fit within
mode m. This macro can only be used for modes whose bitsize is
less than or equal to `HOST_BITS_PER_INT`.

**`GET_MODE_ALIGNMENT (`m`)`**
: Return the required alignment, in bits, for an object of mode m.

**`GET_MODE_UNIT_SIZE (`m`)`**
: Returns the size in bytes of the subunits of a datum of mode m.
This is the same as `GET_MODE_SIZE` except in the case of complex
modes. For them, the unit size is the size of the real or imaginary
part.

**`GET_MODE_NUNITS (`m`)`**
: Returns the number of units contained in a mode, i.e.,
`GET_MODE_SIZE` divided by `GET_MODE_UNIT_SIZE`.

**`GET_CLASS_NARROWEST_MODE (`c`)`**
: Returns the narrowest mode in mode class c.

The global variables `byte_mode` and `word_mode` contain modes
whose classes are `MODE_INT` and whose bitsizes are either
`BITS_PER_UNIT` or `BITS_PER_WORD`, respectively. On 32-bit
machines, these are `QImode` and `SImode`, respectively.
