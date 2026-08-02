---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Insn-Canonicalizations.html
archived_at: '2026-07-15T07:31:02.097717Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Expander Definitions](Expander-Definitions.md#apple-iv4haylomrsxelkemvtgs3tjoruw63tt),
Previous: [Looping Patterns](Looping-Patterns.md#apple-jrxw64djnzts2udbor2gk4toom),
Up: [Machine Desc](Machine-Desc.md#apple-jvqwg2djnzss2rdfonrq)

---

### 14.14 Canonicalization of Instructions

There are often cases where multiple RTL expressions could represent an
operation performed by a single machine instruction. This situation is
most commonly encountered with logical, branch, and multiply-accumulate
instructions. In such cases, the compiler attempts to convert these
multiple RTL expressions into a single canonical form to reduce the
number of insn patterns required.

In addition to algebraic simplifications, following canonicalizations
are performed:

- For commutative and comparison operators, a constant is always made the
  second operand. If a machine only supports a constant as the second
  operand, only patterns that match a constant in the second operand need
  be supplied.
- For associative operators, a sequence of operators will always chain
  to the left; for instance, only the left operand of an integer `plus`
  can itself be a `plus`. `and`, `ior`, `xor`,
  `plus`, `mult`, `smin`, `smax`, `umin`, and
  `umax` are associative when applied to integers, and sometimes to
  floating-point.
- For these operators, if only one operand is a `neg`, `not`,
  `mult`, `plus`, or `minus` expression, it will be the
  first operand.
- In combinations of `neg`, `mult`, `plus`, and
  `minus`, the `neg` operations (if any) will be moved inside
  the operations as far as possible. For instance,
  `(neg (mult A B))` is canonicalized as `(mult (neg A) B)`, but
  `(plus (mult (neg A) B) C)` is canonicalized as
  `(minus A (mult B C))`.

- For the `compare` operator, a constant is always the second operand
  on machines where `cc0` is used (see [Jump Patterns](Jump-Patterns.md#apple-jj2w24bnkbqxi5dfojxhg)). On other
  machines, there are rare cases where the compiler might want to construct
  a `compare` with a constant as the first operand. However, these
  cases are not common enough for it to be worthwhile to provide a pattern
  matching a constant as the first operand unless the machine actually has
  such an instruction.

  An operand of `neg`, `not`, `mult`, `plus`, or
  `minus` is made the first operand under the same conditions as
  above.
- `(minus` x `(const_int` n`))` is converted to
  `(plus` x `(const_int` -n`))`.
- Within address computations (i.e., inside `mem`), a left shift is
  converted into the appropriate multiplication by a power of two.

- De Morgan's Law is used to move bitwise negation inside a bitwise
  logical-and or logical-or operation. If this results in only one
  operand being a `not` expression, it will be the first one.

  A machine that has an instruction that performs a bitwise logical-and of one
  operand with the bitwise negation of the other should specify the pattern
  for that instruction as

  ```
            (define_insn ""
              [(set (match_operand:m 0 ...)
                    (and:m (not:m (match_operand:m 1 ...))
                                 (match_operand:m 2 ...)))]
              "..."
              "...")

  ```

  Similarly, a pattern for a “NAND” instruction should be written

  ```
            (define_insn ""
              [(set (match_operand:m 0 ...)
                    (ior:m (not:m (match_operand:m 1 ...))
                                 (not:m (match_operand:m 2 ...))))]
              "..."
              "...")

  ```

  In both cases, it is not necessary to include patterns for the many
  logically equivalent RTL expressions.

- The only possible RTL expressions involving both bitwise exclusive-or
  and bitwise negation are `(xor:`m x y`)`
  and `(not:`m `(xor:`m x y`))`.
- The sum of three items, one of which is a constant, will only appear in
  the form

  ```
            (plus:m (plus:m x y) constant)

  ```
- On machines that do not use `cc0`,
  `(compare` x `(const_int 0))` will be converted to
  x.

- Equality comparisons of a group of bits (usually a single bit) with zero
  will be written using `zero_extract` rather than the equivalent
  `and` or `sign_extract` operations.

Further canonicalization rules are defined in the function
`commutative_operand_precedence` in `gcc/rtlanal.c`.
