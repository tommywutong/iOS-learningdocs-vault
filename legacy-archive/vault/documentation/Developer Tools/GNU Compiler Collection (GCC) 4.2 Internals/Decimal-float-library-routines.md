---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Decimal-float-library-routines.html
archived_at: '2026-07-15T07:31:01.667948Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Exception handling routines](Exception-handling-routines.md#apple-iv4ggzlqoruw63rnnbqw4zdmnfxgollsn52xi2lomvzq),
Previous: [Soft float library routines](Soft-float-library-routines.md#apple-knxwm5bnmzwg6ylufvwgsytsmfzhsllsn52xi2lomvzq),
Up: [Libgcc](Libgcc.md#apple-jruwez3dmm)

---

### 4.3 Routines for decimal floating point emulation

The software decimal floating point library implements IEEE 754R
decimal floating point arithmetic and is only activated on selected
targets.

#### 4.3.1 Arithmetic functions

— Runtime Function: _Decimal32 ____addsd3__ (_Decimal32 a, _Decimal32 b)
— Runtime Function: _Decimal64 ____adddd3__ (_Decimal64 a, _Decimal64 b)
— Runtime Function: _Decimal128 ____addtd3__ (_Decimal128 a, _Decimal128 b)
> These functions return the sum of a and b.

— Runtime Function: _Decimal32 ____subsd3__ (_Decimal32 a, _Decimal32 b)
— Runtime Function: _Decimal64 ____subdd3__ (_Decimal64 a, _Decimal64 b)
— Runtime Function: _Decimal128 ____subtd3__ (_Decimal128 a, _Decimal128 b)
> These functions return the difference between b and a;
> that is, a - b.

— Runtime Function: _Decimal32 ____mulsd3__ (_Decimal32 a, _Decimal32 b)
— Runtime Function: _Decimal64 ____muldd3__ (_Decimal64 a, _Decimal64 b)
— Runtime Function: _Decimal128 ____multd3__ (_Decimal128 a, _Decimal128 b)
> These functions return the product of a and b.

— Runtime Function: _Decimal32 ____divsd3__ (_Decimal32 a, _Decimal32 b)
— Runtime Function: _Decimal64 ____divdd3__ (_Decimal64 a, _Decimal64 b)
— Runtime Function: _Decimal128 ____divtd3__ (_Decimal128 a, _Decimal128 b)
> These functions return the quotient of a and b; that is,
> a / b.

— Runtime Function: _Decimal32 ____negsd2__ (_Decimal32 a)
— Runtime Function: _Decimal64 ____negdd2__ (_Decimal64 a)
— Runtime Function: _Decimal128 ____negtd2__ (_Decimal128 a)
> These functions return the negation of a. They simply flip the
> sign bit, so they can produce negative zero and negative NaN.

#### 4.3.2 Conversion functions

— Runtime Function: _Decimal64 ____extendsddd2__ (_Decimal32 a)
— Runtime Function: _Decimal128 ____extendsdtd2__ (_Decimal32 a)
— Runtime Function: _Decimal128 ____extendddtd2__ (_Decimal64 a)
> — Runtime Function: _Decimal32 ____extendsfsd__ (float a)
> — Runtime Function: double ____extendsddf__ (_Decimal32 a)
> — Runtime Function: long double ____extendsdxf__ (_Decimal32 a)
> — Runtime Function: _Decimal64 ____extendsfdd__ (float a)
> — Runtime Function: _Decimal64 ____extenddfdd__ (double a)
> — Runtime Function: long double ____extendddxf__ (_Decimal64 a)
> — Runtime Function: _Decimal128 ____extendsftd__ (float a)
> — Runtime Function: _Decimal128 ____extenddftd__ (double a)
> — Runtime Function: _Decimal128 ____extendxftd__ (long double a)
> > These functions extend a to the wider mode of their return type.

— Runtime Function: _Decimal32 ____truncddsd2__ (_Decimal64 a)
— Runtime Function: _Decimal32 ____trunctdsd2__ (_Decimal128 a)
— Runtime Function: _Decimal64 ____trunctddd2__ (_Decimal128 a)
> — Runtime Function: float ____truncsdsf__ (_Decimal32 a)
> — Runtime Function: _Decimal32 ____truncdfsd__ (double a)
> — Runtime Function: _Decimal32 ____truncxfsd__ (long double a)
> — Runtime Function: float ____truncddsf__ (_Decimal64 a)
> — Runtime Function: double ____truncdddf__ (_Decimal64 a)
> — Runtime Function: _Decimal64 ____truncxfdd__ (long double a)
> — Runtime Function: float ____trunctdsf__ (_Decimal128 a)
> — Runtime Function: double ____trunctddf__ (_Decimal128 a)
> — Runtime Function: long double ____trunctdxf__ (_Decimal128 a)
> > These functions truncate a to the narrower mode of their return
> > type.

— Runtime Function: int ____fixsdsi__ (_Decimal32 a)
— Runtime Function: int ____fixddsi__ (_Decimal64 a)
— Runtime Function: int ____fixtdsi__ (_Decimal128 a)
> These functions convert a to a signed integer.

— Runtime Function: long ____fixsddi__ (_Decimal32 a)
— Runtime Function: long ____fixdddi__ (_Decimal64 a)
— Runtime Function: long ____fixtddi__ (_Decimal128 a)
> These functions convert a to a signed long.

— Runtime Function: unsigned int ____fixunssdsi__ (_Decimal32 a)
— Runtime Function: unsigned int ____fixunsddsi__ (_Decimal64 a)
— Runtime Function: unsigned int ____fixunstdsi__ (_Decimal128 a)
> These functions convert a to an unsigned integer. Negative values all become zero.

— Runtime Function: unsigned long ____fixunssddi__ (_Decimal32 a)
— Runtime Function: unsigned long ____fixunsdddi__ (_Decimal64 a)
— Runtime Function: unsigned long ____fixunstddi__ (_Decimal128 a)
> These functions convert a to an unsigned long. Negative values
> all become zero.

— Runtime Function: _Decimal32 ____floatsisd__ (int i)
— Runtime Function: _Decimal64 ____floatsidd__ (int i)
— Runtime Function: _Decimal128 ____floatsitd__ (int i)
> These functions convert i, a signed integer, to decimal floating point.

— Runtime Function: _Decimal32 ____floatdisd__ (long i)
— Runtime Function: _Decimal64 ____floatdidd__ (long i)
— Runtime Function: _Decimal128 ____floatditd__ (long i)
> These functions convert i, a signed long, to decimal floating point.

— Runtime Function: _Decimal32 ____floatunssisd__ (unsigned int i)
— Runtime Function: _Decimal64 ____floatunssidd__ (unsigned int i)
— Runtime Function: _Decimal128 ____floatunssitd__ (unsigned int i)
> These functions convert i, an unsigned integer, to decimal floating point.

— Runtime Function: _Decimal32 ____floatunsdisd__ (unsigned long i)
— Runtime Function: _Decimal64 ____floatunsdidd__ (unsigned long i)
— Runtime Function: _Decimal128 ____floatunsditd__ (unsigned long i)
> These functions convert i, an unsigned long, to decimal floating point.

#### 4.3.3 Comparison functions

— Runtime Function: int ____unordsd2__ (_Decimal32 a, _Decimal32 b)
— Runtime Function: int ____unorddd2__ (_Decimal64 a, _Decimal64 b)
— Runtime Function: int ____unordtd2__ (_Decimal128 a, _Decimal128 b)
> These functions return a nonzero value if either argument is NaN, otherwise 0.

There is also a complete group of higher level functions which
correspond directly to comparison operators. They implement the ISO C
semantics for floating-point comparisons, taking NaN into account.
Pay careful attention to the return values defined for each set.
Under the hood, all of these routines are implemented as

```
       if (__unordXd2 (a, b))
         return E;
       return __cmpXd2 (a, b);
```

where E is a constant chosen to give the proper behavior for
NaN. Thus, the meaning of the return value is different for each set.
Do not rely on this implementation; only the semantics documented
below are guaranteed.

— Runtime Function: int ____eqsd2__ (_Decimal32 a, _Decimal32 b)
— Runtime Function: int ____eqdd2__ (_Decimal64 a, _Decimal64 b)
— Runtime Function: int ____eqtd2__ (_Decimal128 a, _Decimal128 b)
> These functions return zero if neither argument is NaN, and a and
> b are equal.

— Runtime Function: int ____nesd2__ (_Decimal32 a, _Decimal32 b)
— Runtime Function: int ____nedd2__ (_Decimal64 a, _Decimal64 b)
— Runtime Function: int ____netd2__ (_Decimal128 a, _Decimal128 b)
> These functions return a nonzero value if either argument is NaN, or
> if a and b are unequal.

— Runtime Function: int ____gesd2__ (_Decimal32 a, _Decimal32 b)
— Runtime Function: int ____gedd2__ (_Decimal64 a, _Decimal64 b)
— Runtime Function: int ____getd2__ (_Decimal128 a, _Decimal128 b)
> These functions return a value greater than or equal to zero if
> neither argument is NaN, and a is greater than or equal to
> b.

— Runtime Function: int ____ltsd2__ (_Decimal32 a, _Decimal32 b)
— Runtime Function: int ____ltdd2__ (_Decimal64 a, _Decimal64 b)
— Runtime Function: int ____lttd2__ (_Decimal128 a, _Decimal128 b)
> These functions return a value less than zero if neither argument is
> NaN, and a is strictly less than b.

— Runtime Function: int ____lesd2__ (_Decimal32 a, _Decimal32 b)
— Runtime Function: int ____ledd2__ (_Decimal64 a, _Decimal64 b)
— Runtime Function: int ____letd2__ (_Decimal128 a, _Decimal128 b)
> These functions return a value less than or equal to zero if neither
> argument is NaN, and a is less than or equal to b.

— Runtime Function: int ____gtsd2__ (_Decimal32 a, _Decimal32 b)
— Runtime Function: int ____gtdd2__ (_Decimal64 a, _Decimal64 b)
— Runtime Function: int ____gttd2__ (_Decimal128 a, _Decimal128 b)
> These functions return a value greater than zero if neither argument
> is NaN, and a is strictly greater than b.
