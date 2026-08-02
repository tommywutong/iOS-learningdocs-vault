---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Simple-Constraints.html
archived_at: '2026-07-15T07:31:02.799525Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Multi-Alternative](Multi_002dAlternative.md#apple-jv2wy5djl4ydamteifwhizlsnzqxi2lwmu),
Up: [Constraints](Constraints.md#apple-inxw443uojqws3tuom)

---

#### 14.8.1 Simple Constraints

The simplest kind of constraint is a string full of letters, each of
which describes one kind of operand that is permitted. Here are
the letters that are allowed:

**whitespace**
: Whitespace characters are ignored and can be inserted at any position
except the first. This enables each alternative for different operands to
be visually aligned in the machine description even if they have different
number of constraints and modifiers.

**``m`'**
: A memory operand is allowed, with any kind of address that the machine
supports in general.

**``o`'**
: A memory operand is allowed, but only if the address is
offsettable. This means that adding a small integer (actually,
the width in bytes of the operand, as determined by its machine mode)
may be added to the address and the result is also a valid memory
address.

For example, an address which is constant is offsettable; so is an
address that is the sum of a register and a constant (as long as a
slightly larger constant is also within the range of address-offsets
supported by the machine); but an autoincrement or autodecrement
address is not offsettable. More complicated indirect/indexed
addresses may or may not be offsettable depending on the other
addressing modes that the machine supports.

Note that in an output operand which can be matched by another
operand, the constraint letter ``o`' is valid only when accompanied
by both ``<`' (if the target machine has predecrement addressing)
and ``>`' (if the target machine has preincrement addressing).

**``V`'**
: A memory operand that is not offsettable. In other words, anything that
would fit the ``m`' constraint but not the ``o`' constraint.

**``<`'**
: A memory operand with autodecrement addressing (either predecrement or
postdecrement) is allowed.

**``>`'**
: A memory operand with autoincrement addressing (either preincrement or
postincrement) is allowed.

**``r`'**
: A register operand is allowed provided that it is in a general
register.

**``i`'**
: An immediate integer operand (one with constant value) is allowed.
This includes symbolic constants whose values will be known only at
assembly time or later.

**``n`'**
: An immediate integer operand with a known numeric value is allowed.
Many systems cannot support assembly-time constants for operands less
than a word wide. Constraints for these operands should use ``n`'
rather than ``i`'.

**``I`', ``J`', ``K`', ... ``P`'**
: Other letters in the range ``I`' through ``P`' may be defined in
a machine-dependent fashion to permit immediate integer operands with
explicit integer values in specified ranges. For example, on the
68000, ``I`' is defined to stand for the range of values 1 to 8.
This is the range permitted as a shift count in the shift
instructions.

**``E`'**
: An immediate floating operand (expression code `const_double`) is
allowed, but only if the target floating point format is the same as
that of the host machine (on which the compiler is running).

**``F`'**
: An immediate floating operand (expression code `const_double` or
`const_vector`) is allowed.

**``G`', ``H`'**
: ``G`' and ``H`' may be defined in a machine-dependent fashion to
permit immediate floating operands in particular ranges of values.

**``s`'**
: An immediate integer operand whose value is not an explicit integer is
allowed.

This might appear strange; if an insn allows a constant operand with a
value not known at compile time, it certainly must allow any known
value. So why use ``s`' instead of ``i`'? Sometimes it allows
better code to be generated.

For example, on the 68000 in a fullword instruction it is possible to
use an immediate operand; but if the immediate value is between −128
and 127, better code results from loading the value into a register and
using the register. This is because the load into the register can be
done with a ``moveq`' instruction. We arrange for this to happen
by defining the letter ``K`' to mean “any integer outside the
range −128 to 127”, and then specifying ``Ks`' in the operand
constraints.

**``g`'**
: Any register, memory or immediate integer operand is allowed, except for
registers that are not general registers.

**``X`'**
: Any operand whatsoever is allowed, even if it does not satisfy
`general_operand`. This is normally used in the constraint of
a `match_scratch` when certain alternatives will not actually
require a scratch register.

**``0`', ``1`', ``2`', ... ``9`'**
: An operand that matches the specified operand number is allowed. If a
digit is used together with letters within the same alternative, the
digit should come last.

This number is allowed to be more than a single digit. If multiple
digits are encountered consecutively, they are interpreted as a single
decimal integer. There is scant chance for ambiguity, since to-date
it has never been desirable that ``10`' be interpreted as matching
either operand 1 _or_ operand 0. Should this be desired, one
can use multiple alternatives instead.

This is called a matching constraint and what it really means is
that the assembler has only a single operand that fills two roles
considered separate in the RTL insn. For example, an add insn has two
input operands and one output operand in the RTL, but on most CISC
machines an add instruction really has only two operands, one of them an
input-output operand:

```
          addl #35,r12

```

Matching constraints are used in these circumstances.
More precisely, the two operands that match must include one input-only
operand and one output-only operand. Moreover, the digit must be a
smaller number than the number of the operand that uses it in the
constraint.

For operands to match in a particular case usually means that they
are identical-looking RTL expressions. But in a few special cases
specific kinds of dissimilarity are allowed. For example, `*x`
as an input operand will match `*x++` as an output operand.
For proper results in such cases, the output template should always
use the output-operand's number when printing the operand.

**``p`'**
: An operand that is a valid memory address is allowed. This is
for “load address” and “push address” instructions.

``p`' in the constraint must be accompanied by `address_operand`
as the predicate in the `match_operand`. This predicate interprets
the mode specified in the `match_operand` as the mode of the memory
reference for which the address would be valid.

**other-letters**
: Other letters can be defined in machine-dependent fashion to stand for
particular classes of registers or other arbitrary operand types.
``d`', ``a`' and ``f`' are defined on the 68000/68020 to stand
for data, address and floating point registers.

In order to have valid assembler code, each operand must satisfy
its constraint. But a failure to do so does not prevent the pattern
from applying to an insn. Instead, it directs the compiler to modify
the code so that the constraint will be satisfied. Usually this is
done by copying an operand into a register.

Contrast, therefore, the two instruction patterns that follow:

```
     (define_insn ""
       [(set (match_operand:SI 0 "general_operand" "=r")
             (plus:SI (match_dup 0)
                      (match_operand:SI 1 "general_operand" "r")))]
       ""
       "...")
```

which has two operands, one of which must appear in two places, and

```
     (define_insn ""
       [(set (match_operand:SI 0 "general_operand" "=r")
             (plus:SI (match_operand:SI 1 "general_operand" "0")
                      (match_operand:SI 2 "general_operand" "r")))]
       ""
       "...")
```

which has three operands, two of which are required by a constraint to be
identical. If we are considering an insn of the form

```
     (insn n prev next
       (set (reg:SI 3)
            (plus:SI (reg:SI 6) (reg:SI 109)))
       ...)
```

the first pattern would not apply at all, because this insn does not
contain two identical subexpressions in the right place. The pattern would
say, “That does not look like an add instruction; try other patterns”.
The second pattern would say, “Yes, that's an add instruction, but there
is something wrong with it”. It would direct the reload pass of the
compiler to generate additional insns to make the constraint true. The
results might look like this:

```
     (insn n2 prev n
       (set (reg:SI 3) (reg:SI 6))
       ...)

     (insn n n2 next
       (set (reg:SI 3)
            (plus:SI (reg:SI 3) (reg:SI 109)))
       ...)
```

It is up to you to make sure that each operand, in each pattern, has
constraints that can handle any RTL expression that could be present for
that operand. (When multiple alternatives are in use, each pattern must,
for each possible combination of operand expressions, have at least one
alternative which can handle that combination of operands.) The
constraints don't need to _allow_ any possible operand—when this is
the case, they do not constrain—but they must at least point the way to
reloading any possible operand so that it will fit.

- If the constraint accepts whatever operands the predicate permits,
  there is no problem: reloading is never necessary for this operand.

  For example, an operand whose constraints permit everything except
  registers is safe provided its predicate rejects registers.

  An operand whose predicate accepts only constant values is safe
  provided its constraints include the letter ``i`'. If any possible
  constant value is accepted, then nothing less than ``i`' will do;
  if the predicate is more selective, then the constraints may also be
  more selective.
- Any operand expression can be reloaded by copying it into a register.
  So if an operand's constraints allow some kind of register, it is
  certain to be safe. It need not permit all classes of registers; the
  compiler knows how to copy a register into another register of the
  proper class in order to make an instruction valid.

- A nonoffsettable memory reference can be reloaded by copying the
  address into a register. So if the constraint uses the letter
  ``o`', all memory references are taken care of.
- A constant operand can be reloaded by allocating space in memory to
  hold it as preinitialized data. Then the memory reference can be used
  in place of the constant. So if the constraint uses the letters
  ``o`' or ``m`', constant operands are not a problem.
- If the constraint permits a constant and a pseudo register used in an insn
  was not allocated to a hard register and is equivalent to a constant,
  the register will be replaced with the constant. If the predicate does
  not permit a constant and the insn is re-recognized for some reason, the
  compiler will crash. Thus the predicate must always recognize any
  objects allowed by the constraint.

If the operand's predicate can recognize registers, but the constraint does
not permit them, it can make the compiler crash. When this operand happens
to be a register, the reload pass will be stymied, because it does not know
how to copy a register temporarily into memory.

If the predicate accepts a unary operator, the constraint applies to the
operand. For example, the MIPS processor at ISA level 3 supports an
instruction which adds two registers in `SImode` to produce a
`DImode` result, but only if the registers are correctly sign
extended. This predicate for the input operands accepts a
`sign_extend` of an `SImode` register. Write the constraint
to indicate the type of register that is required for the operand of the
`sign_extend`.
