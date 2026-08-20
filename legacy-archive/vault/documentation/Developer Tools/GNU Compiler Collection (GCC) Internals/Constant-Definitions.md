---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Constant-Definitions.html
archived_at: '2026-07-15T07:30:59.604876Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Macros](Macros.md#apple-jvqwg4tpom),
Previous: [Conditional Execution](Conditional-Execution.md#apple-inxw4zdjoruw63tbnqwuk6dfmn2xi2lpny),
Up: [Machine Desc](Machine-Desc.md#apple-jvqwg2djnzss2rdfonrq)

---

### 12.21 Constant Definitions

Using literal constants inside instruction patterns reduces legibility and
can be a maintenance problem.

To overcome this problem, you may use the `define_constants`
expression. It contains a vector of name-value pairs. From that
point on, wherever any of the names appears in the MD file, it is as
if the corresponding value had been written instead. You may use
`define_constants` multiple times; each appearance adds more
constants to the table. It is an error to redefine a constant with
a different value.

To come back to the a29k load multiple example, instead of

```
     (define_insn ""
       [(match_parallel 0 "load_multiple_operation"
          [(set (match_operand:SI 1 "gpc_reg_operand" "=r")
                (match_operand:SI 2 "memory_operand" "m"))
           (use (reg:SI 179))
           (clobber (reg:SI 179))])]
       ""
       "loadm 0,0,%1,%2")
```

You could write:

```
     (define_constants [
         (R_BP 177)
         (R_FC 178)
         (R_CR 179)
         (R_Q  180)
     ])

     (define_insn ""
       [(match_parallel 0 "load_multiple_operation"
          [(set (match_operand:SI 1 "gpc_reg_operand" "=r")
                (match_operand:SI 2 "memory_operand" "m"))
           (use (reg:SI R_CR))
           (clobber (reg:SI R_CR))])]
       ""
       "loadm 0,0,%1,%2")
```

The constants that are defined with a define_constant are also output
in the insn-codes.h header file as #defines.
