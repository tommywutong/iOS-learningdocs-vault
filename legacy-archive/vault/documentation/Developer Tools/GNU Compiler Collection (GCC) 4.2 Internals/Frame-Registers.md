---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Frame-Registers.html
archived_at: '2026-07-15T07:31:01.904319Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Elimination](Elimination.md#apple-ivwgs3ljnzqxi2lpny),
Previous: [Stack Checking](Stack-Checking.md#apple-kn2gcy3lfvbwqzldnnuw4zy),
Up: [Stack and Calling](Stack-and-Calling.md#apple-kn2gcy3lfvqw4zbninqwy3djnztq)

---

#### 15.10.4 Registers That Address the Stack Frame

This discusses registers that address the stack frame.

— Macro: __STACK_POINTER_REGNUM__
> The register number of the stack pointer register, which must also be a
> fixed register according to `FIXED_REGISTERS`. On most machines,
> the hardware determines which register this is.

— Macro: __FRAME_POINTER_REGNUM__
> The register number of the frame pointer register, which is used to
> access automatic variables in the stack frame. On some machines, the
> hardware determines which register this is. On other machines, you can
> choose any register you wish for this purpose.

— Macro: __HARD_FRAME_POINTER_REGNUM__
> On some machines the offset between the frame pointer and starting
> offset of the automatic variables is not known until after register
> allocation has been done (for example, because the saved registers are
> between these two locations). On those machines, define
> `FRAME_POINTER_REGNUM` the number of a special, fixed register to
> be used internally until the offset is known, and define
> `HARD_FRAME_POINTER_REGNUM` to be the actual hard register number
> used for the frame pointer.
>
> You should define this macro only in the very rare circumstances when it
> is not possible to calculate the offset between the frame pointer and
> the automatic variables until after register allocation has been
> completed. When this macro is defined, you must also indicate in your
> definition of `ELIMINABLE_REGS` how to eliminate
> `FRAME_POINTER_REGNUM` into either `HARD_FRAME_POINTER_REGNUM`
> or `STACK_POINTER_REGNUM`.
>
> Do not define this macro if it would be the same as
> `FRAME_POINTER_REGNUM`.

— Macro: __ARG_POINTER_REGNUM__
> The register number of the arg pointer register, which is used to access
> the function's argument list. On some machines, this is the same as the
> frame pointer register. On some machines, the hardware determines which
> register this is. On other machines, you can choose any register you
> wish for this purpose. If this is not the same register as the frame
> pointer register, then you must mark it as a fixed register according to
> `FIXED_REGISTERS`, or arrange to be able to eliminate it
> (see [Elimination](Elimination.md#apple-ivwgs3ljnzqxi2lpny)).

— Macro: __RETURN_ADDRESS_POINTER_REGNUM__
> The register number of the return address pointer register, which is used to
> access the current function's return address from the stack. On some
> machines, the return address is not at a fixed offset from the frame
> pointer or stack pointer or argument pointer. This register can be defined
> to point to the return address on the stack, and then be converted by
> `ELIMINABLE_REGS` into either the frame pointer or stack pointer.
>
> Do not define this macro unless there is no other way to get the return
> address from the stack.

— Macro: __STATIC_CHAIN_REGNUM__
— Macro: __STATIC_CHAIN_INCOMING_REGNUM__
> Register numbers used for passing a function's static chain pointer. If
> register windows are used, the register number as seen by the called
> function is `STATIC_CHAIN_INCOMING_REGNUM`, while the register
> number as seen by the calling function is `STATIC_CHAIN_REGNUM`. If
> these registers are the same, `STATIC_CHAIN_INCOMING_REGNUM` need
> not be defined.
>
> The static chain register need not be a fixed register.
>
> If the static chain is passed in memory, these macros should not be
> defined; instead, the next two macros should be defined.

— Macro: __STATIC_CHAIN__
— Macro: __STATIC_CHAIN_INCOMING__
> If the static chain is passed in memory, these macros provide rtx giving
> `mem` expressions that denote where they are stored.
> `STATIC_CHAIN` and `STATIC_CHAIN_INCOMING` give the locations
> as seen by the calling and called functions, respectively. Often the former
> will be at an offset from the stack pointer and the latter at an offset from
> the frame pointer.
>
> The variables `stack_pointer_rtx`, `frame_pointer_rtx`, and
> `arg_pointer_rtx` will have been initialized prior to the use of these
> macros and should be used to refer to those items.
>
> If the static chain is passed in a register, the two previous macros should
> be defined instead.

— Macro: __DWARF_FRAME_REGISTERS__
> This macro specifies the maximum number of hard registers that can be
> saved in a call frame. This is used to size data structures used in
> DWARF2 exception handling.
>
> Prior to GCC 3.0, this macro was needed in order to establish a stable
> exception handling ABI in the face of adding new hard registers for ISA
> extensions. In GCC 3.0 and later, the EH ABI is insulated from changes
> in the number of hard registers. Nevertheless, this macro can still be
> used to reduce the runtime memory requirements of the exception handling
> routines, which can be substantial if the ISA contains a lot of
> registers that are not call-saved.
>
> If this macro is not defined, it defaults to
> `FIRST_PSEUDO_REGISTER`.

— Macro: __PRE_GCC3_DWARF_FRAME_REGISTERS__
> This macro is similar to `DWARF_FRAME_REGISTERS`, but is provided
> for backward compatibility in pre GCC 3.0 compiled code.
>
> If this macro is not defined, it defaults to
> `DWARF_FRAME_REGISTERS`.

— Macro: __DWARF_REG_TO_UNWIND_COLUMN__ (regno)
> Define this macro if the target's representation for dwarf registers
> is different than the internal representation for unwind column.
> Given a dwarf register, this macro should return the internal unwind
> column number to use instead.
>
> See the PowerPC's SPE target for an example.

— Macro: __DWARF_FRAME_REGNUM__ (regno)
> Define this macro if the target's representation for dwarf registers
> used in .eh_frame or .debug_frame is different from that used in other
> debug info sections. Given a GCC hard register number, this macro
> should return the .eh_frame register number. The default is
> `DBX_REGISTER_NUMBER (`regno`)`.

— Macro: __DWARF2_FRAME_REG_OUT__ (regno, for_eh)
> Define this macro to map register numbers held in the call frame info
> that GCC has collected using `DWARF_FRAME_REGNUM` to those that
> should be output in .debug_frame (for_eh is zero) and
> .eh_frame (for_eh is nonzero). The default is to
> return regno.
