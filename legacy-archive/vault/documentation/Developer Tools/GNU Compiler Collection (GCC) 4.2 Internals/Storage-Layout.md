---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Storage-Layout.html
archived_at: '2026-07-15T07:31:02.909426Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Type Layout](Type-Layout.md#apple-kr4xazjnjrqxs33voq),
Previous: [Per-Function Data](Per_002dFunction-Data.md#apple-kbsxexzqgazgirtvnzrxi2lpnywuiylume),
Up: [Target Macros](Target-Macros.md#apple-krqxez3foqwu2yldojxxg)

---

### 15.5 Storage Layout

Note that the definitions of the macros in this table which are sizes or
alignments measured in bits do not need to be constant. They can be C
expressions that refer to static variables, such as the `target_flags`.
See [Run-time Target](Run_002dtime-Target.md#apple-kj2w4xzqgazgi5djnvss2vdbojtwk5a).

— Macro: __BITS_BIG_ENDIAN__
> Define this macro to have the value 1 if the most significant bit in a
> byte has the lowest number; otherwise define it to have the value zero.
> This means that bit-field instructions count from the most significant
> bit. If the machine has no bit-field instructions, then this must still
> be defined, but it doesn't matter which value it is defined to. This
> macro need not be a constant.
>
> This macro does not affect the way structure fields are packed into
> bytes or words; that is controlled by `BYTES_BIG_ENDIAN`.

— Macro: __BYTES_BIG_ENDIAN__
> Define this macro to have the value 1 if the most significant byte in a
> word has the lowest number. This macro need not be a constant.

— Macro: __WORDS_BIG_ENDIAN__
> Define this macro to have the value 1 if, in a multiword object, the
> most significant word has the lowest number. This applies to both
> memory locations and registers; GCC fundamentally assumes that the
> order of words in memory is the same as the order in registers. This
> macro need not be a constant.

— Macro: __LIBGCC2_WORDS_BIG_ENDIAN__
> Define this macro if `WORDS_BIG_ENDIAN` is not constant. This must be a
> constant value with the same meaning as `WORDS_BIG_ENDIAN`, which will be
> used only when compiling `libgcc2.c`. Typically the value will be set
> based on preprocessor defines.

— Macro: __FLOAT_WORDS_BIG_ENDIAN__
> Define this macro to have the value 1 if `DFmode`, `XFmode` or
> `TFmode` floating point numbers are stored in memory with the word
> containing the sign bit at the lowest address; otherwise define it to
> have the value 0. This macro need not be a constant.
>
> You need not define this macro if the ordering is the same as for
> multi-word integers.

— Macro: __BITS_PER_UNIT__
> Define this macro to be the number of bits in an addressable storage
> unit (byte). If you do not define this macro the default is 8.

— Macro: __BITS_PER_WORD__
> Number of bits in a word. If you do not define this macro, the default
> is `BITS_PER_UNIT * UNITS_PER_WORD`.

— Macro: __MAX_BITS_PER_WORD__
> Maximum number of bits in a word. If this is undefined, the default is
> `BITS_PER_WORD`. Otherwise, it is the constant value that is the
> largest value that `BITS_PER_WORD` can have at run-time.

— Macro: __UNITS_PER_WORD__
> Number of storage units in a word; normally the size of a general-purpose
> register, a power of two from 1 or 8.

— Macro: __MIN_UNITS_PER_WORD__
> Minimum number of units in a word. If this is undefined, the default is
> `UNITS_PER_WORD`. Otherwise, it is the constant value that is the
> smallest value that `UNITS_PER_WORD` can have at run-time.

— Macro: __UNITS_PER_SIMD_WORD__
> Number of units in the vectors that the vectorizer can produce.
> The default is equal to `UNITS_PER_WORD`, because the vectorizer
> can do some transformations even in absence of specialized SIMD
> hardware.

— Macro: __POINTER_SIZE__
> Width of a pointer, in bits. You must specify a value no wider than the
> width of `Pmode`. If it is not equal to the width of `Pmode`,
> you must define `POINTERS_EXTEND_UNSIGNED`. If you do not specify
> a value the default is `BITS_PER_WORD`.

— Macro: __POINTERS_EXTEND_UNSIGNED__
> A C expression whose value is greater than zero if pointers that need to be
> extended from being `POINTER_SIZE` bits wide to `Pmode` are to
> be zero-extended and zero if they are to be sign-extended. If the value
> is less then zero then there must be an "ptr_extend" instruction that
> extends a pointer from `POINTER_SIZE` to `Pmode`.
>
> You need not define this macro if the `POINTER_SIZE` is equal
> to the width of `Pmode`.

— Macro: __PROMOTE_MODE__ (m, unsignedp, type)
> A macro to update m and unsignedp when an object whose type
> is type and which has the specified mode and signedness is to be
> stored in a register. This macro is only called when type is a
> scalar type.
>
> On most RISC machines, which only have operations that operate on a full
> register, define this macro to set m to `word_mode` if
> m is an integer mode narrower than `BITS_PER_WORD`. In most
> cases, only integer modes should be widened because wider-precision
> floating-point operations are usually more expensive than their narrower
> counterparts.
>
> For most machines, the macro definition does not change unsignedp.
> However, some machines, have instructions that preferentially handle
> either signed or unsigned quantities of certain modes. For example, on
> the DEC Alpha, 32-bit loads from memory and 32-bit add instructions
> sign-extend the result to 64 bits. On such machines, set
> unsignedp according to which kind of extension is more efficient.
>
> Do not define this macro if it would never modify m.

— Macro: __PROMOTE_FUNCTION_MODE__
> Like `PROMOTE_MODE`, but is applied to outgoing function arguments or
> function return values, as specified by `TARGET_PROMOTE_FUNCTION_ARGS`
> and `TARGET_PROMOTE_FUNCTION_RETURN`, respectively.
>
> The default is `PROMOTE_MODE`.

— Target Hook: bool __TARGET_PROMOTE_FUNCTION_ARGS__ (tree fntype)
> This target hook should return `true` if the promotion described by
> `PROMOTE_FUNCTION_MODE` should be done for outgoing function
> arguments.

— Target Hook: bool __TARGET_PROMOTE_FUNCTION_RETURN__ (tree fntype)
> This target hook should return `true` if the promotion described by
> `PROMOTE_FUNCTION_MODE` should be done for the return value of
> functions.
>
> If this target hook returns `true`, `TARGET_FUNCTION_VALUE`
> must perform the same promotions done by `PROMOTE_FUNCTION_MODE`.

— Macro: __PARM_BOUNDARY__
> Normal alignment required for function parameters on the stack, in
> bits. All stack parameters receive at least this much alignment
> regardless of data type. On most machines, this is the same as the
> size of an integer.

— Macro: __STACK_BOUNDARY__
> Define this macro to the minimum alignment enforced by hardware for the
> stack pointer on this machine. The definition is a C expression for the
> desired alignment (measured in bits). This value is used as a default
> if `PREFERRED_STACK_BOUNDARY` is not defined. On most machines,
> this should be the same as `PARM_BOUNDARY`.

— Macro: __PREFERRED_STACK_BOUNDARY__
> Define this macro if you wish to preserve a certain alignment for the
> stack pointer, greater than what the hardware enforces. The definition
> is a C expression for the desired alignment (measured in bits). This
> macro must evaluate to a value equal to or larger than
> `STACK_BOUNDARY`.

— Macro: __FUNCTION_BOUNDARY__
> Alignment required for a function entry point, in bits.

— Macro: __BIGGEST_ALIGNMENT__
> Biggest alignment that any data type can require on this machine, in bits.

— Macro: __MINIMUM_ATOMIC_ALIGNMENT__
> If defined, the smallest alignment, in bits, that can be given to an
> object that can be referenced in one operation, without disturbing any
> nearby object. Normally, this is `BITS_PER_UNIT`, but may be larger
> on machines that don't have byte or half-word store operations.

— Macro: __BIGGEST_FIELD_ALIGNMENT__
> Biggest alignment that any structure or union field can require on this
> machine, in bits. If defined, this overrides `BIGGEST_ALIGNMENT` for
> structure and union fields only, unless the field alignment has been set
> by the `__attribute__ ((aligned (`n`)))` construct.

— Macro: __ADJUST_FIELD_ALIGN__ (field, computed)
> An expression for the alignment of a structure field field if the
> alignment computed in the usual way (including applying of
> `BIGGEST_ALIGNMENT` and `BIGGEST_FIELD_ALIGNMENT` to the
> alignment) is computed. It overrides alignment only if the
> field alignment has not been set by the
> `__attribute__ ((aligned (`n`)))` construct.

— Macro: __MAX_OFILE_ALIGNMENT__
> Biggest alignment supported by the object file format of this machine.
> Use this macro to limit the alignment which can be specified using the
> `__attribute__ ((aligned (`n`)))` construct. If not defined,
> the default value is `BIGGEST_ALIGNMENT`.

— Macro: __DATA_ALIGNMENT__ (type, basic-align)
> If defined, a C expression to compute the alignment for a variable in
> the static store. type is the data type, and basic-align is
> the alignment that the object would ordinarily have. The value of this
> macro is used instead of that alignment to align the object.
>
> If this macro is not defined, then basic-align is used.
>
> One use of this macro is to increase alignment of medium-size data to
> make it all fit in fewer cache lines. Another is to cause character
> arrays to be word-aligned so that `strcpy` calls that copy
> constants to character arrays can be done inline.

— Macro: __CONSTANT_ALIGNMENT__ (constant, basic-align)
> If defined, a C expression to compute the alignment given to a constant
> that is being placed in memory. constant is the constant and
> basic-align is the alignment that the object would ordinarily
> have. The value of this macro is used instead of that alignment to
> align the object.
>
> If this macro is not defined, then basic-align is used.
>
> The typical use of this macro is to increase alignment for string
> constants to be word aligned so that `strcpy` calls that copy
> constants can be done inline.

— Macro: __LOCAL_ALIGNMENT__ (type, basic-align)
> If defined, a C expression to compute the alignment for a variable in
> the local store. type is the data type, and basic-align is
> the alignment that the object would ordinarily have. The value of this
> macro is used instead of that alignment to align the object.
>
> If this macro is not defined, then basic-align is used.
>
> One use of this macro is to increase alignment of medium-size data to
> make it all fit in fewer cache lines.

— Macro: __EMPTY_FIELD_BOUNDARY__
> Alignment in bits to be given to a structure bit-field that follows an
> empty field such as `int : 0;`.
>
> If `PCC_BITFIELD_TYPE_MATTERS` is true, it overrides this macro.

— Macro: __STRUCTURE_SIZE_BOUNDARY__
> Number of bits which any structure or union's size must be a multiple of.
> Each structure or union's size is rounded up to a multiple of this.
>
> If you do not define this macro, the default is the same as
> `BITS_PER_UNIT`.

— Macro: __STRICT_ALIGNMENT__
> Define this macro to be the value 1 if instructions will fail to work
> if given data not on the nominal alignment. If instructions will merely
> go slower in that case, define this macro as 0.

— Macro: __PCC_BITFIELD_TYPE_MATTERS__
> Define this if you wish to imitate the way many other C compilers handle
> alignment of bit-fields and the structures that contain them.
>
> The behavior is that the type written for a named bit-field (`int`,
> `short`, or other integer type) imposes an alignment for the entire
> structure, as if the structure really did contain an ordinary field of
> that type. In addition, the bit-field is placed within the structure so
> that it would fit within such a field, not crossing a boundary for it.
>
> Thus, on most machines, a named bit-field whose type is written as
> `int` would not cross a four-byte boundary, and would force
> four-byte alignment for the whole structure. (The alignment used may
> not be four bytes; it is controlled by the other alignment parameters.)
>
> An unnamed bit-field will not affect the alignment of the containing
> structure.
>
> If the macro is defined, its definition should be a C expression;
> a nonzero value for the expression enables this behavior.
>
> Note that if this macro is not defined, or its value is zero, some
> bit-fields may cross more than one alignment boundary. The compiler can
> support such references if there are ``insv`', ``extv`', and
> ``extzv`' insns that can directly reference memory.
>
> The other known way of making bit-fields work is to define
> `STRUCTURE_SIZE_BOUNDARY` as large as `BIGGEST_ALIGNMENT`.
> Then every structure can be accessed with fullwords.
>
> Unless the machine has bit-field instructions or you define
> `STRUCTURE_SIZE_BOUNDARY` that way, you must define
> `PCC_BITFIELD_TYPE_MATTERS` to have a nonzero value.
>
> If your aim is to make GCC use the same conventions for laying out
> bit-fields as are used by another compiler, here is how to investigate
> what the other compiler does. Compile and run this program:
>
> ```
>           struct foo1
>           {
>             char x;
>             char :0;
>             char y;
>           };
>
>           struct foo2
>           {
>             char x;
>             int :0;
>             char y;
>           };
>
>           main ()
>           {
>             printf ("Size of foo1 is %d\n",
>                     sizeof (struct foo1));
>             printf ("Size of foo2 is %d\n",
>                     sizeof (struct foo2));
>             exit (0);
>           }
>
> ```
>
> If this prints 2 and 5, then the compiler's behavior is what you would
> get from `PCC_BITFIELD_TYPE_MATTERS`.

— Macro: __BITFIELD_NBYTES_LIMITED__
> Like `PCC_BITFIELD_TYPE_MATTERS` except that its effect is limited
> to aligning a bit-field within the structure.

— Target Hook: bool __TARGET_ALIGN_ANON_BITFIELDS__ (void)
> When `PCC_BITFIELD_TYPE_MATTERS` is true this hook will determine
> whether unnamed bitfields affect the alignment of the containing
> structure. The hook should return true if the structure should inherit
> the alignment requirements of an unnamed bitfield's type.

— Target Hook: bool __TARGET_NARROW_VOLATILE_BITFIELDS__ (void)
> This target hook should return `true` if accesses to volatile bitfields
> should use the narrowest mode possible. It should return `false` if
> these accesses should use the bitfield container type.
>
> The default is `!TARGET_STRICT_ALIGN`.

— Macro: __MEMBER_TYPE_FORCES_BLK__ (field, mode)
> Return 1 if a structure or array containing field should be accessed using
> `BLKMODE`.
>
> If field is the only field in the structure, mode is its
> mode, otherwise mode is VOIDmode. mode is provided in the
> case where structures of one field would require the structure's mode to
> retain the field's mode.
>
> Normally, this is not needed. See the file `c4x.h` for an example
> of how to use this macro to prevent a structure having a floating point
> field from being accessed in an integer mode.

— Macro: __ROUND_TYPE_ALIGN__ (type, computed, specified)
> Define this macro as an expression for the alignment of a type (given
> by type as a tree node) if the alignment computed in the usual
> way is computed and the alignment explicitly specified was
> specified.
>
> The default is to use specified if it is larger; otherwise, use
> the smaller of computed and `BIGGEST_ALIGNMENT`

— Macro: __MAX_FIXED_MODE_SIZE__
> An integer expression for the size in bits of the largest integer
> machine mode that should actually be used. All integer machine modes of
> this size or smaller can be used for structures and unions with the
> appropriate sizes. If this macro is undefined, `GET_MODE_BITSIZE
> (DImode)` is assumed.

— Macro: __STACK_SAVEAREA_MODE__ (save_level)
> If defined, an expression of type `enum machine_mode` that
> specifies the mode of the save area operand of a
> `save_stack_`level named pattern (see [Standard Names](Standard-Names.md#apple-kn2gc3temfzgilkomfwwk4y)).
> save_level is one of `SAVE_BLOCK`, `SAVE_FUNCTION`, or
> `SAVE_NONLOCAL` and selects which of the three named patterns is
> having its mode specified.
>
> You need not define this macro if it always returns `Pmode`. You
> would most commonly define this macro if the
> `save_stack_`level patterns need to support both a 32- and a
> 64-bit mode.

— Macro: __STACK_SIZE_MODE__
> If defined, an expression of type `enum machine_mode` that
> specifies the mode of the size increment operand of an
> `allocate_stack` named pattern (see [Standard Names](Standard-Names.md#apple-kn2gc3temfzgilkomfwwk4y)).
>
> You need not define this macro if it always returns `word_mode`.
> You would most commonly define this macro if the `allocate_stack`
> pattern needs to support both a 32- and a 64-bit mode.

— Macro: __TARGET_FLOAT_FORMAT__
> A code distinguishing the floating point format of the target machine.
> There are four defined values:
>
> **`IEEE_FLOAT_FORMAT`**
> : This code indicates IEEE floating point. It is the default; there is no
> need to define `TARGET_FLOAT_FORMAT` when the format is IEEE.
>
> **`VAX_FLOAT_FORMAT`**
> : This code indicates the “F float” (for `float`) and “D float”
> or “G float” formats (for `double`) used on the VAX and PDP-11.
>
> **`IBM_FLOAT_FORMAT`**
> : This code indicates the format used on the IBM System/370.
>
> **`C4X_FLOAT_FORMAT`**
> : This code indicates the format used on the TMS320C3x/C4x.
>
> If your target uses a floating point format other than these, you must
> define a new name_FLOAT_FORMAT code for it, and add support for
> it to `real.c`.
>
> The ordering of the component words of floating point values stored in
> memory is controlled by `FLOAT_WORDS_BIG_ENDIAN`.

— Macro: __MODE_HAS_NANS__ (mode)
> When defined, this macro should be true if mode has a NaN
> representation. The compiler assumes that NaNs are not equal to
> anything (including themselves) and that addition, subtraction,
> multiplication and division all return NaNs when one operand is
> NaN.
>
> By default, this macro is true if mode is a floating-point
> mode and the target floating-point format is IEEE.

— Macro: __MODE_HAS_INFINITIES__ (mode)
> This macro should be true if mode can represent infinity. At
> present, the compiler uses this macro to decide whether ``x - x`'
> is always defined. By default, the macro is true when mode
> is a floating-point mode and the target format is IEEE.

— Macro: __MODE_HAS_SIGNED_ZEROS__ (mode)
> True if mode distinguishes between positive and negative zero.
> The rules are expected to follow the IEEE standard:
>
> - ``x + x`' has the same sign as ``x`'.
> - If the sum of two values with opposite sign is zero, the result is
>   positive for all rounding modes expect towards −infinity, for
>   which it is negative.
> - The sign of a product or quotient is negative when exactly one
>   of the operands is negative.
>
> The default definition is true if mode is a floating-point
> mode and the target format is IEEE.

— Macro: __MODE_HAS_SIGN_DEPENDENT_ROUNDING__ (mode)
> If defined, this macro should be true for mode if it has at
> least one rounding mode in which ``x`' and ``-x`' can be
> rounded to numbers of different magnitude. Two such modes are
> towards −infinity and towards +infinity.
>
> The default definition of this macro is true if mode is
> a floating-point mode and the target format is IEEE.

— Macro: __ROUND_TOWARDS_ZERO__
> If defined, this macro should be true if the prevailing rounding
> mode is towards zero. A true value has the following effects:
>
> - `MODE_HAS_SIGN_DEPENDENT_ROUNDING` will be false for all modes.
> - `libgcc.a`'s floating-point emulator will round towards zero
>   rather than towards nearest.
> - The compiler's floating-point emulator will round towards zero after
>   doing arithmetic, and when converting from the internal float format to
>   the target format.
>
> The macro does not affect the parsing of string literals. When the
> primary rounding mode is towards zero, library functions like
> `strtod` might still round towards nearest, and the compiler's
> parser should behave like the target's `strtod` where possible.
>
> Not defining this macro is equivalent to returning zero.

— Macro: __LARGEST_EXPONENT_IS_NORMAL__ (size)
> This macro should return true if floats with size
> bits do not have a NaN or infinity representation, but use the largest
> exponent for normal numbers instead.
>
> Defining this macro to true for size causes `MODE_HAS_NANS`
> and `MODE_HAS_INFINITIES` to be false for size-bit modes.
> It also affects the way `libgcc.a` and `real.c` emulate
> floating-point arithmetic.
>
> The default definition of this macro returns false for all sizes.

— Target Hook: bool __TARGET_VECTOR_OPAQUE_P__ (tree type)
> This target hook should return `true` a vector is opaque. That
> is, if no cast is needed when copying a vector value of type
> type into another vector lvalue of the same size. Vector opaque
> types cannot be initialized. The default is that there are no such
> types.

— Target Hook: bool __TARGET_MS_BITFIELD_LAYOUT_P__ (tree record_type)
> This target hook returns `true` if bit-fields in the given
> record_type are to be laid out following the rules of Microsoft
> Visual C/C++, namely: (i) a bit-field won't share the same storage
> unit with the previous bit-field if their underlying types have
> different sizes, and the bit-field will be aligned to the highest
> alignment of the underlying types of itself and of the previous
> bit-field; (ii) a zero-sized bit-field will affect the alignment of
> the whole enclosing structure, even if it is unnamed; except that
> (iii) a zero-sized bit-field will be disregarded unless it follows
> another bit-field of nonzero size. If this hook returns `true`,
> other macros that control bit-field layout are ignored.
>
> When a bit-field is inserted into a packed record, the whole size
> of the underlying type is used by one or more same-size adjacent
> bit-fields (that is, if its long:3, 32 bits is used in the record,
> and any additional adjacent long bit-fields are packed into the same
> chunk of 32 bits. However, if the size changes, a new field of that
> size is allocated). In an unpacked record, this is the same as using
> alignment, but not equivalent when packing.
>
> If both MS bit-fields and ``__attribute__((packed))`' are used,
> the latter will take precedence. If ``__attribute__((packed))`' is
> used on a single field when MS bit-fields are in use, it will take
> precedence for that field, but the alignment of the rest of the structure
> may affect its placement.

— Target Hook: bool __TARGET_DECIMAL_FLOAT_SUPPORTED_P__ (void)
> Returns true if the target supports decimal floating point.

— Target Hook: const char \* __TARGET_MANGLE_FUNDAMENTAL_TYPE__ (tree type)
> If your target defines any fundamental types, define this hook to
> return the appropriate encoding for these types as part of a C++
> mangled name. The type argument is the tree structure
> representing the type to be mangled. The hook may be applied to trees
> which are not target-specific fundamental types; it should return
> `NULL` for all such types, as well as arguments it does not
> recognize. If the return value is not `NULL`, it must point to
> a statically-allocated string constant.
>
> Target-specific fundamental types might be new fundamental types or
> qualified versions of ordinary fundamental types. Encode new
> fundamental types as ``u n name`', where name
> is the name used for the type in source code, and n is the
> length of name in decimal. Encode qualified versions of
> ordinary types as ``U n name code`', where
> name is the name used for the type qualifier in source code,
> n is the length of name as above, and code is the
> code used to represent the unqualified version of this type. (See
> `write_builtin_type` in `cp/mangle.c` for the list of
> codes.) In both cases the spaces are for clarity; do not include any
> spaces in your string.
>
> The default version of this hook always returns `NULL`, which is
> appropriate for a target that does not define any new fundamental
> types.
