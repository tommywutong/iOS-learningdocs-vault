---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Mode-Switching.html
archived_at: '2026-07-15T07:31:02.409144Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Target Attributes](Target-Attributes.md#apple-krqxez3foqwuc5duojuwe5lumvzq),
Previous: [Floating Point](Floating-Point.md#apple-izwg6ylunfxgolkqn5uw45a),
Up: [Target Macros](Target-Macros.md#apple-krqxez3foqwu2yldojxxg)

---

### 15.24 Mode Switching Instructions

The following macros control mode switching optimizations:

— Macro: __OPTIMIZE_MODE_SWITCHING__ (entity)
> Define this macro if the port needs extra instructions inserted for mode
> switching in an optimizing compilation.
>
> For an example, the SH4 can perform both single and double precision
> floating point operations, but to perform a single precision operation,
> the FPSCR PR bit has to be cleared, while for a double precision
> operation, this bit has to be set. Changing the PR bit requires a general
> purpose register as a scratch register, hence these FPSCR sets have to
> be inserted before reload, i.e. you can't put this into instruction emitting
> or `TARGET_MACHINE_DEPENDENT_REORG`.
>
> You can have multiple entities that are mode-switched, and select at run time
> which entities actually need it. `OPTIMIZE_MODE_SWITCHING` should
> return nonzero for any entity that needs mode-switching.
> If you define this macro, you also have to define
> `NUM_MODES_FOR_MODE_SWITCHING`, `MODE_NEEDED`,
> `MODE_PRIORITY_TO_MODE` and `EMIT_MODE_SET`.
> `MODE_AFTER`, `MODE_ENTRY`, and `MODE_EXIT`
> are optional.

— Macro: __NUM_MODES_FOR_MODE_SWITCHING__
> If you define `OPTIMIZE_MODE_SWITCHING`, you have to define this as
> initializer for an array of integers. Each initializer element
> N refers to an entity that needs mode switching, and specifies the number
> of different modes that might need to be set for this entity.
> The position of the initializer in the initializer—starting counting at
> zero—determines the integer that is used to refer to the mode-switched
> entity in question.
> In macros that take mode arguments / yield a mode result, modes are
> represented as numbers 0 ... N − 1. N is used to specify that no mode
> switch is needed / supplied.

— Macro: __MODE_NEEDED__ (entity, insn)
> entity is an integer specifying a mode-switched entity. If
> `OPTIMIZE_MODE_SWITCHING` is defined, you must define this macro to
> return an integer value not larger than the corresponding element in
> `NUM_MODES_FOR_MODE_SWITCHING`, to denote the mode that entity must
> be switched into prior to the execution of insn.

— Macro: __MODE_AFTER__ (mode, insn)
> If this macro is defined, it is evaluated for every insn during
> mode switching. It determines the mode that an insn results in (if
> different from the incoming mode).

— Macro: __MODE_ENTRY__ (entity)
> If this macro is defined, it is evaluated for every entity that needs
> mode switching. It should evaluate to an integer, which is a mode that
> entity is assumed to be switched to at function entry. If `MODE_ENTRY`
> is defined then `MODE_EXIT` must be defined.

— Macro: __MODE_EXIT__ (entity)
> If this macro is defined, it is evaluated for every entity that needs
> mode switching. It should evaluate to an integer, which is a mode that
> entity is assumed to be switched to at function exit. If `MODE_EXIT`
> is defined then `MODE_ENTRY` must be defined.

— Macro: __MODE_PRIORITY_TO_MODE__ (entity, n)
> This macro specifies the order in which modes for entity are processed.
> 0 is the highest priority, `NUM_MODES_FOR_MODE_SWITCHING[`entity`] - 1` the
> lowest. The value of the macro should be an integer designating a mode
> for entity. For any fixed entity, `mode_priority_to_mode`
> (entity, n) shall be a bijection in 0 ...
> `num_modes_for_mode_switching[`entity`] - 1`.

— Macro: __EMIT_MODE_SET__ (entity, mode, hard_regs_live)
> Generate one or more insns to set entity to mode.
> hard_reg_live is the set of hard registers live at the point where
> the insn(s) are to be inserted.
