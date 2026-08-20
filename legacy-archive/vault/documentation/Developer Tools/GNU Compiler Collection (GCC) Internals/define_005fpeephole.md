---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/define_005fpeephole.html
archived_at: '2026-07-15T07:31:01.030576Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [define_peephole2](define_005fpeephole2.md#apple-mrswm2lomvptambvmzygkzlqnbxwyzjs),
Up: [Peephole Definitions](Peephole-Definitions.md#apple-kbswk4din5wgklkemvtgs3tjoruw63tt)

---

#### 12.18.1 RTL to Text Peephole Optimizers

A definition looks like this:

```
     (define_peephole
       [insn-pattern-1
        insn-pattern-2
        ...]
       "condition"
       "template"
       "optional-insn-attributes")
```

The last string operand may be omitted if you are not using any
machine-specific information in this machine description. If present,
it must obey the same rules as in a `define_insn`.

In this skeleton, insn-pattern-1 and so on are patterns to match
consecutive insns. The optimization applies to a sequence of insns when
insn-pattern-1 matches the first one, insn-pattern-2 matches
the next, and so on.

Each of the insns matched by a peephole must also match a
`define_insn`. Peepholes are checked only at the last stage just
before code generation, and only optionally. Therefore, any insn which
would match a peephole but no `define_insn` will cause a crash in code
generation in an unoptimized compilation, or at various optimization
stages.

The operands of the insns are matched with `match_operands`,
`match_operator`, and `match_dup`, as usual. What is not
usual is that the operand numbers apply to all the insn patterns in the
definition. So, you can check for identical operands in two insns by
using `match_operand` in one insn and `match_dup` in the
other.

The operand constraints used in `match_operand` patterns do not have
any direct effect on the applicability of the peephole, but they will
be validated afterward, so make sure your constraints are general enough
to apply whenever the peephole matches. If the peephole matches
but the constraints are not satisfied, the compiler will crash.

It is safe to omit constraints in all the operands of the peephole; or
you can write constraints which serve as a double-check on the criteria
previously tested.

Once a sequence of insns matches the patterns, the condition is
checked. This is a C expression which makes the final decision whether to
perform the optimization (we do so if the expression is nonzero). If
condition is omitted (in other words, the string is empty) then the
optimization is applied to every sequence of insns that matches the
patterns.

The defined peephole optimizations are applied after register allocation
is complete. Therefore, the peephole definition can check which
operands have ended up in which kinds of registers, just by looking at
the operands.

The way to refer to the operands in condition is to write
`operands[`i`]` for operand number i (as matched by
`(match_operand` i `...)`). Use the variable `insn`
to refer to the last of the insns being matched; use
`prev_active_insn` to find the preceding insns.

When optimizing computations with intermediate results, you can use
condition to match only when the intermediate results are not used
elsewhere. Use the C expression `dead_or_set_p (`insn`,`op`)`, where insn is the insn in which you expect the value
to be used for the last time (from the value of `insn`, together
with use of `prev_nonnote_insn`), and op is the intermediate
value (from `operands[`i`]`).

Applying the optimization means replacing the sequence of insns with one
new insn. The template controls ultimate output of assembler code
for this combined insn. It works exactly like the template of a
`define_insn`. Operand numbers in this template are the same ones
used in matching the original sequence of insns.

The result of a defined peephole optimizer does not need to match any of
the insn patterns in the machine description; it does not even have an
opportunity to match them. The peephole optimizer definition itself serves
as the insn pattern to control how the insn is output.

Defined peephole optimizers are run as assembler code is being output,
so the insns they produce are never combined or rearranged in any way.

Here is an example, taken from the 68000 machine description:

```
     (define_peephole
       [(set (reg:SI 15) (plus:SI (reg:SI 15) (const_int 4)))
        (set (match_operand:DF 0 "register_operand" "=f")
             (match_operand:DF 1 "register_operand" "ad"))]
       "FP_REG_P (operands[0]) && ! FP_REG_P (operands[1])"
     {
       rtx xoperands[2];
       xoperands[1] = gen_rtx_REG (SImode, REGNO (operands[1]) + 1);
     #ifdef MOTOROLA
       output_asm_insn ("move.l %1,(sp)", xoperands);
       output_asm_insn ("move.l %1,-(sp)", operands);
       return "fmove.d (sp)+,%0";
     #else
       output_asm_insn ("movel %1,sp@", xoperands);
       output_asm_insn ("movel %1,sp@-", operands);
       return "fmoved sp@+,%0";
     #endif
     })
```

The effect of this optimization is to change

```
     jbsr _foobar
     addql #4,sp
     movel d1,sp@-
     movel d0,sp@-
     fmoved sp@+,fp0
```

into

```
     jbsr _foobar
     movel d1,sp@
     movel d0,sp@-
     fmoved sp@+,fp0
```

insn-pattern-1 and so on look _almost_ like the second
operand of `define_insn`. There is one important difference: the
second operand of `define_insn` consists of one or more RTX's
enclosed in square brackets. Usually, there is only one: then the same
action can be written as an element of a `define_peephole`. But
when there are multiple actions in a `define_insn`, they are
implicitly enclosed in a `parallel`. Then you must explicitly
write the `parallel`, and the square brackets within it, in the
`define_peephole`. Thus, if an insn pattern looks like this,

```
     (define_insn "divmodsi4"
       [(set (match_operand:SI 0 "general_operand" "=d")
             (div:SI (match_operand:SI 1 "general_operand" "0")
                     (match_operand:SI 2 "general_operand" "dmsK")))
        (set (match_operand:SI 3 "general_operand" "=d")
             (mod:SI (match_dup 1) (match_dup 2)))]
       "TARGET_68020"
       "divsl%.l %2,%3:%0")
```

then the way to mention this insn in a peephole is as follows:

```
     (define_peephole
       [...
        (parallel
         [(set (match_operand:SI 0 "general_operand" "=d")
               (div:SI (match_operand:SI 1 "general_operand" "0")
                       (match_operand:SI 2 "general_operand" "dmsK")))
          (set (match_operand:SI 3 "general_operand" "=d")
               (mod:SI (match_dup 1) (match_dup 2)))])
        ...]
       ...)
```
