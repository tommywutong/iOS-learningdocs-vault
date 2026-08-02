---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Example.html
archived_at: '2026-07-15T07:31:01.777746Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [RTL Template](RTL-Template.md#apple-kjkeylkumvwxa3dborsq),
Previous: [Patterns](Patterns.md#apple-kbqxi5dfojxhg),
Up: [Machine Desc](Machine-Desc.md#apple-jvqwg2djnzss2rdfonrq)

---

### 14.3 Example of `define_insn`

Here is an actual example of an instruction pattern, for the 68000/68020.

```
     (define_insn "tstsi"
       [(set (cc0)
             (match_operand:SI 0 "general_operand" "rm"))]
       ""
       "*
     {
       if (TARGET_68020 || ! ADDRESS_REG_P (operands[0]))
         return \"tstl %0\";
       return \"cmpl #0,%0\";
     }")
```

This can also be written using braced strings:

```
     (define_insn "tstsi"
       [(set (cc0)
             (match_operand:SI 0 "general_operand" "rm"))]
       ""
     {
       if (TARGET_68020 || ! ADDRESS_REG_P (operands[0]))
         return "tstl %0";
       return "cmpl #0,%0";
     })
```

This is an instruction that sets the condition codes based on the value of
a general operand. It has no condition, so any insn whose RTL description
has the form shown may be handled according to this pattern. The name
``tstsi`' means “test a `SImode` value” and tells the RTL generation
pass that, when it is necessary to test such a value, an insn to do so
can be constructed using this pattern.

The output control string is a piece of C code which chooses which
output template to return based on the kind of operand and the specific
type of CPU for which code is being generated.

``"rm"`' is an operand constraint. Its meaning is explained below.
