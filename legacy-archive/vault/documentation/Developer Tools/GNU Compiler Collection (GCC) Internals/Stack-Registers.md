---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Stack-Registers.html
archived_at: '2026-07-15T07:31:00.775088Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Previous: [Leaf Functions](Leaf-Functions.md#apple-jrswczrniz2w4y3unfxw44y),
Up: [Registers](Registers.md#apple-kjswo2ltorsxe4y)

---

#### 13.7.5 Registers That Form a Stack

There are special features to handle computers where some of the
“registers” form a stack. Stack registers are normally written by
pushing onto the stack, and are numbered relative to the top of the
stack.

Currently, GCC can only handle one group of stack-like registers, and
they must be consecutively numbered. Furthermore, the existing
support for stack-like registers is specific to the 80387 floating
point coprocessor. If you have a new architecture that uses
stack-like registers, you will need to do substantial work on
`reg-stack.c` and write your machine description to cooperate
with it, as well as defining these macros.

— Macro: __STACK_REGS__
> Define this if the machine has any stack-like registers.

— Macro: __FIRST_STACK_REG__
> The number of the first stack-like register. This one is the top
> of the stack.

— Macro: __LAST_STACK_REG__
> The number of the last stack-like register. This one is the bottom of
> the stack.
