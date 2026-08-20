---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Containers.html
archived_at: '2026-07-15T07:30:59.623281Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Previous: [Identifiers](Identifiers.md#apple-jfsgk3tunftgszlsom),
Up: [Tree overview](Tree-overview.md#apple-krzgkzjnn53gk4twnfsxo)

---

#### 8.2.3 Containers

Two common container data structures can be represented directly with
tree nodes. A `TREE_LIST` is a singly linked list containing two
trees per node. These are the `TREE_PURPOSE` and `TREE_VALUE`
of each node. (Often, the `TREE_PURPOSE` contains some kind of
tag, or additional information, while the `TREE_VALUE` contains the
majority of the payload. In other cases, the `TREE_PURPOSE` is
simply `NULL_TREE`, while in still others both the
`TREE_PURPOSE` and `TREE_VALUE` are of equal stature.) Given
one `TREE_LIST` node, the next node is found by following the
`TREE_CHAIN`. If the `TREE_CHAIN` is `NULL_TREE`, then
you have reached the end of the list.

A `TREE_VEC` is a simple vector. The `TREE_VEC_LENGTH` is an
integer (not a tree) giving the number of nodes in the vector. The
nodes themselves are accessed using the `TREE_VEC_ELT` macro, which
takes two arguments. The first is the `TREE_VEC` in question; the
second is an integer indicating which element in the vector is desired.
The elements are indexed from zero.
