---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/GGC-Roots.html
archived_at: '2026-07-15T07:30:59.971428Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Files](Files.md#apple-izuwyzlt),
Previous: [GTY Options](GTY-Options.md#apple-i5kfslkpob2gs33oom),
Up: [Type Information](Type-Information.md#apple-kr4xazjnjfxgm33snvqxi2lpny)

---

### 18.2 Marking Roots for the Garbage Collector

In addition to keeping track of types, the type machinery also locates
the global variables (roots) that the garbage collector starts
at. Roots must be declared using one of the following syntaxes:

- `extern GTY(([`options`]))` type name`;`
- `static GTY(([`options`]))` type name`;`

The syntax

- `GTY(([`options`]))` type name`;`

is _not_ accepted. There should be an `extern` declaration
of such a variable in a header somewhere—mark that, not the
definition. Or, if the variable is only used in one file, make it
`static`.
