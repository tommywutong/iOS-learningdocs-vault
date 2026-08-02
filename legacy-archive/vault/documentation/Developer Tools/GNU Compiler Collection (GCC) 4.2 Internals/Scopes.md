---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Scopes.html
archived_at: '2026-07-15T07:31:02.764190Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Functions](Functions.md#apple-iz2w4y3unfxw44y),
Previous: [Types](Types.md#apple-kr4xazlt),
Up: [Trees](Trees.md#apple-krzgkzlt)

---

### 9.4 Scopes

The root of the entire intermediate representation is the variable
`global_namespace`. This is the namespace specified with `::`
in C++ source code. All other namespaces, types, variables, functions,
and so forth can be found starting with this namespace.

Besides namespaces, the other high-level scoping construct in C++ is the
class. (Throughout this manual the term class is used to mean the
types referred to in the ANSI/ISO C++ Standard as classes; these include
types defined with the `class`, `struct`, and `union`
keywords.)

- [Namespaces](Namespaces.md#apple-jzqw2zltobqwgzlt): Member functions, types, etc.
- [Classes](Classes.md#apple-inwgc43tmvzq): Members, bases, friends, etc.
