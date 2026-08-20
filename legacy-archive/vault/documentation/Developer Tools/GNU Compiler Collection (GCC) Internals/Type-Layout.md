---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Type-Layout.html
archived_at: '2026-07-15T07:31:00.964321Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Registers](Registers.md#apple-kjswo2ltorsxe4y),
Previous: [Storage Layout](Storage-Layout.md#apple-kn2g64tbm5ss2tdbpfxxk5a),
Up: [Target Macros](Target-Macros.md#apple-krqxez3foqwu2yldojxxg)

---

### 13.6 Layout of Source Language Data Types

These macros define the sizes and other characteristics of the standard
basic data types used in programs being compiled. Unlike the macros in
the previous section, these apply to specific features of C and related
languages, rather than to fundamental aspects of storage layout.

— Macro: __INT_TYPE_SIZE__
> A C expression for the size in bits of the type `int` on the
> target machine. If you don't define this, the default is one word.

— Macro: __SHORT_TYPE_SIZE__
> A C expression for the size in bits of the type `short` on the
> target machine. If you don't define this, the default is half a word.
> (If this would be less than one storage unit, it is rounded up to one
> unit.)

— Macro: __LONG_TYPE_SIZE__
> A C expression for the size in bits of the type `long` on the
> target machine. If you don't define this, the default is one word.

— Macro: __ADA_LONG_TYPE_SIZE__
> On some machines, the size used for the Ada equivalent of the type
> `long` by a native Ada compiler differs from that used by C. In
> that situation, define this macro to be a C expression to be used for
> the size of that type. If you don't define this, the default is the
> value of `LONG_TYPE_SIZE`.

— Macro: __LONG_LONG_TYPE_SIZE__
> A C expression for the size in bits of the type `long long` on the
> target machine. If you don't define this, the default is two
> words. If you want to support GNU Ada on your machine, the value of this
> macro must be at least 64.

— Macro: __CHAR_TYPE_SIZE__
> A C expression for the size in bits of the type `char` on the
> target machine. If you don't define this, the default is
> `BITS_PER_UNIT`.

— Macro: __BOOL_TYPE_SIZE__
> A C expression for the size in bits of the C++ type `bool` and
> C99 type `_Bool` on the target machine. If you don't define
> this, and you probably shouldn't, the default is `CHAR_TYPE_SIZE`.

— Macro: __FLOAT_TYPE_SIZE__
> A C expression for the size in bits of the type `float` on the
> target machine. If you don't define this, the default is one word.

— Macro: __DOUBLE_TYPE_SIZE__
> A C expression for the size in bits of the type `double` on the
> target machine. If you don't define this, the default is two
> words.

— Macro: __LONG_DOUBLE_TYPE_SIZE__
> A C expression for the size in bits of the type `long double` on
> the target machine. If you don't define this, the default is two
> words.

— Macro: __LIBGCC2_LONG_DOUBLE_TYPE_SIZE__
> Define this macro if `LONG_DOUBLE_TYPE_SIZE` is not constant or
> if you want routines in `libgcc2.a` for a size other than
> `LONG_DOUBLE_TYPE_SIZE`. If you don't define this, the
> default is `LONG_DOUBLE_TYPE_SIZE`.

— Macro: __LIBGCC2_HAS_DF_MODE__
> Define this macro if neither `LIBGCC2_DOUBLE_TYPE_SIZE` nor
> `LIBGCC2_LONG_DOUBLE_TYPE_SIZE` is
> `DFmode` but you want `DFmode` routines in `libgcc2.a`
> anyway. If you don't define this and either `LIBGCC2_DOUBLE_TYPE_SIZE`
> or `LIBGCC2_LONG_DOUBLE_TYPE_SIZE` is 64 then the default is 1,
> otherwise it is 0.

— Macro: __LIBGCC2_HAS_XF_MODE__
> Define this macro if `LIBGCC2_LONG_DOUBLE_TYPE_SIZE` is not
> `XFmode` but you want `XFmode` routines in `libgcc2.a`
> anyway. If you don't define this and `LIBGCC2_LONG_DOUBLE_TYPE_SIZE`
> is 80 then the default is 1, otherwise it is 0.

— Macro: __LIBGCC2_HAS_TF_MODE__
> Define this macro if `LIBGCC2_LONG_DOUBLE_TYPE_SIZE` is not
> `TFmode` but you want `TFmode` routines in `libgcc2.a`
> anyway. If you don't define this and `LIBGCC2_LONG_DOUBLE_TYPE_SIZE`
> is 128 then the default is 1, otherwise it is 0.

— Macro: __TARGET_FLT_EVAL_METHOD__
> A C expression for the value for `FLT_EVAL_METHOD` in `float.h`,
> assuming, if applicable, that the floating-point control word is in its
> default state. If you do not define this macro the value of
> `FLT_EVAL_METHOD` will be zero.

— Macro: __WIDEST_HARDWARE_FP_SIZE__
> A C expression for the size in bits of the widest floating-point format
> supported by the hardware. If you define this macro, you must specify a
> value less than or equal to the value of `LONG_DOUBLE_TYPE_SIZE`.
> If you do not define this macro, the value of `LONG_DOUBLE_TYPE_SIZE`
> is the default.

— Macro: __DEFAULT_SIGNED_CHAR__
> An expression whose value is 1 or 0, according to whether the type
> `char` should be signed or unsigned by default. The user can
> always override this default with the options `-fsigned-char`
> and `-funsigned-char`.

— Target Hook: bool __TARGET_DEFAULT_SHORT_ENUMS__ (void)
> This target hook should return true if the compiler should give an
> `enum` type only as many bytes as it takes to represent the range
> of possible values of that type. It should return false if all
> `enum` types should be allocated like `int`.
>
> The default is to return false.

— Macro: __SIZE_TYPE__
> A C expression for a string describing the name of the data type to use
> for size values. The typedef name `size_t` is defined using the
> contents of the string.
>
> The string can contain more than one keyword. If so, separate them with
> spaces, and write first any length keyword, then `unsigned` if
> appropriate, and finally `int`. The string must exactly match one
> of the data type names defined in the function
> `init_decl_processing` in the file `c-decl.c`. You may not
> omit `int` or change the order—that would cause the compiler to
> crash on startup.
>
> If you don't define this macro, the default is `"long unsigned
> int"`.

— Macro: __PTRDIFF_TYPE__
> A C expression for a string describing the name of the data type to use
> for the result of subtracting two pointers. The typedef name
> `ptrdiff_t` is defined using the contents of the string. See
> `SIZE_TYPE` above for more information.
>
> If you don't define this macro, the default is `"long int"`.

— Macro: __WCHAR_TYPE__
> A C expression for a string describing the name of the data type to use
> for wide characters. The typedef name `wchar_t` is defined using
> the contents of the string. See `SIZE_TYPE` above for more
> information.
>
> If you don't define this macro, the default is `"int"`.

— Macro: __WCHAR_TYPE_SIZE__
> A C expression for the size in bits of the data type for wide
> characters. This is used in `cpp`, which cannot make use of
> `WCHAR_TYPE`.

— Macro: __WINT_TYPE__
> A C expression for a string describing the name of the data type to
> use for wide characters passed to `printf` and returned from
> `getwc`. The typedef name `wint_t` is defined using the
> contents of the string. See `SIZE_TYPE` above for more
> information.
>
> If you don't define this macro, the default is `"unsigned int"`.

— Macro: __INTMAX_TYPE__
> A C expression for a string describing the name of the data type that
> can represent any value of any standard or extended signed integer type.
> The typedef name `intmax_t` is defined using the contents of the
> string. See `SIZE_TYPE` above for more information.
>
> If you don't define this macro, the default is the first of
> `"int"`, `"long int"`, or `"long long int"` that has as
> much precision as `long long int`.

— Macro: __UINTMAX_TYPE__
> A C expression for a string describing the name of the data type that
> can represent any value of any standard or extended unsigned integer
> type. The typedef name `uintmax_t` is defined using the contents
> of the string. See `SIZE_TYPE` above for more information.
>
> If you don't define this macro, the default is the first of
> `"unsigned int"`, `"long unsigned int"`, or `"long long
> unsigned int"` that has as much precision as `long long unsigned
> int`.

— Macro: __TARGET_PTRMEMFUNC_VBIT_LOCATION__
> The C++ compiler represents a pointer-to-member-function with a struct
> that looks like:
>
> ```
>             struct {
>               union {
>                 void (*fn)();
>                 ptrdiff_t vtable_index;
>               };
>               ptrdiff_t delta;
>             };
>
> ```
>
> The C++ compiler must use one bit to indicate whether the function that
> will be called through a pointer-to-member-function is virtual.
> Normally, we assume that the low-order bit of a function pointer must
> always be zero. Then, by ensuring that the vtable_index is odd, we can
> distinguish which variant of the union is in use. But, on some
> platforms function pointers can be odd, and so this doesn't work. In
> that case, we use the low-order bit of the `delta` field, and shift
> the remainder of the `delta` field to the left.
>
> GCC will automatically make the right selection about where to store
> this bit using the `FUNCTION_BOUNDARY` setting for your platform.
> However, some platforms such as ARM/Thumb have `FUNCTION_BOUNDARY`
> set such that functions always start at even addresses, but the lowest
> bit of pointers to functions indicate whether the function at that
> address is in ARM or Thumb mode. If this is the case of your
> architecture, you should define this macro to
> `ptrmemfunc_vbit_in_delta`.
>
> In general, you should not have to define this macro. On architectures
> in which function addresses are always even, according to
> `FUNCTION_BOUNDARY`, GCC will automatically define this macro to
> `ptrmemfunc_vbit_in_pfn`.

— Macro: __TARGET_VTABLE_USES_DESCRIPTORS__
> Normally, the C++ compiler uses function pointers in vtables. This
> macro allows the target to change to use “function descriptors”
> instead. Function descriptors are found on targets for whom a
> function pointer is actually a small data structure. Normally the
> data structure consists of the actual code address plus a data
> pointer to which the function's data is relative.
>
> If vtables are used, the value of this macro should be the number
> of words that the function descriptor occupies.

— Macro: __TARGET_VTABLE_ENTRY_ALIGN__
> By default, the vtable entries are void pointers, the so the alignment
> is the same as pointer alignment. The value of this macro specifies
> the alignment of the vtable entry in bits. It should be defined only
> when special alignment is necessary. \*/

— Macro: __TARGET_VTABLE_DATA_ENTRY_DISTANCE__
> There are a few non-descriptor entries in the vtable at offsets below
> zero. If these entries must be padded (say, to preserve the alignment
> specified by `TARGET_VTABLE_ENTRY_ALIGN`), set this to the number
> of words in each data entry.
