---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Current-structure-hierarchy.html
archived_at: '2026-07-15T07:31:01.634305Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Adding new DECL node types](Adding-new-DECL-node-types.md#apple-ifsgi2lom4ww4zlxfvcekq2mfvxg6zdffv2hs4dfom),
Up: [Internal structure](Internal-structure.md#apple-jfxhizlsnzqwylltorzhky3uovzgk)

---

##### 9.5.2.1 Current structure hierarchy

**`struct tree_decl_minimal`**
: This is the minimal structure to inherit from in order for common
`DECL` macros to work. The fields it contains are a unique ID,
source location, context, and name.

**`struct tree_decl_common`**
: This structure inherits from `struct tree_decl_minimal`. It
contains fields that most `DECL` nodes need, such as a field to
store alignment, machine mode, size, and attributes.

**`struct tree_field_decl`**
: This structure inherits from `struct tree_decl_common`. It is
used to represent `FIELD_DECL`.

**`struct tree_label_decl`**
: This structure inherits from `struct tree_decl_common`. It is
used to represent `LABEL_DECL`.

**`struct tree_translation_unit_decl`**
: This structure inherits from `struct tree_decl_common`. It is
used to represent `TRANSLATION_UNIT_DECL`.

**`struct tree_decl_with_rtl`**
: This structure inherits from `struct tree_decl_common`. It
contains a field to store the low-level RTL associated with a
`DECL` node.

**`struct tree_result_decl`**
: This structure inherits from `struct tree_decl_with_rtl`. It is
used to represent `RESULT_DECL`.

**`struct tree_const_decl`**
: This structure inherits from `struct tree_decl_with_rtl`. It is
used to represent `CONST_DECL`.

**`struct tree_parm_decl`**
: This structure inherits from `struct tree_decl_with_rtl`. It is
used to represent `PARM_DECL`.

**`struct tree_decl_with_vis`**
: This structure inherits from `struct tree_decl_with_rtl`. It
contains fields necessary to store visibility information, as well as
a section name and assembler name.

**`struct tree_var_decl`**
: This structure inherits from `struct tree_decl_with_vis`. It is
used to represent `VAR_DECL`.

**`struct tree_function_decl`**
: This structure inherits from `struct tree_decl_with_vis`. It is
used to represent `FUNCTION_DECL`.
