---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Delay-Slots.html
archived_at: '2026-07-15T07:31:01.716549Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Processor pipeline description](Processor-pipeline-description.md#apple-kbzg6y3fonzw64rnobuxazlmnfxgkllemvzwg4tjob2gs33o),
Previous: [Constant Attributes](Constant-Attributes.md#apple-inxw443umfxhilkbor2he2lcov2gk4y),
Up: [Insn Attributes](Insn-Attributes.md#apple-jfxhg3rnif2hi4tjmj2xizlt)

---

#### 14.19.7 Delay Slot Scheduling

The insn attribute mechanism can be used to specify the requirements for
delay slots, if any, on a target machine. An instruction is said to
require a delay slot if some instructions that are physically
after the instruction are executed as if they were located before it.
Classic examples are branch and call instructions, which often execute
the following instruction before the branch or call is performed.

On some machines, conditional branch instructions can optionally
annul instructions in the delay slot. This means that the
instruction will not be executed for certain branch outcomes. Both
instructions that annul if the branch is true and instructions that
annul if the branch is false are supported.

Delay slot scheduling differs from instruction scheduling in that
determining whether an instruction needs a delay slot is dependent only
on the type of instruction being generated, not on data flow between the
instructions. See the next section for a discussion of data-dependent
instruction scheduling.

The requirement of an insn needing one or more delay slots is indicated
via the `define_delay` expression. It has the following form:

```
     (define_delay test
                   [delay-1 annul-true-1 annul-false-1
                    delay-2 annul-true-2 annul-false-2
                    ...])
```

test is an attribute test that indicates whether this
`define_delay` applies to a particular insn. If so, the number of
required delay slots is determined by the length of the vector specified
as the second argument. An insn placed in delay slot n must
satisfy attribute test delay-n. annul-true-n is an
attribute test that specifies which insns may be annulled if the branch
is true. Similarly, annul-false-n specifies which insns in the
delay slot may be annulled if the branch is false. If annulling is not
supported for that delay slot, `(nil)` should be coded.

For example, in the common case where branch and call insns require
a single delay slot, which may contain any insn other than a branch or
call, the following would be placed in the `md` file:

```
     (define_delay (eq_attr "type" "branch,call")
                   [(eq_attr "type" "!branch,call") (nil) (nil)])
```

Multiple `define_delay` expressions may be specified. In this
case, each such expression specifies different delay slot requirements
and there must be no insn for which tests in two `define_delay`
expressions are both true.

For example, if we have a machine that requires one delay slot for branches
but two for calls, no delay slot can contain a branch or call insn,
and any valid insn in the delay slot for the branch can be annulled if the
branch is true, we might represent this as follows:

```
     (define_delay (eq_attr "type" "branch")
        [(eq_attr "type" "!branch,call")
         (eq_attr "type" "!branch,call")
         (nil)])

     (define_delay (eq_attr "type" "call")
                   [(eq_attr "type" "!branch,call") (nil) (nil)
                    (eq_attr "type" "!branch,call") (nil) (nil)])
```
