---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Jump-Patterns.html
archived_at: '2026-07-15T07:31:02.163623Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Looping Patterns](Looping-Patterns.md#apple-jrxw64djnzts2udbor2gk4toom),
Previous: [Dependent Patterns](Dependent-Patterns.md#apple-irsxazlomrsw45bnkbqxi5dfojxhg),
Up: [Machine Desc](Machine-Desc.md#apple-jvqwg2djnzss2rdfonrq)

---

### 14.12 Defining Jump Instruction Patterns

For most machines, GCC assumes that the machine has a condition code.
A comparison insn sets the condition code, recording the results of both
signed and unsigned comparison of the given operands. A separate branch
insn tests the condition code and branches or not according its value.
The branch insns come in distinct signed and unsigned flavors. Many
common machines, such as the VAX, the 68000 and the 32000, work this
way.

Some machines have distinct signed and unsigned compare instructions, and
only one set of conditional branch instructions. The easiest way to handle
these machines is to treat them just like the others until the final stage
where assembly code is written. At this time, when outputting code for the
compare instruction, peek ahead at the following branch using
`next_cc0_user (insn)`. (The variable `insn` refers to the insn
being output, in the output-writing code in an instruction pattern.) If
the RTL says that is an unsigned branch, output an unsigned compare;
otherwise output a signed compare. When the branch itself is output, you
can treat signed and unsigned branches identically.

The reason you can do this is that GCC always generates a pair of
consecutive RTL insns, possibly separated by `note` insns, one to
set the condition code and one to test it, and keeps the pair inviolate
until the end.

To go with this technique, you must define the machine-description macro
`NOTICE_UPDATE_CC` to do `CC_STATUS_INIT`; in other words, no
compare instruction is superfluous.

Some machines have compare-and-branch instructions and no condition code.
A similar technique works for them. When it is time to “output” a
compare instruction, record its operands in two static variables. When
outputting the branch-on-condition-code instruction that follows, actually
output a compare-and-branch instruction that uses the remembered operands.

It also works to define patterns for compare-and-branch instructions.
In optimizing compilation, the pair of compare and branch instructions
will be combined according to these patterns. But this does not happen
if optimization is not requested. So you must use one of the solutions
above in addition to any special patterns you define.

In many RISC machines, most instructions do not affect the condition
code and there may not even be a separate condition code register. On
these machines, the restriction that the definition and use of the
condition code be adjacent insns is not necessary and can prevent
important optimizations. For example, on the IBM RS/6000, there is a
delay for taken branches unless the condition code register is set three
instructions earlier than the conditional branch. The instruction
scheduler cannot perform this optimization if it is not permitted to
separate the definition and use of the condition code register.

On these machines, do not use `(cc0)`, but instead use a register
to represent the condition code. If there is a specific condition code
register in the machine, use a hard register. If the condition code or
comparison result can be placed in any general register, or if there are
multiple condition registers, use a pseudo register.

On some machines, the type of branch instruction generated may depend on
the way the condition code was produced; for example, on the 68k and
SPARC, setting the condition code directly from an add or subtract
instruction does not clear the overflow bit the way that a test
instruction does, so a different branch instruction must be used for
some conditional branches. For machines that use `(cc0)`, the set
and use of the condition code must be adjacent (separated only by
`note` insns) allowing flags in `cc_status` to be used.
(See [Condition Code](Condition-Code.md#apple-inxw4zdjoruw63rninxwizi).) Also, the comparison and branch insns can be
located from each other by using the functions `prev_cc0_setter`
and `next_cc0_user`.

However, this is not true on machines that do not use `(cc0)`. On
those machines, no assumptions can be made about the adjacency of the
compare and branch insns and the above methods cannot be used. Instead,
we use the machine mode of the condition code register to record
different formats of the condition code register.

Registers used to store the condition code value should have a mode that
is in class `MODE_CC`. Normally, it will be `CCmode`. If
additional modes are required (as for the add example mentioned above in
the SPARC), define them in `machine-modes.def`
(see [Condition Code](Condition-Code.md#apple-inxw4zdjoruw63rninxwizi)). Also define `SELECT_CC_MODE` to choose
a mode given an operand of a compare.

If it is known during RTL generation that a different mode will be
required (for example, if the machine has separate compare instructions
for signed and unsigned quantities, like most IBM processors), they can
be specified at that time.

If the cases that require different modes would be made by instruction
combination, the macro `SELECT_CC_MODE` determines which machine
mode should be used for the comparison result. The patterns should be
written using that mode. To support the case of the add on the SPARC
discussed above, we have the pattern

```
     (define_insn ""
       [(set (reg:CC_NOOV 0)
             (compare:CC_NOOV
               (plus:SI (match_operand:SI 0 "register_operand" "%r")
                        (match_operand:SI 1 "arith_operand" "rI"))
               (const_int 0)))]
       ""
       "...")
```

The `SELECT_CC_MODE` macro on the SPARC returns `CC_NOOVmode`
for comparisons whose argument is a `plus`.
