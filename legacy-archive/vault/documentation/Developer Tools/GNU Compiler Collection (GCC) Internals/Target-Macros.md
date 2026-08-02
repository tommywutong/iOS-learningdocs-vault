---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Target-Macros.html
archived_at: '2026-07-15T07:31:00.882063Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Host Config](Host-Config.md#apple-jbxxg5bninxw4ztjm4),
Previous: [Machine Desc](Machine-Desc.md#apple-jvqwg2djnzss2rdfonrq),
Up: [Top](index.md#apple-krxxa)

---

## 13 Target Description Macros and Functions

In addition to the file `machine.md`, a machine description
includes a C header file conventionally given the name
`machine.h` and a C source file named `machine.c`.
The header file defines numerous macros that convey the information
about the target machine that does not fit into the scheme of the
`.md` file. The file `tm.h` should be a link to
`machine.h`. The header file `config.h` includes
`tm.h` and most compiler source files include `config.h`. The
source file defines a variable `targetm`, which is a structure
containing pointers to functions and data relating to the target
machine. `machine.c` should also contain their definitions,
if they are not defined elsewhere in GCC, and other functions called
through the macros defined in the `.h` file.

- [Target Structure](Target-Structure.md#apple-krqxez3foqwvg5dsovrxi5lsmu): The `targetm` variable.
- [Driver](Driver.md#apple-irzgs5tfoi): Controlling how the driver runs the compilation passes.
- [Run-time Target](Run_002dtime-Target.md#apple-kj2w4xzqgazgi5djnvss2vdbojtwk5a): Defining ``-m`' options like `-m68000` and `-m68020`.
- [Per-Function Data](Per_002dFunction-Data.md#apple-kbsxexzqgazgirtvnzrxi2lpnywuiylume): Defining data structures for per-function information.
- [Storage Layout](Storage-Layout.md#apple-kn2g64tbm5ss2tdbpfxxk5a): Defining sizes and alignments of data.
- [Type Layout](Type-Layout.md#apple-kr4xazjnjrqxs33voq): Defining sizes and properties of basic user data types.
- [Registers](Registers.md#apple-kjswo2ltorsxe4y): Naming and describing the hardware registers.
- [Register Classes](Register-Classes.md#apple-kjswo2ltorsxelkdnrqxg43fom): Defining the classes of hardware registers.
- [Stack and Calling](Stack-and-Calling.md#apple-kn2gcy3lfvqw4zbninqwy3djnztq): Defining which way the stack grows and by how much.
- [Varargs](Varargs.md#apple-kzqxeylsm5zq): Defining the varargs macros.
- [Trampolines](Trampolines.md#apple-krzgc3lqn5wgs3tfom): Code set up at run time to enter a nested function.
- [Library Calls](Library-Calls.md#apple-jruwe4tboj4s2q3bnrwhg): Controlling how library routines are implicitly called.
- [Addressing Modes](Addressing-Modes.md#apple-ifsgi4tfonzws3thfvgw6zdfom): Defining addressing modes valid for memory operands.
- [Condition Code](Condition-Code.md#apple-inxw4zdjoruw63rninxwizi): Defining how insns update the condition code.
- [Costs](Costs.md#apple-inxxg5dt): Defining relative costs of different operations.
- [Scheduling](Scheduling.md#apple-knrwqzleovwgs3th): Adjusting the behavior of the instruction scheduler.
- [Sections](Sections.md#apple-knswg5djn5xhg): Dividing storage into text, data, and other sections.
- [PIC](PIC.md#apple-kbeug): Macros for position independent code.
- [Assembler Format](Assembler-Format.md#apple-ifzxgzlnmjwgk4rnizxxe3lboq): Defining how to write insns and pseudo-ops to output.
- [Debugging Info](Debugging-Info.md#apple-irswe5lhm5uw4zznjfxgm3y): Defining the format of debugging output.
- [Floating Point](Floating-Point.md#apple-izwg6ylunfxgolkqn5uw45a): Handling floating point for cross-compilers.
- [Mode Switching](Mode-Switching.md#apple-jvxwizjnkn3ws5ddnbuw4zy): Insertion of mode-switching instructions.
- [Target Attributes](Target-Attributes.md#apple-krqxez3foqwuc5duojuwe5lumvzq): Defining target-specific uses of `__attribute__`.
- [MIPS Coprocessors](MIPS-Coprocessors.md#apple-jvevauzninxxa4tpmnsxg43pojzq): MIPS coprocessor support and how to customize it.
- [PCH Target](PCH-Target.md#apple-kbbuqlkumfzgozlu): Validity checking for precompiled headers.
- [C++ ABI](C_002b_002b-ABI.md#apple-inptambsmjptambsmiwucqsj): Controlling C++ ABI changes.
- [Misc](Misc.md#apple-jvuxgyy): Everything else.
