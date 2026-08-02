---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Cleanups.html
archived_at: '2026-07-15T07:30:59.369156Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [GIMPLE Exception Handling](GIMPLE-Exception-Handling.md#apple-i5eu2ucmiuwuk6ddmvyhi2lpnywuqylomrwgs3th),
Previous: [Jumps](Jumps.md#apple-jj2w24dt),
Up: [Statements](Statements.md#apple-kn2gc5dfnvsw45dt)

---

##### 9.2.4.7 Cleanups

Destructors for local C++ objects and similar dynamic cleanups are
represented in GIMPLE by a `TRY_FINALLY_EXPR`. When the controlled
block exits, the cleanup is run.

`TRY_FINALLY_EXPR` complicates the flow graph, since the cleanup
needs to appear on every edge out of the controlled block; this
reduces the freedom to move code across these edges. Therefore, the
EH lowering pass which runs before most of the optimization passes
eliminates these expressions by explicitly adding the cleanup to each
edge.
