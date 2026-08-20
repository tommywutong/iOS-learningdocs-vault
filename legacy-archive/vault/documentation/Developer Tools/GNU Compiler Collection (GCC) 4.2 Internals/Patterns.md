---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Patterns.html
archived_at: '2026-07-15T07:31:02.583855Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Example](Example.md#apple-iv4gc3lqnrsq),
Previous: [Overview](Overview.md#apple-j53gk4twnfsxo),
Up: [Machine Desc](Machine-Desc.md#apple-jvqwg2djnzss2rdfonrq)

---

### 14.2 Everything about Instruction Patterns

Each instruction pattern contains an incomplete RTL expression, with pieces
to be filled in later, operand constraints that restrict how the pieces can
be filled in, and an output pattern or C code to generate the assembler
output, all wrapped up in a `define_insn` expression.

A `define_insn` is an RTL expression containing four or five operands:

1. An optional name. The presence of a name indicate that this instruction
   pattern can perform a certain standard job for the RTL-generation
   pass of the compiler. This pass knows certain names and will use
   the instruction patterns with those names, if the names are defined
   in the machine description.

   The absence of a name is indicated by writing an empty string
   where the name should go. Nameless instruction patterns are never
   used for generating RTL code, but they may permit several simpler insns
   to be combined later on.

   Names that are not thus known and used in RTL-generation have no
   effect; they are equivalent to no name at all.

   For the purpose of debugging the compiler, you may also specify a
   name beginning with the ``*`' character. Such a name is used only
   for identifying the instruction in RTL dumps; it is entirely equivalent
   to having a nameless pattern for all other purposes.
2. The RTL template (see [RTL Template](RTL-Template.md#apple-kjkeylkumvwxa3dborsq)) is a vector of incomplete
   RTL expressions which show what the instruction should look like. It is
   incomplete because it may contain `match_operand`,
   `match_operator`, and `match_dup` expressions that stand for
   operands of the instruction.

   If the vector has only one element, that element is the template for the
   instruction pattern. If the vector has multiple elements, then the
   instruction pattern is a `parallel` expression containing the
   elements described.
3. A condition. This is a string which contains a C expression that is
   the final test to decide whether an insn body matches this pattern.

   For a named pattern, the condition (if present) may not depend on
   the data in the insn being matched, but only the target-machine-type
   flags. The compiler needs to test these conditions during
   initialization in order to learn exactly which named instructions are
   available in a particular run.

   For nameless patterns, the condition is applied only when matching an
   individual insn, and only after the insn has matched the pattern's
   recognition template. The insn's operands may be found in the vector
   `operands`. For an insn where the condition has once matched, it
   can't be used to control register allocation, for example by excluding
   certain hard registers or hard register combinations.
4. The output template: a string that says how to output matching
   insns as assembler code. ``%`' in this string specifies where
   to substitute the value of an operand. See [Output Template](Output-Template.md#apple-j52xi4dvoqwvizlnobwgc5df).

   When simple substitution isn't general enough, you can specify a piece
   of C code to compute the output. See [Output Statement](Output-Statement.md#apple-j52xi4dvoqwvg5dborsw2zlooq).
5. Optionally, a vector containing the values of attributes for insns matching
   this pattern. See [Insn Attributes](Insn-Attributes.md#apple-jfxhg3rnif2hi4tjmj2xizlt).
