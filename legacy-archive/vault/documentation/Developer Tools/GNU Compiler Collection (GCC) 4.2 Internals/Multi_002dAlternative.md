---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Multi_002dAlternative.html
archived_at: '2026-07-15T07:31:02.420547Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Class Preferences](Class-Preferences.md#apple-inwgc43tfvihezlgmvzgk3tdmvzq),
Previous: [Simple Constraints](Simple-Constraints.md#apple-knuw24dmmuwug33oon2heyljnz2hg),
Up: [Constraints](Constraints.md#apple-inxw443uojqws3tuom)

---

#### 14.8.2 Multiple Alternative Constraints

Sometimes a single instruction has multiple alternative sets of possible
operands. For example, on the 68000, a logical-or instruction can combine
register or an immediate value into memory, or it can combine any kind of
operand into a register; but it cannot combine one memory location into
another.

These constraints are represented as multiple alternatives. An alternative
can be described by a series of letters for each operand. The overall
constraint for an operand is made from the letters for this operand
from the first alternative, a comma, the letters for this operand from
the second alternative, a comma, and so on until the last alternative.
Here is how it is done for fullword logical-or on the 68000:

```
     (define_insn "iorsi3"
       [(set (match_operand:SI 0 "general_operand" "=m,d")
             (ior:SI (match_operand:SI 1 "general_operand" "%0,0")
                     (match_operand:SI 2 "general_operand" "dKs,dmKs")))]
       ...)
```

The first alternative has ``m`' (memory) for operand 0, ``0`' for
operand 1 (meaning it must match operand 0), and ``dKs`' for operand
2. The second alternative has ``d`' (data register) for operand 0,
``0`' for operand 1, and ``dmKs`' for operand 2. The ``=`' and
``%`' in the constraints apply to all the alternatives; their
meaning is explained in the next section (see [Class Preferences](Class-Preferences.md#apple-inwgc43tfvihezlgmvzgk3tdmvzq)).

If all the operands fit any one alternative, the instruction is valid.
Otherwise, for each alternative, the compiler counts how many instructions
must be added to copy the operands so that that alternative applies.
The alternative requiring the least copying is chosen. If two alternatives
need the same amount of copying, the one that comes first is chosen.
These choices can be altered with the ``?`' and ``!`' characters:

**`?`**
: Disparage slightly the alternative that the ``?`' appears in,
as a choice when no alternative applies exactly. The compiler regards
this alternative as one unit more costly for each ``?`' that appears
in it.

**`!`**
: Disparage severely the alternative that the ``!`' appears in.
This alternative can still be used if it fits without reloading,
but if reloading is needed, some other alternative will be used.

When an insn pattern has multiple alternatives in its constraints, often
the appearance of the assembler code is determined mostly by which
alternative was matched. When this is so, the C code for writing the
assembler code can use the variable `which_alternative`, which is
the ordinal number of the alternative that was actually satisfied (0 for
the first, 1 for the second alternative, etc.). See [Output Statement](Output-Statement.md#apple-j52xi4dvoqwvg5dborsw2zlooq).
