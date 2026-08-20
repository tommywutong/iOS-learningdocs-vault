---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Accessors.html
archived_at: '2026-07-15T07:30:59.206490Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Special Accessors](Special-Accessors.md#apple-knygky3jmfwc2qldmnsxg43pojzq),
Previous: [RTL Classes](RTL-Classes.md#apple-kjkeylkdnrqxg43fom),
Up: [RTL](RTL.md#apple-kjkey)

---

### 10.3 Access to Operands

Operands of expressions are accessed using the macros `XEXP`,
`XINT`, `XWINT` and `XSTR`. Each of these macros takes
two arguments: an expression-pointer (RTX) and an operand number
(counting from zero). Thus,

```
     XEXP (x, 2)
```

accesses operand 2 of expression x, as an expression.

```
     XINT (x, 2)
```

accesses the same operand as an integer. `XSTR`, used in the same
fashion, would access it as a string.

Any operand can be accessed as an integer, as an expression or as a string.
You must choose the correct method of access for the kind of value actually
stored in the operand. You would do this based on the expression code of
the containing expression. That is also how you would know how many
operands there are.

For example, if x is a `subreg` expression, you know that it has
two operands which can be correctly accessed as `XEXP (`x`, 0)`
and `XINT (`x`, 1)`. If you did `XINT (`x`, 0)`, you
would get the address of the expression operand but cast as an integer;
that might occasionally be useful, but it would be cleaner to write
`(int) XEXP (`x`, 0)`. `XEXP (`x`, 1)` would also
compile without error, and would return the second, integer operand cast as
an expression pointer, which would probably result in a crash when
accessed. Nothing stops you from writing `XEXP (`x`, 28)` either,
but this will access memory past the end of the expression with
unpredictable results.

Access to operands which are vectors is more complicated. You can use the
macro `XVEC` to get the vector-pointer itself, or the macros
`XVECEXP` and `XVECLEN` to access the elements and length of a
vector.

**`XVEC (`exp`,` idx`)`**
: Access the vector-pointer which is operand number idx in exp.

**`XVECLEN (`exp`,` idx`)`**
: Access the length (number of elements) in the vector which is
in operand number idx in exp. This value is an `int`.

**`XVECEXP (`exp`,` idx`,` eltnum`)`**
: Access element number eltnum in the vector which is
in operand number idx in exp. This value is an RTX.

It is up to you to make sure that eltnum is not negative
and is less than `XVECLEN (`exp`,` idx`)`.

All the macros defined in this section expand into lvalues and therefore
can be used to assign the operands, lengths and vector elements as well as
to access them.
