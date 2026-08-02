---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Reading-RTL.html
archived_at: '2026-07-15T07:31:02.671475Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Previous: [Sharing](Sharing.md#apple-knugc4tjnztq),
Up: [RTL](RTL.md#apple-kjkey)

---

### 12.21 Reading RTL

To read an RTL object from a file, call `read_rtx`. It takes one
argument, a stdio stream, and returns a single RTL object. This routine
is defined in `read-rtl.c`. It is not available in the compiler
itself, only the various programs that generate the compiler back end
from the machine description.

People frequently have the idea of using RTL stored as text in a file as
an interface between a language front end and the bulk of GCC. This
idea is not feasible.

GCC was designed to use RTL internally only. Correct RTL for a given
program is very dependent on the particular target machine. And the RTL
does not contain all the information about the program.

The proper way to interface GCC to a new language front end is with
the “tree” data structure, described in the files `tree.h` and
`tree.def`. The documentation for this structure (see [Trees](Trees.md#apple-krzgkzlt))
is incomplete.
