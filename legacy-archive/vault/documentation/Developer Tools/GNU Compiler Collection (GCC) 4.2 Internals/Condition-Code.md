---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Condition-Code.html
archived_at: '2026-07-15T07:31:01.521952Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Costs](Costs.md#apple-inxxg5dt),
Previous: [Anchored Addresses](Anchored-Addresses.md#apple-ifxgg2dpojswilkbmrshezltonsxg),
Up: [Target Macros](Target-Macros.md#apple-krqxez3foqwu2yldojxxg)

---

### 15.16 Condition Code Status

This describes the condition code status.

The file `conditions.h` defines a variable `cc_status` to
describe how the condition code was computed (in case the interpretation of
the condition code depends on the instruction that it was set by). This
variable contains the RTL expressions on which the condition code is
currently based, and several standard flags.

Sometimes additional machine-specific flags must be defined in the machine
description header file. It can also add additional machine-specific
information by defining `CC_STATUS_MDEP`.

— Macro: __CC_STATUS_MDEP__
> C code for a data type which is used for declaring the `mdep`
> component of `cc_status`. It defaults to `int`.
>
> This macro is not used on machines that do not use `cc0`.

— Macro: __CC_STATUS_MDEP_INIT__
> A C expression to initialize the `mdep` field to “empty”.
> The default definition does nothing, since most machines don't use
> the field anyway. If you want to use the field, you should probably
> define this macro to initialize it.
>
> This macro is not used on machines that do not use `cc0`.

— Macro: __NOTICE_UPDATE_CC__ (exp, insn)
> A C compound statement to set the components of `cc_status`
> appropriately for an insn insn whose body is exp. It is
> this macro's responsibility to recognize insns that set the condition
> code as a byproduct of other activity as well as those that explicitly
> set `(cc0)`.
>
> This macro is not used on machines that do not use `cc0`.
>
> If there are insns that do not set the condition code but do alter
> other machine registers, this macro must check to see whether they
> invalidate the expressions that the condition code is recorded as
> reflecting. For example, on the 68000, insns that store in address
> registers do not set the condition code, which means that usually
> `NOTICE_UPDATE_CC` can leave `cc_status` unaltered for such
> insns. But suppose that the previous insn set the condition code
> based on location ``a4@(102)`' and the current insn stores a new
> value in ``a4`'. Although the condition code is not changed by
> this, it will no longer be true that it reflects the contents of
> ``a4@(102)`'. Therefore, `NOTICE_UPDATE_CC` must alter
> `cc_status` in this case to say that nothing is known about the
> condition code value.
>
> The definition of `NOTICE_UPDATE_CC` must be prepared to deal
> with the results of peephole optimization: insns whose patterns are
> `parallel` RTXs containing various `reg`, `mem` or
> constants which are just the operands. The RTL structure of these
> insns is not sufficient to indicate what the insns actually do. What
> `NOTICE_UPDATE_CC` should do when it sees one is just to run
> `CC_STATUS_INIT`.
>
> A possible definition of `NOTICE_UPDATE_CC` is to call a function
> that looks at an attribute (see [Insn Attributes](Insn-Attributes.md#apple-jfxhg3rnif2hi4tjmj2xizlt)) named, for example,
> ``cc`'. This avoids having detailed information about patterns in
> two places, the `md` file and in `NOTICE_UPDATE_CC`.

— Macro: __SELECT_CC_MODE__ (op, x, y)
> Returns a mode from class `MODE_CC` to be used when comparison
> operation code op is applied to rtx x and y. For
> example, on the SPARC, `SELECT_CC_MODE` is defined as (see
> see [Jump Patterns](Jump-Patterns.md#apple-jj2w24bnkbqxi5dfojxhg) for a description of the reason for this
> definition)
>
> ```
>           #define SELECT_CC_MODE(OP,X,Y) \
>             (GET_MODE_CLASS (GET_MODE (X)) == MODE_FLOAT          \
>              ? ((OP == EQ || OP == NE) ? CCFPmode : CCFPEmode)    \
>              : ((GET_CODE (X) == PLUS || GET_CODE (X) == MINUS    \
>                  || GET_CODE (X) == NEG) \
>                 ? CC_NOOVmode : CCmode))
>
> ```
>
> You should define this macro if and only if you define extra CC modes
> in `machine-modes.def`.

— Macro: __CANONICALIZE_COMPARISON__ (code, op0, op1)
> On some machines not all possible comparisons are defined, but you can
> convert an invalid comparison into a valid one. For example, the Alpha
> does not have a `GT` comparison, but you can use an `LT`
> comparison instead and swap the order of the operands.
>
> On such machines, define this macro to be a C statement to do any
> required conversions. code is the initial comparison code
> and op0 and op1 are the left and right operands of the
> comparison, respectively. You should modify code, op0, and
> op1 as required.
>
> GCC will not assume that the comparison resulting from this macro is
> valid but will see if the resulting insn matches a pattern in the
> `md` file.
>
> You need not define this macro if it would never change the comparison
> code or operands.

— Macro: __REVERSIBLE_CC_MODE__ (mode)
> A C expression whose value is one if it is always safe to reverse a
> comparison whose mode is mode. If `SELECT_CC_MODE`
> can ever return mode for a floating-point inequality comparison,
> then `REVERSIBLE_CC_MODE (`mode`)` must be zero.
>
> You need not define this macro if it would always returns zero or if the
> floating-point format is anything other than `IEEE_FLOAT_FORMAT`.
> For example, here is the definition used on the SPARC, where floating-point
> inequality comparisons are always given `CCFPEmode`:
>
> ```
>           #define REVERSIBLE_CC_MODE(MODE)  ((MODE) != CCFPEmode)
>
> ```

— Macro: __REVERSE_CONDITION__ (code, mode)
> A C expression whose value is reversed condition code of the code for
> comparison done in CC_MODE mode. The macro is used only in case
> `REVERSIBLE_CC_MODE (`mode`)` is nonzero. Define this macro in case
> machine has some non-standard way how to reverse certain conditionals. For
> instance in case all floating point conditions are non-trapping, compiler may
> freely convert unordered compares to ordered one. Then definition may look
> like:
>
> ```
>           #define REVERSE_CONDITION(CODE, MODE) \
>              ((MODE) != CCFPmode ? reverse_condition (CODE) \
>               : reverse_condition_maybe_unordered (CODE))
>
> ```

— Macro: __REVERSE_CONDEXEC_PREDICATES_P__ (op1, op2)
> A C expression that returns true if the conditional execution predicate
> op1, a comparison operation, is the inverse of op2 and vice
> versa. Define this to return 0 if the target has conditional execution
> predicates that cannot be reversed safely. There is no need to validate
> that the arguments of op1 and op2 are the same, this is done separately.
> If no expansion is specified, this macro is defined as follows:
>
> ```
>           #define REVERSE_CONDEXEC_PREDICATES_P (x, y) \
>              (GET_CODE ((x)) == reversed_comparison_code ((y), NULL))
>
> ```

— Target Hook: bool __TARGET_FIXED_CONDITION_CODE_REGS__ (unsigned int \*, unsigned int \*)
> On targets which do not use `(cc0)`, and which use a hard
> register rather than a pseudo-register to hold condition codes, the
> regular CSE passes are often not able to identify cases in which the
> hard register is set to a common value. Use this hook to enable a
> small pass which optimizes such cases. This hook should return true
> to enable this pass, and it should set the integers to which its
> arguments point to the hard register numbers used for condition codes.
> When there is only one such register, as is true on most systems, the
> integer pointed to by the second argument should be set to
> `INVALID_REGNUM`.
>
> The default version of this hook returns false.

— Target Hook: enum __machine_mode__ TARGET_CC_MODES_COMPATIBLE (enum machine_mode, enum machine_mode)
> On targets which use multiple condition code modes in class
> `MODE_CC`, it is sometimes the case that a comparison can be
> validly done in more than one mode. On such a system, define this
> target hook to take two mode arguments and to return a mode in which
> both comparisons may be validly done. If there is no such mode,
> return `VOIDmode`.
>
> The default version of this hook checks whether the modes are the
> same. If they are, it returns that mode. If they are different, it
> returns `VOIDmode`.
