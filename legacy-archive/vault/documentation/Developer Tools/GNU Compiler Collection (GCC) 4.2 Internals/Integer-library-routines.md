---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Integer-library-routines.html
archived_at: '2026-07-15T07:31:02.137580Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Soft float library routines](Soft-float-library-routines.md#apple-knxwm5bnmzwg6ylufvwgsytsmfzhsllsn52xi2lomvzq),
Up: [Libgcc](Libgcc.md#apple-jruwez3dmm)

---

### 4.1 Routines for integer arithmetic

The integer arithmetic routines are used on platforms that don't provide
hardware support for arithmetic operations on some modes.

#### 4.1.1 Arithmetic functions

— Runtime Function: int ____ashlsi3__ (int a, int b)
— Runtime Function: long ____ashldi3__ (long a, int b)
— Runtime Function: long long ____ashlti3__ (long long a, int b)
> These functions return the result of shifting a left by b bits.

— Runtime Function: int ____ashrsi3__ (int a, int b)
— Runtime Function: long ____ashrdi3__ (long a, int b)
— Runtime Function: long long ____ashrti3__ (long long a, int b)
> These functions return the result of arithmetically shifting a right
> by b bits.

— Runtime Function: int ____divsi3__ (int a, int b)
— Runtime Function: long ____divdi3__ (long a, long b)
— Runtime Function: long long ____divti3__ (long long a, long long b)
> These functions return the quotient of the signed division of a and
> b.

— Runtime Function: int ____lshrsi3__ (int a, int b)
— Runtime Function: long ____lshrdi3__ (long a, int b)
— Runtime Function: long long ____lshrti3__ (long long a, int b)
> These functions return the result of logically shifting a right by
> b bits.

— Runtime Function: int ____modsi3__ (int a, int b)
— Runtime Function: long ____moddi3__ (long a, long b)
— Runtime Function: long long ____modti3__ (long long a, long long b)
> These functions return the remainder of the signed division of a
> and b.

— Runtime Function: int ____mulsi3__ (int a, int b)
— Runtime Function: long ____muldi3__ (long a, long b)
— Runtime Function: long long ____multi3__ (long long a, long long b)
> These functions return the product of a and b.

— Runtime Function: long ____negdi2__ (long a)
— Runtime Function: long long ____negti2__ (long long a)
> These functions return the negation of a.

— Runtime Function: unsigned int ____udivsi3__ (unsigned int a, unsigned int b)
— Runtime Function: unsigned long ____udivdi3__ (unsigned long a, unsigned long b)
— Runtime Function: unsigned long long ____udivti3__ (unsigned long long a, unsigned long long b)
> These functions return the quotient of the unsigned division of a
> and b.

— Runtime Function: unsigned long ____udivmoddi3__ (unsigned long a, unsigned long b, unsigned long \*c)
— Runtime Function: unsigned long long ____udivti3__ (unsigned long long a, unsigned long long b, unsigned long long \*c)
> These functions calculate both the quotient and remainder of the unsigned
> division of a and b. The return value is the quotient, and
> the remainder is placed in variable pointed to by c.

— Runtime Function: unsigned int ____umodsi3__ (unsigned int a, unsigned int b)
— Runtime Function: unsigned long ____umoddi3__ (unsigned long a, unsigned long b)
— Runtime Function: unsigned long long ____umodti3__ (unsigned long long a, unsigned long long b)
> These functions return the remainder of the unsigned division of a
> and b.

#### 4.1.2 Comparison functions

The following functions implement integral comparisons. These functions
implement a low-level compare, upon which the higher level comparison
operators (such as less than and greater than or equal to) can be
constructed. The returned values lie in the range zero to two, to allow
the high-level operators to be implemented by testing the returned
result using either signed or unsigned comparison.

— Runtime Function: int ____cmpdi2__ (long a, long b)
— Runtime Function: int ____cmpti2__ (long long a, long long b)
> These functions perform a signed comparison of a and b. If
> a is less than b, they return 0; if a is greater than
> b, they return 2; and if a and b are equal they return 1.

— Runtime Function: int ____ucmpdi2__ (unsigned long a, unsigned long b)
— Runtime Function: int ____ucmpti2__ (unsigned long long a, unsigned long long b)
> These functions perform an unsigned comparison of a and b.
> If a is less than b, they return 0; if a is greater than
> b, they return 2; and if a and b are equal they return 1.

#### 4.1.3 Trapping arithmetic functions

The following functions implement trapping arithmetic. These functions
call the libc function `abort` upon signed arithmetic overflow.

— Runtime Function: int ____absvsi2__ (int a)
— Runtime Function: long ____absvdi2__ (long a)
> These functions return the absolute value of a.

— Runtime Function: int ____addvsi3__ (int a, int b)
— Runtime Function: long ____addvdi3__ (long a, long b)
> These functions return the sum of a and b; that is
> a `+` b.

— Runtime Function: int ____mulvsi3__ (int a, int b)
— Runtime Function: long ____mulvdi3__ (long a, long b)
> The functions return the product of a and b; that is
> a `*` b.

— Runtime Function: int ____negvsi2__ (int a)
— Runtime Function: long ____negvdi2__ (long a)
> These functions return the negation of a; that is `-`a.

— Runtime Function: int ____subvsi3__ (int a, int b)
— Runtime Function: long ____subvdi3__ (long a, long b)
> These functions return the difference between b and a;
> that is a `-` b.

#### 4.1.4 Bit operations

— Runtime Function: int ____clzsi2__ (int a)
— Runtime Function: int ____clzdi2__ (long a)
— Runtime Function: int ____clzti2__ (long long a)
> These functions return the number of leading 0-bits in a, starting
> at the most significant bit position. If a is zero, the result is
> undefined.

— Runtime Function: int ____ctzsi2__ (int a)
— Runtime Function: int ____ctzdi2__ (long a)
— Runtime Function: int ____ctzti2__ (long long a)
> These functions return the number of trailing 0-bits in a, starting
> at the least significant bit position. If a is zero, the result is
> undefined.

— Runtime Function: int ____ffsdi2__ (long a)
— Runtime Function: int ____ffsti2__ (long long a)
> These functions return the index of the least significant 1-bit in a,
> or the value zero if a is zero. The least significant bit is index
> one.

— Runtime Function: int ____paritysi2__ (int a)
— Runtime Function: int ____paritydi2__ (long a)
— Runtime Function: int ____parityti2__ (long long a)
> These functions return the value zero if the number of bits set in
> a is even, and the value one otherwise.

— Runtime Function: int ____popcountsi2__ (int a)
— Runtime Function: int ____popcountdi2__ (long a)
— Runtime Function: int ____popcountti2__ (long long a)
> These functions return the number of bits set in a.

— Runtime Function: int32_t ____bswapsi2__ (int32_t a)
— Runtime Function: int64_t ____bswapdi2__ (int64_t a)
> These functions return the a byteswapped.
