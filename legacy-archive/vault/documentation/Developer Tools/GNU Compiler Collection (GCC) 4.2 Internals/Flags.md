---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Flags.html
archived_at: '2026-07-15T07:31:01.870755Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Machine Modes](Machine-Modes.md#apple-jvqwg2djnzss2tlpmrsxg),
Previous: [Special Accessors](Special-Accessors.md#apple-knygky3jmfwc2qldmnsxg43pojzq),
Up: [RTL](RTL.md#apple-kjkey)

---

### 12.5 Flags in an RTL Expression

RTL expressions contain several flags (one-bit bit-fields)
that are used in certain types of expression. Most often they
are accessed with the following macros, which expand into lvalues.

**`CONSTANT_POOL_ADDRESS_P (`x`)`**
: Nonzero in a `symbol_ref` if it refers to part of the current
function's constant pool. For most targets these addresses are in a
`.rodata` section entirely separate from the function, but for
some targets the addresses are close to the beginning of the function.
In either case GCC assumes these addresses can be addressed directly,
perhaps with the help of base registers.
Stored in the `unchanging` field and printed as ``/u`'.

**`CONST_OR_PURE_CALL_P (`x`)`**
: In a `call_insn`, `note`, or an `expr_list` for notes,
indicates that the insn represents a call to a const or pure function.
Stored in the `unchanging` field and printed as ``/u`'.

**`INSN_ANNULLED_BRANCH_P (`x`)`**
: In a `jump_insn`, `call_insn`, or `insn` indicates
that the branch is an annulling one. See the discussion under
`sequence` below. Stored in the `unchanging` field and
printed as ``/u`'.

**`INSN_DELETED_P (`x`)`**
: In an `insn`, `call_insn`, `jump_insn`, `code_label`,
`barrier`, or `note`,
nonzero if the insn has been deleted. Stored in the
`volatil` field and printed as ``/v`'.

**`INSN_FROM_TARGET_P (`x`)`**
: In an `insn` or `jump_insn` or `call_insn` in a delay
slot of a branch, indicates that the insn
is from the target of the branch. If the branch insn has
`INSN_ANNULLED_BRANCH_P` set, this insn will only be executed if
the branch is taken. For annulled branches with
`INSN_FROM_TARGET_P` clear, the insn will be executed only if the
branch is not taken. When `INSN_ANNULLED_BRANCH_P` is not set,
this insn will always be executed. Stored in the `in_struct`
field and printed as ``/s`'.

**`LABEL_PRESERVE_P (`x`)`**
: In a `code_label` or `note`, indicates that the label is referenced by
code or data not visible to the RTL of a given function.
Labels referenced by a non-local goto will have this bit set. Stored
in the `in_struct` field and printed as ``/s`'.

**`LABEL_REF_NONLOCAL_P (`x`)`**
: In `label_ref` and `reg_label` expressions, nonzero if this is
a reference to a non-local label.
Stored in the `volatil` field and printed as ``/v`'.

**`MEM_IN_STRUCT_P (`x`)`**
: In `mem` expressions, nonzero for reference to an entire structure,
union or array, or to a component of one. Zero for references to a
scalar variable or through a pointer to a scalar. If both this flag and
`MEM_SCALAR_P` are clear, then we don't know whether this `mem`
is in a structure or not. Both flags should never be simultaneously set.
Stored in the `in_struct` field and printed as ``/s`'.

**`MEM_KEEP_ALIAS_SET_P (`x`)`**
: In `mem` expressions, 1 if we should keep the alias set for this
mem unchanged when we access a component. Set to 1, for example, when we
are already in a non-addressable component of an aggregate.
Stored in the `jump` field and printed as ``/j`'.

**`MEM_SCALAR_P (`x`)`**
: In `mem` expressions, nonzero for reference to a scalar known not
to be a member of a structure, union, or array. Zero for such
references and for indirections through pointers, even pointers pointing
to scalar types. If both this flag and `MEM_IN_STRUCT_P` are clear,
then we don't know whether this `mem` is in a structure or not.
Both flags should never be simultaneously set.
Stored in the `frame_related` field and printed as ``/f`'.

**`MEM_VOLATILE_P (`x`)`**
: In `mem`, `asm_operands`, and `asm_input` expressions,
nonzero for volatile memory references.
Stored in the `volatil` field and printed as ``/v`'.

**`MEM_NOTRAP_P (`x`)`**
: In `mem`, nonzero for memory references that will not trap.
Stored in the `call` field and printed as ``/c`'.

**`REG_FUNCTION_VALUE_P (`x`)`**
: Nonzero in a `reg` if it is the place in which this function's
value is going to be returned. (This happens only in a hard
register.) Stored in the `integrated` field and printed as
``/i`'.

**`REG_POINTER (`x`)`**
: Nonzero in a `reg` if the register holds a pointer. Stored in the
`frame_related` field and printed as ``/f`'.

**`REG_USERVAR_P (`x`)`**
: In a `reg`, nonzero if it corresponds to a variable present in
the user's source code. Zero for temporaries generated internally by
the compiler. Stored in the `volatil` field and printed as
``/v`'.

The same hard register may be used also for collecting the values of
functions called by this one, but `REG_FUNCTION_VALUE_P` is zero
in this kind of use.

**`RTX_FRAME_RELATED_P (`x`)`**
: Nonzero in an `insn`, `call_insn`, `jump_insn`,
`barrier`, or `set` which is part of a function prologue
and sets the stack pointer, sets the frame pointer, or saves a register.
This flag should also be set on an instruction that sets up a temporary
register to use in place of the frame pointer.
Stored in the `frame_related` field and printed as ``/f`'.

In particular, on RISC targets where there are limits on the sizes of
immediate constants, it is sometimes impossible to reach the register
save area directly from the stack pointer. In that case, a temporary
register is used that is near enough to the register save area, and the
Canonical Frame Address, i.e., DWARF2's logical frame pointer, register
must (temporarily) be changed to be this temporary register. So, the
instruction that sets this temporary register must be marked as
`RTX_FRAME_RELATED_P`.

If the marked instruction is overly complex (defined in terms of what
`dwarf2out_frame_debug_expr` can handle), you will also have to
create a `REG_FRAME_RELATED_EXPR` note and attach it to the
instruction. This note should contain a simple expression of the
computation performed by this instruction, i.e., one that
`dwarf2out_frame_debug_expr` can handle.

This flag is required for exception handling support on targets with RTL
prologues.

`code_label`, `insn_list`, `const`, or `note` if it
resulted from an in-line function call.
Stored in the `integrated` field and printed as ``/i`'.

**`MEM_READONLY_P (`x`)`**
: Nonzero in a `mem`, if the memory is statically allocated and read-only.

Read-only in this context means never modified during the lifetime of the
program, not necessarily in ROM or in write-disabled pages. A common
example of the later is a shared library's global offset table. This
table is initialized by the runtime loader, so the memory is technically
writable, but after control is transfered from the runtime loader to the
application, this memory will never be subsequently modified.

Stored in the `unchanging` field and printed as ``/u`'.

**`SCHED_GROUP_P (`x`)`**
: During instruction scheduling, in an `insn`, `call_insn` or
`jump_insn`, indicates that the
previous insn must be scheduled together with this insn. This is used to
ensure that certain groups of instructions will not be split up by the
instruction scheduling pass, for example, `use` insns before
a `call_insn` may not be separated from the `call_insn`.
Stored in the `in_struct` field and printed as ``/s`'.

**`SET_IS_RETURN_P (`x`)`**
: For a `set`, nonzero if it is for a return.
Stored in the `jump` field and printed as ``/j`'.

**`SIBLING_CALL_P (`x`)`**
: For a `call_insn`, nonzero if the insn is a sibling call.
Stored in the `jump` field and printed as ``/j`'.

**`STRING_POOL_ADDRESS_P (`x`)`**
: For a `symbol_ref` expression, nonzero if it addresses this function's
string constant pool.
Stored in the `frame_related` field and printed as ``/f`'.

**`SUBREG_PROMOTED_UNSIGNED_P (`x`)`**
: Returns a value greater then zero for a `subreg` that has
`SUBREG_PROMOTED_VAR_P` nonzero if the object being referenced is kept
zero-extended, zero if it is kept sign-extended, and less then zero if it is
extended some other way via the `ptr_extend` instruction.
Stored in the `unchanging`
field and `volatil` field, printed as ``/u`' and ``/v`'.
This macro may only be used to get the value it may not be used to change
the value. Use `SUBREG_PROMOTED_UNSIGNED_SET` to change the value.

**`SUBREG_PROMOTED_UNSIGNED_SET (`x`)`**
: Set the `unchanging` and `volatil` fields in a `subreg`
to reflect zero, sign, or other extension. If `volatil` is
zero, then `unchanging` as nonzero means zero extension and as
zero means sign extension. If `volatil` is nonzero then some
other type of extension was done via the `ptr_extend` instruction.

**`SUBREG_PROMOTED_VAR_P (`x`)`**
: Nonzero in a `subreg` if it was made when accessing an object that
was promoted to a wider mode in accord with the `PROMOTED_MODE` machine
description macro (see [Storage Layout](Storage-Layout.md#apple-kn2g64tbm5ss2tdbpfxxk5a)). In this case, the mode of
the `subreg` is the declared mode of the object and the mode of
`SUBREG_REG` is the mode of the register that holds the object.
Promoted variables are always either sign- or zero-extended to the wider
mode on every assignment. Stored in the `in_struct` field and
printed as ``/s`'.

**`SYMBOL_REF_USED (`x`)`**
: In a `symbol_ref`, indicates that x has been used. This is
normally only used to ensure that x is only declared external
once. Stored in the `used` field.

**`SYMBOL_REF_WEAK (`x`)`**
: In a `symbol_ref`, indicates that x has been declared weak.
Stored in the `integrated` field and printed as ``/i`'.

**`SYMBOL_REF_FLAG (`x`)`**
: In a `symbol_ref`, this is used as a flag for machine-specific purposes.
Stored in the `volatil` field and printed as ``/v`'.

Most uses of `SYMBOL_REF_FLAG` are historic and may be subsumed
by `SYMBOL_REF_FLAGS`. Certainly use of `SYMBOL_REF_FLAGS`
is mandatory if the target requires more than one bit of storage.

These are the fields to which the above macros refer:

**`call`**
: In a `mem`, 1 means that the memory reference will not trap.

In an RTL dump, this flag is represented as ``/c`'.

**`frame_related`**
: In an `insn` or `set` expression, 1 means that it is part of
a function prologue and sets the stack pointer, sets the frame pointer,
saves a register, or sets up a temporary register to use in place of the
frame pointer.

In `reg` expressions, 1 means that the register holds a pointer.

In `symbol_ref` expressions, 1 means that the reference addresses
this function's string constant pool.

In `mem` expressions, 1 means that the reference is to a scalar.

In an RTL dump, this flag is represented as ``/f`'.

**`in_struct`**
: In `mem` expressions, it is 1 if the memory datum referred to is
all or part of a structure or array; 0 if it is (or might be) a scalar
variable. A reference through a C pointer has 0 because the pointer
might point to a scalar variable. This information allows the compiler
to determine something about possible cases of aliasing.

In `reg` expressions, it is 1 if the register has its entire life
contained within the test expression of some loop.

In `subreg` expressions, 1 means that the `subreg` is accessing
an object that has had its mode promoted from a wider mode.

In `label_ref` expressions, 1 means that the referenced label is
outside the innermost loop containing the insn in which the `label_ref`
was found.

In `code_label` expressions, it is 1 if the label may never be deleted.
This is used for labels which are the target of non-local gotos. Such a
label that would have been deleted is replaced with a `note` of type
`NOTE_INSN_DELETED_LABEL`.

In an `insn` during dead-code elimination, 1 means that the insn is
dead code.

In an `insn` or `jump_insn` during reorg for an insn in the
delay slot of a branch,
1 means that this insn is from the target of the branch.

In an `insn` during instruction scheduling, 1 means that this insn
must be scheduled as part of a group together with the previous insn.

In an RTL dump, this flag is represented as ``/s`'.

**`integrated`**
: In an `insn`, `insn_list`, or `const`, 1 means the RTL was
produced by procedure integration.

In `reg` expressions, 1 means the register contains
the value to be returned by the current function. On
machines that pass parameters in registers, the same register number
may be used for parameters as well, but this flag is not set on such
uses.

In `symbol_ref` expressions, 1 means the referenced symbol is weak.

In an RTL dump, this flag is represented as ``/i`'.

**`jump`**
: In a `mem` expression, 1 means we should keep the alias set for this
mem unchanged when we access a component.

In a `set`, 1 means it is for a return.

In a `call_insn`, 1 means it is a sibling call.

In an RTL dump, this flag is represented as ``/j`'.

**`unchanging`**
: In `reg` and `mem` expressions, 1 means
that the value of the expression never changes.

In `subreg` expressions, it is 1 if the `subreg` references an
unsigned object whose mode has been promoted to a wider mode.

In an `insn` or `jump_insn` in the delay slot of a branch
instruction, 1 means an annulling branch should be used.

In a `symbol_ref` expression, 1 means that this symbol addresses
something in the per-function constant pool.

In a `call_insn`, `note`, or an `expr_list` of notes,
1 means that this instruction is a call to a const or pure function.

In an RTL dump, this flag is represented as ``/u`'.

**`used`**
: This flag is used directly (without an access macro) at the end of RTL
generation for a function, to count the number of times an expression
appears in insns. Expressions that appear more than once are copied,
according to the rules for shared structure (see [Sharing](Sharing.md#apple-knugc4tjnztq)).

For a `reg`, it is used directly (without an access macro) by the
leaf register renumbering code to ensure that each register is only
renumbered once.

In a `symbol_ref`, it indicates that an external declaration for
the symbol has already been written.

**`volatil`**
: In a `mem`, `asm_operands`, or `asm_input`
expression, it is 1 if the memory
reference is volatile. Volatile memory references may not be deleted,
reordered or combined.

In a `symbol_ref` expression, it is used for machine-specific
purposes.

In a `reg` expression, it is 1 if the value is a user-level variable.
0 indicates an internal compiler temporary.

In an `insn`, 1 means the insn has been deleted.

In `label_ref` and `reg_label` expressions, 1 means a reference
to a non-local label.

In an RTL dump, this flag is represented as ``/v`'.
