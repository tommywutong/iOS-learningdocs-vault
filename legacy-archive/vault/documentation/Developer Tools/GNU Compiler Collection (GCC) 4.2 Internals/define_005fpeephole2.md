---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/define_005fpeephole2.html
archived_at: '2026-07-15T07:31:03.131011Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Previous: [define_peephole](define_005fpeephole.md#apple-mrswm2lomvptambvmzygkzlqnbxwyzi),
Up: [Peephole Definitions](Peephole-Definitions.md#apple-kbswk4din5wgklkemvtgs3tjoruw63tt)

---

#### 14.18.2 RTL to RTL Peephole Optimizers

The `define_peephole2` definition tells the compiler how to
substitute one sequence of instructions for another sequence,
what additional scratch registers may be needed and what their
lifetimes must be.

```
     (define_peephole2
       [insn-pattern-1
        insn-pattern-2
        ...]
       "condition"
       [new-insn-pattern-1
        new-insn-pattern-2
        ...]
       "preparation-statements")
```

The definition is almost identical to `define_split`
(see [Insn Splitting](Insn-Splitting.md#apple-jfxhg3rnknygy2luoruw4zy)) except that the pattern to match is not a
single instruction, but a sequence of instructions.

It is possible to request additional scratch registers for use in the
output template. If appropriate registers are not free, the pattern
will simply not match.

Scratch registers are requested with a `match_scratch` pattern at
the top level of the input pattern. The allocated register (initially) will
be dead at the point requested within the original sequence. If the scratch
is used at more than a single point, a `match_dup` pattern at the
top level of the input pattern marks the last position in the input sequence
at which the register must be available.

Here is an example from the IA-32 machine description:

```
     (define_peephole2
       [(match_scratch:SI 2 "r")
        (parallel [(set (match_operand:SI 0 "register_operand" "")
                        (match_operator:SI 3 "arith_or_logical_operator"
                          [(match_dup 0)
                           (match_operand:SI 1 "memory_operand" "")]))
                   (clobber (reg:CC 17))])]
       "! optimize_size && ! TARGET_READ_MODIFY"
       [(set (match_dup 2) (match_dup 1))
        (parallel [(set (match_dup 0)
                        (match_op_dup 3 [(match_dup 0) (match_dup 2)]))
                   (clobber (reg:CC 17))])]
       "")
```

This pattern tries to split a load from its use in the hopes that we'll be
able to schedule around the memory load latency. It allocates a single
`SImode` register of class `GENERAL_REGS` (`"r"`) that needs
to be live only at the point just before the arithmetic.

A real example requiring extended scratch lifetimes is harder to come by,
so here's a silly made-up example:

```
     (define_peephole2
       [(match_scratch:SI 4 "r")
        (set (match_operand:SI 0 "" "") (match_operand:SI 1 "" ""))
        (set (match_operand:SI 2 "" "") (match_dup 1))
        (match_dup 4)
        (set (match_operand:SI 3 "" "") (match_dup 1))]
       "/* determine 1 does not overlap 0 and 2 */"
       [(set (match_dup 4) (match_dup 1))
        (set (match_dup 0) (match_dup 4))
        (set (match_dup 2) (match_dup 4))]
        (set (match_dup 3) (match_dup 4))]
       "")
```

If we had not added the `(match_dup 4)` in the middle of the input
sequence, it might have been the case that the register we chose at the
beginning of the sequence is killed by the first or second `set`.
