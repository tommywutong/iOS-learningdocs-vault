---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Trees.html
archived_at: '2026-07-15T07:31:03.039885Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [RTL](RTL.md#apple-kjkey),
Previous: [Passes](Passes.md#apple-kbqxg43fom),
Up: [Top](index.md#apple-krxxa)

---

## 9 Trees: The intermediate representation used by the C and C++ front ends

This chapter documents the internal representation used by GCC to
represent C and C++ source programs. When presented with a C or C++
source program, GCC parses the program, performs semantic analysis
(including the generation of error messages), and then produces the
internal representation described here. This representation contains a
complete representation for the entire translation unit provided as
input to the front end. This representation is then typically processed
by a code-generator in order to produce machine code, but could also be
used in the creation of source browsers, intelligent editors, automatic
documentation generators, interpreters, and any other programs needing
the ability to process C or C++ code.

This chapter explains the internal representation. In particular, it
documents the internal representation for C and C++ source
constructs, and the macros, functions, and variables that can be used to
access these constructs. The C++ representation is largely a superset
of the representation used in the C front end. There is only one
construct used in C that does not appear in the C++ front end and that
is the GNU “nested function” extension. Many of the macros documented
here do not apply in C because the corresponding language constructs do
not appear in C.

If you are developing a “back end”, be it is a code-generator or some
other tool, that uses this representation, you may occasionally find
that you need to ask questions not easily answered by the functions and
macros available here. If that situation occurs, it is quite likely
that GCC already supports the functionality you desire, but that the
interface is simply not documented here. In that case, you should ask
the GCC maintainers (via mail to [gcc@gcc.gnu.org](mailto:gcc@gcc.gnu.org)) about
documenting the functionality you require. Similarly, if you find
yourself writing functions that do not deal directly with your back end,
but instead might be useful to other people using the GCC front end, you
should submit your patches for inclusion in GCC.

- [Deficiencies](Deficiencies.md#apple-irswm2ldnfsw4y3jmvzq): Topics net yet covered in this document.
- [Tree overview](Tree-overview.md#apple-krzgkzjnn53gk4twnfsxo): All about `tree`s.
- [Types](Types.md#apple-kr4xazlt): Fundamental and aggregate types.
- [Scopes](Scopes.md#apple-knrw64dfom): Namespaces and classes.
- [Functions](Functions.md#apple-iz2w4y3unfxw44y): Overloading, function bodies, and linkage.
- [Declarations](Declarations.md#apple-irswg3dbojqxi2lpnzzq): Type declarations and variables.
- [Attributes](Attributes.md#apple-if2hi4tjmj2xizlt): Declaration and type attributes.
- [Expression trees](Expression-trees.md#apple-iv4ha4tfonzws33ofv2hezlfom): From `typeid` to `throw`.
