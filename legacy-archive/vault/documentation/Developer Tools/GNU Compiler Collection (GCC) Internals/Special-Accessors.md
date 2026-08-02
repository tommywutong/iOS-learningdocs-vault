---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Special-Accessors.html
archived_at: '2026-07-15T07:31:00.756917Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Flags](Flags.md#apple-izwgcz3t),
Previous: [Accessors](Accessors.md#apple-ifrwgzltonxxe4y),
Up: [RTL](RTL.md#apple-kjkey)

---

### 10.4 Access to Special Operands

Some RTL nodes have special annotations associated with them.

**`MEM`**
: 

**`MEM_ALIAS_SET (`x`)`**
: If 0, x is not in any alias set, and may alias anything. Otherwise,
x can only alias `MEM`s in a conflicting alias set. This value
is set in a language-dependent manner in the front-end, and should not be
altered in the back-end. In some front-ends, these numbers may correspond
in some way to types, or other language-level entities, but they need not,
and the back-end makes no such assumptions.
These set numbers are tested with `alias_sets_conflict_p`.

**`MEM_EXPR (`x`)`**
: If this register is known to hold the value of some user-level
declaration, this is that tree node. It may also be a
`COMPONENT_REF`, in which case this is some field reference,
and `TREE_OPERAND (`x`, 0)` contains the declaration,
or another `COMPONENT_REF`, or null if there is no compile-time
object associated with the reference.

**`MEM_OFFSET (`x`)`**
: The offset from the start of `MEM_EXPR` as a `CONST_INT` rtx.

**`MEM_SIZE (`x`)`**
: The size in bytes of the memory reference as a `CONST_INT` rtx.
This is mostly relevant for `BLKmode` references as otherwise
the size is implied by the mode.

**`MEM_ALIGN (`x`)`**
: The known alignment in bits of the memory reference.

**`REG`**
: 

**`ORIGINAL_REGNO (`x`)`**
: This field holds the number the register “originally” had; for a
pseudo register turned into a hard reg this will hold the old pseudo
register number.

**`REG_EXPR (`x`)`**
: If this register is known to hold the value of some user-level
declaration, this is that tree node.

**`REG_OFFSET (`x`)`**
: If this register is known to hold the value of some user-level
declaration, this is the offset into that logical storage.

**`SYMBOL_REF`**
: 

**`SYMBOL_REF_DECL (`x`)`**
: If the `symbol_ref` x was created for a `VAR_DECL` or
a `FUNCTION_DECL`, that tree is recorded here. If this value is
null, then x was created by back end code generation routines,
and there is no associated front end symbol table entry.

`SYMBOL_REF_DECL` may also point to a tree of class `'c'`,
that is, some sort of constant. In this case, the `symbol_ref`
is an entry in the per-file constant pool; again, there is no associated
front end symbol table entry.

**`SYMBOL_REF_FLAGS (`x`)`**
: In a `symbol_ref`, this is used to communicate various predicates
about the symbol. Some of these are common enough to be computed by
common code, some are specific to the target. The common bits are:

**`SYMBOL_FLAG_FUNCTION`**
: Set if the symbol refers to a function.

**`SYMBOL_FLAG_LOCAL`**
: Set if the symbol is local to this “module”.
See `TARGET_BINDS_LOCAL_P`.

**`SYMBOL_FLAG_EXTERNAL`**
: Set if this symbol is not defined in this translation unit.
Note that this is not the inverse of `SYMBOL_FLAG_LOCAL`.

**`SYMBOL_FLAG_SMALL`**
: Set if the symbol is located in the small data section.
See `TARGET_IN_SMALL_DATA_P`.

**`SYMBOL_REF_TLS_MODEL (`x`)`**
: This is a multi-bit field accessor that returns the `tls_model`
to be used for a thread-local storage symbol. It returns zero for
non-thread-local symbols.

Bits beginning with `SYMBOL_FLAG_MACH_DEP` are available for
the target's use.
