---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Soft-float-library-routines.html
archived_at: '2026-07-15T07:31:02.807906Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Decimal float library routines](Decimal-float-library-routines.md#apple-irswg2lnmfwc2ztmn5qxillmnfrheylspewxe33voruw4zlt),
Previous: [Integer library routines](Integer-library-routines.md#apple-jfxhizlhmvzc23djmjzgc4tzfvzg65lunfxgk4y),
Up: [Libgcc](Libgcc.md#apple-jruwez3dmm)

---

### 4.2 Routines for floating point emulation

The software floating point library is used on machines which do not
have hardware support for floating point. It is also used whenever
`-msoft-float` is used to disable generation of floating point
instructions. (Not all targets support this switch.)

For compatibility with other compilers, the floating point emulation
routines can be renamed with the `DECLARE_LIBRARY_RENAMES` macro
(see [Library Calls](Library-Calls.md#apple-jruwe4tboj4s2q3bnrwhg)). In this section, the default names are used.

Presently the library does not support `XFmode`, which is used
for `long double` on some architectures.

#### 4.2.1 Arithmetic functions

— Runtime Function: float ____addsf3__ (float a, float b)
— Runtime Function: double ____adddf3__ (double a, double b)
— Runtime Function: long double ____addtf3__ (long double a, long double b)
— Runtime Function: long double ____addxf3__ (long double a, long double b)
> These functions return the sum of a and b.

— Runtime Function: float ____subsf3__ (float a, float b)
— Runtime Function: double ____subdf3__ (double a, double b)
— Runtime Function: long double ____subtf3__ (long double a, long double b)
— Runtime Function: long double ____subxf3__ (long double a, long double b)
> These functions return the difference between b and a;
> that is, a - b.

— Runtime Function: float ____mulsf3__ (float a, float b)
— Runtime Function: double ____muldf3__ (double a, double b)
— Runtime Function: long double ____multf3__ (long double a, long double b)
— Runtime Function: long double ____mulxf3__ (long double a, long double b)
> These functions return the product of a and b.

— Runtime Function: float ____divsf3__ (float a, float b)
— Runtime Function: double ____divdf3__ (double a, double b)
— Runtime Function: long double ____divtf3__ (long double a, long double b)
— Runtime Function: long double ____divxf3__ (long double a, long double b)
> These functions return the quotient of a and b; that is,
> a / b.

— Runtime Function: float ____negsf2__ (float a)
— Runtime Function: double ____negdf2__ (double a)
— Runtime Function: long double ____negtf2__ (long double a)
— Runtime Function: long double ____negxf2__ (long double a)
> These functions return the negation of a. They simply flip the
> sign bit, so they can produce negative zero and negative NaN.

#### 4.2.2 Conversion functions

— Runtime Function: double ____extendsfdf2__ (float a)
— Runtime Function: long double ____extendsftf2__ (float a)
— Runtime Function: long double ____extendsfxf2__ (float a)
— Runtime Function: long double ____extenddftf2__ (double a)
— Runtime Function: long double ____extenddfxf2__ (double a)
> These functions extend a to the wider mode of their return
> type.

— Runtime Function: double ____truncxfdf2__ (long double a)
— Runtime Function: double ____trunctfdf2__ (long double a)
— Runtime Function: float ____truncxfsf2__ (long double a)
— Runtime Function: float ____trunctfsf2__ (long double a)
— Runtime Function: float ____truncdfsf2__ (double a)
> These functions truncate a to the narrower mode of their return
> type, rounding toward zero.

— Runtime Function: int ____fixsfsi__ (float a)
— Runtime Function: int ____fixdfsi__ (double a)
— Runtime Function: int ____fixtfsi__ (long double a)
— Runtime Function: int ____fixxfsi__ (long double a)
> These functions convert a to a signed integer, rounding toward zero.

— Runtime Function: long ____fixsfdi__ (float a)
— Runtime Function: long ____fixdfdi__ (double a)
— Runtime Function: long ____fixtfdi__ (long double a)
— Runtime Function: long ____fixxfdi__ (long double a)
> These functions convert a to a signed long, rounding toward zero.

— Runtime Function: long long ____fixsfti__ (float a)
— Runtime Function: long long ____fixdfti__ (double a)
— Runtime Function: long long ____fixtfti__ (long double a)
— Runtime Function: long long ____fixxfti__ (long double a)
> These functions convert a to a signed long long, rounding toward zero.

— Runtime Function: unsigned int ____fixunssfsi__ (float a)
— Runtime Function: unsigned int ____fixunsdfsi__ (double a)
— Runtime Function: unsigned int ____fixunstfsi__ (long double a)
— Runtime Function: unsigned int ____fixunsxfsi__ (long double a)
> These functions convert a to an unsigned integer, rounding
> toward zero. Negative values all become zero.

— Runtime Function: unsigned long ____fixunssfdi__ (float a)
— Runtime Function: unsigned long ____fixunsdfdi__ (double a)
— Runtime Function: unsigned long ____fixunstfdi__ (long double a)
— Runtime Function: unsigned long ____fixunsxfdi__ (long double a)
> These functions convert a to an unsigned long, rounding
> toward zero. Negative values all become zero.

— Runtime Function: unsigned long long ____fixunssfti__ (float a)
— Runtime Function: unsigned long long ____fixunsdfti__ (double a)
— Runtime Function: unsigned long long ____fixunstfti__ (long double a)
— Runtime Function: unsigned long long ____fixunsxfti__ (long double a)
> These functions convert a to an unsigned long long, rounding
> toward zero. Negative values all become zero.

— Runtime Function: float ____floatsisf__ (int i)
— Runtime Function: double ____floatsidf__ (int i)
— Runtime Function: long double ____floatsitf__ (int i)
— Runtime Function: long double ____floatsixf__ (int i)
> These functions convert i, a signed integer, to floating point.

— Runtime Function: float ____floatdisf__ (long i)
— Runtime Function: double ____floatdidf__ (long i)
— Runtime Function: long double ____floatditf__ (long i)
— Runtime Function: long double ____floatdixf__ (long i)
> These functions convert i, a signed long, to floating point.

— Runtime Function: float ____floattisf__ (long long i)
— Runtime Function: double ____floattidf__ (long long i)
— Runtime Function: long double ____floattitf__ (long long i)
— Runtime Function: long double ____floattixf__ (long long i)
> These functions convert i, a signed long long, to floating point.

— Runtime Function: float ____floatunsisf__ (unsigned int i)
— Runtime Function: double ____floatunsidf__ (unsigned int i)
— Runtime Function: long double ____floatunsitf__ (unsigned int i)
— Runtime Function: long double ____floatunsixf__ (unsigned int i)
> These functions convert i, an unsigned integer, to floating point.

— Runtime Function: float ____floatundisf__ (unsigned long i)
— Runtime Function: double ____floatundidf__ (unsigned long i)
— Runtime Function: long double ____floatunditf__ (unsigned long i)
— Runtime Function: long double ____floatundixf__ (unsigned long i)
> These functions convert i, an unsigned long, to floating point.

— Runtime Function: float ____floatuntisf__ (unsigned long long i)
— Runtime Function: double ____floatuntidf__ (unsigned long long i)
— Runtime Function: long double ____floatuntitf__ (unsigned long long i)
— Runtime Function: long double ____floatuntixf__ (unsigned long long i)
> These functions convert i, an unsigned long long, to floating point.

#### 4.2.3 Comparison functions

There are two sets of basic comparison functions.

— Runtime Function: int ____cmpsf2__ (float a, float b)
— Runtime Function: int ____cmpdf2__ (double a, double b)
— Runtime Function: int ____cmptf2__ (long double a, long double b)
> These functions calculate a <=> b. That is, if a is less
> than b, they return −1; if a is greater than b, they
> return 1; and if a and b are equal they return 0. If
> either argument is NaN they return 1, but you should not rely on this;
> if NaN is a possibility, use one of the higher-level comparison
> functions.

— Runtime Function: int ____unordsf2__ (float a, float b)
— Runtime Function: int ____unorddf2__ (double a, double b)
— Runtime Function: int ____unordtf2__ (long double a, long double b)
> These functions return a nonzero value if either argument is NaN, otherwise 0.

There is also a complete group of higher level functions which
correspond directly to comparison operators. They implement the ISO C
semantics for floating-point comparisons, taking NaN into account.
Pay careful attention to the return values defined for each set.
Under the hood, all of these routines are implemented as

```
       if (__unordXf2 (a, b))
         return E;
       return __cmpXf2 (a, b);
```

where E is a constant chosen to give the proper behavior for
NaN. Thus, the meaning of the return value is different for each set.
Do not rely on this implementation; only the semantics documented
below are guaranteed.

— Runtime Function: int ____eqsf2__ (float a, float b)
— Runtime Function: int ____eqdf2__ (double a, double b)
— Runtime Function: int ____eqtf2__ (long double a, long double b)
> These functions return zero if neither argument is NaN, and a and
> b are equal.

— Runtime Function: int ____nesf2__ (float a, float b)
— Runtime Function: int ____nedf2__ (double a, double b)
— Runtime Function: int ____netf2__ (long double a, long double b)
> These functions return a nonzero value if either argument is NaN, or
> if a and b are unequal.

— Runtime Function: int ____gesf2__ (float a, float b)
— Runtime Function: int ____gedf2__ (double a, double b)
— Runtime Function: int ____getf2__ (long double a, long double b)
> These functions return a value greater than or equal to zero if
> neither argument is NaN, and a is greater than or equal to
> b.

— Runtime Function: int ____ltsf2__ (float a, float b)
— Runtime Function: int ____ltdf2__ (double a, double b)
— Runtime Function: int ____lttf2__ (long double a, long double b)
> These functions return a value less than zero if neither argument is
> NaN, and a is strictly less than b.

— Runtime Function: int ____lesf2__ (float a, float b)
— Runtime Function: int ____ledf2__ (double a, double b)
— Runtime Function: int ____letf2__ (long double a, long double b)
> These functions return a value less than or equal to zero if neither
> argument is NaN, and a is less than or equal to b.

— Runtime Function: int ____gtsf2__ (float a, float b)
— Runtime Function: int ____gtdf2__ (double a, double b)
— Runtime Function: int ____gttf2__ (long double a, long double b)
> These functions return a value greater than zero if neither argument
> is NaN, and a is strictly greater than b.

#### 4.2.4 Other floating-point functions

— Runtime Function: float ____powisf2__ (float a, int b)
— Runtime Function: double ____powidf2__ (double a, int b)
— Runtime Function: long double ____powitf2__ (long double a, int b)
— Runtime Function: long double ____powixf2__ (long double a, int b)
> These functions convert raise a to the power b.

— Runtime Function: complex float ____mulsc3__ (float a, float b, float c, float d)
— Runtime Function: complex double ____muldc3__ (double a, double b, double c, double d)
— Runtime Function: complex long double ____multc3__ (long double a, long double b, long double c, long double d)
— Runtime Function: complex long double ____mulxc3__ (long double a, long double b, long double c, long double d)
> These functions return the product of a + ib and
> c + id, following the rules of C99 Annex G.

— Runtime Function: complex float ____divsc3__ (float a, float b, float c, float d)
— Runtime Function: complex double ____divdc3__ (double a, double b, double c, double d)
— Runtime Function: complex long double ____divtc3__ (long double a, long double b, long double c, long double d)
— Runtime Function: complex long double ____divxc3__ (long double a, long double b, long double c, long double d)
> These functions return the quotient of a + ib and
> c + id (i.e., (a + ib) / (c
> + id)), following the rules of C99 Annex G.
