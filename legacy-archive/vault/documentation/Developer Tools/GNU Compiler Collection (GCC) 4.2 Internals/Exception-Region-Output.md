---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Exception-Region-Output.html
archived_at: '2026-07-15T07:31:01.797359Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Alignment Output](Alignment-Output.md#apple-ifwgsz3onvsw45bnj52xi4dvoq),
Previous: [Dispatch Tables](Dispatch-Tables.md#apple-iruxg4dborrwqlkumfrgyzlt),
Up: [Assembler Format](Assembler-Format.md#apple-ifzxgzlnmjwgk4rnizxxe3lboq)

---

#### 15.21.9 Assembler Commands for Exception Regions

This describes commands marking the start and the end of an exception
region.

— Macro: __EH_FRAME_SECTION_NAME__
> If defined, a C string constant for the name of the section containing
> exception handling frame unwind information. If not defined, GCC will
> provide a default definition if the target supports named sections.
> `crtstuff.c` uses this macro to switch to the appropriate section.
>
> You should define this symbol if your target supports DWARF 2 frame
> unwind information and the default definition does not work.

— Macro: __EH_FRAME_IN_DATA_SECTION__
> If defined, DWARF 2 frame unwind information will be placed in the
> data section even though the target supports named sections. This
> might be necessary, for instance, if the system linker does garbage
> collection and sections cannot be marked as not to be collected.
>
> Do not define this macro unless `TARGET_ASM_NAMED_SECTION` is
> also defined.

— Macro: __EH_TABLES_CAN_BE_READ_ONLY__
> Define this macro to 1 if your target is such that no frame unwind
> information encoding used with non-PIC code will ever require a
> runtime relocation, but the linker may not support merging read-only
> and read-write sections into a single read-write section.

— Macro: __MASK_RETURN_ADDR__
> An rtx used to mask the return address found via `RETURN_ADDR_RTX`, so
> that it does not contain any extraneous set bits in it.

— Macro: __DWARF2_UNWIND_INFO__
> Define this macro to 0 if your target supports DWARF 2 frame unwind
> information, but it does not yet work with exception handling.
> Otherwise, if your target supports this information (if it defines
> ``INCOMING_RETURN_ADDR_RTX`' and either ``UNALIGNED_INT_ASM_OP`'
> or ``OBJECT_FORMAT_ELF`'), GCC will provide a default definition of 1.
>
> If `TARGET_UNWIND_INFO` is defined, the target specific unwinder
> will be used in all cases. Defining this macro will enable the generation
> of DWARF 2 frame debugging information.
>
> If `TARGET_UNWIND_INFO` is not defined, and this macro is defined to 1,
> the DWARF 2 unwinder will be the default exception handling mechanism;
> otherwise, the `setjmp`/`longjmp`-based scheme will be used by
> default.

— Macro: __TARGET_UNWIND_INFO__
> Define this macro if your target has ABI specified unwind tables. Usually
> these will be output by `TARGET_UNWIND_EMIT`.

— Variable: Target Hook __bool__ TARGET_UNWIND_TABLES_DEFAULT
> This variable should be set to `true` if the target ABI requires unwinding
> tables even when exceptions are not used.

— Macro: __MUST_USE_SJLJ_EXCEPTIONS__
> This macro need only be defined if `DWARF2_UNWIND_INFO` is
> runtime-variable. In that case, `except.h` cannot correctly
> determine the corresponding definition of `MUST_USE_SJLJ_EXCEPTIONS`,
> so the target must provide it directly.

— Macro: __DONT_USE_BUILTIN_SETJMP__
> Define this macro to 1 if the `setjmp`/`longjmp`-based scheme
> should use the `setjmp`/`longjmp` functions from the C library
> instead of the `__builtin_setjmp`/`__builtin_longjmp` machinery.

— Macro: __DWARF_CIE_DATA_ALIGNMENT__
> This macro need only be defined if the target might save registers in the
> function prologue at an offset to the stack pointer that is not aligned to
> `UNITS_PER_WORD`. The definition should be the negative minimum
> alignment if `STACK_GROWS_DOWNWARD` is defined, and the positive
> minimum alignment otherwise. See [SDB and DWARF](SDB-and-DWARF.md#apple-knceellbnzsc2rcxifjem). Only applicable if
> the target supports DWARF 2 frame unwind information.

— Variable: Target Hook __bool__ TARGET_TERMINATE_DW2_EH_FRAME_INFO
> Contains the value true if the target should add a zero word onto the
> end of a Dwarf-2 frame info section when used for exception handling.
> Default value is false if `EH_FRAME_SECTION_NAME` is defined, and
> true otherwise.

— Target Hook: rtx __TARGET_DWARF_REGISTER_SPAN__ (rtx reg)
> Given a register, this hook should return a parallel of registers to
> represent where to find the register pieces. Define this hook if the
> register and its mode are represented in Dwarf in non-contiguous
> locations, or if the register should be represented in more than one
> register in Dwarf. Otherwise, this hook should return `NULL_RTX`.
> If not defined, the default is to return `NULL_RTX`.

— Target Hook: bool __TARGET_ASM_TTYPE__ (rtx sym)
> This hook is used to output a reference from a frame unwinding table to
> the type_info object identified by sym. It should return `true`
> if the reference was output. Returning `false` will cause the
> reference to be output using the normal Dwarf2 routines.

— Target Hook: bool __TARGET_ARM_EABI_UNWINDER__
> This hook should be set to `true` on targets that use an ARM EABI
> based unwinding library, and `false` on other targets. This effects
> the format of unwinding tables, and how the unwinder in entered after
> running a cleanup. The default is `false`.
