---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Classes.html
archived_at: '2026-07-15T07:30:59.362700Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Previous: [Namespaces](Namespaces.md#apple-jzqw2zltobqwgzlt),
Up: [Scopes](Scopes.md#apple-knrw64dfom)

---

#### 8.4.2 Classes

A class type is represented by either a `RECORD_TYPE` or a
`UNION_TYPE`. A class declared with the `union` tag is
represented by a `UNION_TYPE`, while classes declared with either
the `struct` or the `class` tag are represented by
`RECORD_TYPE`s. You can use the `CLASSTYPE_DECLARED_CLASS`
macro to discern whether or not a particular type is a `class` as
opposed to a `struct`. This macro will be true only for classes
declared with the `class` tag.

Almost all non-function members are available on the `TYPE_FIELDS`
list. Given one member, the next can be found by following the
`TREE_CHAIN`. You should not depend in any way on the order in
which fields appear on this list. All nodes on this list will be
``DECL`' nodes. A `FIELD_DECL` is used to represent a non-static
data member, a `VAR_DECL` is used to represent a static data
member, and a `TYPE_DECL` is used to represent a type. Note that
the `CONST_DECL` for an enumeration constant will appear on this
list, if the enumeration type was declared in the class. (Of course,
the `TYPE_DECL` for the enumeration type will appear here as well.)
There are no entries for base classes on this list. In particular,
there is no `FIELD_DECL` for the “base-class portion” of an
object.

The `TYPE_VFIELD` is a compiler-generated field used to point to
virtual function tables. It may or may not appear on the
`TYPE_FIELDS` list. However, back ends should handle the
`TYPE_VFIELD` just like all the entries on the `TYPE_FIELDS`
list.

The function members are available on the `TYPE_METHODS` list.
Again, subsequent members are found by following the `TREE_CHAIN`
field. If a function is overloaded, each of the overloaded functions
appears; no `OVERLOAD` nodes appear on the `TYPE_METHODS`
list. Implicitly declared functions (including default constructors,
copy constructors, assignment operators, and destructors) will appear on
this list as well.

Every class has an associated binfo, which can be obtained with
`TYPE_BINFO`. Binfos are used to represent base-classes. The
binfo given by `TYPE_BINFO` is the degenerate case, whereby every
class is considered to be its own base-class. The base binfos for a
particular binfo are held in a vector, whose length is obtained with
`BINFO_N_BASE_BINFOS`. The base binfos themselves are obtained
with `BINFO_BASE_BINFO` and `BINFO_BASE_ITERATE`. To add a
new binfo, use `BINFO_BASE_APPEND`. The vector of base binfos can
be obtained with `BINFO_BASE_BINFOS`, but normally you do not need
to use that. The class type associated with a binfo is given by
`BINFO_TYPE`. It is not always the case that `BINFO_TYPE
(TYPE_BINFO (x))`, because of typedefs and qualified types. Neither is
it the case that `TYPE_BINFO (BINFO_TYPE (y))` is the same binfo as
`y`. The reason is that if `y` is a binfo representing a
base-class `B` of a derived class `D`, then `BINFO_TYPE
(y)` will be `B`, and `TYPE_BINFO (BINFO_TYPE (y))` will be
`B` as its own base-class, rather than as a base-class of `D`.

The access to a base type can be found with `BINFO_BASE_ACCESS`.
This will produce `access_public_node`, `access_private_node`
or `access_protected_node`. If bases are always public,
`BINFO_BASE_ACCESSES` may be `NULL`.

`BINFO_VIRTUAL_P` is used to specify whether the binfo is inherited
virtually or not. The other flags, `BINFO_MARKED_P` and
`BINFO_FLAG_1` to `BINFO_FLAG_6` can be used for language
specific use.

The following macros can be used on a tree node representing a class-type.

**`LOCAL_CLASS_P`**
: This predicate holds if the class is local class _i.e._ declared
inside a function body.

**`TYPE_POLYMORPHIC_P`**
: This predicate holds if the class has at least one virtual function
(declared or inherited).

**`TYPE_HAS_DEFAULT_CONSTRUCTOR`**
: This predicate holds whenever its argument represents a class-type with
default constructor.

**`CLASSTYPE_HAS_MUTABLE`

**`TYPE_HAS_MUTABLE_P`****
: These predicates hold for a class-type having a mutable data member.

**`CLASSTYPE_NON_POD_P`**
: This predicate holds only for class-types that are not PODs.

**`TYPE_HAS_NEW_OPERATOR`**
: This predicate holds for a class-type that defines
`operator new`.

**`TYPE_HAS_ARRAY_NEW_OPERATOR`**
: This predicate holds for a class-type for which
`operator new[]` is defined.

**`TYPE_OVERLOADS_CALL_EXPR`**
: This predicate holds for class-type for which the function call
`operator()` is overloaded.

**`TYPE_OVERLOADS_ARRAY_REF`**
: This predicate holds for a class-type that overloads
`operator[]`

**`TYPE_OVERLOADS_ARROW`**
: This predicate holds for a class-type for which `operator->` is
overloaded.
