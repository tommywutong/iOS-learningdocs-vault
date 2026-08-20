---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/GIMPLE-Exception-Handling.html
archived_at: '2026-07-15T07:31:01.996233Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Previous: [Cleanups](Cleanups.md#apple-inwgkyloovyhg),
Up: [Statements](Statements.md#apple-kn2gc5dfnvsw45dt)

---

##### 10.2.4.8 Exception Handling

Other exception handling constructs are represented using
`TRY_CATCH_EXPR`. `TRY_CATCH_EXPR` has two operands. The
first operand is a sequence of statements to execute. If executing
these statements does not throw an exception, then the second operand
is ignored. Otherwise, if an exception is thrown, then the second
operand of the `TRY_CATCH_EXPR` is checked. The second operand
may have the following forms:

1. A sequence of statements to execute. When an exception occurs,
   these statements are executed, and then the exception is rethrown.
2. A sequence of `CATCH_EXPR` expressions. Each `CATCH_EXPR`
   has a list of applicable exception types and handler code. If the
   thrown exception matches one of the caught types, the associated
   handler code is executed. If the handler code falls off the bottom,
   execution continues after the original `TRY_CATCH_EXPR`.
3. An `EH_FILTER_EXPR` expression. This has a list of
   permitted exception types, and code to handle a match failure. If the
   thrown exception does not match one of the allowed types, the
   associated match failure code is executed. If the thrown exception
   does match, it continues unwinding the stack looking for the next
   handler.

Currently throwing an exception is not directly represented in GIMPLE,
since it is implemented by calling a function. At some point in the future
we will want to add some way to express that the call will throw an
exception of a known type.

Just before running the optimizers, the compiler lowers the high-level
EH constructs above into a set of ``goto`'s, magic labels, and EH
regions. Continuing to unwind at the end of a cleanup is represented
with a `RESX_EXPR`.
