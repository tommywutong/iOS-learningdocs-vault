---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Machine_002dIndependent-Predicates.html
archived_at: '2026-07-15T07:31:00.303274Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Defining Predicates](Defining-Predicates.md#apple-irswm2lonfxgolkqojswi2ldmf2gk4y),
Up: [Predicates](Predicates.md#apple-kbzgkzdjmnqxizlt)

---

#### 12.7.1 Machine-Independent Predicates

These are the generic predicates available to all back ends. They are
defined in `recog.c`. The first category of predicates allow
only constant, or immediate, operands.

— Function: __immediate_operand__
> This predicate allows any sort of constant that fits in mode.
> It is an appropriate choice for instructions that take operands that
> must be constant.

— Function: __const_int_operand__
> This predicate allows any `CONST_INT` expression that fits in
> mode. It is an appropriate choice for an immediate operand that
> does not allow a symbol or label.

— Function: __const_double_operand__
> This predicate accepts any `CONST_DOUBLE` expression that has
> exactly mode. If mode is `VOIDmode`, it will also
> accept `CONST_INT`. It is intended for immediate floating point
> constants.

The second category of predicates allow only some kind of machine
register.

— Function: __register_operand__
> This predicate allows any `REG` or `SUBREG` expression that
> is valid for mode. It is often suitable for arithmetic
> instruction operands on a RISC machine.

— Function: __pmode_register_operand__
> This is a slight variant on `register_operand` which works around
> a limitation in the machine-description reader.
>
> ```
>           (match_operand n "pmode_register_operand" constraint)
>
> ```
>
> means exactly what
>
> ```
>           (match_operand:P n "register_operand" constraint)
>
> ```
>
> would mean, if the machine-description reader accepted ``:P`'
> mode suffixes. Unfortunately, it cannot, because `Pmode` is an
> alias for some other mode, and might vary with machine-specific
> options. See [Misc](Misc.md#apple-jvuxgyy).

— Function: __scratch_operand__
> This predicate allows hard registers and `SCRATCH` expressions,
> but not pseudo-registers. It is used internally by `match_scratch`;
> it should not be used directly.

The third category of predicates allow only some kind of memory reference.

— Function: __memory_operand__
> This predicate allows any valid reference to a quantity of mode
> mode in memory, as determined by the weak form of
> `GO_IF_LEGITIMATE_ADDRESS` (see [Addressing Modes](Addressing-Modes.md#apple-ifsgi4tfonzws3thfvgw6zdfom)).

— Function: __address_operand__
> This predicate is a little unusual; it allows any operand that is a
> valid expression for the _address_ of a quantity of mode
> mode, again determined by the weak form of
> `GO_IF_LEGITIMATE_ADDRESS`. To first order, if
> ``(mem:mode (exp))`' is acceptable to
> `memory_operand`, then exp is acceptable to
> `address_operand`. Note that exp does not necessarily have
> the mode mode.

— Function: __indirect_operand__
> This is a stricter form of `memory_operand` which allows only
> memory references with a `general_operand` as the address
> expression. New uses of this predicate are discouraged, because
> `general_operand` is very permissive, so it's hard to tell what
> an `indirect_operand` does or does not allow. If a target has
> different requirements for memory operands for different instructions,
> it is better to define target-specific predicates which enforce the
> hardware's requirements explicitly.

— Function: __push_operand__
> This predicate allows a memory reference suitable for pushing a value
> onto the stack. This will be a `MEM` which refers to
> `stack_pointer_rtx`, with a side-effect in its address expression
> (see [Incdec](Incdec.md#apple-jfxggzdfmm)); which one is determined by the
> `STACK_PUSH_CODE` macro (see [Frame Layout](Frame-Layout.md#apple-izzgc3lffvggc6lpov2a)).

— Function: __pop_operand__
> This predicate allows a memory reference suitable for popping a value
> off the stack. Again, this will be a `MEM` referring to
> `stack_pointer_rtx`, with a side-effect in its address
> expression. However, this time `STACK_POP_CODE` is expected.

The fourth category of predicates allow some combination of the above
operands.

— Function: __nonmemory_operand__
> This predicate allows any immediate or register operand valid for mode.

— Function: __nonimmediate_operand__
> This predicate allows any register or memory operand valid for mode.

— Function: __general_operand__
> This predicate allows any immediate, register, or memory operand
> valid for mode.

Finally, there is one generic operator predicate.

— Function: __comparison_operator__
> This predicate matches any expression which performs an arithmetic
> comparison in mode; that is, `COMPARISON_P` is true for the
> expression code.
