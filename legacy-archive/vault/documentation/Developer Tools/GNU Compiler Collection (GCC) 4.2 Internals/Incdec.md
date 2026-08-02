---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Incdec.html
archived_at: '2026-07-15T07:31:02.075003Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Assembler](Assembler.md#apple-ifzxgzlnmjwgk4q),
Previous: [Side Effects](Side-Effects.md#apple-knuwizjnivtgmzldorzq),
Up: [RTL](RTL.md#apple-kjkey)

---

### 12.16 Embedded Side-Effects on Addresses

Six special side-effect expression codes appear as memory addresses.

**`(pre_dec:`m x`)`**
: Represents the side effect of decrementing x by a standard
amount and represents also the value that x has after being
decremented. x must be a `reg` or `mem`, but most
machines allow only a `reg`. m must be the machine mode
for pointers on the machine in use. The amount x is decremented
by is the length in bytes of the machine mode of the containing memory
reference of which this expression serves as the address. Here is an
example of its use:

```
          (mem:DF (pre_dec:SI (reg:SI 39)))

```

This says to decrement pseudo register 39 by the length of a `DFmode`
value and use the result to address a `DFmode` value.

**`(pre_inc:`m x`)`**
: Similar, but specifies incrementing x instead of decrementing it.

**`(post_dec:`m x`)`**
: Represents the same side effect as `pre_dec` but a different
value. The value represented here is the value x has _before_
being decremented.

**`(post_inc:`m x`)`**
: Similar, but specifies incrementing x instead of decrementing it.

**`(post_modify:`m x y`)`**
: Represents the side effect of setting x to y and
represents x before x is modified. x must be a
`reg` or `mem`, but most machines allow only a `reg`.
m must be the machine mode for pointers on the machine in use.

The expression y must be one of three forms:

`(plus:`m x z`)`,
`(minus:`m x z`)`, or
`(plus:`m x i`)`,

where z is an index register and i is a constant.

Here is an example of its use:

```
          (mem:SF (post_modify:SI (reg:SI 42) (plus (reg:SI 42)
                                                    (reg:SI 48))))

```

This says to modify pseudo register 42 by adding the contents of pseudo
register 48 to it, after the use of what ever 42 points to.

**`(pre_modify:`m x expr`)`**
: Similar except side effects happen before the use.

These embedded side effect expressions must be used with care. Instruction
patterns may not use them. Until the ``flow`' pass of the compiler,
they may occur only to represent pushes onto the stack. The ``flow`'
pass finds cases where registers are incremented or decremented in one
instruction and used as an address shortly before or after; these cases are
then transformed to use pre- or post-increment or -decrement.

If a register used as the operand of these expressions is used in
another address in an insn, the original value of the register is used.
Uses of the register outside of an address are not permitted within the
same insn as a use in an embedded side effect expression because such
insns behave differently on different machines and hence must be treated
as ambiguous and disallowed.

An instruction that can be represented with an embedded side effect
could also be represented using `parallel` containing an additional
`set` to describe how the address register is altered. This is not
done because machines that allow these operations at all typically
allow them wherever a memory address is called for. Describing them as
additional parallel stores would require doubling the number of entries
in the machine description.
