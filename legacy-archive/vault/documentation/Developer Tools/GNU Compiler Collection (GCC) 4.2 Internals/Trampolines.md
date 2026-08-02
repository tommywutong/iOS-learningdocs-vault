---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Trampolines.html
archived_at: '2026-07-15T07:31:03.014985Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Library Calls](Library-Calls.md#apple-jruwe4tboj4s2q3bnrwhg),
Previous: [Varargs](Varargs.md#apple-kzqxeylsm5zq),
Up: [Target Macros](Target-Macros.md#apple-krqxez3foqwu2yldojxxg)

---

### 15.12 Trampolines for Nested Functions

A trampoline is a small piece of code that is created at run time
when the address of a nested function is taken. It normally resides on
the stack, in the stack frame of the containing function. These macros
tell GCC how to generate code to allocate and initialize a
trampoline.

The instructions in the trampoline must do two things: load a constant
address into the static chain register, and jump to the real address of
the nested function. On CISC machines such as the m68k, this requires
two instructions, a move immediate and a jump. Then the two addresses
exist in the trampoline as word-long immediate operands. On RISC
machines, it is often necessary to load each address into a register in
two parts. Then pieces of each address form separate immediate
operands.

The code generated to initialize the trampoline must store the variable
parts—the static chain value and the function address—into the
immediate operands of the instructions. On a CISC machine, this is
simply a matter of copying each address to a memory reference at the
proper offset from the start of the trampoline. On a RISC machine, it
may be necessary to take out pieces of the address and store them
separately.

— Macro: __TRAMPOLINE_TEMPLATE__ (file)
> A C statement to output, on the stream file, assembler code for a
> block of data that contains the constant parts of a trampoline. This
> code should not include a label—the label is taken care of
> automatically.
>
> If you do not define this macro, it means no template is needed
> for the target. Do not define this macro on systems where the block move
> code to copy the trampoline into place would be larger than the code
> to generate it on the spot.

— Macro: __TRAMPOLINE_SECTION__
> Return the section into which the trampoline template is to be placed
> (see [Sections](Sections.md#apple-knswg5djn5xhg)). The default value is `readonly_data_section`.

— Macro: __TRAMPOLINE_SIZE__
> A C expression for the size in bytes of the trampoline, as an integer.

— Macro: __TRAMPOLINE_ALIGNMENT__
> Alignment required for trampolines, in bits.
>
> If you don't define this macro, the value of `BIGGEST_ALIGNMENT`
> is used for aligning trampolines.

— Macro: __INITIALIZE_TRAMPOLINE__ (addr, fnaddr, static_chain)
> A C statement to initialize the variable parts of a trampoline.
> addr is an RTX for the address of the trampoline; fnaddr is
> an RTX for the address of the nested function; static_chain is an
> RTX for the static chain value that should be passed to the function
> when it is called.

— Macro: __TRAMPOLINE_ADJUST_ADDRESS__ (addr)
> A C statement that should perform any machine-specific adjustment in
> the address of the trampoline. Its argument contains the address that
> was passed to `INITIALIZE_TRAMPOLINE`. In case the address to be
> used for a function call should be different from the address in which
> the template was stored, the different address should be assigned to
> addr. If this macro is not defined, addr will be used for
> function calls.
>
> If this macro is not defined, by default the trampoline is allocated as
> a stack slot. This default is right for most machines. The exceptions
> are machines where it is impossible to execute instructions in the stack
> area. On such machines, you may have to implement a separate stack,
> using this macro in conjunction with `TARGET_ASM_FUNCTION_PROLOGUE`
> and `TARGET_ASM_FUNCTION_EPILOGUE`.
>
> fp points to a data structure, a `struct function`, which
> describes the compilation status of the immediate containing function of
> the function which the trampoline is for. The stack slot for the
> trampoline is in the stack frame of this containing function. Other
> allocation strategies probably must do something analogous with this
> information.

Implementing trampolines is difficult on many machines because they have
separate instruction and data caches. Writing into a stack location
fails to clear the memory in the instruction cache, so when the program
jumps to that location, it executes the old contents.

Here are two possible solutions. One is to clear the relevant parts of
the instruction cache whenever a trampoline is set up. The other is to
make all trampolines identical, by having them jump to a standard
subroutine. The former technique makes trampoline execution faster; the
latter makes initialization faster.

To clear the instruction cache when a trampoline is initialized, define
the following macro.

— Macro: __CLEAR_INSN_CACHE__ (beg, end)
> If defined, expands to a C expression clearing the _instruction
> cache_ in the specified interval. The definition of this macro would
> typically be a series of `asm` statements. Both beg and
> end are both pointer expressions.

The operating system may also require the stack to be made executable
before calling the trampoline. To implement this requirement, define
the following macro.

— Macro: __ENABLE_EXECUTE_STACK__
> Define this macro if certain operations must be performed before executing
> code located on the stack. The macro should expand to a series of C
> file-scope constructs (e.g. functions) and provide a unique entry point
> named `__enable_execute_stack`. The target is responsible for
> emitting calls to the entry point in the code, for example from the
> `INITIALIZE_TRAMPOLINE` macro.

To use a standard subroutine, define the following macro. In addition,
you must make sure that the instructions in a trampoline fill an entire
cache line with identical instructions, or else ensure that the
beginning of the trampoline code is always aligned at the same point in
its cache line. Look in `m68k.h` as a guide.

— Macro: __TRANSFER_FROM_TRAMPOLINE__
> Define this macro if trampolines need a special subroutine to do their
> work. The macro should expand to a series of `asm` statements
> which will be compiled with GCC. They go in a library function named
> `__transfer_from_trampoline`.
>
> If you need to avoid executing the ordinary prologue code of a compiled
> C function when you jump to the subroutine, you can do so by placing a
> special label of your own in the assembler code. Use one `asm`
> statement to generate an assembler label, and another to make the label
> global. Then trampolines can use that label to jump directly to your
> special assembler code.
