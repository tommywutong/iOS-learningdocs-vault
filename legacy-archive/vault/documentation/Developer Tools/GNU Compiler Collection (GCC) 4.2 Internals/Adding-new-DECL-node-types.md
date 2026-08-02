---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Adding-new-DECL-node-types.html
archived_at: '2026-07-15T07:31:01.147582Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Previous: [Current structure hierarchy](Current-structure-hierarchy.md#apple-in2xe4tfnz2c243uoj2wg5dvojss22djmvzgc4tdnb4q),
Up: [Internal structure](Internal-structure.md#apple-jfxhizlsnzqwylltorzhky3uovzgk)

---

##### 9.5.2.2 Adding new DECL node types

Adding a new `DECL` tree consists of the following steps

**Add a new tree code for the `DECL` node**
: For language specific `DECL` nodes, there is a `.def` file
in each frontend directory where the tree code should be added.
For `DECL` nodes that are part of the middle-end, the code should
be added to `tree.def`.

**Create a new structure type for the `DECL` node**
: These structures should inherit from one of the existing structures in
the language hierarchy by using that structure as the first member.

```
          struct tree_foo_decl
          {
             struct tree_decl_with_vis common;
          }

```

Would create a structure name `tree_foo_decl` that inherits from
`struct tree_decl_with_vis`.

For language specific `DECL` nodes, this new structure type
should go in the appropriate `.h` file.
For `DECL` nodes that are part of the middle-end, the structure
type should go in `tree.h`.

**Add a member to the tree structure enumerator for the node**
: For garbage collection and dynamic checking purposes, each `DECL`
node structure type is required to have a unique enumerator value
specified with it.
For language specific `DECL` nodes, this new enumerator value
should go in the appropriate `.def` file.
For `DECL` nodes that are part of the middle-end, the enumerator
values are specified in `treestruct.def`.

**Update `union tree_node`**
: In order to make your new structure type usable, it must be added to
`union tree_node`.
For language specific `DECL` nodes, a new entry should be added
to the appropriate `.h` file of the form

```
            struct tree_foo_decl GTY ((tag ("TS_VAR_DECL"))) foo_decl;

```

For `DECL` nodes that are part of the middle-end, the additional
member goes directly into `union tree_node` in `tree.h`.

**Update dynamic checking info**
: In order to be able to check whether accessing a named portion of
`union tree_node` is legal, and whether a certain `DECL` node
contains one of the enumerated `DECL` node structures in the
hierarchy, a simple lookup table is used.
This lookup table needs to be kept up to date with the tree structure
hierarchy, or else checking and containment macros will fail
inappropriately.

For language specific `DECL` nodes, their is an `init_ts`
function in an appropriate `.c` file, which initializes the lookup
table.
Code setting up the table for new `DECL` nodes should be added
there.
For each `DECL` tree code and enumerator value representing a
member of the inheritance hierarchy, the table should contain 1 if
that tree code inherits (directly or indirectly) from that member.
Thus, a `FOO_DECL` node derived from `struct decl_with_rtl`,
and enumerator value `TS_FOO_DECL`, would be set up as follows

```
          tree_contains_struct[FOO_DECL][TS_FOO_DECL] = 1;
          tree_contains_struct[FOO_DECL][TS_DECL_WRTL] = 1;
          tree_contains_struct[FOO_DECL][TS_DECL_COMMON] = 1;
          tree_contains_struct[FOO_DECL][TS_DECL_MINIMAL] = 1;

```

For `DECL` nodes that are part of the middle-end, the setup code
goes into `tree.c`.

**Add macros to access any new fields and flags**
: Each added field or flag should have a macro that is used to access
it, that performs appropriate checking to ensure only the right type of
`DECL` nodes access the field.

These macros generally take the following form

```swift
          #define FOO_DECL_FIELDNAME(NODE) FOO_DECL_CHECK(NODE)->foo_decl.fieldname

```

However, if the structure is simply a base class for further
structures, something like the following should be used

```swift
          #define BASE_STRUCT_CHECK(T) CONTAINS_STRUCT_CHECK(T, TS_BASE_STRUCT)
          #define BASE_STRUCT_FIELDNAME(NODE) \
             (BASE_STRUCT_CHECK(NODE)->base_struct.fieldname

```
