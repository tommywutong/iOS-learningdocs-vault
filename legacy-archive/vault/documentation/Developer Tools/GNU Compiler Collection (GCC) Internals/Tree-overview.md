---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Tree-overview.html
archived_at: '2026-07-15T07:31:00.938978Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Types](Types.md#apple-kr4xazlt),
Previous: [Deficiencies](Deficiencies.md#apple-irswm2ldnfsw4y3jmvzq),
Up: [Trees](Trees.md#apple-krzgkzlt)

---

### 8.2 Overview

The central data structure used by the internal representation is the
`tree`. These nodes, while all of the C type `tree`, are of
many varieties. A `tree` is a pointer type, but the object to
which it points may be of a variety of types. From this point forward,
we will refer to trees in ordinary type, rather than in `this
font`, except when talking about the actual C type `tree`.

You can tell what kind of node a particular tree is by using the
`TREE_CODE` macro. Many, many macros take trees as input and
return trees as output. However, most macros require a certain kind of
tree node as input. In other words, there is a type-system for trees,
but it is not reflected in the C type-system.

For safety, it is useful to configure GCC with `--enable-checking`.
Although this results in a significant performance penalty (since all
tree types are checked at run-time), and is therefore inappropriate in a
release version, it is extremely helpful during the development process.

Many macros behave as predicates. Many, although not all, of these
predicates end in ``_P`'. Do not rely on the result type of these
macros being of any particular type. You may, however, rely on the fact
that the type can be compared to `0`, so that statements like

```
     if (TEST_P (t) && !TEST_P (y))
       x = 1;
```

and

```
     int i = (TEST_P (t) != 0);
```

are legal. Macros that return `int` values now may be changed to
return `tree` values, or other pointers in the future. Even those
that continue to return `int` may return multiple nonzero codes
where previously they returned only zero and one. Therefore, you should
not write code like

```
     if (TEST_P (t) == 1)
```

as this code is not guaranteed to work correctly in the future.

You should not take the address of values returned by the macros or
functions described here. In particular, no guarantee is given that the
values are lvalues.

In general, the names of macros are all in uppercase, while the names of
functions are entirely in lowercase. There are rare exceptions to this
rule. You should assume that any macro or function whose name is made
up entirely of uppercase letters may evaluate its arguments more than
once. You may assume that a macro or function whose name is made up
entirely of lowercase letters will evaluate its arguments only once.

The `error_mark_node` is a special tree. Its tree code is
`ERROR_MARK`, but since there is only ever one node with that code,
the usual practice is to compare the tree against
`error_mark_node`. (This test is just a test for pointer
equality.) If an error has occurred during front-end processing the
flag `errorcount` will be set. If the front end has encountered
code it cannot handle, it will issue a message to the user and set
`sorrycount`. When these flags are set, any macro or function
which normally returns a tree of a particular kind may instead return
the `error_mark_node`. Thus, if you intend to do any processing of
erroneous code, you must be prepared to deal with the
`error_mark_node`.

Occasionally, a particular tree slot (like an operand to an expression,
or a particular field in a declaration) will be referred to as
“reserved for the back end”. These slots are used to store RTL when
the tree is converted to RTL for use by the GCC back end. However, if
that process is not taking place (e.g., if the front end is being hooked
up to an intelligent editor), then those slots may be used by the
back end presently in use.

If you encounter situations that do not match this documentation, such
as tree nodes of types not mentioned here, or macros documented to
return entities of a particular kind that instead return entities of
some different kind, you have found a bug, either in the front end or in
the documentation. Please report these bugs as you would any other
bug.

- [Macros and Functions](Macros-and-Functions.md#apple-jvqwg4tpomwwc3tefvdhk3tdoruw63tt): Macros and functions that can be used with all trees.
- [Identifiers](Identifiers.md#apple-jfsgk3tunftgszlsom): The names of things.
- [Containers](Containers.md#apple-inxw45dbnfxgk4tt): Lists and vectors.
