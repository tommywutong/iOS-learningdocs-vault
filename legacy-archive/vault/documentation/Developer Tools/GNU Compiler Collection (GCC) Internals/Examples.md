---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Examples.html
archived_at: '2026-07-15T07:30:59.783744Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Previous: [String Substitutions](String-Substitutions.md#apple-kn2he2lom4wvg5lcon2gs5dvoruw63tt),
Up: [Mode Macros](Mode-Macros.md#apple-jvxwizjnjvqwg4tpom)

---

##### 12.22.1.3 Mode Macro Examples

Here is an example from the MIPS port. It defines the following
modes and attributes (among others):

```
     (define_mode_macro GPR [SI (DI "TARGET_64BIT")])
     (define_mode_attr d [(SI "") (DI "d")])
```

and uses the following template to define both `subsi3`
and `subdi3`:

```
     (define_insn "sub<mode>3"
       [(set (match_operand:GPR 0 "register_operand" "=d")
             (minus:GPR (match_operand:GPR 1 "register_operand" "d")
                        (match_operand:GPR 2 "register_operand" "d")))]
       ""
       "<d>subu\t%0,%1,%2"
       [(set_attr "type" "arith")
        (set_attr "mode" "<MODE>")])
```

This is exactly equivalent to:

```
     (define_insn "subsi3"
       [(set (match_operand:SI 0 "register_operand" "=d")
             (minus:SI (match_operand:SI 1 "register_operand" "d")
                       (match_operand:SI 2 "register_operand" "d")))]
       ""
       "subu\t%0,%1,%2"
       [(set_attr "type" "arith")
        (set_attr "mode" "SI")])

     (define_insn "subdi3"
       [(set (match_operand:DI 0 "register_operand" "=d")
             (minus:DI (match_operand:DI 1 "register_operand" "d")
                       (match_operand:DI 2 "register_operand" "d")))]
       ""
       "dsubu\t%0,%1,%2"
       [(set_attr "type" "arith")
        (set_attr "mode" "DI")])
```
