---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Assembler-Format.html
archived_at: '2026-07-15T07:31:01.219285Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Debugging Info](Debugging-Info.md#apple-irswe5lhm5uw4zznjfxgm3y),
Previous: [PIC](PIC.md#apple-kbeug),
Up: [Target Macros](Target-Macros.md#apple-krqxez3foqwu2yldojxxg)

---

### 15.21 Defining the Output Assembler Language

This section describes macros whose principal purpose is to describe how
to write instructions in assembler language—rather than what the
instructions do.

- [File Framework](File-Framework.md#apple-izuwyzjnizzgc3lfo5xxe2y): Structural information for the assembler file.
- [Data Output](Data-Output.md#apple-irqxiyjnj52xi4dvoq): Output of constants (numbers, strings, addresses).
- [Uninitialized Data](Uninitialized-Data.md#apple-kvxgs3tjoruwc3djpjswilkemf2gc): Output of uninitialized variables.
- [Label Output](Label-Output.md#apple-jrqwezlmfvhxk5dqov2a): Output and generation of labels.
- [Initialization](Initialization.md#apple-jfxgs5djmfwgs6tboruw63q): General principles of initialization
  and termination routines.
- [Macros for Initialization](Macros-for-Initialization.md#apple-jvqwg4tpomwwm33sfvew42lunfqwy2l2mf2gs33o)
  Specific macros that control the handling of
  initialization and termination routines.
- [Instruction Output](Instruction-Output.md#apple-jfxhg5dsovrxi2lpnywu65luob2xi): Output of actual instructions.
- [Dispatch Tables](Dispatch-Tables.md#apple-iruxg4dborrwqlkumfrgyzlt): Output of jump tables.
- [Exception Region Output](Exception-Region-Output.md#apple-iv4ggzlqoruw63rnkjswo2lpnywu65luob2xi): Output of exception region code.
- [Alignment Output](Alignment-Output.md#apple-ifwgsz3onvsw45bnj52xi4dvoq): Pseudo ops for alignment and skipping data.
