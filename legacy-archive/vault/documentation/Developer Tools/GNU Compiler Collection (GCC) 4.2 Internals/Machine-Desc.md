---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Machine-Desc.html
archived_at: '2026-07-15T07:31:02.301793Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Target Macros](Target-Macros.md#apple-krqxez3foqwu2yldojxxg),
Previous: [Loop Analysis and Representation](Loop-Analysis-and-Representation.md#apple-jrxw64bnifxgc3dzonuxgllbnzsc2utfobzgk43fnz2gc5djn5xa),
Up: [Top](index.md#apple-krxxa)

---

## 14 Machine Descriptions

A machine description has two parts: a file of instruction patterns
(`.md` file) and a C header file of macro definitions.

The `.md` file for a target machine contains a pattern for each
instruction that the target machine supports (or at least each instruction
that is worth telling the compiler about). It may also contain comments.
A semicolon causes the rest of the line to be a comment, unless the semicolon
is inside a quoted string.

See the next chapter for information on the C header file.

- [Overview](Overview.md#apple-j53gk4twnfsxo): How the machine description is used.
- [Patterns](Patterns.md#apple-kbqxi5dfojxhg): How to write instruction patterns.
- [Example](Example.md#apple-iv4gc3lqnrsq): An explained example of a `define_insn` pattern.
- [RTL Template](RTL-Template.md#apple-kjkeylkumvwxa3dborsq): The RTL template defines what insns match a pattern.
- [Output Template](Output-Template.md#apple-j52xi4dvoqwvizlnobwgc5df): The output template says how to make assembler code
  from such an insn.
- [Output Statement](Output-Statement.md#apple-j52xi4dvoqwvg5dborsw2zlooq): For more generality, write C code to output
  the assembler code.
- [Predicates](Predicates.md#apple-kbzgkzdjmnqxizlt): Controlling what kinds of operands can be used
  for an insn.
- [Constraints](Constraints.md#apple-inxw443uojqws3tuom): Fine-tuning operand selection.
- [Standard Names](Standard-Names.md#apple-kn2gc3temfzgilkomfwwk4y): Names mark patterns to use for code generation.
- [Pattern Ordering](Pattern-Ordering.md#apple-kbqxi5dfojxc2t3smrsxe2lom4): When the order of patterns makes a difference.
- [Dependent Patterns](Dependent-Patterns.md#apple-irsxazlomrsw45bnkbqxi5dfojxhg): Having one pattern may make you need another.
- [Jump Patterns](Jump-Patterns.md#apple-jj2w24bnkbqxi5dfojxhg): Special considerations for patterns for jump insns.
- [Looping Patterns](Looping-Patterns.md#apple-jrxw64djnzts2udbor2gk4toom): How to define patterns for special looping insns.
- [Insn Canonicalizations](Insn-Canonicalizations.md#apple-jfxhg3rninqw433onfrwc3djpjqxi2lpnzzq): Canonicalization of Instructions
- [Expander Definitions](Expander-Definitions.md#apple-iv4haylomrsxelkemvtgs3tjoruw63tt): Generating a sequence of several RTL insns
  for a standard operation.
- [Insn Splitting](Insn-Splitting.md#apple-jfxhg3rnknygy2luoruw4zy): Splitting Instructions into Multiple Instructions.
- [Including Patterns](Including-Patterns.md#apple-jfxgg3dvmruw4zznkbqxi5dfojxhg): Including Patterns in Machine Descriptions.
- [Peephole Definitions](Peephole-Definitions.md#apple-kbswk4din5wgklkemvtgs3tjoruw63tt): Defining machine-specific peephole optimizations.
- [Insn Attributes](Insn-Attributes.md#apple-jfxhg3rnif2hi4tjmj2xizlt): Specifying the value of attributes for generated insns.
- [Conditional Execution](Conditional-Execution.md#apple-inxw4zdjoruw63tbnqwuk6dfmn2xi2lpny): Generating `define_insn` patterns for
  predication.
- [Constant Definitions](Constant-Definitions.md#apple-inxw443umfxhilkemvtgs3tjoruw63tt): Defining symbolic constants that can be used in the
  md file.
- [Macros](Macros.md#apple-jvqwg4tpom): Using macros to generate patterns from a template.
