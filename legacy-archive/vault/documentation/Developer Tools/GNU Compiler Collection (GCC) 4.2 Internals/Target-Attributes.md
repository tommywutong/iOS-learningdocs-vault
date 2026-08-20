---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Target-Attributes.html
archived_at: '2026-07-15T07:31:02.948905Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [MIPS Coprocessors](MIPS-Coprocessors.md#apple-jvevauzninxxa4tpmnsxg43pojzq),
Previous: [Mode Switching](Mode-Switching.md#apple-jvxwizjnkn3ws5ddnbuw4zy),
Up: [Target Macros](Target-Macros.md#apple-krqxez3foqwu2yldojxxg)

---

### 15.25 Defining target-specific uses of `__attribute__`

Target-specific attributes may be defined for functions, data and types.
These are described using the following target hooks; they also need to
be documented in `extend.texi`.

— Target Hook: const struct attribute_spec \* __TARGET_ATTRIBUTE_TABLE__
> If defined, this target hook points to an array of ``struct
> attribute_spec`' (defined in `tree.h`) specifying the machine
> specific attributes for this target and some of the restrictions on the
> entities to which these attributes are applied and the arguments they
> take.

— Target Hook: int __TARGET_COMP_TYPE_ATTRIBUTES__ (tree type1, tree type2)
> If defined, this target hook is a function which returns zero if the attributes on
> type1 and type2 are incompatible, one if they are compatible,
> and two if they are nearly compatible (which causes a warning to be
> generated). If this is not defined, machine-specific attributes are
> supposed always to be compatible.

— Target Hook: void __TARGET_SET_DEFAULT_TYPE_ATTRIBUTES__ (tree type)
> If defined, this target hook is a function which assigns default attributes to
> newly defined type.

— Target Hook: tree __TARGET_MERGE_TYPE_ATTRIBUTES__ (tree type1, tree type2)
> Define this target hook if the merging of type attributes needs special
> handling. If defined, the result is a list of the combined
> `TYPE_ATTRIBUTES` of type1 and type2. It is assumed
> that `comptypes` has already been called and returned 1. This
> function may call `merge_attributes` to handle machine-independent
> merging.

— Target Hook: tree __TARGET_MERGE_DECL_ATTRIBUTES__ (tree olddecl, tree newdecl)
> Define this target hook if the merging of decl attributes needs special
> handling. If defined, the result is a list of the combined
> `DECL_ATTRIBUTES` of olddecl and newdecl.
> newdecl is a duplicate declaration of olddecl. Examples of
> when this is needed are when one attribute overrides another, or when an
> attribute is nullified by a subsequent definition. This function may
> call `merge_attributes` to handle machine-independent merging.
>
> If the only target-specific handling you require is ``dllimport`'
> for Microsoft Windows targets, you should define the macro
> `TARGET_DLLIMPORT_DECL_ATTRIBUTES` to `1`. The compiler
> will then define a function called
> `merge_dllimport_decl_attributes` which can then be defined as
> the expansion of `TARGET_MERGE_DECL_ATTRIBUTES`. You can also
> add `handle_dll_attribute` in the attribute table for your port
> to perform initial processing of the ``dllimport`' and
> ``dllexport`' attributes. This is done in `i386/cygwin.h` and
> `i386/i386.c`, for example.

— Target Hook: bool __TARGET_VALID_DLLIMPORT_ATTRIBUTE_P__ (tree decl)
> decl is a variable or function with `__attribute__((dllimport))`
> specified. Use this hook if the target needs to add extra validation
> checks to `handle_dll_attribute`.

— Macro: __TARGET_DECLSPEC__
> Define this macro to a nonzero value if you want to treat
> `__declspec(X)` as equivalent to `__attribute((X))`. By
> default, this behavior is enabled only for targets that define
> `TARGET_DLLIMPORT_DECL_ATTRIBUTES`. The current implementation
> of `__declspec` is via a built-in macro, but you should not rely
> on this implementation detail.

— Target Hook: void __TARGET_INSERT_ATTRIBUTES__ (tree node, tree \*attr_ptr)
> Define this target hook if you want to be able to add attributes to a decl
> when it is being created. This is normally useful for back ends which
> wish to implement a pragma by using the attributes which correspond to
> the pragma's effect. The node argument is the decl which is being
> created. The attr_ptr argument is a pointer to the attribute list
> for this decl. The list itself should not be modified, since it may be
> shared with other decls, but attributes may be chained on the head of
> the list and `*`attr_ptr modified to point to the new
> attributes, or a copy of the list may be made if further changes are
> needed.

— Target Hook: bool __TARGET_FUNCTION_ATTRIBUTE_INLINABLE_P__ (tree fndecl)
> This target hook returns `true` if it is ok to inline fndecl
> into the current function, despite its having target-specific
> attributes, `false` otherwise. By default, if a function has a
> target specific attribute attached to it, it will not be inlined.
