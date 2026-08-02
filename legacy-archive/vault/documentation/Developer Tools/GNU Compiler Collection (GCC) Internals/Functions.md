---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Functions.html
archived_at: '2026-07-15T07:30:59.957369Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Declarations](Declarations.md#apple-irswg3dbojqxi2lpnzzq),
Previous: [Scopes](Scopes.md#apple-knrw64dfom),
Up: [Trees](Trees.md#apple-krzgkzlt)

---

### 8.6 Functions

A function is represented by a `FUNCTION_DECL` node. A set of
overloaded functions is sometimes represented by a `OVERLOAD` node.

An `OVERLOAD` node is not a declaration, so none of the
``DECL_`' macros should be used on an `OVERLOAD`. An
`OVERLOAD` node is similar to a `TREE_LIST`. Use
`OVL_CURRENT` to get the function associated with an
`OVERLOAD` node; use `OVL_NEXT` to get the next
`OVERLOAD` node in the list of overloaded functions. The macros
`OVL_CURRENT` and `OVL_NEXT` are actually polymorphic; you can
use them to work with `FUNCTION_DECL` nodes as well as with
overloads. In the case of a `FUNCTION_DECL`, `OVL_CURRENT`
will always return the function itself, and `OVL_NEXT` will always
be `NULL_TREE`.

To determine the scope of a function, you can use the
`DECL_CONTEXT` macro. This macro will return the class
(either a `RECORD_TYPE` or a `UNION_TYPE`) or namespace (a
`NAMESPACE_DECL`) of which the function is a member. For a virtual
function, this macro returns the class in which the function was
actually defined, not the base class in which the virtual declaration
occurred.

If a friend function is defined in a class scope, the
`DECL_FRIEND_CONTEXT` macro can be used to determine the class in
which it was defined. For example, in

```
     class C { friend void f() {} };
```

the `DECL_CONTEXT` for `f` will be the
`global_namespace`, but the `DECL_FRIEND_CONTEXT` will be the
`RECORD_TYPE` for `C`.

In C, the `DECL_CONTEXT` for a function maybe another function.
This representation indicates that the GNU nested function extension
is in use. For details on the semantics of nested functions, see the
GCC Manual. The nested function can refer to local variables in its
containing function. Such references are not explicitly marked in the
tree structure; back ends must look at the `DECL_CONTEXT` for the
referenced `VAR_DECL`. If the `DECL_CONTEXT` for the
referenced `VAR_DECL` is not the same as the function currently
being processed, and neither `DECL_EXTERNAL` nor
`DECL_STATIC` hold, then the reference is to a local variable in
a containing function, and the back end must take appropriate action.

- [Function Basics](Function-Basics.md#apple-iz2w4y3unfxw4lkcmfzwsy3t): Function names, linkage, and so forth.
- [Function Bodies](Function-Bodies.md#apple-iz2w4y3unfxw4lkcn5sgszlt): The statements that make up a function body.
