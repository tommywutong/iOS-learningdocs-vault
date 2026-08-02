---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Attr-Example.html
archived_at: '2026-07-15T07:30:59.296672Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Insn Lengths](Insn-Lengths.md#apple-jfxhg3rnjrsw4z3unbzq),
Previous: [Tagging Insns](Tagging-Insns.md#apple-krqwoz3jnzts2sloonxhg),
Up: [Insn Attributes](Insn-Attributes.md#apple-jfxhg3rnif2hi4tjmj2xizlt)

---

#### 12.19.4 Example of Attribute Specifications

The judicious use of defaulting is important in the efficient use of
insn attributes. Typically, insns are divided into types and an
attribute, customarily called `type`, is used to represent this
value. This attribute is normally used only to define the default value
for other attributes. An example will clarify this usage.

Assume we have a RISC machine with a condition code and in which only
full-word operations are performed in registers. Let us assume that we
can divide all insns into loads, stores, (integer) arithmetic
operations, floating point operations, and branches.

Here we will concern ourselves with determining the effect of an insn on
the condition code and will limit ourselves to the following possible
effects: The condition code can be set unpredictably (clobbered), not
be changed, be set to agree with the results of the operation, or only
changed if the item previously set into the condition code has been
modified.

Here is part of a sample `md` file for such a machine:

```
     (define_attr "type" "load,store,arith,fp,branch" (const_string "arith"))

     (define_attr "cc" "clobber,unchanged,set,change0"
                  (cond [(eq_attr "type" "load")
                             (const_string "change0")
                         (eq_attr "type" "store,branch")
                             (const_string "unchanged")
                         (eq_attr "type" "arith")
                             (if_then_else (match_operand:SI 0 "" "")
                                           (const_string "set")
                                           (const_string "clobber"))]
                        (const_string "clobber")))

     (define_insn ""
       [(set (match_operand:SI 0 "general_operand" "=r,r,m")
             (match_operand:SI 1 "general_operand" "r,m,r"))]
       ""
       "@
        move %0,%1
        load %0,%1
        store %0,%1"
       [(set_attr "type" "arith,load,store")])
```

Note that we assume in the above example that arithmetic operations
performed on quantities smaller than a machine word clobber the condition
code since they will set the condition code to a value corresponding to the
full-word result.
