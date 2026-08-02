---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Function-Entry.html
archived_at: '2026-07-15T07:30:59.949190Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Profiling](Profiling.md#apple-kbzg6ztjnruw4zy),
Previous: [Caller Saves](Caller-Saves.md#apple-inqwy3dfoiwvgylwmvzq),
Up: [Stack and Calling](Stack-and-Calling.md#apple-kn2gcy3lfvqw4zbninqwy3djnztq)

---

#### 13.9.11 Function Entry and Exit

This section describes the macros that output function entry
(prologue) and exit (epilogue) code.

— Target Hook: void __TARGET_ASM_FUNCTION_PROLOGUE__ (FILE \*file, HOST_WIDE_INT size)
> If defined, a function that outputs the assembler code for entry to a
> function. The prologue is responsible for setting up the stack frame,
> initializing the frame pointer register, saving registers that must be
> saved, and allocating size additional bytes of storage for the
> local variables. size is an integer. file is a stdio
> stream to which the assembler code should be output.
>
> The label for the beginning of the function need not be output by this
> macro. That has already been done when the macro is run.
>
> To determine which registers to save, the macro can refer to the array
> `regs_ever_live`: element r is nonzero if hard register
> r is used anywhere within the function. This implies the function
> prologue should save register r, provided it is not one of the
> call-used registers. (`TARGET_ASM_FUNCTION_EPILOGUE` must likewise use
> `regs_ever_live`.)
>
> On machines that have “register windows”, the function entry code does
> not save on the stack the registers that are in the windows, even if
> they are supposed to be preserved by function calls; instead it takes
> appropriate steps to “push” the register stack, if any non-call-used
> registers are used in the function.
>
> On machines where functions may or may not have frame-pointers, the
> function entry code must vary accordingly; it must set up the frame
> pointer if one is wanted, and not otherwise. To determine whether a
> frame pointer is in wanted, the macro can refer to the variable
> `frame_pointer_needed`. The variable's value will be 1 at run
> time in a function that needs a frame pointer. See [Elimination](Elimination.md#apple-ivwgs3ljnzqxi2lpny).
>
> The function entry code is responsible for allocating any stack space
> required for the function. This stack space consists of the regions
> listed below. In most cases, these regions are allocated in the
> order listed, with the last listed region closest to the top of the
> stack (the lowest address if `STACK_GROWS_DOWNWARD` is defined, and
> the highest address if it is not defined). You can use a different order
> for a machine if doing so is more convenient or required for
> compatibility reasons. Except in cases where required by standard
> or by a debugger, there is no reason why the stack layout used by GCC
> need agree with that used by other compilers for a machine.

— Target Hook: void __TARGET_ASM_FUNCTION_END_PROLOGUE__ (FILE \*file)
> If defined, a function that outputs assembler code at the end of a
> prologue. This should be used when the function prologue is being
> emitted as RTL, and you have some extra assembler that needs to be
> emitted. See [prologue instruction pattern](https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/prologue-instruction-pattern.html#prologue-instruction-pattern).

— Target Hook: void __TARGET_ASM_FUNCTION_BEGIN_EPILOGUE__ (FILE \*file)
> If defined, a function that outputs assembler code at the start of an
> epilogue. This should be used when the function epilogue is being
> emitted as RTL, and you have some extra assembler that needs to be
> emitted. See [epilogue instruction pattern](https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/epilogue-instruction-pattern.html#epilogue-instruction-pattern).

— Target Hook: void __TARGET_ASM_FUNCTION_EPILOGUE__ (FILE \*file, HOST_WIDE_INT size)
> If defined, a function that outputs the assembler code for exit from a
> function. The epilogue is responsible for restoring the saved
> registers and stack pointer to their values when the function was
> called, and returning control to the caller. This macro takes the
> same arguments as the macro `TARGET_ASM_FUNCTION_PROLOGUE`, and the
> registers to restore are determined from `regs_ever_live` and
> `CALL_USED_REGISTERS` in the same way.
>
> On some machines, there is a single instruction that does all the work
> of returning from the function. On these machines, give that
> instruction the name ``return`' and do not define the macro
> `TARGET_ASM_FUNCTION_EPILOGUE` at all.
>
> Do not define a pattern named ``return`' if you want the
> `TARGET_ASM_FUNCTION_EPILOGUE` to be used. If you want the target
> switches to control whether return instructions or epilogues are used,
> define a ``return`' pattern with a validity condition that tests the
> target switches appropriately. If the ``return`' pattern's validity
> condition is false, epilogues will be used.
>
> On machines where functions may or may not have frame-pointers, the
> function exit code must vary accordingly. Sometimes the code for these
> two cases is completely different. To determine whether a frame pointer
> is wanted, the macro can refer to the variable
> `frame_pointer_needed`. The variable's value will be 1 when compiling
> a function that needs a frame pointer.
>
> Normally, `TARGET_ASM_FUNCTION_PROLOGUE` and
> `TARGET_ASM_FUNCTION_EPILOGUE` must treat leaf functions specially.
> The C variable `current_function_is_leaf` is nonzero for such a
> function. See [Leaf Functions](Leaf-Functions.md#apple-jrswczrniz2w4y3unfxw44y).
>
> On some machines, some functions pop their arguments on exit while
> others leave that for the caller to do. For example, the 68020 when
> given `-mrtd` pops arguments in functions that take a fixed
> number of arguments.
>
> Your definition of the macro `RETURN_POPS_ARGS` decides which
> functions pop their own arguments. `TARGET_ASM_FUNCTION_EPILOGUE`
> needs to know what was decided. The variable that is called
> `current_function_pops_args` is the number of bytes of its
> arguments that a function should pop. See [Scalar Return](Scalar-Return.md#apple-knrwc3dboiwvezluovzg4).

- A region of `current_function_pretend_args_size` bytes of
  uninitialized space just underneath the first argument arriving on the
  stack. (This may not be at the very start of the allocated stack region
  if the calling sequence has pushed anything else since pushing the stack
  arguments. But usually, on such machines, nothing else has been pushed
  yet, because the function prologue itself does all the pushing.) This
  region is used on machines where an argument may be passed partly in
  registers and partly in memory, and, in some cases to support the
  features in `<stdarg.h>`.
- An area of memory used to save certain registers used by the function.
  The size of this area, which may also include space for such things as
  the return address and pointers to previous stack frames, is
  machine-specific and usually depends on which registers have been used
  in the function. Machines with register windows often do not require
  a save area.
- A region of at least size bytes, possibly rounded up to an allocation
  boundary, to contain the local variables of the function. On some machines,
  this region and the save area may occur in the opposite order, with the
  save area closer to the top of the stack.
- Optionally, when `ACCUMULATE_OUTGOING_ARGS` is defined, a region of
  `current_function_outgoing_args_size` bytes to be used for outgoing
  argument lists of the function. See [Stack Arguments](Stack-Arguments.md#apple-kn2gcy3lfvaxez3vnvsw45dt).

— Macro: __EXIT_IGNORE_STACK__
> Define this macro as a C expression that is nonzero if the return
> instruction or the function epilogue ignores the value of the stack
> pointer; in other words, if it is safe to delete an instruction to
> adjust the stack pointer before a return from the function. The
> default is 0.
>
> Note that this macro's value is relevant only for functions for which
> frame pointers are maintained. It is never safe to delete a final
> stack adjustment in a function that has no frame pointer, and the
> compiler knows this regardless of `EXIT_IGNORE_STACK`.

— Macro: __EPILOGUE_USES__ (regno)
> Define this macro as a C expression that is nonzero for registers that are
> used by the epilogue or the ``return`' pattern. The stack and frame
> pointer registers are already be assumed to be used as needed.

— Macro: __EH_USES__ (regno)
> Define this macro as a C expression that is nonzero for registers that are
> used by the exception handling mechanism, and so should be considered live
> on entry to an exception edge.

— Macro: __DELAY_SLOTS_FOR_EPILOGUE__
> Define this macro if the function epilogue contains delay slots to which
> instructions from the rest of the function can be “moved”. The
> definition should be a C expression whose value is an integer
> representing the number of delay slots there.

— Macro: __ELIGIBLE_FOR_EPILOGUE_DELAY__ (insn, n)
> A C expression that returns 1 if insn can be placed in delay
> slot number n of the epilogue.
>
> The argument n is an integer which identifies the delay slot now
> being considered (since different slots may have different rules of
> eligibility). It is never negative and is always less than the number
> of epilogue delay slots (what `DELAY_SLOTS_FOR_EPILOGUE` returns).
> If you reject a particular insn for a given delay slot, in principle, it
> may be reconsidered for a subsequent delay slot. Also, other insns may
> (at least in principle) be considered for the so far unfilled delay
> slot.
>
> The insns accepted to fill the epilogue delay slots are put in an RTL
> list made with `insn_list` objects, stored in the variable
> `current_function_epilogue_delay_list`. The insn for the first
> delay slot comes first in the list. Your definition of the macro
> `TARGET_ASM_FUNCTION_EPILOGUE` should fill the delay slots by
> outputting the insns in this list, usually by calling
> `final_scan_insn`.
>
> You need not define this macro if you did not define
> `DELAY_SLOTS_FOR_EPILOGUE`.

— Target Hook: void __TARGET_ASM_OUTPUT_MI_THUNK__ (FILE \*file, tree thunk_fndecl, HOST_WIDE_INT delta, HOST_WIDE_INT vcall_offset, tree function)
> A function that outputs the assembler code for a thunk
> function, used to implement C++ virtual function calls with multiple
> inheritance. The thunk acts as a wrapper around a virtual function,
> adjusting the implicit object parameter before handing control off to
> the real function.
>
> First, emit code to add the integer delta to the location that
> contains the incoming first argument. Assume that this argument
> contains a pointer, and is the one used to pass the `this` pointer
> in C++. This is the incoming argument _before_ the function prologue,
> e.g. ``%o0`' on a sparc. The addition must preserve the values of
> all other incoming arguments.
>
> Then, if vcall_offset is nonzero, an additional adjustment should be
> made after adding `delta`. In particular, if p is the
> adjusted pointer, the following adjustment should be made:
>
> ```
>           p += (*((ptrdiff_t **)p))[vcall_offset/sizeof(ptrdiff_t)]
>
> ```
>
> After the additions, emit code to jump to function, which is a
> `FUNCTION_DECL`. This is a direct pure jump, not a call, and does
> not touch the return address. Hence returning from FUNCTION will
> return to whoever called the current ``thunk`'.
>
> The effect must be as if function had been called directly with
> the adjusted first argument. This macro is responsible for emitting all
> of the code for a thunk function; `TARGET_ASM_FUNCTION_PROLOGUE`
> and `TARGET_ASM_FUNCTION_EPILOGUE` are not invoked.
>
> The thunk_fndecl is redundant. (delta and function
> have already been extracted from it.) It might possibly be useful on
> some targets, but probably not.
>
> If you do not define this macro, the target-independent code in the C++
> front end will generate a less efficient heavyweight thunk that calls
> function instead of jumping to it. The generic approach does
> not support varargs.

— Target Hook: bool __TARGET_ASM_CAN_OUTPUT_MI_THUNK__ (tree thunk_fndecl, HOST_WIDE_INT delta, HOST_WIDE_INT vcall_offset, tree function)
> A function that returns true if TARGET_ASM_OUTPUT_MI_THUNK would be able
> to output the assembler code for the thunk function specified by the
> arguments it is passed, and false otherwise. In the latter case, the
> generic approach will be used by the C++ front end, with the limitations
> previously exposed.
