---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Standard-Names.html
archived_at: '2026-07-15T07:31:02.862819Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Pattern Ordering](Pattern-Ordering.md#apple-kbqxi5dfojxc2t3smrsxe2lom4),
Previous: [Constraints](Constraints.md#apple-inxw443uojqws3tuom),
Up: [Machine Desc](Machine-Desc.md#apple-jvqwg2djnzss2rdfonrq)

---

### 14.9 Standard Pattern Names For Generation

Here is a table of the instruction names that are meaningful in the RTL
generation pass of the compiler. Giving one of these names to an
instruction pattern tells the RTL generation pass that it can use the
pattern to accomplish a certain task.

**``movm`'**
: Here m stands for a two-letter machine mode name, in lowercase.
This instruction pattern moves data with that machine mode from operand
1 to operand 0. For example, ``movsi`' moves full-word data.

If operand 0 is a `subreg` with mode m of a register whose
own mode is wider than m, the effect of this instruction is
to store the specified value in the part of the register that corresponds
to mode m. Bits outside of m, but which are within the
same target word as the `subreg` are undefined. Bits which are
outside the target word are left unchanged.

This class of patterns is special in several ways. First of all, each
of these names up to and including full word size _must_ be defined,
because there is no other way to copy a datum from one place to another.
If there are patterns accepting operands in larger modes,
``movm`' must be defined for integer modes of those sizes.

Second, these patterns are not used solely in the RTL generation pass.
Even the reload pass can generate move insns to copy values from stack
slots into temporary registers. When it does so, one of the operands is
a hard register and the other is an operand that can need to be reloaded
into a register.

Therefore, when given such a pair of operands, the pattern must generate
RTL which needs no reloading and needs no temporary registers—no
registers other than the operands. For example, if you support the
pattern with a `define_expand`, then in such a case the
`define_expand` mustn't call `force_reg` or any other such
function which might generate new pseudo registers.

This requirement exists even for subword modes on a RISC machine where
fetching those modes from memory normally requires several insns and
some temporary registers.

During reload a memory reference with an invalid address may be passed
as an operand. Such an address will be replaced with a valid address
later in the reload pass. In this case, nothing may be done with the
address except to use it as it stands. If it is copied, it will not be
replaced with a valid address. No attempt should be made to make such
an address into a valid address and no routine (such as
`change_address`) that will do so may be called. Note that
`general_operand` will fail when applied to such an address.

The global variable `reload_in_progress` (which must be explicitly
declared if required) can be used to determine whether such special
handling is required.

The variety of operands that have reloads depends on the rest of the
machine description, but typically on a RISC machine these can only be
pseudo registers that did not get hard registers, while on other
machines explicit memory references will get optional reloads.

If a scratch register is required to move an object to or from memory,
it can be allocated using `gen_reg_rtx` prior to life analysis.

If there are cases which need scratch registers during or after reload,
you must provide an appropriate secondary_reload target hook.

The global variable `no_new_pseudos` can be used to determine if it
is unsafe to create new pseudo registers. If this variable is nonzero, then
it is unsafe to call `gen_reg_rtx` to allocate a new pseudo.

The constraints on a ``movm`' must permit moving any hard
register to any other hard register provided that
`HARD_REGNO_MODE_OK` permits mode m in both registers and
`REGISTER_MOVE_COST` applied to their classes returns a value of 2.

It is obligatory to support floating point ``movm`'
instructions into and out of any registers that can hold fixed point
values, because unions and structures (which have modes `SImode` or
`DImode`) can be in those registers and they may have floating
point members.

There may also be a need to support fixed point ``movm`'
instructions in and out of floating point registers. Unfortunately, I
have forgotten why this was so, and I don't know whether it is still
true. If `HARD_REGNO_MODE_OK` rejects fixed point values in
floating point registers, then the constraints of the fixed point
``movm`' instructions must be designed to avoid ever trying to
reload into a floating point register.

**``reload_inm`'

**``reload_outm`'****
: These named patterns have been obsoleted by the target hook
`secondary_reload`.

Like ``movm`', but used when a scratch register is required to
move between operand 0 and operand 1. Operand 2 describes the scratch
register. See the discussion of the `SECONDARY_RELOAD_CLASS`
macro in see [Register Classes](Register-Classes.md#apple-kjswo2ltorsxelkdnrqxg43fom).

There are special restrictions on the form of the `match_operand`s
used in these patterns. First, only the predicate for the reload
operand is examined, i.e., `reload_in` examines operand 1, but not
the predicates for operand 0 or 2. Second, there may be only one
alternative in the constraints. Third, only a single register class
letter may be used for the constraint; subsequent constraint letters
are ignored. As a special exception, an empty constraint string
matches the `ALL_REGS` register class. This may relieve ports
of the burden of defining an `ALL_REGS` constraint letter just
for these patterns.

**``movstrictm`'**
: Like ``movm`' except that if operand 0 is a `subreg`
with mode m of a register whose natural mode is wider,
the ``movstrictm`' instruction is guaranteed not to alter
any of the register except the part which belongs to mode m.

**``movmisalignm`'**
: This variant of a move pattern is designed to load or store a value
from a memory address that is not naturally aligned for its mode.
For a store, the memory will be in operand 0; for a load, the memory
will be in operand 1. The other operand is guaranteed not to be a
memory, so that it's easy to tell whether this is a load or store.

This pattern is used by the autovectorizer, and when expanding a
`MISALIGNED_INDIRECT_REF` expression.

**``load_multiple`'**
: Load several consecutive memory locations into consecutive registers.
Operand 0 is the first of the consecutive registers, operand 1
is the first memory location, and operand 2 is a constant: the
number of consecutive registers.

Define this only if the target machine really has such an instruction;
do not define this if the most efficient way of loading consecutive
registers from memory is to do them one at a time.

On some machines, there are restrictions as to which consecutive
registers can be stored into memory, such as particular starting or
ending register numbers or only a range of valid counts. For those
machines, use a `define_expand` (see [Expander Definitions](Expander-Definitions.md#apple-iv4haylomrsxelkemvtgs3tjoruw63tt))
and make the pattern fail if the restrictions are not met.

Write the generated insn as a `parallel` with elements being a
`set` of one register from the appropriate memory location (you may
also need `use` or `clobber` elements). Use a
`match_parallel` (see [RTL Template](RTL-Template.md#apple-kjkeylkumvwxa3dborsq)) to recognize the insn. See
`rs6000.md` for examples of the use of this insn pattern.

**``store_multiple`'**
: Similar to ``load_multiple`', but store several consecutive registers
into consecutive memory locations. Operand 0 is the first of the
consecutive memory locations, operand 1 is the first register, and
operand 2 is a constant: the number of consecutive registers.

**``vec_setm`'**
: Set given field in the vector value. Operand 0 is the vector to modify,
operand 1 is new value of field and operand 2 specify the field index.

**``vec_extractm`'**
: Extract given field from the vector value. Operand 1 is the vector, operand 2
specify field index and operand 0 place to store value into.

**``vec_initm`'**
: Initialize the vector to given values. Operand 0 is the vector to initialize
and operand 1 is parallel containing values for individual fields.

**``pushm1`'**
: Output a push instruction. Operand 0 is value to push. Used only when
`PUSH_ROUNDING` is defined. For historical reason, this pattern may be
missing and in such case an `mov` expander is used instead, with a
`MEM` expression forming the push operation. The `mov` expander
method is deprecated.

**``addm3`'**
: Add operand 2 and operand 1, storing the result in operand 0. All operands
must have mode m. This can be used even on two-address machines, by
means of constraints requiring operands 1 and 0 to be the same location.

**``subm3`', ``mulm3`'

**``divm3`', ``udivm3`'

**``modm3`', ``umodm3`'

**``uminm3`', ``umaxm3`'

**``andm3`', ``iorm3`', ``xorm3`'**********
: Similar, for other arithmetic operations.

**``sminm3`', ``smaxm3`'**
: Signed minimum and maximum operations. When used with floating point,
if both operands are zeros, or if either operand is `NaN`, then
it is unspecified which of the two operands is returned as the result.

**``reduc_smin_m`', ``reduc_smax_m`'**
: Find the signed minimum/maximum of the elements of a vector. The vector is
operand 1, and the scalar result is stored in the least significant bits of
operand 0 (also a vector). The output and input vector should have the same
modes.

**``reduc_umin_m`', ``reduc_umax_m`'**
: Find the unsigned minimum/maximum of the elements of a vector. The vector is
operand 1, and the scalar result is stored in the least significant bits of
operand 0 (also a vector). The output and input vector should have the same
modes.

**``reduc_splus_m`'**
: Compute the sum of the signed elements of a vector. The vector is operand 1,
and the scalar result is stored in the least significant bits of operand 0
(also a vector). The output and input vector should have the same modes.

**``reduc_uplus_m`'**
: Compute the sum of the unsigned elements of a vector. The vector is operand 1,
and the scalar result is stored in the least significant bits of operand 0
(also a vector). The output and input vector should have the same modes.

**``sdot_prodm`'**
: 

**``udot_prodm`'**
: Compute the sum of the products of two signed/unsigned elements.
Operand 1 and operand 2 are of the same mode. Their product, which is of a
wider mode, is computed and added to operand 3. Operand 3 is of a mode equal or
wider than the mode of the product. The result is placed in operand 0, which
is of the same mode as operand 3.

**``ssum_widenm3`'**
: 

**``usum_widenm3`'**
: Operands 0 and 2 are of the same mode, which is wider than the mode of
operand 1. Add operand 1 to operand 2 and place the widened result in
operand 0. (This is used express accumulation of elements into an accumulator
of a wider mode.)

**``vec_shl_m`', ``vec_shr_m`'**
: Whole vector left/right shift in bits.
Operand 1 is a vector to be shifted.
Operand 2 is an integer shift amount in bits.
Operand 0 is where the resulting shifted vector is stored.
The output and input vectors should have the same modes.

**``mulhisi3`'**
: Multiply operands 1 and 2, which have mode `HImode`, and store
a `SImode` product in operand 0.

**``mulqihi3`', ``mulsidi3`'**
: Similar widening-multiplication instructions of other widths.

**``umulqihi3`', ``umulhisi3`', ``umulsidi3`'**
: Similar widening-multiplication instructions that do unsigned
multiplication.

**``usmulqihi3`', ``usmulhisi3`', ``usmulsidi3`'**
: Similar widening-multiplication instructions that interpret the first
operand as unsigned and the second operand as signed, then do a signed
multiplication.

**``smulm3_highpart`'**
: Perform a signed multiplication of operands 1 and 2, which have mode
m, and store the most significant half of the product in operand 0.
The least significant half of the product is discarded.

**``umulm3_highpart`'**
: Similar, but the multiplication is unsigned.

**``divmodm4`'**
: Signed division that produces both a quotient and a remainder.
Operand 1 is divided by operand 2 to produce a quotient stored
in operand 0 and a remainder stored in operand 3.

For machines with an instruction that produces both a quotient and a
remainder, provide a pattern for ``divmodm4`' but do not
provide patterns for ``divm3`' and ``modm3`'. This
allows optimization in the relatively common case when both the quotient
and remainder are computed.

If an instruction that just produces a quotient or just a remainder
exists and is more efficient than the instruction that produces both,
write the output routine of ``divmodm4`' to call
`find_reg_note` and look for a `REG_UNUSED` note on the
quotient or remainder and generate the appropriate instruction.

**``udivmodm4`'**
: Similar, but does unsigned division.

**``ashlm3`'**
: Arithmetic-shift operand 1 left by a number of bits specified by operand
2, and store the result in operand 0. Here m is the mode of
operand 0 and operand 1; operand 2's mode is specified by the
instruction pattern, and the compiler will convert the operand to that
mode before generating the instruction. The meaning of out-of-range shift
counts can optionally be specified by `TARGET_SHIFT_TRUNCATION_MASK`.
See [TARGET_SHIFT_TRUNCATION_MASK](https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/TARGET_005fSHIFT_005fTRUNCATION_005fMASK.html#TARGET_005fSHIFT_005fTRUNCATION_005fMASK).

**``ashrm3`', ``lshrm3`', ``rotlm3`', ``rotrm3`'**
: Other shift and rotate instructions, analogous to the
`ashl`m`3` instructions.

**``negm2`'**
: Negate operand 1 and store the result in operand 0.

**``absm2`'**
: Store the absolute value of operand 1 into operand 0.

**``sqrtm2`'**
: Store the square root of operand 1 into operand 0.

The `sqrt` built-in function of C always uses the mode which
corresponds to the C data type `double` and the `sqrtf`
built-in function uses the mode which corresponds to the C data
type `float`.

**``cosm2`'**
: Store the cosine of operand 1 into operand 0.

The `cos` built-in function of C always uses the mode which
corresponds to the C data type `double` and the `cosf`
built-in function uses the mode which corresponds to the C data
type `float`.

**``sinm2`'**
: Store the sine of operand 1 into operand 0.

The `sin` built-in function of C always uses the mode which
corresponds to the C data type `double` and the `sinf`
built-in function uses the mode which corresponds to the C data
type `float`.

**``expm2`'**
: Store the exponential of operand 1 into operand 0.

The `exp` built-in function of C always uses the mode which
corresponds to the C data type `double` and the `expf`
built-in function uses the mode which corresponds to the C data
type `float`.

**``logm2`'**
: Store the natural logarithm of operand 1 into operand 0.

The `log` built-in function of C always uses the mode which
corresponds to the C data type `double` and the `logf`
built-in function uses the mode which corresponds to the C data
type `float`.

**``powm3`'**
: Store the value of operand 1 raised to the exponent operand 2
into operand 0.

The `pow` built-in function of C always uses the mode which
corresponds to the C data type `double` and the `powf`
built-in function uses the mode which corresponds to the C data
type `float`.

**``atan2m3`'**
: Store the arc tangent (inverse tangent) of operand 1 divided by
operand 2 into operand 0, using the signs of both arguments to
determine the quadrant of the result.

The `atan2` built-in function of C always uses the mode which
corresponds to the C data type `double` and the `atan2f`
built-in function uses the mode which corresponds to the C data
type `float`.

**``floorm2`'**
: Store the largest integral value not greater than argument.

The `floor` built-in function of C always uses the mode which
corresponds to the C data type `double` and the `floorf`
built-in function uses the mode which corresponds to the C data
type `float`.

**``btruncm2`'**
: Store the argument rounded to integer towards zero.

The `trunc` built-in function of C always uses the mode which
corresponds to the C data type `double` and the `truncf`
built-in function uses the mode which corresponds to the C data
type `float`.

**``roundm2`'**
: Store the argument rounded to integer away from zero.

The `round` built-in function of C always uses the mode which
corresponds to the C data type `double` and the `roundf`
built-in function uses the mode which corresponds to the C data
type `float`.

**``ceilm2`'**
: Store the argument rounded to integer away from zero.

The `ceil` built-in function of C always uses the mode which
corresponds to the C data type `double` and the `ceilf`
built-in function uses the mode which corresponds to the C data
type `float`.

**``nearbyintm2`'**
: Store the argument rounded according to the default rounding mode

The `nearbyint` built-in function of C always uses the mode which
corresponds to the C data type `double` and the `nearbyintf`
built-in function uses the mode which corresponds to the C data
type `float`.

**``rintm2`'**
: Store the argument rounded according to the default rounding mode and
raise the inexact exception when the result differs in value from
the argument

The `rint` built-in function of C always uses the mode which
corresponds to the C data type `double` and the `rintf`
built-in function uses the mode which corresponds to the C data
type `float`.

**``copysignm3`'**
: Store a value with the magnitude of operand 1 and the sign of operand
2 into operand 0.

The `copysign` built-in function of C always uses the mode which
corresponds to the C data type `double` and the `copysignf`
built-in function uses the mode which corresponds to the C data
type `float`.

**``ffsm2`'**
: Store into operand 0 one plus the index of the least significant 1-bit
of operand 1. If operand 1 is zero, store zero. m is the mode
of operand 0; operand 1's mode is specified by the instruction
pattern, and the compiler will convert the operand to that mode before
generating the instruction.

The `ffs` built-in function of C always uses the mode which
corresponds to the C data type `int`.

**``clzm2`'**
: Store into operand 0 the number of leading 0-bits in x, starting
at the most significant bit position. If x is 0, the result is
undefined. m is the mode of operand 0; operand 1's mode is
specified by the instruction pattern, and the compiler will convert the
operand to that mode before generating the instruction.

**``ctzm2`'**
: Store into operand 0 the number of trailing 0-bits in x, starting
at the least significant bit position. If x is 0, the result is
undefined. m is the mode of operand 0; operand 1's mode is
specified by the instruction pattern, and the compiler will convert the
operand to that mode before generating the instruction.

**``popcountm2`'**
: Store into operand 0 the number of 1-bits in x. m is the
mode of operand 0; operand 1's mode is specified by the instruction
pattern, and the compiler will convert the operand to that mode before
generating the instruction.

**``paritym2`'**
: Store into operand 0 the parity of x, i.e. the number of 1-bits
in x modulo 2. m is the mode of operand 0; operand 1's mode
is specified by the instruction pattern, and the compiler will convert
the operand to that mode before generating the instruction.

**``one_cmplm2`'**
: Store the bitwise-complement of operand 1 into operand 0.

**``cmpm`'**
: Compare operand 0 and operand 1, and set the condition codes.
The RTL pattern should look like this:

```
          (set (cc0) (compare (match_operand:m 0 ...)
                              (match_operand:m 1 ...)))

```


**``tstm`'**
: Compare operand 0 against zero, and set the condition codes.
The RTL pattern should look like this:

```
          (set (cc0) (match_operand:m 0 ...))

```

``tstm`' patterns should not be defined for machines that do
not use `(cc0)`. Doing so would confuse the optimizer since it
would no longer be clear which `set` operations were comparisons.
The ``cmpm`' patterns should be used instead.

**``movmemm`'**
: Block move instruction. The destination and source blocks of memory
are the first two operands, and both are `mem:BLK`s with an
address in mode `Pmode`.

The number of bytes to move is the third operand, in mode m.
Usually, you specify `word_mode` for m. However, if you can
generate better code knowing the range of valid lengths is smaller than
those representable in a full word, you should provide a pattern with a
mode corresponding to the range of values you can handle efficiently
(e.g., `QImode` for values in the range 0–127; note we avoid numbers
that appear negative) and also a pattern with `word_mode`.

The fourth operand is the known shared alignment of the source and
destination, in the form of a `const_int` rtx. Thus, if the
compiler knows that both source and destination are word-aligned,
it may provide the value 4 for this operand.

Descriptions of multiple `movmem`m patterns can only be
beneficial if the patterns for smaller modes have fewer restrictions
on their first, second and fourth operands. Note that the mode m
in `movmem`m does not impose any restriction on the mode of
individually moved data units in the block.

These patterns need not give special consideration to the possibility
that the source and destination strings might overlap.

**``movstr`'**
: String copy instruction, with `stpcpy` semantics. Operand 0 is
an output operand in mode `Pmode`. The addresses of the
destination and source strings are operands 1 and 2, and both are
`mem:BLK`s with addresses in mode `Pmode`. The execution of
the expansion of this pattern should store in operand 0 the address in
which the `NUL` terminator was stored in the destination string.

**``setmemm`'**
: Block set instruction. The destination string is the first operand,
given as a `mem:BLK` whose address is in mode `Pmode`. The
number of bytes to set is the second operand, in mode m. The value to
initialize the memory with is the third operand. Targets that only support the
clearing of memory should reject any value that is not the constant 0. See
``movmemm`' for a discussion of the choice of mode.

The fourth operand is the known alignment of the destination, in the form
of a `const_int` rtx. Thus, if the compiler knows that the
destination is word-aligned, it may provide the value 4 for this
operand.

The use for multiple `setmem`m is as for `movmem`m.

**``cmpstrnm`'**
: String compare instruction, with five operands. Operand 0 is the output;
it has mode m. The remaining four operands are like the operands
of ``movmemm`'. The two memory blocks specified are compared
byte by byte in lexicographic order starting at the beginning of each
string. The instruction is not allowed to prefetch more than one byte
at a time since either string may end in the first byte and reading past
that may access an invalid page or segment and cause a fault. The
effect of the instruction is to store a value in operand 0 whose sign
indicates the result of the comparison.

**``cmpstrm`'**
: String compare instruction, without known maximum length. Operand 0 is the
output; it has mode m. The second and third operand are the blocks of
memory to be compared; both are `mem:BLK` with an address in mode
`Pmode`.

The fourth operand is the known shared alignment of the source and
destination, in the form of a `const_int` rtx. Thus, if the
compiler knows that both source and destination are word-aligned,
it may provide the value 4 for this operand.

The two memory blocks specified are compared byte by byte in lexicographic
order starting at the beginning of each string. The instruction is not allowed
to prefetch more than one byte at a time since either string may end in the
first byte and reading past that may access an invalid page or segment and
cause a fault. The effect of the instruction is to store a value in operand 0
whose sign indicates the result of the comparison.

**``cmpmemm`'**
: Block compare instruction, with five operands like the operands
of ``cmpstrm`'. The two memory blocks specified are compared
byte by byte in lexicographic order starting at the beginning of each
block. Unlike ``cmpstrm`' the instruction can prefetch
any bytes in the two memory blocks. The effect of the instruction is
to store a value in operand 0 whose sign indicates the result of the
comparison.

**``strlenm`'**
: Compute the length of a string, with three operands.
Operand 0 is the result (of mode m), operand 1 is
a `mem` referring to the first character of the string,
operand 2 is the character to search for (normally zero),
and operand 3 is a constant describing the known alignment
of the beginning of the string.

**``floatmn2`'**
: Convert signed integer operand 1 (valid for fixed point mode m) to
floating point mode n and store in operand 0 (which has mode
n).

**``floatunsmn2`'**
: Convert unsigned integer operand 1 (valid for fixed point mode m)
to floating point mode n and store in operand 0 (which has mode
n).

**``fixmn2`'**
: Convert operand 1 (valid for floating point mode m) to fixed
point mode n as a signed number and store in operand 0 (which
has mode n). This instruction's result is defined only when
the value of operand 1 is an integer.

If the machine description defines this pattern, it also needs to
define the `ftrunc` pattern.

**``fixunsmn2`'**
: Convert operand 1 (valid for floating point mode m) to fixed
point mode n as an unsigned number and store in operand 0 (which
has mode n). This instruction's result is defined only when the
value of operand 1 is an integer.

**``ftruncm2`'**
: Convert operand 1 (valid for floating point mode m) to an
integer value, still represented in floating point mode m, and
store it in operand 0 (valid for floating point mode m).

**``fix_truncmn2`'**
: Like ``fixmn2`' but works for any floating point value
of mode m by converting the value to an integer.

**``fixuns_truncmn2`'**
: Like ``fixunsmn2`' but works for any floating point
value of mode m by converting the value to an integer.

**``truncmn2`'**
: Truncate operand 1 (valid for mode m) to mode n and
store in operand 0 (which has mode n). Both modes must be fixed
point or both floating point.

**``extendmn2`'**
: Sign-extend operand 1 (valid for mode m) to mode n and
store in operand 0 (which has mode n). Both modes must be fixed
point or both floating point.

**``zero_extendmn2`'**
: Zero-extend operand 1 (valid for mode m) to mode n and
store in operand 0 (which has mode n). Both modes must be fixed
point.

**``extv`'**
: Extract a bit-field from operand 1 (a register or memory operand), where
operand 2 specifies the width in bits and operand 3 the starting bit,
and store it in operand 0. Operand 0 must have mode `word_mode`.
Operand 1 may have mode `byte_mode` or `word_mode`; often
`word_mode` is allowed only for registers. Operands 2 and 3 must
be valid for `word_mode`.

The RTL generation pass generates this instruction only with constants
for operands 2 and 3 and the constant is never zero for operand 2.

The bit-field value is sign-extended to a full word integer
before it is stored in operand 0.

**``extzv`'**
: Like ``extv`' except that the bit-field value is zero-extended.

**``insv`'**
: Store operand 3 (which must be valid for `word_mode`) into a
bit-field in operand 0, where operand 1 specifies the width in bits and
operand 2 the starting bit. Operand 0 may have mode `byte_mode` or
`word_mode`; often `word_mode` is allowed only for registers.
Operands 1 and 2 must be valid for `word_mode`.

The RTL generation pass generates this instruction only with constants
for operands 1 and 2 and the constant is never zero for operand 1.

**``movmodecc`'**
: Conditionally move operand 2 or operand 3 into operand 0 according to the
comparison in operand 1. If the comparison is true, operand 2 is moved
into operand 0, otherwise operand 3 is moved.

The mode of the operands being compared need not be the same as the operands
being moved. Some machines, sparc64 for example, have instructions that
conditionally move an integer value based on the floating point condition
codes and vice versa.

If the machine does not have conditional move instructions, do not
define these patterns.

**``addmodecc`'**
: Similar to ``movmodecc`' but for conditional addition. Conditionally
move operand 2 or (operands 2 + operand 3) into operand 0 according to the
comparison in operand 1. If the comparison is true, operand 2 is moved into
operand 0, otherwise (operand 2 + operand 3) is moved.

**``scond`'**
: Store zero or nonzero in the operand according to the condition codes.
Value stored is nonzero iff the condition cond is true.
cond is the name of a comparison operation expression code, such
as `eq`, `lt` or `leu`.

You specify the mode that the operand must have when you write the
`match_operand` expression. The compiler automatically sees
which mode you have used and supplies an operand of that mode.

The value stored for a true condition must have 1 as its low bit, or
else must be negative. Otherwise the instruction is not suitable and
you should omit it from the machine description. You describe to the
compiler exactly which value is stored by defining the macro
`STORE_FLAG_VALUE` (see [Misc](Misc.md#apple-jvuxgyy)). If a description cannot be
found that can be used for all the ``scond`' patterns, you
should omit those operations from the machine description.

These operations may fail, but should do so only in relatively
uncommon cases; if they would fail for common cases involving
integer comparisons, it is best to omit these patterns.

If these operations are omitted, the compiler will usually generate code
that copies the constant one to the target and branches around an
assignment of zero to the target. If this code is more efficient than
the potential instructions used for the ``scond`' pattern
followed by those required to convert the result into a 1 or a zero in
`SImode`, you should omit the ``scond`' operations from
the machine description.

**``bcond`'**
: Conditional branch instruction. Operand 0 is a `label_ref` that
refers to the label to jump to. Jump if the condition codes meet
condition cond.

Some machines do not follow the model assumed here where a comparison
instruction is followed by a conditional branch instruction. In that
case, the ``cmpm`' (and ``tstm`') patterns should
simply store the operands away and generate all the required insns in a
`define_expand` (see [Expander Definitions](Expander-Definitions.md#apple-iv4haylomrsxelkemvtgs3tjoruw63tt)) for the conditional
branch operations. All calls to expand ``bcond`' patterns are
immediately preceded by calls to expand either a ``cmpm`'
pattern or a ``tstm`' pattern.

Machines that use a pseudo register for the condition code value, or
where the mode used for the comparison depends on the condition being
tested, should also use the above mechanism. See [Jump Patterns](Jump-Patterns.md#apple-jj2w24bnkbqxi5dfojxhg).

The above discussion also applies to the ``movmodecc`' and
``scond`' patterns.

**``cbranchmode4`'**
: Conditional branch instruction combined with a compare instruction.
Operand 0 is a comparison operator. Operand 1 and operand 2 are the
first and second operands of the comparison, respectively. Operand 3
is a `label_ref` that refers to the label to jump to.

**``jump`'**
: A jump inside a function; an unconditional branch. Operand 0 is the
`label_ref` of the label to jump to. This pattern name is mandatory
on all machines.

**``call`'**
: Subroutine call instruction returning no value. Operand 0 is the
function to call; operand 1 is the number of bytes of arguments pushed
as a `const_int`; operand 2 is the number of registers used as
operands.

On most machines, operand 2 is not actually stored into the RTL
pattern. It is supplied for the sake of some RISC machines which need
to put this information into the assembler code; they can put it in
the RTL instead of operand 1.

Operand 0 should be a `mem` RTX whose address is the address of the
function. Note, however, that this address can be a `symbol_ref`
expression even if it would not be a legitimate memory address on the
target machine. If it is also not a valid argument for a call
instruction, the pattern for this operation should be a
`define_expand` (see [Expander Definitions](Expander-Definitions.md#apple-iv4haylomrsxelkemvtgs3tjoruw63tt)) that places the
address into a register and uses that register in the call instruction.

**``call_value`'**
: Subroutine call instruction returning a value. Operand 0 is the hard
register in which the value is returned. There are three more
operands, the same as the three operands of the ``call`'
instruction (but with numbers increased by one).

Subroutines that return `BLKmode` objects use the ``call`'
insn.

**``call_pop`', ``call_value_pop`'**
: Similar to ``call`' and ``call_value`', except used if defined and
if `RETURN_POPS_ARGS` is nonzero. They should emit a `parallel`
that contains both the function call and a `set` to indicate the
adjustment made to the frame pointer.

For machines where `RETURN_POPS_ARGS` can be nonzero, the use of these
patterns increases the number of functions for which the frame pointer
can be eliminated, if desired.

**``untyped_call`'**
: Subroutine call instruction returning a value of any type. Operand 0 is
the function to call; operand 1 is a memory location where the result of
calling the function is to be stored; operand 2 is a `parallel`
expression where each element is a `set` expression that indicates
the saving of a function return value into the result block.

This instruction pattern should be defined to support
`__builtin_apply` on machines where special instructions are needed
to call a subroutine with arbitrary arguments or to save the value
returned. This instruction pattern is required on machines that have
multiple registers that can hold a return value
(i.e. `FUNCTION_VALUE_REGNO_P` is true for more than one register).

**``return`'**
: Subroutine return instruction. This instruction pattern name should be
defined only if a single instruction can do all the work of returning
from a function.

Like the ``movm`' patterns, this pattern is also used after the
RTL generation phase. In this case it is to support machines where
multiple instructions are usually needed to return from a function, but
some class of functions only requires one instruction to implement a
return. Normally, the applicable functions are those which do not need
to save any registers or allocate stack space.

For such machines, the condition specified in this pattern should only
be true when `reload_completed` is nonzero and the function's
epilogue would only be a single instruction. For machines with register
windows, the routine `leaf_function_p` may be used to determine if
a register window push is required.

Machines that have conditional return instructions should define patterns
such as

```
          (define_insn ""
            [(set (pc)
                  (if_then_else (match_operator
                                   0 "comparison_operator"
                                   [(cc0) (const_int 0)])
                                (return)
                                (pc)))]
            "condition"
            "...")

```

where condition would normally be the same condition specified on the
named ``return`' pattern.

**``untyped_return`'**
: Untyped subroutine return instruction. This instruction pattern should
be defined to support `__builtin_return` on machines where special
instructions are needed to return a value of any type.

Operand 0 is a memory location where the result of calling a function
with `__builtin_apply` is stored; operand 1 is a `parallel`
expression where each element is a `set` expression that indicates
the restoring of a function return value from the result block.

**``nop`'**
: No-op instruction. This instruction pattern name should always be defined
to output a no-op in assembler code. `(const_int 0)` will do as an
RTL pattern.

**``indirect_jump`'**
: An instruction to jump to an address which is operand zero.
This pattern name is mandatory on all machines.

**``casesi`'**
: Instruction to jump through a dispatch table, including bounds checking.
This instruction takes five operands:

1. The index to dispatch on, which has mode `SImode`.
2. The lower bound for indices in the table, an integer constant.
3. The total range of indices in the table—the largest index
   minus the smallest one (both inclusive).
4. A label that precedes the table itself.
5. A label to jump to if the index has a value outside the bounds.

The table is a `addr_vec` or `addr_diff_vec` inside of a
`jump_insn`. The number of elements in the table is one plus the
difference between the upper bound and the lower bound.

**``tablejump`'**
: Instruction to jump to a variable address. This is a low-level
capability which can be used to implement a dispatch table when there
is no ``casesi`' pattern.

This pattern requires two operands: the address or offset, and a label
which should immediately precede the jump table. If the macro
`CASE_VECTOR_PC_RELATIVE` evaluates to a nonzero value then the first
operand is an offset which counts from the address of the table; otherwise,
it is an absolute address to jump to. In either case, the first operand has
mode `Pmode`.

The ``tablejump`' insn is always the last insn before the jump
table it uses. Its assembler code normally has no need to use the
second operand, but you should incorporate it in the RTL pattern so
that the jump optimizer will not delete the table as unreachable code.

**``decrement_and_branch_until_zero`'**
: Conditional branch instruction that decrements a register and
jumps if the register is nonzero. Operand 0 is the register to
decrement and test; operand 1 is the label to jump to if the
register is nonzero. See [Looping Patterns](Looping-Patterns.md#apple-jrxw64djnzts2udbor2gk4toom).

This optional instruction pattern is only used by the combiner,
typically for loops reversed by the loop optimizer when strength
reduction is enabled.

**``doloop_end`'**
: Conditional branch instruction that decrements a register and jumps if
the register is nonzero. This instruction takes five operands: Operand
0 is the register to decrement and test; operand 1 is the number of loop
iterations as a `const_int` or `const0_rtx` if this cannot be
determined until run-time; operand 2 is the actual or estimated maximum
number of iterations as a `const_int`; operand 3 is the number of
enclosed loops as a `const_int` (an innermost loop has a value of
1); operand 4 is the label to jump to if the register is nonzero.
See [Looping Patterns](Looping-Patterns.md#apple-jrxw64djnzts2udbor2gk4toom).

This optional instruction pattern should be defined for machines with
low-overhead looping instructions as the loop optimizer will try to
modify suitable loops to utilize it. If nested low-overhead looping is
not supported, use a `define_expand` (see [Expander Definitions](Expander-Definitions.md#apple-iv4haylomrsxelkemvtgs3tjoruw63tt))
and make the pattern fail if operand 3 is not `const1_rtx`.
Similarly, if the actual or estimated maximum number of iterations is
too large for this instruction, make it fail.

**``doloop_begin`'**
: Companion instruction to `doloop_end` required for machines that
need to perform some initialization, such as loading special registers
used by a low-overhead looping instruction. If initialization insns do
not always need to be emitted, use a `define_expand`
(see [Expander Definitions](Expander-Definitions.md#apple-iv4haylomrsxelkemvtgs3tjoruw63tt)) and make it fail.

**``canonicalize_funcptr_for_compare`'**
: Canonicalize the function pointer in operand 1 and store the result
into operand 0.

Operand 0 is always a `reg` and has mode `Pmode`; operand 1
may be a `reg`, `mem`, `symbol_ref`, `const_int`, etc
and also has mode `Pmode`.

Canonicalization of a function pointer usually involves computing
the address of the function which would be called if the function
pointer were used in an indirect call.

Only define this pattern if function pointers on the target machine
can have different values but still call the same function when
used in an indirect call.

**``save_stack_block`'

**``save_stack_function`'

**``save_stack_nonlocal`'

**``restore_stack_block`'

**``restore_stack_function`'

**``restore_stack_nonlocal`'************
: Most machines save and restore the stack pointer by copying it to or
from an object of mode `Pmode`. Do not define these patterns on
such machines.

Some machines require special handling for stack pointer saves and
restores. On those machines, define the patterns corresponding to the
non-standard cases by using a `define_expand` (see [Expander Definitions](Expander-Definitions.md#apple-iv4haylomrsxelkemvtgs3tjoruw63tt)) that produces the required insns. The three types of
saves and restores are:

1. ``save_stack_block`' saves the stack pointer at the start of a block
   that allocates a variable-sized object, and ``restore_stack_block`'
   restores the stack pointer when the block is exited.
2. ``save_stack_function`' and ``restore_stack_function`' do a
   similar job for the outermost block of a function and are used when the
   function allocates variable-sized objects or calls `alloca`. Only
   the epilogue uses the restored stack pointer, allowing a simpler save or
   restore sequence on some machines.
3. ``save_stack_nonlocal`' is used in functions that contain labels
   branched to by nested functions. It saves the stack pointer in such a
   way that the inner function can use ``restore_stack_nonlocal`' to
   restore the stack pointer. The compiler generates code to restore the
   frame and argument pointer registers, but some machines require saving
   and restoring additional data such as register window information or
   stack backchains. Place insns in these patterns to save and restore any
   such required data.

When saving the stack pointer, operand 0 is the save area and operand 1
is the stack pointer. The mode used to allocate the save area defaults
to `Pmode` but you can override that choice by defining the
`STACK_SAVEAREA_MODE` macro (see [Storage Layout](Storage-Layout.md#apple-kn2g64tbm5ss2tdbpfxxk5a)). You must
specify an integral mode, or `VOIDmode` if no save area is needed
for a particular type of save (either because no save is needed or
because a machine-specific save area can be used). Operand 0 is the
stack pointer and operand 1 is the save area for restore operations. If
``save_stack_block`' is defined, operand 0 must not be
`VOIDmode` since these saves can be arbitrarily nested.

A save area is a `mem` that is at a constant offset from
`virtual_stack_vars_rtx` when the stack pointer is saved for use by
nonlocal gotos and a `reg` in the other two cases.

**``allocate_stack`'**
: Subtract (or add if `STACK_GROWS_DOWNWARD` is undefined) operand 1 from
the stack pointer to create space for dynamically allocated data.

Store the resultant pointer to this space into operand 0. If you
are allocating space from the main stack, do this by emitting a
move insn to copy `virtual_stack_dynamic_rtx` to operand 0.
If you are allocating the space elsewhere, generate code to copy the
location of the space to operand 0. In the latter case, you must
ensure this space gets freed when the corresponding space on the main
stack is free.

Do not define this pattern if all that must be done is the subtraction.
Some machines require other operations such as stack probes or
maintaining the back chain. Define this pattern to emit those
operations in addition to updating the stack pointer.

**``check_stack`'**
: If stack checking cannot be done on your system by probing the stack with
a load or store instruction (see [Stack Checking](Stack-Checking.md#apple-kn2gcy3lfvbwqzldnnuw4zy)), define this pattern
to perform the needed check and signaling an error if the stack
has overflowed. The single operand is the location in the stack furthest
from the current stack pointer that you need to validate. Normally,
on machines where this pattern is needed, you would obtain the stack
limit from a global or thread-specific variable or register.

**``nonlocal_goto`'**
: Emit code to generate a non-local goto, e.g., a jump from one function
to a label in an outer function. This pattern has four arguments,
each representing a value to be used in the jump. The first
argument is to be loaded into the frame pointer, the second is
the address to branch to (code to dispatch to the actual label),
the third is the address of a location where the stack is saved,
and the last is the address of the label, to be placed in the
location for the incoming static chain.

On most machines you need not define this pattern, since GCC will
already generate the correct code, which is to load the frame pointer
and static chain, restore the stack (using the
``restore_stack_nonlocal`' pattern, if defined), and jump indirectly
to the dispatcher. You need only define this pattern if this code will
not work on your machine.

**``nonlocal_goto_receiver`'**
: This pattern, if defined, contains code needed at the target of a
nonlocal goto after the code already generated by GCC. You will not
normally need to define this pattern. A typical reason why you might
need this pattern is if some value, such as a pointer to a global table,
must be restored when the frame pointer is restored. Note that a nonlocal
goto only occurs within a unit-of-translation, so a global table pointer
that is shared by all functions of a given module need not be restored.
There are no arguments.

**``exception_receiver`'**
: This pattern, if defined, contains code needed at the site of an
exception handler that isn't needed at the site of a nonlocal goto. You
will not normally need to define this pattern. A typical reason why you
might need this pattern is if some value, such as a pointer to a global
table, must be restored after control flow is branched to the handler of
an exception. There are no arguments.

**``builtin_setjmp_setup`'**
: This pattern, if defined, contains additional code needed to initialize
the `jmp_buf`. You will not normally need to define this pattern.
A typical reason why you might need this pattern is if some value, such
as a pointer to a global table, must be restored. Though it is
preferred that the pointer value be recalculated if possible (given the
address of a label for instance). The single argument is a pointer to
the `jmp_buf`. Note that the buffer is five words long and that
the first three are normally used by the generic mechanism.

**``builtin_setjmp_receiver`'**
: This pattern, if defined, contains code needed at the site of an
built-in setjmp that isn't needed at the site of a nonlocal goto. You
will not normally need to define this pattern. A typical reason why you
might need this pattern is if some value, such as a pointer to a global
table, must be restored. It takes one argument, which is the label
to which builtin_longjmp transfered control; this pattern may be emitted
at a small offset from that label.

**``builtin_longjmp`'**
: This pattern, if defined, performs the entire action of the longjmp.
You will not normally need to define this pattern unless you also define
`builtin_setjmp_setup`. The single argument is a pointer to the
`jmp_buf`.

**``eh_return`'**
: This pattern, if defined, affects the way `__builtin_eh_return`,
and thence the call frame exception handling library routines, are
built. It is intended to handle non-trivial actions needed along
the abnormal return path.

The address of the exception handler to which the function should return
is passed as operand to this pattern. It will normally need to copied by
the pattern to some special register or memory location.
If the pattern needs to determine the location of the target call
frame in order to do so, it may use `EH_RETURN_STACKADJ_RTX`,
if defined; it will have already been assigned.

If this pattern is not defined, the default action will be to simply
copy the return address to `EH_RETURN_HANDLER_RTX`. Either
that macro or this pattern needs to be defined if call frame exception
handling is to be used.

**``prologue`'**
: This pattern, if defined, emits RTL for entry to a function. The function
entry is responsible for setting up the stack frame, initializing the frame
pointer register, saving callee saved registers, etc.

Using a prologue pattern is generally preferred over defining
`TARGET_ASM_FUNCTION_PROLOGUE` to emit assembly code for the prologue.

The `prologue` pattern is particularly useful for targets which perform
instruction scheduling.

**``epilogue`'**
: This pattern emits RTL for exit from a function. The function
exit is responsible for deallocating the stack frame, restoring callee saved
registers and emitting the return instruction.

Using an epilogue pattern is generally preferred over defining
`TARGET_ASM_FUNCTION_EPILOGUE` to emit assembly code for the epilogue.

The `epilogue` pattern is particularly useful for targets which perform
instruction scheduling or which have delay slots for their return instruction.

**``sibcall_epilogue`'**
: This pattern, if defined, emits RTL for exit from a function without the final
branch back to the calling function. This pattern will be emitted before any
sibling call (aka tail call) sites.

The `sibcall_epilogue` pattern must not clobber any arguments used for
parameter passing or any stack slots for arguments passed to the current
function.

**``trap`'**
: This pattern, if defined, signals an error, typically by causing some
kind of signal to be raised. Among other places, it is used by the Java
front end to signal `invalid array index' exceptions.

**``conditional_trap`'**
: Conditional trap instruction. Operand 0 is a piece of RTL which
performs a comparison. Operand 1 is the trap code, an integer.

A typical `conditional_trap` pattern looks like

```
          (define_insn "conditional_trap"
            [(trap_if (match_operator 0 "trap_operator"
                       [(cc0) (const_int 0)])
                      (match_operand 1 "const_int_operand" "i"))]
            ""
            "...")

```


**``prefetch`'**
: This pattern, if defined, emits code for a non-faulting data prefetch
instruction. Operand 0 is the address of the memory to prefetch. Operand 1
is a constant 1 if the prefetch is preparing for a write to the memory
address, or a constant 0 otherwise. Operand 2 is the expected degree of
temporal locality of the data and is a value between 0 and 3, inclusive; 0
means that the data has no temporal locality, so it need not be left in the
cache after the access; 3 means that the data has a high degree of temporal
locality and should be left in all levels of cache possible; 1 and 2 mean,
respectively, a low or moderate degree of temporal locality.

Targets that do not support write prefetches or locality hints can ignore
the values of operands 1 and 2.

**``memory_barrier`'**
: If the target memory model is not fully synchronous, then this pattern
should be defined to an instruction that orders both loads and stores
before the instruction with respect to loads and stores after the instruction.
This pattern has no operands.

**``sync_compare_and_swapmode`'**
: This pattern, if defined, emits code for an atomic compare-and-swap
operation. Operand 1 is the memory on which the atomic operation is
performed. Operand 2 is the “old” value to be compared against the
current contents of the memory location. Operand 3 is the “new” value
to store in the memory if the compare succeeds. Operand 0 is the result
of the operation; it should contain the contents of the memory
before the operation. If the compare succeeds, this should obviously be
a copy of operand 2.

This pattern must show that both operand 0 and operand 1 are modified.

This pattern must issue any memory barrier instructions such that all
memory operations before the atomic operation occur before the atomic
operation and all memory operations after the atomic operation occur
after the atomic operation.

**``sync_compare_and_swap_ccmode`'**
: This pattern is just like `sync_compare_and_swap`mode, except
it should act as if compare part of the compare-and-swap were issued via
`cmp`m. This comparison will only be used with `EQ` and
`NE` branches and `setcc` operations.

Some targets do expose the success or failure of the compare-and-swap
operation via the status flags. Ideally we wouldn't need a separate
named pattern in order to take advantage of this, but the combine pass
does not handle patterns with multiple sets, which is required by
definition for `sync_compare_and_swap`mode.

**``sync_addmode`', ``sync_submode`'

**``sync_iormode`', ``sync_andmode`'

**``sync_xormode`', ``sync_nandmode`'******
: These patterns emit code for an atomic operation on memory.
Operand 0 is the memory on which the atomic operation is performed.
Operand 1 is the second operand to the binary operator.

The “nand” operation is `~op0 & op1`.

This pattern must issue any memory barrier instructions such that all
memory operations before the atomic operation occur before the atomic
operation and all memory operations after the atomic operation occur
after the atomic operation.

If these patterns are not defined, the operation will be constructed
from a compare-and-swap operation, if defined.

**``sync_old_addmode`', ``sync_old_submode`'

**``sync_old_iormode`', ``sync_old_andmode`'

**``sync_old_xormode`', ``sync_old_nandmode`'******
: These patterns are emit code for an atomic operation on memory,
and return the value that the memory contained before the operation.
Operand 0 is the result value, operand 1 is the memory on which the
atomic operation is performed, and operand 2 is the second operand
to the binary operator.

This pattern must issue any memory barrier instructions such that all
memory operations before the atomic operation occur before the atomic
operation and all memory operations after the atomic operation occur
after the atomic operation.

If these patterns are not defined, the operation will be constructed
from a compare-and-swap operation, if defined.

**``sync_new_addmode`', ``sync_new_submode`'

**``sync_new_iormode`', ``sync_new_andmode`'

**``sync_new_xormode`', ``sync_new_nandmode`'******
: These patterns are like their `sync_old_`op counterparts,
except that they return the value that exists in the memory location
after the operation, rather than before the operation.

**``sync_lock_test_and_setmode`'**
: This pattern takes two forms, based on the capabilities of the target.
In either case, operand 0 is the result of the operand, operand 1 is
the memory on which the atomic operation is performed, and operand 2
is the value to set in the lock.

In the ideal case, this operation is an atomic exchange operation, in
which the previous value in memory operand is copied into the result
operand, and the value operand is stored in the memory operand.

For less capable targets, any value operand that is not the constant 1
should be rejected with `FAIL`. In this case the target may use
an atomic test-and-set bit operation. The result operand should contain
1 if the bit was previously set and 0 if the bit was previously clear.
The true contents of the memory operand are implementation defined.

This pattern must issue any memory barrier instructions such that the
pattern as a whole acts as an acquire barrier, that is all memory
operations after the pattern do not occur until the lock is acquired.

If this pattern is not defined, the operation will be constructed from
a compare-and-swap operation, if defined.

**``sync_lock_releasemode`'**
: This pattern, if defined, releases a lock set by
`sync_lock_test_and_set`mode. Operand 0 is the memory
that contains the lock; operand 1 is the value to store in the lock.

If the target doesn't implement full semantics for
`sync_lock_test_and_set`mode, any value operand which is not
the constant 0 should be rejected with `FAIL`, and the true contents
of the memory operand are implementation defined.

This pattern must issue any memory barrier instructions such that the
pattern as a whole acts as a release barrier, that is the lock is
released only after all previous memory operations have completed.

If this pattern is not defined, then a `memory_barrier` pattern
will be emitted, followed by a store of the value to the memory operand.

**``stack_protect_set`'**
: This pattern, if defined, moves a `Pmode` value from the memory
in operand 1 to the memory in operand 0 without leaving the value in
a register afterward. This is to avoid leaking the value some place
that an attacker might use to rewrite the stack guard slot after
having clobbered it.

If this pattern is not defined, then a plain move pattern is generated.

**``stack_protect_test`'**
: This pattern, if defined, compares a `Pmode` value from the
memory in operand 1 with the memory in operand 0 without leaving the
value in a register afterward and branches to operand 2 if the values
weren't equal.

If this pattern is not defined, then a plain compare pattern and
conditional branch pattern is used.
