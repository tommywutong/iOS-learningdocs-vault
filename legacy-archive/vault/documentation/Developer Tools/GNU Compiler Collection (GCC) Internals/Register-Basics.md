---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Register-Basics.html
archived_at: '2026-07-15T07:31:00.620348Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Allocation Order](Allocation-Order.md#apple-ifwgy33dmf2gs33ofvhxezdfoi),
Up: [Registers](Registers.md#apple-kjswo2ltorsxe4y)

---

#### 13.7.1 Basic Characteristics of Registers

Registers have various characteristics.

— Macro: __FIRST_PSEUDO_REGISTER__
> Number of hardware registers known to the compiler. They receive
> numbers 0 through `FIRST_PSEUDO_REGISTER-1`; thus, the first
> pseudo register's number really is assigned the number
> `FIRST_PSEUDO_REGISTER`.

— Macro: __FIXED_REGISTERS__
> An initializer that says which registers are used for fixed purposes
> all throughout the compiled code and are therefore not available for
> general allocation. These would include the stack pointer, the frame
> pointer (except on machines where that can be used as a general
> register when no frame pointer is needed), the program counter on
> machines where that is considered one of the addressable registers,
> and any other numbered register with a standard use.
>
> This information is expressed as a sequence of numbers, separated by
> commas and surrounded by braces. The nth number is 1 if
> register n is fixed, 0 otherwise.
>
> The table initialized from this macro, and the table initialized by
> the following one, may be overridden at run time either automatically,
> by the actions of the macro `CONDITIONAL_REGISTER_USAGE`, or by
> the user with the command options `-ffixed-reg`,
> `-fcall-used-reg` and `-fcall-saved-reg`.

— Macro: __CALL_USED_REGISTERS__
> Like `FIXED_REGISTERS` but has 1 for each register that is
> clobbered (in general) by function calls as well as for fixed
> registers. This macro therefore identifies the registers that are not
> available for general allocation of values that must live across
> function calls.
>
> If a register has 0 in `CALL_USED_REGISTERS`, the compiler
> automatically saves it on function entry and restores it on function
> exit, if the register is used within the function.

— Macro: __CALL_REALLY_USED_REGISTERS__
> Like `CALL_USED_REGISTERS` except this macro doesn't require
> that the entire set of `FIXED_REGISTERS` be included.
> (`CALL_USED_REGISTERS` must be a superset of `FIXED_REGISTERS`).
> This macro is optional. If not specified, it defaults to the value
> of `CALL_USED_REGISTERS`.

— Macro: __HARD_REGNO_CALL_PART_CLOBBERED__ (regno, mode)
> A C expression that is nonzero if it is not permissible to store a
> value of mode mode in hard register number regno across a
> call without some part of it being clobbered. For most machines this
> macro need not be defined. It is only required for machines that do not
> preserve the entire contents of a register across a call.

— Macro: __CONDITIONAL_REGISTER_USAGE__
> Zero or more C statements that may conditionally modify five variables
> `fixed_regs`, `call_used_regs`, `global_regs`,
> `reg_names`, and `reg_class_contents`, to take into account
> any dependence of these register sets on target flags. The first three
> of these are of type `char []` (interpreted as Boolean vectors).
> `global_regs` is a `const char *[]`, and
> `reg_class_contents` is a `HARD_REG_SET`. Before the macro is
> called, `fixed_regs`, `call_used_regs`,
> `reg_class_contents`, and `reg_names` have been initialized
> from `FIXED_REGISTERS`, `CALL_USED_REGISTERS`,
> `REG_CLASS_CONTENTS`, and `REGISTER_NAMES`, respectively.
> `global_regs` has been cleared, and any `-ffixed-reg`,
> `-fcall-used-reg` and `-fcall-saved-reg`
> command options have been applied.
>
> You need not define this macro if it has no work to do.
>
> If the usage of an entire class of registers depends on the target
> flags, you may indicate this to GCC by using this macro to modify
> `fixed_regs` and `call_used_regs` to 1 for each of the
> registers in the classes which should not be used by GCC. Also define
> the macro `REG_CLASS_FROM_LETTER` / `REG_CLASS_FROM_CONSTRAINT`
> to return `NO_REGS` if it
> is called with a letter for a class that shouldn't be used.
>
> (However, if this class is not included in `GENERAL_REGS` and all
> of the insn patterns whose constraints permit this class are
> controlled by target switches, then GCC will automatically avoid using
> these registers when the target switches are opposed to them.)

— Macro: __INCOMING_REGNO__ (out)
> Define this macro if the target machine has register windows. This C
> expression returns the register number as seen by the called function
> corresponding to the register number out as seen by the calling
> function. Return out if register number out is not an
> outbound register.

— Macro: __OUTGOING_REGNO__ (in)
> Define this macro if the target machine has register windows. This C
> expression returns the register number as seen by the calling function
> corresponding to the register number in as seen by the called
> function. Return in if register number in is not an inbound
> register.

— Macro: __LOCAL_REGNO__ (regno)
> Define this macro if the target machine has register windows. This C
> expression returns true if the register is call-saved but is in the
> register window. Unlike most call-saved registers, such registers
> need not be explicitly restored on function exit or during non-local
> gotos.

— Macro: __PC_REGNUM__
> If the program counter has a register number, define this as that
> register number. Otherwise, do not define it.
