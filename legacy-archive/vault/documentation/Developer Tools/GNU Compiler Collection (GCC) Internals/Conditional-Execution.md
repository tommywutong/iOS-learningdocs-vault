---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Conditional-Execution.html
archived_at: '2026-07-15T07:30:59.564461Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Constant Definitions](Constant-Definitions.md#apple-inxw443umfxhilkemvtgs3tjoruw63tt),
Previous: [Insn Attributes](Insn-Attributes.md#apple-jfxhg3rnif2hi4tjmj2xizlt),
Up: [Machine Desc](Machine-Desc.md#apple-jvqwg2djnzss2rdfonrq)

---

### 12.20 Conditional Execution

A number of architectures provide for some form of conditional
execution, or predication. The hallmark of this feature is the
ability to nullify most of the instructions in the instruction set.
When the instruction set is large and not entirely symmetric, it
can be quite tedious to describe these forms directly in the
`.md` file. An alternative is the `define_cond_exec` template.


```
     (define_cond_exec
       [predicate-pattern]
       "condition"
       "output-template")
```

predicate-pattern is the condition that must be true for the
insn to be executed at runtime and should match a relational operator.
One can use `match_operator` to match several relational operators
at once. Any `match_operand` operands must have no more than one
alternative.

condition is a C expression that must be true for the generated
pattern to match.

output-template is a string similar to the `define_insn`
output template (see [Output Template](Output-Template.md#apple-j52xi4dvoqwvizlnobwgc5df)), except that the ``*`'
and ``@`' special cases do not apply. This is only useful if the
assembly text for the predicate is a simple prefix to the main insn.
In order to handle the general case, there is a global variable
`current_insn_predicate` that will contain the entire predicate
if the current insn is predicated, and will otherwise be `NULL`.

When `define_cond_exec` is used, an implicit reference to
the `predicable` instruction attribute is made.
See [Insn Attributes](Insn-Attributes.md#apple-jfxhg3rnif2hi4tjmj2xizlt). This attribute must be boolean (i.e. have
exactly two elements in its list-of-values). Further, it must
not be used with complex expressions. That is, the default and all
uses in the insns must be a simple constant, not dependent on the
alternative or anything else.

For each `define_insn` for which the `predicable`
attribute is true, a new `define_insn` pattern will be
generated that matches a predicated version of the instruction.
For example,

```
     (define_insn "addsi"
       [(set (match_operand:SI 0 "register_operand" "r")
             (plus:SI (match_operand:SI 1 "register_operand" "r")
                      (match_operand:SI 2 "register_operand" "r")))]
       "test1"
       "add %2,%1,%0")

     (define_cond_exec
       [(ne (match_operand:CC 0 "register_operand" "c")
            (const_int 0))]
       "test2"
       "(%0)")
```

generates a new pattern

```
     (define_insn ""
       [(cond_exec
          (ne (match_operand:CC 3 "register_operand" "c") (const_int 0))
          (set (match_operand:SI 0 "register_operand" "r")
               (plus:SI (match_operand:SI 1 "register_operand" "r")
                        (match_operand:SI 2 "register_operand" "r"))))]
       "(test2) && (test1)"
       "(%3) add %2,%1,%0")
```
