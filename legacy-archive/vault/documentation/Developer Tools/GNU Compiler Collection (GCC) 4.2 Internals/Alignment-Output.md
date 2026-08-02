---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Alignment-Output.html
archived_at: '2026-07-15T07:31:01.177862Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Previous: [Exception Region Output](Exception-Region-Output.md#apple-iv4ggzlqoruw63rnkjswo2lpnywu65luob2xi),
Up: [Assembler Format](Assembler-Format.md#apple-ifzxgzlnmjwgk4rnizxxe3lboq)

---

#### 15.21.10 Assembler Commands for Alignment

This describes commands for alignment.

— Macro: __JUMP_ALIGN__ (label)
> The alignment (log base 2) to put in front of label, which is
> a common destination of jumps and has no fallthru incoming edge.
>
> This macro need not be defined if you don't want any special alignment
> to be done at such a time. Most machine descriptions do not currently
> define the macro.
>
> Unless it's necessary to inspect the label parameter, it is better
> to set the variable align_jumps in the target's
> `OVERRIDE_OPTIONS`. Otherwise, you should try to honor the user's
> selection in align_jumps in a `JUMP_ALIGN` implementation.

— Macro: __LABEL_ALIGN_AFTER_BARRIER__ (label)
> The alignment (log base 2) to put in front of label, which follows
> a `BARRIER`.
>
> This macro need not be defined if you don't want any special alignment
> to be done at such a time. Most machine descriptions do not currently
> define the macro.

— Macro: __LABEL_ALIGN_AFTER_BARRIER_MAX_SKIP__
> The maximum number of bytes to skip when applying
> `LABEL_ALIGN_AFTER_BARRIER`. This works only if
> `ASM_OUTPUT_MAX_SKIP_ALIGN` is defined.

— Macro: __LOOP_ALIGN__ (label)
> The alignment (log base 2) to put in front of label, which follows
> a `NOTE_INSN_LOOP_BEG` note.
>
> This macro need not be defined if you don't want any special alignment
> to be done at such a time. Most machine descriptions do not currently
> define the macro.
>
> Unless it's necessary to inspect the label parameter, it is better
> to set the variable `align_loops` in the target's
> `OVERRIDE_OPTIONS`. Otherwise, you should try to honor the user's
> selection in `align_loops` in a `LOOP_ALIGN` implementation.

— Macro: __LOOP_ALIGN_MAX_SKIP__
> The maximum number of bytes to skip when applying `LOOP_ALIGN`.
> This works only if `ASM_OUTPUT_MAX_SKIP_ALIGN` is defined.

— Macro: __LABEL_ALIGN__ (label)
> The alignment (log base 2) to put in front of label.
> If `LABEL_ALIGN_AFTER_BARRIER` / `LOOP_ALIGN` specify a different alignment,
> the maximum of the specified values is used.
>
> Unless it's necessary to inspect the label parameter, it is better
> to set the variable `align_labels` in the target's
> `OVERRIDE_OPTIONS`. Otherwise, you should try to honor the user's
> selection in `align_labels` in a `LABEL_ALIGN` implementation.

— Macro: __LABEL_ALIGN_MAX_SKIP__
> The maximum number of bytes to skip when applying `LABEL_ALIGN`.
> This works only if `ASM_OUTPUT_MAX_SKIP_ALIGN` is defined.

— Macro: __ASM_OUTPUT_SKIP__ (stream, nbytes)
> A C statement to output to the stdio stream stream an assembler
> instruction to advance the location counter by nbytes bytes.
> Those bytes should be zero when loaded. nbytes will be a C
> expression of type `int`.

— Macro: __ASM_NO_SKIP_IN_TEXT__
> Define this macro if `ASM_OUTPUT_SKIP` should not be used in the
> text section because it fails to put zeros in the bytes that are skipped.
> This is true on many Unix systems, where the pseudo–op to skip bytes
> produces no-op instructions rather than zeros when used in the text
> section.

— Macro: __ASM_OUTPUT_ALIGN__ (stream, power)
> A C statement to output to the stdio stream stream an assembler
> command to advance the location counter to a multiple of 2 to the
> power bytes. power will be a C expression of type `int`.

— Macro: __ASM_OUTPUT_ALIGN_WITH_NOP__ (stream, power)
> Like `ASM_OUTPUT_ALIGN`, except that the “nop” instruction is used
> for padding, if necessary.

— Macro: __ASM_OUTPUT_MAX_SKIP_ALIGN__ (stream, power, max_skip)
> A C statement to output to the stdio stream stream an assembler
> command to advance the location counter to a multiple of 2 to the
> power bytes, but only if max_skip or fewer bytes are needed to
> satisfy the alignment request. power and max_skip will be
> a C expression of type `int`.
