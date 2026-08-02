---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Insn-Attributes.html
archived_at: '2026-07-15T07:31:00.072569Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Conditional Execution](Conditional-Execution.md#apple-inxw4zdjoruw63tbnqwuk6dfmn2xi2lpny),
Previous: [Peephole Definitions](Peephole-Definitions.md#apple-kbswk4din5wgklkemvtgs3tjoruw63tt),
Up: [Machine Desc](Machine-Desc.md#apple-jvqwg2djnzss2rdfonrq)

---

### 12.19 Instruction Attributes

In addition to describing the instruction supported by the target machine,
the `md` file also defines a group of attributes and a set of
values for each. Every generated insn is assigned a value for each attribute.
One possible attribute would be the effect that the insn has on the machine's
condition code. This attribute can then be used by `NOTICE_UPDATE_CC`
to track the condition codes.

- [Defining Attributes](Defining-Attributes.md#apple-irswm2lonfxgolkbor2he2lcov2gk4y): Specifying attributes and their values.
- [Expressions](Expressions.md#apple-iv4ha4tfonzws33oom): Valid expressions for attribute values.
- [Tagging Insns](Tagging-Insns.md#apple-krqwoz3jnzts2sloonxhg): Assigning attribute values to insns.
- [Attr Example](Attr-Example.md#apple-if2hi4rniv4gc3lqnrsq): An example of assigning attributes.
- [Insn Lengths](Insn-Lengths.md#apple-jfxhg3rnjrsw4z3unbzq): Computing the length of insns.
- [Constant Attributes](Constant-Attributes.md#apple-inxw443umfxhilkbor2he2lcov2gk4y): Defining attributes that are constant.
- [Delay Slots](Delay-Slots.md#apple-irswyylzfvjwy33uom): Defining delay slots required for a machine.
- [Processor pipeline description](Processor-pipeline-description.md#apple-kbzg6y3fonzw64rnobuxazlmnfxgkllemvzwg4tjob2gs33o): Specifying information for insn scheduling.
