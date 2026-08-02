---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Instruction-Output.html
archived_at: '2026-07-15T07:31:00.111899Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Dispatch Tables](Dispatch-Tables.md#apple-iruxg4dborrwqlkumfrgyzlt),
Previous: [Macros for Initialization](Macros-for-Initialization.md#apple-jvqwg4tpomwwm33sfvew42lunfqwy2l2mf2gs33o),
Up: [Assembler Format](Assembler-Format.md#apple-ifzxgzlnmjwgk4rnizxxe3lboq)

---

#### 13.19.7 Output of Assembler Instructions

This describes assembler instruction output.

— Macro: __REGISTER_NAMES__
> A C initializer containing the assembler's names for the machine
> registers, each one as a C string constant. This is what translates
> register numbers in the compiler into assembler language.

— Macro: __ADDITIONAL_REGISTER_NAMES__
> If defined, a C initializer for an array of structures containing a name
> and a register number. This macro defines additional names for hard
> registers, thus allowing the `asm` option in declarations to refer
> to registers using alternate names.

— Macro: __ASM_OUTPUT_OPCODE__ (stream, ptr)
> Define this macro if you are using an unusual assembler that
> requires different names for the machine instructions.
>
> The definition is a C statement or statements which output an
> assembler instruction opcode to the stdio stream stream. The
> macro-operand ptr is a variable of type `char *` which
> points to the opcode name in its “internal” form—the form that is
> written in the machine description. The definition should output the
> opcode name to stream, performing any translation you desire, and
> increment the variable ptr to point at the end of the opcode
> so that it will not be output twice.
>
> In fact, your macro definition may process less than the entire opcode
> name, or more than the opcode name; but if you want to process text
> that includes ``%`'-sequences to substitute operands, you must take
> care of the substitution yourself. Just be sure to increment
> ptr over whatever text should not be output normally.
>
> If you need to look at the operand values, they can be found as the
> elements of `recog_data.operand`.
>
> If the macro definition does nothing, the instruction is output
> in the usual way.

— Macro: __FINAL_PRESCAN_INSN__ (insn, opvec, noperands)
> If defined, a C statement to be executed just prior to the output of
> assembler code for insn, to modify the extracted operands so
> they will be output differently.
>
> Here the argument opvec is the vector containing the operands
> extracted from insn, and noperands is the number of
> elements of the vector which contain meaningful data for this insn.
> The contents of this vector are what will be used to convert the insn
> template into assembler code, so you can change the assembler output
> by changing the contents of the vector.
>
> This macro is useful when various assembler syntaxes share a single
> file of instruction patterns; by defining this macro differently, you
> can cause a large class of instructions to be output differently (such
> as with rearranged operands). Naturally, variations in assembler
> syntax affecting individual insn patterns ought to be handled by
> writing conditional output routines in those patterns.
>
> If this macro is not defined, it is equivalent to a null statement.

— Macro: __PRINT_OPERAND__ (stream, x, code)
> A C compound statement to output to stdio stream stream the
> assembler syntax for an instruction operand x. x is an
> RTL expression.
>
> code is a value that can be used to specify one of several ways
> of printing the operand. It is used when identical operands must be
> printed differently depending on the context. code comes from
> the ``%`' specification that was used to request printing of the
> operand. If the specification was just ``%digit`' then
> code is 0; if the specification was ``%ltr
> digit`' then code is the ASCII code for ltr.
>
> If x is a register, this macro should print the register's name.
> The names can be found in an array `reg_names` whose type is
> `char *[]`. `reg_names` is initialized from
> `REGISTER_NAMES`.
>
> When the machine description has a specification ``%punct`'
> (a ``%`' followed by a punctuation character), this macro is called
> with a null pointer for x and the punctuation character for
> code.

— Macro: __PRINT_OPERAND_PUNCT_VALID_P__ (code)
> A C expression which evaluates to true if code is a valid
> punctuation character for use in the `PRINT_OPERAND` macro. If
> `PRINT_OPERAND_PUNCT_VALID_P` is not defined, it means that no
> punctuation characters (except for the standard one, ``%`') are used
> in this way.

— Macro: __PRINT_OPERAND_ADDRESS__ (stream, x)
> A C compound statement to output to stdio stream stream the
> assembler syntax for an instruction operand that is a memory reference
> whose address is x. x is an RTL expression.
>
> On some machines, the syntax for a symbolic address depends on the
> section that the address refers to. On these machines, define the hook
> `TARGET_ENCODE_SECTION_INFO` to store the information into the
> `symbol_ref`, and then check for it here. See [Assembler Format](Assembler-Format.md#apple-ifzxgzlnmjwgk4rnizxxe3lboq).

— Macro: __DBR_OUTPUT_SEQEND__ (file)
> A C statement, to be executed after all slot-filler instructions have
> been output. If necessary, call `dbr_sequence_length` to
> determine the number of slots filled in a sequence (zero if not
> currently outputting a sequence), to decide how many no-ops to output,
> or whatever.
>
> Don't define this macro if it has nothing to do, but it is helpful in
> reading assembly output if the extent of the delay sequence is made
> explicit (e.g. with white space).

Note that output routines for instructions with delay slots must be
prepared to deal with not being output as part of a sequence
(i.e. when the scheduling pass is not run, or when no slot fillers could be
found.) The variable `final_sequence` is null when not
processing a sequence, otherwise it contains the `sequence` rtx
being output.

— Macro: __REGISTER_PREFIX__
— Macro: __LOCAL_LABEL_PREFIX__
— Macro: __USER_LABEL_PREFIX__
— Macro: __IMMEDIATE_PREFIX__
> If defined, C string expressions to be used for the ``%R`', ``%L`',
> ``%U`', and ``%I`' options of `asm_fprintf` (see
> `final.c`). These are useful when a single `md` file must
> support multiple assembler formats. In that case, the various `tm.h`
> files can define these macros differently.

— Macro: __ASM_FPRINTF_EXTENSIONS__ (file, argptr, format)
> If defined this macro should expand to a series of `case`
> statements which will be parsed inside the `switch` statement of
> the `asm_fprintf` function. This allows targets to define extra
> printf formats which may useful when generating their assembler
> statements. Note that uppercase letters are reserved for future
> generic extensions to asm_fprintf, and so are not available to target
> specific code. The output file is given by the parameter file.
> The varargs input pointer is argptr and the rest of the format
> string, starting the character after the one that is being switched
> upon, is pointed to by format.

— Macro: __ASSEMBLER_DIALECT__
> If your target supports multiple dialects of assembler language (such as
> different opcodes), define this macro as a C expression that gives the
> numeric index of the assembler language dialect to use, with zero as the
> first variant.
>
> If this macro is defined, you may use constructs of the form
>
> ```
>           `{option0|option1|option2...}'
>
> ```
>
> in the output templates of patterns (see [Output Template](Output-Template.md#apple-j52xi4dvoqwvizlnobwgc5df)) or in the
> first argument of `asm_fprintf`. This construct outputs
> ``option0`', ``option1`', ``option2`', etc., if the value of
> `ASSEMBLER_DIALECT` is zero, one, two, etc. Any special characters
> within these strings retain their usual meaning. If there are fewer
> alternatives within the braces than the value of
> `ASSEMBLER_DIALECT`, the construct outputs nothing.
>
> If you do not define this macro, the characters ``{`', ``|`' and
> ``}`' do not have any special meaning when used in templates or
> operands to `asm_fprintf`.
>
> Define the macros `REGISTER_PREFIX`, `LOCAL_LABEL_PREFIX`,
> `USER_LABEL_PREFIX` and `IMMEDIATE_PREFIX` if you can express
> the variations in assembler language syntax with that mechanism. Define
> `ASSEMBLER_DIALECT` and use the ``{option0|option1}`' syntax
> if the syntax variant are larger and involve such things as different
> opcodes or operand order.

— Macro: __ASM_OUTPUT_REG_PUSH__ (stream, regno)
> A C expression to output to stream some assembler code
> which will push hard register number regno onto the stack.
> The code need not be optimal, since this macro is used only when
> profiling.

— Macro: __ASM_OUTPUT_REG_POP__ (stream, regno)
> A C expression to output to stream some assembler code
> which will pop hard register number regno off of the stack.
> The code need not be optimal, since this macro is used only when
> profiling.
