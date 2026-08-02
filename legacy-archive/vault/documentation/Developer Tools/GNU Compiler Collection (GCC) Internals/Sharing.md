---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Sharing.html
archived_at: '2026-07-15T07:31:00.714149Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Reading RTL](Reading-RTL.md#apple-kjswczdjnzts2usujq),
Previous: [Calls](Calls.md#apple-inqwy3dt),
Up: [RTL](RTL.md#apple-kjkey)

---

### 10.20 Structure Sharing Assumptions

The compiler assumes that certain kinds of RTL expressions are unique;
there do not exist two distinct objects representing the same value.
In other cases, it makes an opposite assumption: that no RTL expression
object of a certain kind appears in more than one place in the
containing structure.

These assumptions refer to a single function; except for the RTL
objects that describe global variables and external functions,
and a few standard objects such as small integer constants,
no RTL objects are common to two functions.

- Each pseudo-register has only a single `reg` object to represent it,
  and therefore only a single machine mode.

- For any symbolic label, there is only one `symbol_ref` object
  referring to it.

- All `const_int` expressions with equal values are shared.

- There is only one `pc` expression.

- There is only one `cc0` expression.

- There is only one `const_double` expression with value 0 for
  each floating point mode. Likewise for values 1 and 2.

- There is only one `const_vector` expression with value 0 for
  each vector mode, be it an integer or a double constant vector.

- No `label_ref` or `scratch` appears in more than one place in
  the RTL structure; in other words, it is safe to do a tree-walk of all
  the insns in the function and assume that each time a `label_ref`
  or `scratch` is seen it is distinct from all others that are seen.

- Only one `mem` object is normally created for each static
  variable or stack slot, so these objects are frequently shared in all
  the places they appear. However, separate but equal objects for these
  variables are occasionally made.

- When a single `asm` statement has multiple output operands, a
  distinct `asm_operands` expression is made for each output operand.
  However, these all share the vector which contains the sequence of input
  operands. This sharing is used later on to test whether two
  `asm_operands` expressions come from the same statement, so all
  optimizations must carefully preserve the sharing if they copy the
  vector at all.
- No RTL object appears in more than one place in the RTL structure
  except as described above. Many passes of the compiler rely on this
  by assuming that they can modify RTL objects in place without unwanted
  side-effects on other insns.

- During initial RTL generation, shared structure is freely introduced.
  After all the RTL for a function has been generated, all shared
  structure is copied by `unshare_all_rtl` in `emit-rtl.c`,
  after which the above rules are guaranteed to be followed.

- During the combiner pass, shared structure within an insn can exist
  temporarily. However, the shared structure is copied before the
  combiner is finished with the insn. This is done by calling
  `copy_rtx_if_shared`, which is a subroutine of
  `unshare_all_rtl`.
