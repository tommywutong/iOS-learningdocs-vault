---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Assembler.html
archived_at: '2026-07-15T07:30:59.290569Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Insns](Insns.md#apple-jfxhg3tt),
Previous: [Incdec](Incdec.md#apple-jfxggzdfmm),
Up: [RTL](RTL.md#apple-kjkey)

---

### 10.17 Assembler Instructions as Expressions

The RTX code `asm_operands` represents a value produced by a
user-specified assembler instruction. It is used to represent
an `asm` statement with arguments. An `asm` statement with
a single output operand, like this:

```
     asm ("foo %1,%2,%0" : "=a" (outputvar) : "g" (x + y), "di" (*z));
```

is represented using a single `asm_operands` RTX which represents
the value that is stored in `outputvar`:

```
     (set rtx-for-outputvar
          (asm_operands "foo %1,%2,%0" "a" 0
                        [rtx-for-addition-result rtx-for-*z]
                        [(asm_input:m1 "g")
                         (asm_input:m2 "di")]))
```

Here the operands of the `asm_operands` RTX are the assembler
template string, the output-operand's constraint, the index-number of the
output operand among the output operands specified, a vector of input
operand RTX's, and a vector of input-operand modes and constraints. The
mode m1 is the mode of the sum `x+y`; m2 is that of
`*z`.

When an `asm` statement has multiple output values, its insn has
several such `set` RTX's inside of a `parallel`. Each `set`
contains a `asm_operands`; all of these share the same assembler
template and vectors, but each contains the constraint for the respective
output operand. They are also distinguished by the output-operand index
number, which is 0, 1, ... for successive output operands.
