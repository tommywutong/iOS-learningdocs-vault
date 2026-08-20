---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Insn-Lengths.html
archived_at: '2026-07-15T07:31:02.105001Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Constant Attributes](Constant-Attributes.md#apple-inxw443umfxhilkbor2he2lcov2gk4y),
Previous: [Attr Example](Attr-Example.md#apple-if2hi4rniv4gc3lqnrsq),
Up: [Insn Attributes](Insn-Attributes.md#apple-jfxhg3rnif2hi4tjmj2xizlt)

---

#### 14.19.5 Computing the Length of an Insn

For many machines, multiple types of branch instructions are provided, each
for different length branch displacements. In most cases, the assembler
will choose the correct instruction to use. However, when the assembler
cannot do so, GCC can when a special attribute, the `length`
attribute, is defined. This attribute must be defined to have numeric
values by specifying a null string in its `define_attr`.

In the case of the `length` attribute, two additional forms of
arithmetic terms are allowed in test expressions:

**`(match_dup` n`)`**
: This refers to the address of operand n of the current insn, which
must be a `label_ref`.

**`(pc)`**
: This refers to the address of the _current_ insn. It might have
been more consistent with other usage to make this the address of the
_next_ insn but this would be confusing because the length of the
current insn is to be computed.

For normal insns, the length will be determined by value of the
`length` attribute. In the case of `addr_vec` and
`addr_diff_vec` insn patterns, the length is computed as
the number of vectors multiplied by the size of each vector.

Lengths are measured in addressable storage units (bytes).

The following macros can be used to refine the length computation:

**`ADJUST_INSN_LENGTH (`insn`,` length`)`**
: If defined, modifies the length assigned to instruction insn as a
function of the context in which it is used. length is an lvalue
that contains the initially computed length of the insn and should be
updated with the correct length of the insn.

This macro will normally not be required. A case in which it is
required is the ROMP. On this machine, the size of an `addr_vec`
insn must be increased by two to compensate for the fact that alignment
may be required.

The routine that returns `get_attr_length` (the value of the
`length` attribute) can be used by the output routine to
determine the form of the branch instruction to be written, as the
example below illustrates.

As an example of the specification of variable-length branches, consider
the IBM 360. If we adopt the convention that a register will be set to
the starting address of a function, we can jump to labels within 4k of
the start using a four-byte instruction. Otherwise, we need a six-byte
sequence to load the address from memory and then branch to it.

On such a machine, a pattern for a branch instruction might be specified
as follows:

```
     (define_insn "jump"
       [(set (pc)
             (label_ref (match_operand 0 "" "")))]
       ""
     {
        return (get_attr_length (insn) == 4
                ? "b %l0" : "l r15,=a(%l0); br r15");
     }
       [(set (attr "length")
             (if_then_else (lt (match_dup 0) (const_int 4096))
                           (const_int 4)
                           (const_int 6)))])
```
