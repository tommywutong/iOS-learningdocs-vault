---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/GENERIC.html
archived_at: '2026-07-15T07:31:01.965069Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [GIMPLE](GIMPLE.md#apple-i5eu2ucmiu),
Up: [Tree SSA](Tree-SSA.md#apple-krzgkzjnknjuc)

---

### 10.1 GENERIC

The purpose of GENERIC is simply to provide a language-independent way of
representing an entire function in trees. To this end, it was necessary to
add a few new tree codes to the back end, but most everything was already
there. If you can express it with the codes in `gcc/tree.def`, it's
GENERIC.

Early on, there was a great deal of debate about how to think about
statements in a tree IL. In GENERIC, a statement is defined as any
expression whose value, if any, is ignored. A statement will always
have `TREE_SIDE_EFFECTS` set (or it will be discarded), but a
non-statement expression may also have side effects. A
`CALL_EXPR`, for instance.

It would be possible for some local optimizations to work on the
GENERIC form of a function; indeed, the adapted tree inliner works
fine on GENERIC, but the current compiler performs inlining after
lowering to GIMPLE (a restricted form described in the next section).
Indeed, currently the frontends perform this lowering before handing
off to `tree_rest_of_compilation`, but this seems inelegant.

If necessary, a front end can use some language-dependent tree codes
in its GENERIC representation, so long as it provides a hook for
converting them to GIMPLE and doesn't expect them to work with any
(hypothetical) optimizers that run before the conversion to GIMPLE.
The intermediate representation used while parsing C and C++ looks
very little like GENERIC, but the C and C++ gimplifier hooks are
perfectly happy to take it as input and spit out GIMPLE.
