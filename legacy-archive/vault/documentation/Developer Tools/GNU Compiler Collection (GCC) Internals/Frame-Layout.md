---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Frame-Layout.html
archived_at: '2026-07-15T07:30:59.901393Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Exception Handling](Exception-Handling.md#apple-iv4ggzlqoruw63rnjbqw4zdmnfxgo),
Up: [Stack and Calling](Stack-and-Calling.md#apple-kn2gcy3lfvqw4zbninqwy3djnztq)

---

#### 13.9.1 Basic Stack Layout

Here is the basic stack layout.

— Macro: __STACK_GROWS_DOWNWARD__
> Define this macro if pushing a word onto the stack moves the stack
> pointer to a smaller address.
>
> When we say, “define this macro if ...”, it means that the
> compiler checks this macro only with `#ifdef` so the precise
> definition used does not matter.

— Macro: __STACK_PUSH_CODE__
> This macro defines the operation used when something is pushed
> on the stack. In RTL, a push operation will be
> `(set (mem (STACK_PUSH_CODE (reg sp))) ...)`
>
> The choices are `PRE_DEC`, `POST_DEC`, `PRE_INC`,
> and `POST_INC`. Which of these is correct depends on
> the stack direction and on whether the stack pointer points
> to the last item on the stack or whether it points to the
> space for the next item on the stack.
>
> The default is `PRE_DEC` when `STACK_GROWS_DOWNWARD` is
> defined, which is almost always right, and `PRE_INC` otherwise,
> which is often wrong.

— Macro: __FRAME_GROWS_DOWNWARD__
> Define this macro if the addresses of local variable slots are at negative
> offsets from the frame pointer.

— Macro: __ARGS_GROW_DOWNWARD__
> Define this macro if successive arguments to a function occupy decreasing
> addresses on the stack.

— Macro: __STARTING_FRAME_OFFSET__
> Offset from the frame pointer to the first local variable slot to be allocated.
>
> If `FRAME_GROWS_DOWNWARD`, find the next slot's offset by
> subtracting the first slot's length from `STARTING_FRAME_OFFSET`.
> Otherwise, it is found by adding the length of the first slot to the
> value `STARTING_FRAME_OFFSET`.

— Macro: __STACK_ALIGNMENT_NEEDED__
> Define to zero to disable final alignment of the stack during reload.
> The nonzero default for this macro is suitable for most ports.
>
> On ports where `STARTING_FRAME_OFFSET` is nonzero or where there
> is a register save block following the local block that doesn't require
> alignment to `STACK_BOUNDARY`, it may be beneficial to disable
> stack alignment and do it in the backend.

— Macro: __STACK_POINTER_OFFSET__
> Offset from the stack pointer register to the first location at which
> outgoing arguments are placed. If not specified, the default value of
> zero is used. This is the proper value for most machines.
>
> If `ARGS_GROW_DOWNWARD`, this is the offset to the location above
> the first location at which outgoing arguments are placed.

— Macro: __FIRST_PARM_OFFSET__ (fundecl)
> Offset from the argument pointer register to the first argument's
> address. On some machines it may depend on the data type of the
> function.
>
> If `ARGS_GROW_DOWNWARD`, this is the offset to the location above
> the first argument's address.

— Macro: __STACK_DYNAMIC_OFFSET__ (fundecl)
> Offset from the stack pointer register to an item dynamically allocated
> on the stack, e.g., by `alloca`.
>
> The default value for this macro is `STACK_POINTER_OFFSET` plus the
> length of the outgoing arguments. The default is correct for most
> machines. See `function.c` for details.

— Macro: __INITIAL_FRAME_ADDRESS_RTX__
> A C expression whose value is RTL representing the address of the initial
> stack frame. This address is passed to `RETURN_ADDR_RTX` and
> `DYNAMIC_CHAIN_ADDRESS`.
> If you don't define this macro, the default is to return
> `hard_frame_pointer_rtx`.
> This default is usually correct unless `-fomit-frame-pointer` is in
> effect.
> Define this macro in order to make `__builtin_frame_address (0)` and
> `__builtin_return_address (0)` work even in absence of a hard frame pointer.

— Macro: __DYNAMIC_CHAIN_ADDRESS__ (frameaddr)
> A C expression whose value is RTL representing the address in a stack
> frame where the pointer to the caller's frame is stored. Assume that
> frameaddr is an RTL expression for the address of the stack frame
> itself.
>
> If you don't define this macro, the default is to return the value
> of frameaddr—that is, the stack frame address is also the
> address of the stack word that points to the previous frame.

— Macro: __SETUP_FRAME_ADDRESSES__
> If defined, a C expression that produces the machine-specific code to
> setup the stack so that arbitrary frames can be accessed. For example,
> on the SPARC, we must flush all of the register windows to the stack
> before we can access arbitrary stack frames. You will seldom need to
> define this macro.

— Target Hook: bool __TARGET_BUILTIN_SETJMP_FRAME_VALUE__ ()
> This target hook should return an rtx that is used to store
> the address of the current frame into the built in `setjmp` buffer.
> The default value, `virtual_stack_vars_rtx`, is correct for most
> machines. One reason you may need to define this target hook is if
> `hard_frame_pointer_rtx` is the appropriate value on your machine.

— Macro: __RETURN_ADDR_RTX__ (count, frameaddr)
> A C expression whose value is RTL representing the value of the return
> address for the frame count steps up from the current frame, after
> the prologue. frameaddr is the frame pointer of the count
> frame, or the frame pointer of the count − 1 frame if
> `RETURN_ADDR_IN_PREVIOUS_FRAME` is defined.
>
> The value of the expression must always be the correct address when
> count is zero, but may be `NULL_RTX` if there is not way to
> determine the return address of other frames.

— Macro: __RETURN_ADDR_IN_PREVIOUS_FRAME__
> Define this if the return address of a particular stack frame is accessed
> from the frame pointer of the previous stack frame.

— Macro: __INCOMING_RETURN_ADDR_RTX__
> A C expression whose value is RTL representing the location of the
> incoming return address at the beginning of any function, before the
> prologue. This RTL is either a `REG`, indicating that the return
> value is saved in ``REG`', or a `MEM` representing a location in
> the stack.
>
> You only need to define this macro if you want to support call frame
> debugging information like that provided by DWARF 2.
>
> If this RTL is a `REG`, you should also define
> `DWARF_FRAME_RETURN_COLUMN` to `DWARF_FRAME_REGNUM (REGNO)`.

— Macro: __DWARF_ALT_FRAME_RETURN_COLUMN__
> A C expression whose value is an integer giving a DWARF 2 column
> number that may be used as an alternate return column. This should
> be defined only if `DWARF_FRAME_RETURN_COLUMN` is set to a
> general register, but an alternate column needs to be used for
> signal frames.

— Macro: __DWARF_ZERO_REG__
> A C expression whose value is an integer giving a DWARF 2 register
> number that is considered to always have the value zero. This should
> only be defined if the target has an architected zero register, and
> someone decided it was a good idea to use that register number to
> terminate the stack backtrace. New ports should avoid this.

— Target Hook: void __TARGET_DWARF_HANDLE_FRAME_UNSPEC__ (const char \*label, rtx pattern, int index)
> This target hook allows the backend to emit frame-related insns that
> contain UNSPECs or UNSPEC_VOLATILEs. The DWARF 2 call frame debugging
> info engine will invoke it on insns of the form
>
> ```
>           (set (reg) (unspec [...] UNSPEC_INDEX))
>
> ```
>
> and
>
> ```
>           (set (reg) (unspec_volatile [...] UNSPECV_INDEX)).
>
> ```
>
> to let the backend emit the call frame instructions. label is
> the CFI label attached to the insn, pattern is the pattern of
> the insn and index is `UNSPEC_INDEX` or `UNSPECV_INDEX`.

— Macro: __INCOMING_FRAME_SP_OFFSET__
> A C expression whose value is an integer giving the offset, in bytes,
> from the value of the stack pointer register to the top of the stack
> frame at the beginning of any function, before the prologue. The top of
> the frame is defined to be the value of the stack pointer in the
> previous frame, just before the call instruction.
>
> You only need to define this macro if you want to support call frame
> debugging information like that provided by DWARF 2.

— Macro: __ARG_POINTER_CFA_OFFSET__ (fundecl)
> A C expression whose value is an integer giving the offset, in bytes,
> from the argument pointer to the canonical frame address (cfa). The
> final value should coincide with that calculated by
> `INCOMING_FRAME_SP_OFFSET`. Which is unfortunately not usable
> during virtual register instantiation.
>
> The default value for this macro is `FIRST_PARM_OFFSET (fundecl)`,
> which is correct for most machines; in general, the arguments are found
> immediately before the stack frame. Note that this is not the case on
> some targets that save registers into the caller's frame, such as SPARC
> and rs6000, and so such targets need to define this macro.
>
> You only need to define this macro if the default is incorrect, and you
> want to support call frame debugging information like that provided by
> DWARF 2.
