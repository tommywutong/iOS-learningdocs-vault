---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/RTL.html
archived_at: '2026-07-15T07:31:00.600681Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Control Flow](Control-Flow.md#apple-inxw45dsn5wc2rtmn53q),
Previous: [Trees](Trees.md#apple-krzgkzlt),
Up: [Top](index.md#apple-krxxa)

---

## 10 RTL Representation

Most of the work of the compiler is done on an intermediate representation
called register transfer language. In this language, the instructions to be
output are described, pretty much one by one, in an algebraic form that
describes what the instruction does.

RTL is inspired by Lisp lists. It has both an internal form, made up of
structures that point at other structures, and a textual form that is used
in the machine description and in printed debugging dumps. The textual
form uses nested parentheses to indicate the pointers in the internal form.

- [RTL Objects](RTL-Objects.md#apple-kjkeylkpmjvgky3uom): Expressions vs vectors vs strings vs integers.
- [RTL Classes](RTL-Classes.md#apple-kjkeylkdnrqxg43fom): Categories of RTL expression objects, and their structure.
- [Accessors](Accessors.md#apple-ifrwgzltonxxe4y): Macros to access expression operands or vector elts.
- [Special Accessors](Special-Accessors.md#apple-knygky3jmfwc2qldmnsxg43pojzq): Macros to access specific annotations on RTL.
- [Flags](Flags.md#apple-izwgcz3t): Other flags in an RTL expression.
- [Machine Modes](Machine-Modes.md#apple-jvqwg2djnzss2tlpmrsxg): Describing the size and format of a datum.
- [Constants](Constants.md#apple-inxw443umfxhi4y): Expressions with constant values.
- [Regs and Memory](Regs-and-Memory.md#apple-kjswo4znmfxgilknmvww64tz): Expressions representing register contents or memory.
- [Arithmetic](Arithmetic.md#apple-ifzgs5dinvsxi2ld): Expressions representing arithmetic on other expressions.
- [Comparisons](Comparisons.md#apple-inxw24dbojuxg33oom): Expressions representing comparison of expressions.
- [Bit-Fields](Bit_002dFields.md#apple-ijuxixzqgazgirtjmvwgi4y): Expressions representing bit-fields in memory or reg.
- [Vector Operations](Vector-Operations.md#apple-kzswg5dpoiwu64dfojqxi2lpnzzq): Expressions involving vector datatypes.
- [Conversions](Conversions.md#apple-inxw45tfojzws33oom): Extending, truncating, floating or fixing.
- [RTL Declarations](RTL-Declarations.md#apple-kjkeylkemvrwyylsmf2gs33oom): Declaring volatility, constancy, etc.
- [Side Effects](Side-Effects.md#apple-knuwizjnivtgmzldorzq): Expressions for storing in registers, etc.
- [Incdec](Incdec.md#apple-jfxggzdfmm): Embedded side-effects for autoincrement addressing.
- [Assembler](Assembler.md#apple-ifzxgzlnmjwgk4q): Representing `asm` with operands.
- [Insns](Insns.md#apple-jfxhg3tt): Expression types for entire insns.
- [Calls](Calls.md#apple-inqwy3dt): RTL representation of function call insns.
- [Sharing](Sharing.md#apple-knugc4tjnztq): Some expressions are unique; others \*must\* be copied.
- [Reading RTL](Reading-RTL.md#apple-kjswczdjnzts2usujq): Reading textual RTL from a file.
