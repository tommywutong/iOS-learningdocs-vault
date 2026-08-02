---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Identifiers.html
archived_at: '2026-07-15T07:31:00.050480Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Containers](Containers.md#apple-inxw45dbnfxgk4tt),
Previous: [Macros and Functions](Macros-and-Functions.md#apple-jvqwg4tpomwwc3tefvdhk3tdoruw63tt),
Up: [Tree overview](Tree-overview.md#apple-krzgkzjnn53gk4twnfsxo)

---

#### 8.2.2 Identifiers

An `IDENTIFIER_NODE` represents a slightly more general concept
that the standard C or C++ concept of identifier. In particular, an
`IDENTIFIER_NODE` may contain a ``$`', or other extraordinary
characters.

There are never two distinct `IDENTIFIER_NODE`s representing the
same identifier. Therefore, you may use pointer equality to compare
`IDENTIFIER_NODE`s, rather than using a routine like `strcmp`.

You can use the following macros to access identifiers:

**`IDENTIFIER_POINTER`**
: The string represented by the identifier, represented as a
`char*`. This string is always `NUL`-terminated, and contains
no embedded `NUL` characters.

**`IDENTIFIER_LENGTH`**
: The length of the string returned by `IDENTIFIER_POINTER`, not
including the trailing `NUL`. This value of
`IDENTIFIER_LENGTH (x)` is always the same as `strlen
(IDENTIFIER_POINTER (x))`.

**`IDENTIFIER_OPNAME_P`**
: This predicate holds if the identifier represents the name of an
overloaded operator. In this case, you should not depend on the
contents of either the `IDENTIFIER_POINTER` or the
`IDENTIFIER_LENGTH`.

**`IDENTIFIER_TYPENAME_P`**
: This predicate holds if the identifier represents the name of a
user-defined conversion operator. In this case, the `TREE_TYPE` of
the `IDENTIFIER_NODE` holds the type to which the conversion
operator converts.
