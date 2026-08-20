---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/PIC.html
archived_at: '2026-07-15T07:31:02.555453Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Assembler Format](Assembler-Format.md#apple-ifzxgzlnmjwgk4rnizxxe3lboq),
Previous: [Sections](Sections.md#apple-knswg5djn5xhg),
Up: [Target Macros](Target-Macros.md#apple-krqxez3foqwu2yldojxxg)

---

### 15.20 Position Independent Code

This section describes macros that help implement generation of position
independent code. Simply defining these macros is not enough to
generate valid PIC; you must also add support to the macros
`GO_IF_LEGITIMATE_ADDRESS` and `PRINT_OPERAND_ADDRESS`, as
well as `LEGITIMIZE_ADDRESS`. You must modify the definition of
``movsi`' to do something appropriate when the source operand
contains a symbolic address. You may also need to alter the handling of
switch statements so that they use relative addresses.

— Macro: __PIC_OFFSET_TABLE_REGNUM__
> The register number of the register used to address a table of static
> data addresses in memory. In some cases this register is defined by a
> processor's “application binary interface” (ABI). When this macro
> is defined, RTL is generated for this register once, as with the stack
> pointer and frame pointer registers. If this macro is not defined, it
> is up to the machine-dependent files to allocate such a register (if
> necessary). Note that this register must be fixed when in use (e.g.
> when `flag_pic` is true).

— Macro: __PIC_OFFSET_TABLE_REG_CALL_CLOBBERED__
> Define this macro if the register defined by
> `PIC_OFFSET_TABLE_REGNUM` is clobbered by calls. Do not define
> this macro if `PIC_OFFSET_TABLE_REGNUM` is not defined.

— Macro: __LEGITIMATE_PIC_OPERAND_P__ (x)
> A C expression that is nonzero if x is a legitimate immediate
> operand on the target machine when generating position independent code.
> You can assume that x satisfies `CONSTANT_P`, so you need not
> check this. You can also assume flag_pic is true, so you need not
> check it either. You need not define this macro if all constants
> (including `SYMBOL_REF`) can be immediate operands when generating
> position independent code.
