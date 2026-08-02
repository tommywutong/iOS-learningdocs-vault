---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Pass-manager.html
archived_at: '2026-07-15T07:31:02.568557Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Tree-SSA passes](Tree_002dSSA-passes.md#apple-krzgkzk7gaydezctknas24dbonzwk4y),
Previous: [Gimplification pass](Gimplification-pass.md#apple-i5uw24dmnftgsy3boruw63rnobqxg4y),
Up: [Passes](Passes.md#apple-kbqxg43fom)

---

### 8.3 Pass manager

The pass manager is located in `passes.c`, `tree-optimize.c`
and `tree-pass.h`.
Its job is to run all of the individual passes in the correct order,
and take care of standard bookkeeping that applies to every pass.

The theory of operation is that each pass defines a structure that
represents everything we need to know about that pass—when it
should be run, how it should be run, what intermediate language
form or on-the-side data structures it needs. We register the pass
to be run in some particular order, and the pass manager arranges
for everything to happen in the correct order.

The actuality doesn't completely live up to the theory at present.
Command-line switches and `timevar_id_t` enumerations must still
be defined elsewhere. The pass manager validates constraints but does
not attempt to (re-)generate data structures or lower intermediate
language form based on the requirements of the next pass. Nevertheless,
what is present is useful, and a far sight better than nothing at all.

TODO: describe the global variables set up by the pass manager,
and a brief description of how a new pass should use it.
I need to look at what info rtl passes use first...
