---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Stack-and-Calling.html
archived_at: '2026-07-15T07:31:02.857835Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Varargs](Varargs.md#apple-kzqxeylsm5zq),
Previous: [Old Constraints](Old-Constraints.md#apple-j5wgilkdn5xhg5dsmfuw45dt),
Up: [Target Macros](Target-Macros.md#apple-krqxez3foqwu2yldojxxg)

---

### 15.10 Stack Layout and Calling Conventions

This describes the stack layout and calling conventions.

- [Frame Layout](Frame-Layout.md#apple-izzgc3lffvggc6lpov2a)
- [Exception Handling](Exception-Handling.md#apple-iv4ggzlqoruw63rnjbqw4zdmnfxgo)
- [Stack Checking](Stack-Checking.md#apple-kn2gcy3lfvbwqzldnnuw4zy)
- [Frame Registers](Frame-Registers.md#apple-izzgc3lffvjgkz3jon2gk4tt)
- [Elimination](Elimination.md#apple-ivwgs3ljnzqxi2lpny)
- [Stack Arguments](Stack-Arguments.md#apple-kn2gcy3lfvaxez3vnvsw45dt)
- [Register Arguments](Register-Arguments.md#apple-kjswo2ltorsxelkbojtxk3lfnz2hg)
- [Scalar Return](Scalar-Return.md#apple-knrwc3dboiwvezluovzg4)
- [Aggregate Return](Aggregate-Return.md#apple-iftwo4tfm5qxizjnkjsxi5lsny)
- [Caller Saves](Caller-Saves.md#apple-inqwy3dfoiwvgylwmvzq)
- [Function Entry](Function-Entry.md#apple-iz2w4y3unfxw4lkfnz2he6i)
- [Profiling](Profiling.md#apple-kbzg6ztjnruw4zy)
- [Tail Calls](Tail-Calls.md#apple-krqws3bninqwy3dt)
- [Stack Smashing Protection](Stack-Smashing-Protection.md#apple-kn2gcy3lfvjw2yltnbuw4zznkbzg65dfmn2gs33o)
