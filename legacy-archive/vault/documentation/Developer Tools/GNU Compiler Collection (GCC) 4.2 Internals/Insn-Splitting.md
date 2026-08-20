---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Insn-Splitting.html
archived_at: '2026-07-15T07:31:02.110699Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Including Patterns](Including-Patterns.md#apple-jfxgg3dvmruw4zznkbqxi5dfojxhg),
Previous: [Expander Definitions](Expander-Definitions.md#apple-iv4haylomrsxelkemvtgs3tjoruw63tt),
Up: [Machine Desc](Machine-Desc.md#apple-jvqwg2djnzss2rdfonrq)

---

### 14.16 Defining How to Split Instructions

There are two cases where you should specify how to split a pattern
into multiple insns. On machines that have instructions requiring
delay slots (see [Delay Slots](Delay-Slots.md#apple-irswyylzfvjwy33uom)) or that have instructions whose
output is not available for multiple cycles (see [Processor pipeline description](Processor-pipeline-description.md#apple-kbzg6y3fonzw64rnobuxazlmnfxgkllemvzwg4tjob2gs33o)), the compiler phases that optimize these cases need to
be able to move insns into one-instruction delay slots. However, some
insns may generate more than one machine instruction. These insns
cannot be placed into a delay slot.

Often you can rewrite the single insn as a list of individual insns,
each corresponding to one machine instruction. The disadvantage of
doing so is that it will cause the compilation to be slower and require
more space. If the resulting insns are too complex, it may also
suppress some optimizations. The compiler splits the insn if there is a
reason to believe that it might improve instruction or delay slot
scheduling.

The insn combiner phase also splits putative insns. If three insns are
merged into one insn with a complex expression that cannot be matched by
some `define_insn` pattern, the combiner phase attempts to split
the complex pattern into two insns that are recognized. Usually it can
break the complex pattern into two patterns by splitting out some
subexpression. However, in some other cases, such as performing an
addition of a large constant in two insns on a RISC machine, the way to
split the addition into two insns is machine-dependent.

The `define_split` definition tells the compiler how to split a
complex insn into several simpler insns. It looks like this:

```
     (define_split
       [insn-pattern]
       "condition"
       [new-insn-pattern-1
        new-insn-pattern-2
        ...]
       "preparation-statements")
```

insn-pattern is a pattern that needs to be split and
condition is the final condition to be tested, as in a
`define_insn`. When an insn matching insn-pattern and
satisfying condition is found, it is replaced in the insn list
with the insns given by new-insn-pattern-1,
new-insn-pattern-2, etc.

The preparation-statements are similar to those statements that
are specified for `define_expand` (see [Expander Definitions](Expander-Definitions.md#apple-iv4haylomrsxelkemvtgs3tjoruw63tt))
and are executed before the new RTL is generated to prepare for the
generated code or emit some insns whose pattern is not fixed. Unlike
those in `define_expand`, however, these statements must not
generate any new pseudo-registers. Once reload has completed, they also
must not allocate any space in the stack frame.

Patterns are matched against insn-pattern in two different
circumstances. If an insn needs to be split for delay slot scheduling
or insn scheduling, the insn is already known to be valid, which means
that it must have been matched by some `define_insn` and, if
`reload_completed` is nonzero, is known to satisfy the constraints
of that `define_insn`. In that case, the new insn patterns must
also be insns that are matched by some `define_insn` and, if
`reload_completed` is nonzero, must also satisfy the constraints
of those definitions.

As an example of this usage of `define_split`, consider the following
example from `a29k.md`, which splits a `sign_extend` from
`HImode` to `SImode` into a pair of shift insns:

```
     (define_split
       [(set (match_operand:SI 0 "gen_reg_operand" "")
             (sign_extend:SI (match_operand:HI 1 "gen_reg_operand" "")))]
       ""
       [(set (match_dup 0)
             (ashift:SI (match_dup 1)
                        (const_int 16)))
        (set (match_dup 0)
             (ashiftrt:SI (match_dup 0)
                          (const_int 16)))]
       "
     { operands[1] = gen_lowpart (SImode, operands[1]); }")
```

When the combiner phase tries to split an insn pattern, it is always the
case that the pattern is _not_ matched by any `define_insn`.
The combiner pass first tries to split a single `set` expression
and then the same `set` expression inside a `parallel`, but
followed by a `clobber` of a pseudo-reg to use as a scratch
register. In these cases, the combiner expects exactly two new insn
patterns to be generated. It will verify that these patterns match some
`define_insn` definitions, so you need not do this test in the
`define_split` (of course, there is no point in writing a
`define_split` that will never produce insns that match).

Here is an example of this use of `define_split`, taken from
`rs6000.md`:

```
     (define_split
       [(set (match_operand:SI 0 "gen_reg_operand" "")
             (plus:SI (match_operand:SI 1 "gen_reg_operand" "")
                      (match_operand:SI 2 "non_add_cint_operand" "")))]
       ""
       [(set (match_dup 0) (plus:SI (match_dup 1) (match_dup 3)))
        (set (match_dup 0) (plus:SI (match_dup 0) (match_dup 4)))]
     "
     {
       int low = INTVAL (operands[2]) & 0xffff;
       int high = (unsigned) INTVAL (operands[2]) >> 16;

       if (low & 0x8000)
         high++, low |= 0xffff0000;

       operands[3] = GEN_INT (high << 16);
       operands[4] = GEN_INT (low);
     }")
```

Here the predicate `non_add_cint_operand` matches any
`const_int` that is _not_ a valid operand of a single add
insn. The add with the smaller displacement is written so that it
can be substituted into the address of a subsequent operation.

An example that uses a scratch register, from the same file, generates
an equality comparison of a register and a large constant:

```
     (define_split
       [(set (match_operand:CC 0 "cc_reg_operand" "")
             (compare:CC (match_operand:SI 1 "gen_reg_operand" "")
                         (match_operand:SI 2 "non_short_cint_operand" "")))
        (clobber (match_operand:SI 3 "gen_reg_operand" ""))]
       "find_single_use (operands[0], insn, 0)
        && (GET_CODE (*find_single_use (operands[0], insn, 0)) == EQ
            || GET_CODE (*find_single_use (operands[0], insn, 0)) == NE)"
       [(set (match_dup 3) (xor:SI (match_dup 1) (match_dup 4)))
        (set (match_dup 0) (compare:CC (match_dup 3) (match_dup 5)))]
       "
     {
       /* Get the constant we are comparing against, C, and see what it
          looks like sign-extended to 16 bits.  Then see what constant
          could be XOR'ed with C to get the sign-extended value.  */

       int c = INTVAL (operands[2]);
       int sextc = (c << 16) >> 16;
       int xorv = c ^ sextc;

       operands[4] = GEN_INT (xorv);
       operands[5] = GEN_INT (sextc);
     }")
```

To avoid confusion, don't write a single `define_split` that
accepts some insns that match some `define_insn` as well as some
insns that don't. Instead, write two separate `define_split`
definitions, one for the insns that are valid and one for the insns that
are not valid.

The splitter is allowed to split jump instructions into sequence of
jumps or create new jumps in while splitting non-jump instructions. As
the central flowgraph and branch prediction information needs to be updated,
several restriction apply.

Splitting of jump instruction into sequence that over by another jump
instruction is always valid, as compiler expect identical behavior of new
jump. When new sequence contains multiple jump instructions or new labels,
more assistance is needed. Splitter is required to create only unconditional
jumps, or simple conditional jump instructions. Additionally it must attach a
`REG_BR_PROB` note to each conditional jump. A global variable
`split_branch_probability` holds the probability of the original branch in case
it was an simple conditional jump, −1 otherwise. To simplify
recomputing of edge frequencies, the new sequence is required to have only
forward jumps to the newly created labels.

For the common case where the pattern of a define_split exactly matches the
pattern of a define_insn, use `define_insn_and_split`. It looks like
this:

```
     (define_insn_and_split
       [insn-pattern]
       "condition"
       "output-template"
       "split-condition"
       [new-insn-pattern-1
        new-insn-pattern-2
        ...]
       "preparation-statements"
       [insn-attributes])

```

insn-pattern, condition, output-template, and
insn-attributes are used as in `define_insn`. The
new-insn-pattern vector and the preparation-statements are used as
in a `define_split`. The split-condition is also used as in
`define_split`, with the additional behavior that if the condition starts
with ``&&`', the condition used for the split will be the constructed as a
logical “and” of the split condition with the insn condition. For example,
from i386.md:

```
     (define_insn_and_split "zero_extendhisi2_and"
       [(set (match_operand:SI 0 "register_operand" "=r")
          (zero_extend:SI (match_operand:HI 1 "register_operand" "0")))
        (clobber (reg:CC 17))]
       "TARGET_ZERO_EXTEND_WITH_AND && !optimize_size"
       "#"
       "&& reload_completed"
       [(parallel [(set (match_dup 0)
                        (and:SI (match_dup 0) (const_int 65535)))
               (clobber (reg:CC 17))])]
       ""
       [(set_attr "type" "alu1")])

```

In this case, the actual split condition will be
``TARGET_ZERO_EXTEND_WITH_AND && !optimize_size && reload_completed`'.

The `define_insn_and_split` construction provides exactly the same
functionality as two separate `define_insn` and `define_split`
patterns. It exists for compactness, and as a maintenance tool to prevent
having to ensure the two patterns' templates match.
