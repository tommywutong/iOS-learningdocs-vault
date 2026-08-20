---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Dependent-Patterns.html
archived_at: '2026-07-15T07:30:59.730795Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Jump Patterns](Jump-Patterns.md#apple-jj2w24bnkbqxi5dfojxhg),
Previous: [Pattern Ordering](Pattern-Ordering.md#apple-kbqxi5dfojxc2t3smrsxe2lom4),
Up: [Machine Desc](Machine-Desc.md#apple-jvqwg2djnzss2rdfonrq)

---

### 12.11 Interdependence of Patterns

Every machine description must have a named pattern for each of the
conditional branch names ``bcond`'. The recognition template
must always have the form

```
     (set (pc)
          (if_then_else (cond (cc0) (const_int 0))
                        (label_ref (match_operand 0 "" ""))
                        (pc)))
```

In addition, every machine description must have an anonymous pattern
for each of the possible reverse-conditional branches. Their templates
look like

```
     (set (pc)
          (if_then_else (cond (cc0) (const_int 0))
                        (pc)
                        (label_ref (match_operand 0 "" ""))))
```

They are necessary because jump optimization can turn direct-conditional
branches into reverse-conditional branches.

It is often convenient to use the `match_operator` construct to
reduce the number of patterns that must be specified for branches. For
example,

```
     (define_insn ""
       [(set (pc)
             (if_then_else (match_operator 0 "comparison_operator"
                                           [(cc0) (const_int 0)])
                           (pc)
                           (label_ref (match_operand 1 "" ""))))]
       "condition"
       "...")
```

In some cases machines support instructions identical except for the
machine mode of one or more operands. For example, there may be
“sign-extend halfword” and “sign-extend byte” instructions whose
patterns are

```
     (set (match_operand:SI 0 ...)
          (extend:SI (match_operand:HI 1 ...)))

     (set (match_operand:SI 0 ...)
          (extend:SI (match_operand:QI 1 ...)))
```

Constant integers do not specify a machine mode, so an instruction to
extend a constant value could match either pattern. The pattern it
actually will match is the one that appears first in the file. For correct
results, this must be the one for the widest possible mode (`HImode`,
here). If the pattern matches the `QImode` instruction, the results
will be incorrect if the constant value does not actually fit that mode.

Such instructions to extend constants are rarely generated because they are
optimized away, but they do occasionally happen in nonoptimized
compilations.

If a constraint in a pattern allows a constant, the reload pass may
replace a register with a constant permitted by the constraint in some
cases. Similarly for memory references. Because of this substitution,
you should not provide separate patterns for increment and decrement
instructions. Instead, they should be generated from the same pattern
that supports register-register add insns by examining the operands and
generating the appropriate machine instruction.
