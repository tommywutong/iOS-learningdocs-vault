---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Namespaces.html
archived_at: '2026-07-15T07:31:00.431407Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Classes](Classes.md#apple-inwgc43tmvzq),
Up: [Scopes](Scopes.md#apple-knrw64dfom)

---

#### 8.4.1 Namespaces

A namespace is represented by a `NAMESPACE_DECL` node.

However, except for the fact that it is distinguished as the root of the
representation, the global namespace is no different from any other
namespace. Thus, in what follows, we describe namespaces generally,
rather than the global namespace in particular.

The following macros and functions can be used on a `NAMESPACE_DECL`:

**`DECL_NAME`**
: This macro is used to obtain the `IDENTIFIER_NODE` corresponding to
the unqualified name of the name of the namespace (see [Identifiers](Identifiers.md#apple-jfsgk3tunftgszlsom)).
The name of the global namespace is ``::`', even though in C++ the
global namespace is unnamed. However, you should use comparison with
`global_namespace`, rather than `DECL_NAME` to determine
whether or not a namespace is the global one. An unnamed namespace
will have a `DECL_NAME` equal to `anonymous_namespace_name`.
Within a single translation unit, all unnamed namespaces will have the
same name.

**`DECL_CONTEXT`**
: This macro returns the enclosing namespace. The `DECL_CONTEXT` for
the `global_namespace` is `NULL_TREE`.

**`DECL_NAMESPACE_ALIAS`**
: If this declaration is for a namespace alias, then
`DECL_NAMESPACE_ALIAS` is the namespace for which this one is an
alias.

Do not attempt to use `cp_namespace_decls` for a namespace which is
an alias. Instead, follow `DECL_NAMESPACE_ALIAS` links until you
reach an ordinary, non-alias, namespace, and call
`cp_namespace_decls` there.

**`DECL_NAMESPACE_STD_P`**
: This predicate holds if the namespace is the special `::std`
namespace.

**`cp_namespace_decls`**
: This function will return the declarations contained in the namespace,
including types, overloaded functions, other namespaces, and so forth.
If there are no declarations, this function will return
`NULL_TREE`. The declarations are connected through their
`TREE_CHAIN` fields.

Although most entries on this list will be declarations,
`TREE_LIST` nodes may also appear. In this case, the
`TREE_VALUE` will be an `OVERLOAD`. The value of the
`TREE_PURPOSE` is unspecified; back ends should ignore this value.
As with the other kinds of declarations returned by
`cp_namespace_decls`, the `TREE_CHAIN` will point to the next
declaration in this list.

For more information on the kinds of declarations that can occur on this
list, See [Declarations](Declarations.md#apple-irswg3dbojqxi2lpnzzq). Some declarations will not appear on this
list. In particular, no `FIELD_DECL`, `LABEL_DECL`, or
`PARM_DECL` nodes will appear here.

This function cannot be used with namespaces that have
`DECL_NAMESPACE_ALIAS` set.
