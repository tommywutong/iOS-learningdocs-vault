---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Dispatch-Tables.html
archived_at: '2026-07-15T07:31:01.734113Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Exception Region Output](Exception-Region-Output.md#apple-iv4ggzlqoruw63rnkjswo2lpnywu65luob2xi),
Previous: [Instruction Output](Instruction-Output.md#apple-jfxhg5dsovrxi2lpnywu65luob2xi),
Up: [Assembler Format](Assembler-Format.md#apple-ifzxgzlnmjwgk4rnizxxe3lboq)

---

#### 15.21.8 Output of Dispatch Tables

This concerns dispatch tables.

— Macro: __ASM_OUTPUT_ADDR_DIFF_ELT__ (stream, body, value, rel)
> A C statement to output to the stdio stream stream an assembler
> pseudo-instruction to generate a difference between two labels.
> value and rel are the numbers of two internal labels. The
> definitions of these labels are output using
> `(*targetm.asm_out.internal_label)`, and they must be printed in the same
> way here. For example,
>
> ```
>           fprintf (stream, "\t.word L%d-L%d\n",
>                    value, rel)
>
> ```
>
> You must provide this macro on machines where the addresses in a
> dispatch table are relative to the table's own address. If defined, GCC
> will also use this macro on all machines when producing PIC.
> body is the body of the `ADDR_DIFF_VEC`; it is provided so that the
> mode and flags can be read.

— Macro: __ASM_OUTPUT_ADDR_VEC_ELT__ (stream, value)
> This macro should be provided on machines where the addresses
> in a dispatch table are absolute.
>
> The definition should be a C statement to output to the stdio stream
> stream an assembler pseudo-instruction to generate a reference to
> a label. value is the number of an internal label whose
> definition is output using `(*targetm.asm_out.internal_label)`.
> For example,
>
> ```
>           fprintf (stream, "\t.word L%d\n", value)
>
> ```

— Macro: __ASM_OUTPUT_CASE_LABEL__ (stream, prefix, num, table)
> Define this if the label before a jump-table needs to be output
> specially. The first three arguments are the same as for
> `(*targetm.asm_out.internal_label)`; the fourth argument is the
> jump-table which follows (a `jump_insn` containing an
> `addr_vec` or `addr_diff_vec`).
>
> This feature is used on system V to output a `swbeg` statement
> for the table.
>
> If this macro is not defined, these labels are output with
> `(*targetm.asm_out.internal_label)`.

— Macro: __ASM_OUTPUT_CASE_END__ (stream, num, table)
> Define this if something special must be output at the end of a
> jump-table. The definition should be a C statement to be executed
> after the assembler code for the table is written. It should write
> the appropriate code to stdio stream stream. The argument
> table is the jump-table insn, and num is the label-number
> of the preceding label.
>
> If this macro is not defined, nothing special is output at the end of
> the jump-table.

— Target Hook: void __TARGET_ASM_EMIT_UNWIND_LABEL__ (stream, decl, for_eh, empty)
> This target hook emits a label at the beginning of each FDE. It
> should be defined on targets where FDEs need special labels, and it
> should write the appropriate label, for the FDE associated with the
> function declaration decl, to the stdio stream stream.
> The third argument, for_eh, is a boolean: true if this is for an
> exception table. The fourth argument, empty, is a boolean:
> true if this is a placeholder label for an omitted FDE.
>
> The default is that FDEs are not given nonlocal labels.

— Target Hook: void __TARGET_ASM_EMIT_EXCEPT_TABLE_LABEL__ (stream)
> This target hook emits a label at the beginning of the exception table.
> It should be defined on targets where it is desirable for the table
> to be broken up according to function.
>
> The default is that no label is emitted.

— Target Hook: void __TARGET_UNWIND_EMIT__ (FILE \* stream, rtx insn)
> This target hook emits and assembly directives required to unwind the
> given instruction. This is only used when TARGET_UNWIND_INFO is set.
