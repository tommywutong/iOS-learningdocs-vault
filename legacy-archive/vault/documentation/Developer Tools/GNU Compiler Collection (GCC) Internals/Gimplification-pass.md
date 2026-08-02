---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Gimplification-pass.html
archived_at: '2026-07-15T07:31:00.013140Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Pass manager](Pass-manager.md#apple-kbqxg4znnvqw4ylhmvza),
Previous: [Parsing pass](Parsing-pass.md#apple-kbqxe43jnzts24dbonzq),
Up: [Passes](Passes.md#apple-kbqxg43fom)

---

### 7.2 Gimplification pass

Gimplification is a whimsical term for the process of converting
the intermediate representation of a function into the GIMPLE language
(CROSSREF). The term stuck, and so words like “gimplification”,
“gimplify”, “gimplifier” and the like are sprinkled throughout this
section of code.

While a front end may certainly choose to generate GIMPLE directly if
it chooses, this can be a moderately complex process unless the
intermediate language used by the front end is already fairly simple.
Usually it is easier to generate GENERIC trees plus extensions
and let the language-independent gimplifier do most of the work.

The main entry point to this pass is `gimplify_function_tree`
located in `gimplify.c`. From here we process the entire
function gimplifying each statement in turn. The main workhorse
for this pass is `gimplify_expr`. Approximately everything
passes through here at least once, and it is from here that we
invoke the `lang_hooks.gimplify_expr` callback.

The callback should examine the expression in question and return
`GS_UNHANDLED` if the expression is not a language specific
construct that requires attention. Otherwise it should alter the
expression in some way to such that forward progress is made toward
producing valid GIMPLE. If the callback is certain that the
transformation is complete and the expression is valid GIMPLE, it
should return `GS_ALL_DONE`. Otherwise it should return
`GS_OK`, which will cause the expression to be processed again.
If the callback encounters an error during the transformation (because
the front end is relying on the gimplification process to finish
semantic checks), it should return `GS_ERROR`.
