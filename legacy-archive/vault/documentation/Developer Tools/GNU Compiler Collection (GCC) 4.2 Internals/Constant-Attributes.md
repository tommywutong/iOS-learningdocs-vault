---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Constant-Attributes.html
archived_at: '2026-07-15T07:31:01.563180Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Delay Slots](Delay-Slots.md#apple-irswyylzfvjwy33uom),
Previous: [Insn Lengths](Insn-Lengths.md#apple-jfxhg3rnjrsw4z3unbzq),
Up: [Insn Attributes](Insn-Attributes.md#apple-jfxhg3rnif2hi4tjmj2xizlt)

---

#### 14.19.6 Constant Attributes

A special form of `define_attr`, where the expression for the
default value is a `const` expression, indicates an attribute that
is constant for a given run of the compiler. Constant attributes may be
used to specify which variety of processor is used. For example,

```
     (define_attr "cpu" "m88100,m88110,m88000"
      (const
       (cond [(symbol_ref "TARGET_88100") (const_string "m88100")
              (symbol_ref "TARGET_88110") (const_string "m88110")]
             (const_string "m88000"))))

     (define_attr "memory" "fast,slow"
      (const
       (if_then_else (symbol_ref "TARGET_FAST_MEM")
                     (const_string "fast")
                     (const_string "slow"))))
```

The routine generated for constant attributes has no parameters as it
does not depend on any particular insn. RTL expressions used to define
the value of a constant attribute may use the `symbol_ref` form,
but may not use either the `match_operand` form or `eq_attr`
forms involving insn attributes.
