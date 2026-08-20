---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Values-in-Registers.html
archived_at: '2026-07-15T07:31:03.083558Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Leaf Functions](Leaf-Functions.md#apple-jrswczrniz2w4y3unfxw44y),
Previous: [Allocation Order](Allocation-Order.md#apple-ifwgy33dmf2gs33ofvhxezdfoi),
Up: [Registers](Registers.md#apple-kjswo2ltorsxe4y)

---

#### 15.7.3 How Values Fit in Registers

This section discusses the macros that describe which kinds of values
(specifically, which machine modes) each register can hold, and how many
consecutive registers are needed for a given mode.

— Macro: __HARD_REGNO_NREGS__ (regno, mode)
> A C expression for the number of consecutive hard registers, starting
> at register number regno, required to hold a value of mode
> mode.
>
> On a machine where all registers are exactly one word, a suitable
> definition of this macro is
>
> ```
>           #define HARD_REGNO_NREGS(REGNO, MODE)            \
>              ((GET_MODE_SIZE (MODE) + UNITS_PER_WORD - 1)  \
>               / UNITS_PER_WORD)
>
> ```

— Macro: __HARD_REGNO_NREGS_HAS_PADDING__ (regno, mode)
> A C expression that is nonzero if a value of mode mode, stored
> in memory, ends with padding that causes it to take up more space than
> in registers starting at register number regno (as determined by
> multiplying GCC's notion of the size of the register when containing
> this mode by the number of registers returned by
> `HARD_REGNO_NREGS`). By default this is zero.
>
> For example, if a floating-point value is stored in three 32-bit
> registers but takes up 128 bits in memory, then this would be
> nonzero.
>
> This macros only needs to be defined if there are cases where
> `subreg_regno_offset` and `subreg_offset_representable_p`
> would otherwise wrongly determine that a `subreg` can be
> represented by an offset to the register number, when in fact such a
> `subreg` would contain some of the padding not stored in
> registers and so not be representable.

— Macro: __HARD_REGNO_NREGS_WITH_PADDING__ (regno, mode)
> For values of regno and mode for which
> `HARD_REGNO_NREGS_HAS_PADDING` returns nonzero, a C expression
> returning the greater number of registers required to hold the value
> including any padding. In the example above, the value would be four.

— Macro: __REGMODE_NATURAL_SIZE__ (mode)
> Define this macro if the natural size of registers that hold values
> of mode mode is not the word size. It is a C expression that
> should give the natural size in bytes for the specified mode. It is
> used by the register allocator to try to optimize its results. This
> happens for example on SPARC 64-bit where the natural size of
> floating-point registers is still 32-bit.

— Macro: __HARD_REGNO_MODE_OK__ (regno, mode)
> A C expression that is nonzero if it is permissible to store a value
> of mode mode in hard register number regno (or in several
> registers starting with that one). For a machine where all registers
> are equivalent, a suitable definition is
>
> ```
>           #define HARD_REGNO_MODE_OK(REGNO, MODE) 1
>
> ```
>
> You need not include code to check for the numbers of fixed registers,
> because the allocation mechanism considers them to be always occupied.
>
> On some machines, double-precision values must be kept in even/odd
> register pairs. You can implement that by defining this macro to reject
> odd register numbers for such modes.
>
> The minimum requirement for a mode to be OK in a register is that the
> ``movmode`' instruction pattern support moves between the
> register and other hard register in the same class and that moving a
> value into the register and back out not alter it.
>
> Since the same instruction used to move `word_mode` will work for
> all narrower integer modes, it is not necessary on any machine for
> `HARD_REGNO_MODE_OK` to distinguish between these modes, provided
> you define patterns ``movhi`', etc., to take advantage of this. This
> is useful because of the interaction between `HARD_REGNO_MODE_OK`
> and `MODES_TIEABLE_P`; it is very desirable for all integer modes
> to be tieable.
>
> Many machines have special registers for floating point arithmetic.
> Often people assume that floating point machine modes are allowed only
> in floating point registers. This is not true. Any registers that
> can hold integers can safely _hold_ a floating point machine
> mode, whether or not floating arithmetic can be done on it in those
> registers. Integer move instructions can be used to move the values.
>
> On some machines, though, the converse is true: fixed-point machine
> modes may not go in floating registers. This is true if the floating
> registers normalize any value stored in them, because storing a
> non-floating value there would garble it. In this case,
> `HARD_REGNO_MODE_OK` should reject fixed-point machine modes in
> floating registers. But if the floating registers do not automatically
> normalize, if you can store any bit pattern in one and retrieve it
> unchanged without a trap, then any machine mode may go in a floating
> register, so you can define this macro to say so.
>
> The primary significance of special floating registers is rather that
> they are the registers acceptable in floating point arithmetic
> instructions. However, this is of no concern to
> `HARD_REGNO_MODE_OK`. You handle it by writing the proper
> constraints for those instructions.
>
> On some machines, the floating registers are especially slow to access,
> so that it is better to store a value in a stack frame than in such a
> register if floating point arithmetic is not being done. As long as the
> floating registers are not in class `GENERAL_REGS`, they will not
> be used unless some pattern's constraint asks for one.

— Macro: __HARD_REGNO_RENAME_OK__ (from, to)
> A C expression that is nonzero if it is OK to rename a hard register
> from to another hard register to.
>
> One common use of this macro is to prevent renaming of a register to
> another register that is not saved by a prologue in an interrupt
> handler.
>
> The default is always nonzero.

— Macro: __MODES_TIEABLE_P__ (mode1, mode2)
> A C expression that is nonzero if a value of mode
> mode1 is accessible in mode mode2 without copying.
>
> If `HARD_REGNO_MODE_OK (`r`,` mode1`)` and
> `HARD_REGNO_MODE_OK (`r`,` mode2`)` are always the same for
> any r, then `MODES_TIEABLE_P (`mode1`,` mode2`)`
> should be nonzero. If they differ for any r, you should define
> this macro to return zero unless some other mechanism ensures the
> accessibility of the value in a narrower mode.
>
> You should define this macro to return nonzero in as many cases as
> possible since doing so will allow GCC to perform better register
> allocation.

— Macro: __AVOID_CCMODE_COPIES__
> Define this macro if the compiler should avoid copies to/from `CCmode`
> registers. You should only define this macro if support for copying to/from
> `CCmode` is incomplete.
