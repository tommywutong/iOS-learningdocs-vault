---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Costs.html
archived_at: '2026-07-15T07:30:59.660988Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Scheduling](Scheduling.md#apple-knrwqzleovwgs3th),
Previous: [Condition Code](Condition-Code.md#apple-inxw4zdjoruw63rninxwizi),
Up: [Target Macros](Target-Macros.md#apple-krqxez3foqwu2yldojxxg)

---

### 13.15 Describing Relative Costs of Operations

These macros let you describe the relative speed of various operations
on the target machine.

— Macro: __REGISTER_MOVE_COST__ (mode, from, to)
> A C expression for the cost of moving data of mode mode from a
> register in class from to one in class to. The classes are
> expressed using the enumeration values such as `GENERAL_REGS`. A
> value of 2 is the default; other values are interpreted relative to
> that.
>
> It is not required that the cost always equal 2 when from is the
> same as to; on some machines it is expensive to move between
> registers if they are not general registers.
>
> If reload sees an insn consisting of a single `set` between two
> hard registers, and if `REGISTER_MOVE_COST` applied to their
> classes returns a value of 2, reload does not check to ensure that the
> constraints of the insn are met. Setting a cost of other than 2 will
> allow reload to verify that the constraints are met. You should do this
> if the ``movm`' pattern's constraints do not allow such copying.

— Macro: __MEMORY_MOVE_COST__ (mode, class, in)
> A C expression for the cost of moving data of mode mode between a
> register of class class and memory; in is zero if the value
> is to be written to memory, nonzero if it is to be read in. This cost
> is relative to those in `REGISTER_MOVE_COST`. If moving between
> registers and memory is more expensive than between two registers, you
> should define this macro to express the relative cost.
>
> If you do not define this macro, GCC uses a default cost of 4 plus
> the cost of copying via a secondary reload register, if one is
> needed. If your machine requires a secondary reload register to copy
> between memory and a register of class but the reload mechanism is
> more complex than copying via an intermediate, define this macro to
> reflect the actual cost of the move.
>
> GCC defines the function `memory_move_secondary_cost` if
> secondary reloads are needed. It computes the costs due to copying via
> a secondary register. If your machine copies from memory using a
> secondary register in the conventional way but the default base value of
> 4 is not correct for your machine, define this macro to add some other
> value to the result of that function. The arguments to that function
> are the same as to this macro.

— Macro: __BRANCH_COST__
> A C expression for the cost of a branch instruction. A value of 1 is
> the default; other values are interpreted relative to that.

Here are additional macros which do not specify precise relative costs,
but only that certain actions are more expensive than GCC would
ordinarily expect.

— Macro: __SLOW_BYTE_ACCESS__
> Define this macro as a C expression which is nonzero if accessing less
> than a word of memory (i.e. a `char` or a `short`) is no
> faster than accessing a word of memory, i.e., if such access
> require more than one instruction or if there is no difference in cost
> between byte and (aligned) word loads.
>
> When this macro is not defined, the compiler will access a field by
> finding the smallest containing object; when it is defined, a fullword
> load will be used if alignment permits. Unless bytes accesses are
> faster than word accesses, using word accesses is preferable since it
> may eliminate subsequent memory access if subsequent accesses occur to
> other fields in the same word of the structure, but to different bytes.

— Macro: __SLOW_UNALIGNED_ACCESS__ (mode, alignment)
> Define this macro to be the value 1 if memory accesses described by the
> mode and alignment parameters have a cost many times greater
> than aligned accesses, for example if they are emulated in a trap
> handler.
>
> When this macro is nonzero, the compiler will act as if
> `STRICT_ALIGNMENT` were nonzero when generating code for block
> moves. This can cause significantly more instructions to be produced.
> Therefore, do not set this macro nonzero if unaligned accesses only add a
> cycle or two to the time for a memory access.
>
> If the value of this macro is always zero, it need not be defined. If
> this macro is defined, it should produce a nonzero value when
> `STRICT_ALIGNMENT` is nonzero.

— Macro: __MOVE_RATIO__
> The threshold of number of scalar memory-to-memory move insns, _below_
> which a sequence of insns should be generated instead of a
> string move insn or a library call. Increasing the value will always
> make code faster, but eventually incurs high cost in increased code size.
>
> Note that on machines where the corresponding move insn is a
> `define_expand` that emits a sequence of insns, this macro counts
> the number of such sequences.
>
> If you don't define this, a reasonable default is used.

— Macro: __MOVE_BY_PIECES_P__ (size, alignment)
> A C expression used to determine whether `move_by_pieces` will be used to
> copy a chunk of memory, or whether some other block move mechanism
> will be used. Defaults to 1 if `move_by_pieces_ninsns` returns less
> than `MOVE_RATIO`.

— Macro: __MOVE_MAX_PIECES__
> A C expression used by `move_by_pieces` to determine the largest unit
> a load or store used to copy memory is. Defaults to `MOVE_MAX`.

— Macro: __CLEAR_RATIO__
> The threshold of number of scalar move insns, _below_ which a sequence
> of insns should be generated to clear memory instead of a string clear insn
> or a library call. Increasing the value will always make code faster, but
> eventually incurs high cost in increased code size.
>
> If you don't define this, a reasonable default is used.

— Macro: __CLEAR_BY_PIECES_P__ (size, alignment)
> A C expression used to determine whether `clear_by_pieces` will be used
> to clear a chunk of memory, or whether some other block clear mechanism
> will be used. Defaults to 1 if `move_by_pieces_ninsns` returns less
> than `CLEAR_RATIO`.

— Macro: __STORE_BY_PIECES_P__ (size, alignment)
> A C expression used to determine whether `store_by_pieces` will be
> used to set a chunk of memory to a constant value, or whether some other
> mechanism will be used. Used by `__builtin_memset` when storing
> values other than constant zero and by `__builtin_strcpy` when
> when called with a constant source string.
> Defaults to 1 if `move_by_pieces_ninsns` returns less
> than `MOVE_RATIO`.

— Macro: __USE_LOAD_POST_INCREMENT__ (mode)
> A C expression used to determine whether a load postincrement is a good
> thing to use for a given mode. Defaults to the value of
> `HAVE_POST_INCREMENT`.

— Macro: __USE_LOAD_POST_DECREMENT__ (mode)
> A C expression used to determine whether a load postdecrement is a good
> thing to use for a given mode. Defaults to the value of
> `HAVE_POST_DECREMENT`.

— Macro: __USE_LOAD_PRE_INCREMENT__ (mode)
> A C expression used to determine whether a load preincrement is a good
> thing to use for a given mode. Defaults to the value of
> `HAVE_PRE_INCREMENT`.

— Macro: __USE_LOAD_PRE_DECREMENT__ (mode)
> A C expression used to determine whether a load predecrement is a good
> thing to use for a given mode. Defaults to the value of
> `HAVE_PRE_DECREMENT`.

— Macro: __USE_STORE_POST_INCREMENT__ (mode)
> A C expression used to determine whether a store postincrement is a good
> thing to use for a given mode. Defaults to the value of
> `HAVE_POST_INCREMENT`.

— Macro: __USE_STORE_POST_DECREMENT__ (mode)
> A C expression used to determine whether a store postdecrement is a good
> thing to use for a given mode. Defaults to the value of
> `HAVE_POST_DECREMENT`.

— Macro: __USE_STORE_PRE_INCREMENT__ (mode)
> This macro is used to determine whether a store preincrement is a good
> thing to use for a given mode. Defaults to the value of
> `HAVE_PRE_INCREMENT`.

— Macro: __USE_STORE_PRE_DECREMENT__ (mode)
> This macro is used to determine whether a store predecrement is a good
> thing to use for a given mode. Defaults to the value of
> `HAVE_PRE_DECREMENT`.

— Macro: __NO_FUNCTION_CSE__
> Define this macro if it is as good or better to call a constant
> function address than to call an address kept in a register.

— Macro: __RANGE_TEST_NON_SHORT_CIRCUIT__
> Define this macro if a non-short-circuit operation produced by
> ``fold_range_test ()`' is optimal. This macro defaults to true if
> `BRANCH_COST` is greater than or equal to the value 2.

— Target Hook: bool __TARGET_RTX_COSTS__ (rtx x, int code, int outer_code, int \*total)
> This target hook describes the relative costs of RTL expressions.
>
> The cost may depend on the precise form of the expression, which is
> available for examination in x, and the rtx code of the expression
> in which it is contained, found in outer_code. code is the
> expression code—redundant, since it can be obtained with
> `GET_CODE (`x`)`.
>
> In implementing this hook, you can use the construct
> `COSTS_N_INSNS (`n`)` to specify a cost equal to n fast
> instructions.
>
> On entry to the hook, `*`total contains a default estimate
> for the cost of the expression. The hook should modify this value as
> necessary. Traditionally, the default costs are `COSTS_N_INSNS (5)`
> for multiplications, `COSTS_N_INSNS (7)` for division and modulus
> operations, and `COSTS_N_INSNS (1)` for all other operations.
>
> When optimizing for code size, i.e. when `optimize_size` is
> nonzero, this target hook should be used to estimate the relative
> size cost of an expression, again relative to `COSTS_N_INSNS`.
>
> The hook returns true when all subexpressions of x have been
> processed, and false when `rtx_cost` should recurse.

— Target Hook: int __TARGET_ADDRESS_COST__ (rtx address)
> This hook computes the cost of an addressing mode that contains
> address. If not defined, the cost is computed from
> the address expression and the `TARGET_RTX_COST` hook.
>
> For most CISC machines, the default cost is a good approximation of the
> true cost of the addressing mode. However, on RISC machines, all
> instructions normally have the same length and execution time. Hence
> all addresses will have equal costs.
>
> In cases where more than one form of an address is known, the form with
> the lowest cost will be used. If multiple forms have the same, lowest,
> cost, the one that is the most complex will be used.
>
> For example, suppose an address that is equal to the sum of a register
> and a constant is used twice in the same basic block. When this macro
> is not defined, the address will be computed in a register and memory
> references will be indirect through that register. On machines where
> the cost of the addressing mode containing the sum is no higher than
> that of a simple indirect reference, this will produce an additional
> instruction and possibly require an additional register. Proper
> specification of this macro eliminates this overhead for such machines.
>
> This hook is never called with an invalid address.
>
> On machines where an address involving more than one register is as
> cheap as an address computation involving only one register, defining
> `TARGET_ADDRESS_COST` to reflect this can cause two registers to
> be live over a region of code where only one would have been if
> `TARGET_ADDRESS_COST` were not defined in that manner. This effect
> should be considered in the definition of this macro. Equivalent costs
> should probably only be given to addresses with different numbers of
> registers on machines with lots of registers.
