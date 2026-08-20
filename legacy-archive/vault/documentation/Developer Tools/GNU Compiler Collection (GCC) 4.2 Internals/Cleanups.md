---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Cleanups.html
archived_at: '2026-07-15T07:31:01.322013Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [GIMPLE Exception Handling](GIMPLE-Exception-Handling.md#apple-i5eu2ucmiuwuk6ddmvyhi2lpnywuqylomrwgs3th),
Previous: [Jumps](Jumps.md#apple-jj2w24dt),
Up: [Statements](Statements.md#apple-kn2gc5dfnvsw45dt)

---

##### 10.2.4.7 Cleanups

Destructors for local C++ objects and similar dynamic cleanups are
represented in GIMPLE by a `TRY_FINALLY_EXPR`.
`TRY_FINALLY_EXPR` has two operands, both of which are a sequence
of statements to execute. The first sequence is executed. When it
completes the second sequence is executed.

The first sequence may complete in the following ways:

1. Execute the last statement in the sequence and fall off the
   end.
2. Execute a goto statement (`GOTO_EXPR`) to an ordinary
   label outside the sequence.
3. Execute a return statement (`RETURN_EXPR`).
4. Throw an exception. This is currently not explicitly represented in
   GIMPLE.

The second sequence is not executed if the first sequence completes by
calling `setjmp` or `exit` or any other function that does
not return. The second sequence is also not executed if the first
sequence completes via a non-local goto or a computed goto (in general
the compiler does not know whether such a goto statement exits the
first sequence or not, so we assume that it doesn't).

After the second sequence is executed, if it completes normally by
falling off the end, execution continues wherever the first sequence
would have continued, by falling off the end, or doing a goto, etc.

`TRY_FINALLY_EXPR` complicates the flow graph, since the cleanup
needs to appear on every edge out of the controlled block; this
reduces the freedom to move code across these edges. Therefore, the
EH lowering pass which runs before most of the optimization passes
eliminates these expressions by explicitly adding the cleanup to each
edge. Rethrowing the exception is represented using `RESX_EXPR`.
