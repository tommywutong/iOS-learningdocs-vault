---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/GIMPLE-Exception-Handling.html
archived_at: '2026-07-15T07:30:59.980943Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Previous: [Cleanups](Cleanups.md#apple-inwgkyloovyhg),
Up: [Statements](Statements.md#apple-kn2gc5dfnvsw45dt)

---

##### 9.2.4.8 Exception Handling

Other exception handling constructs are represented using
`TRY_CATCH_EXPR`. The handler operand of a `TRY_CATCH_EXPR`
can be a normal statement to be executed if the controlled block throws an
exception, or it can have one of two special forms:

1. A `CATCH_EXPR` executes its handler if the thrown exception
   matches one of the allowed types. Multiple handlers can be
   expressed by a sequence of `CATCH_EXPR` statements.
2. An `EH_FILTER_EXPR` executes its handler if the thrown
   exception does not match one of the allowed types.

Currently throwing an exception is not directly represented in GIMPLE,
since it is implemented by calling a function. At some point in the future
we will want to add some way to express that the call will throw an
exception of a known type.

Just before running the optimizers, the compiler lowers the high-level
EH constructs above into a set of ``goto`'s, magic labels, and EH
regions. Continuing to unwind at the end of a cleanup is represented
with a `RESX_EXPR`.
