---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Attributes.html
archived_at: '2026-07-15T07:31:01.235311Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Expression trees](Expression-trees.md#apple-iv4ha4tfonzws33ofv2hezlfom),
Previous: [Declarations](Declarations.md#apple-irswg3dbojqxi2lpnzzq),
Up: [Trees](Trees.md#apple-krzgkzlt)

---

### 9.7 Attributes in trees

Attributes, as specified using the `__attribute__` keyword, are
represented internally as a `TREE_LIST`. The `TREE_PURPOSE`
is the name of the attribute, as an `IDENTIFIER_NODE`. The
`TREE_VALUE` is a `TREE_LIST` of the arguments of the
attribute, if any, or `NULL_TREE` if there are no arguments; the
arguments are stored as the `TREE_VALUE` of successive entries in
the list, and may be identifiers or expressions. The `TREE_CHAIN`
of the attribute is the next attribute in a list of attributes applying
to the same declaration or type, or `NULL_TREE` if there are no
further attributes in the list.

Attributes may be attached to declarations and to types; these
attributes may be accessed with the following macros. All attributes
are stored in this way, and many also cause other changes to the
declaration or type or to other internal compiler data structures.

— Tree Macro: tree __DECL_ATTRIBUTES__ (tree decl)
> This macro returns the attributes on the declaration decl.

— Tree Macro: tree __TYPE_ATTRIBUTES__ (tree type)
> This macro returns the attributes on the type type.
