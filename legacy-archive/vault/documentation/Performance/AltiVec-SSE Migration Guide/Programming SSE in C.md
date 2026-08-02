---
title: AltiVec/SSE Migration Guide
apple_id: TP40002729
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2005-09-08'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/Accelerate_sse_migration/migration_sse_C/migration_sse_C.html
archived_at: '2026-07-18T01:39:31.422805Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [AltiVec/SSE Migration Guide](Introduction%20to%20AltiVec-SSE%20Migration%20Guide.md)


[Next](Translating%20Altivec%20to%20SSE.md)[Previous](AltiVec%20to%20SSE%20Migration%20Overview.md)

# Programming SSE in C

This chapter describes the C data types and
intrinsics for use in programming SSE. It also shows how to detect
the availability of SSE3 at run time.

Like AltiVec, there is a C Programming Interface for SSE.
The two follow the same general design:

- The SIMD vector register is described in C as
  a special 128 bit data type.
- A series of function-like intrinsics are used to do SIMD style
  operations on those variables.

A notable difference is that many more intrinsics in the Intel
C programming extensions do not correspond 1:1 with instructions
in the ISA. Some developers may choose to limit their use of intrinsics
to those that map 1:1 with ISA, so as not to introduce hidden expensive
calculations.

_Data Types_

Intel defines three basic data types for SSE programming in
C:

__Table 2-1__  Basic SSE Data Types

| Any Packed Integer | float[4] | double[2] |
| __m128i | __m128 | __m128d |

These types are portable across the Gnu C Compiler, the Intel
C Compiler and various x86 C compilers targeted towards the Windows™
operating system.

One shortcoming of this set of data types is that the __m128i
type does not adequately describe the type and number of integer
elements in the __m128i vector. Both Intel and Microsoft defined
extensions to this subset to build in this information, and Apple
is no exception. The Accelerate.framework defines a series of vector
types that may be used for both AltiVec and SSE programming. It
is recommended that you use these, since the extra information will
make it easier to read your own code and make it possible for gdb
and xcode to properly format vector data. In addition, it will allow
you to share data types with AltiVec, which may simplify some programming
tasks. To use the types described below, use the following `#include` line:

```c
#include <Accelerate/Accelerate.h>
```


__Table 2-2__  Vector Data Types for Both AltiVec
and SSE

|  | 8-bit | 16-bit | 32-bit | 64-bit |
| signed | vSInt8 | vSInt16 | vSInt32 | vSInt64 |
| unsigned | vUInt8 | vUInt16 | vUInt32 | vUInt64 |
| floating point | - | - | vFloat | vDouble |

Please note that while the 64-bit types are indeed defined
for AltiVec by Accelerate.framework (and do work in the sense that
you can load and store vectors full of 64-bit data types in and
out of AltiVec register), there are no intrinsics (or instructions) defined
by AltiVec itself to do SIMD style operations on elements of this
size. The Accelerate.framework vBasicOps.h header declares some
functions to allow you to do packed 64-bit integer operations. (These
function using AltiVec intrinsics for smaller element sizes to build
up larger operations — see available source code for vBasicOps[available source code for vBasicOps](https://developer.apple.com/hardwaredrivers/ve/vector_libraries.html#vBasicOps).) Certain C language operators (e.g.
+, -, \*, /) may function with the vDouble type on GCC-4.0 and later
on PowerPC. However these simply map the vector type to the scalar
FPU and do standard arithmetic on the data using scalar code.

_Intrinsics_

Intel also defines a set of function-like intrinsics for programming
SSE in C. These are similar to those provided by AltiVec, with some
small differences. The Intel intrinsics use `_mm_-` instead
of `vec_-` as the operator
prefix. In addition, where AltiVec relies on C++ style function
overloading to decide based on argument type which particular flavor
of add to use among many, Intel has encoded this information as
a suffix on the intrinsic:

__Table 2-3__  Suffixes of SSE Intrinsics

| AltiVec | SSE |
| vec_add( vSInt8, vSInt8 ); | _mm_add_epi8( vSInt8, vSInt8 ); |
| vec_add( vSInt16, vSInt16 ); | _mm_add_epi16( vSInt16, vSInt16 ); |
| vec_add( vSInt32, vSInt32 ); | _mm_add_epi32( vSInt32, vSInt32 ); |
| vec_add( vFloat, vFloat ); | _mm_add_ps( vFloat, vFloat ); |
| - | _mm_add_epi64( vSInt64, vSInt64 ); |
| - | _mm_add_pd( vDouble, vDouble ); |
| - | _mm_add_ss( vFloat, vFloat ); |
| - | _mm_add_sd( vDouble, vDouble ); |

The suffixes are defined as follows:

__Table 2-4__  SSE Intrinsics Suffix Definitions

| suffix | description |
| -pi# | MMX (64-bit) vector containing packed #-bit integers |
| -pu# | MMX (64-bit) vector containing packed #-bit unsigned integers |
| -epi# | XMM (128-bit) vector containing packed #-bit integers |
| -epu# | XMM (128-bit) vector containing packed #-bit unsigned integers |
| -ps | XMM (128-bit) vector containing packed single precision floating point values |
| -ss | XMM (128-bit) vector containing one single precision floating point value |
| -pd | XMM (128-bit) vector containing packed double precision floating point values |
| -sd | XMM (128-bit) vector containing one double precision floating point value |
| -si64 | MMX (64-bit) vector containing a single 64-bit int |
| -si128 | XMM (128-bit) vector |

The various intrinsics are available in one of four headers,
one each for MMX, SSE, SSE2, and SSE3, when the corresponding ISA
appeared:

__Table 2-5__  Headers for SSE Intrinsics

| MMX | mmintrin.h |
| SSE | xmmintrin.h |
| SSE2 | emmintrin.h |
| SSE3 | pmmintrin.h |

The complete set of operations available for the Intel architecture
is detailed in the Intel Architecture Software Developer's Manual
(Volume 2, see link in the Introduction at top of page). There is
a partial AltiVec to SSE translation table in the Universal Binary Programming
Guide, Appendix B. More thorough conversion tables appear in various segments
entitled Algorithms/Conversions in the part of this document to
follow.

In addition, GCC has a set of GCC native non-portable intrinsics,
described here. Please note that these are subject to change. GCC
can and does regularly remove `__builtins` from
the programming environment.

_Sample function_

Here is a function that calculates the distances from the
origin {0,0} of a set of 4 {x,y} pairs in AltiVec:

```c
#include <Accelerate/Accelerate.h> //contains data types used
vFloat Distance( vFloat x, vFloat y )
{
    vFloat x2 = vec_madd( x, x, (vFloat) (-0.0f) ); //x * x
    vFloat distance2 = vec_madd( y, y, x2 ); // x*x + y*y
    return vsqrtf( distance2 ); //from Accelerate.framework
}
```

and here is the same thing in SSE:

```c
#include <Accelerate/Accelerate.h> //contains data types used
#include <xmmintrin.h> //declares _mm_* intrinsics
vFloat Distance( vFloat x, vFloat y )
{
    vFloat x2 = _mm_mul_ps( x, x); //x * x
    vFloat distance2 = _mm_add_ps(_mm_mul_ps( y, y), x2); // x*x + y*y
    return vsqrtf( distance2 ); //from Accelerate.framework
}
```

If you wish to tie yourself to GCC specific features, you
may investigate GCC's unified vector programming interfaces. That
would allow you to write the following and compile for both platforms:

```c
#include <Accelerate/Accelerate.h>
//Not portable to other compilers!
vFloat Distance( vFloat x, vFloat y )
{
    return vsqrtf( x*x + y*y ); //from Accelerate.framework
}
```

Since this is a new feature, it is suggested that you inspect
generated code thoroughly. In addition, there are clearly other
ways to do the same thing, using some inline functions or macros
using more traditional interfaces, that may preserve your compiler
independence.

SSE3 is an optional hardware feature on MacOS X for Intel.
If you wish to use SSE3 features, you must detect them first, similar
to how you are required to check for AltiVec. The same interfaces
are used, just a different `sysctlbyname()` selector:

```c
#include <sys/sysctl.h>
int IsSSE3Present( void )
{
    int hasSSE3 = 0;
    size_t length = sizeof( hasSSE3 );
    int error = sysctlbyname("hw.optional.sse3", &hasSSE3, &length, NULL, 0);
    if( 0 != error ) return 0;
    return hasSSE3;
}
```

Similar selectors exist for MMX, SSE and SSE2, but since those
are required features for MacOS X for Intel, it is not required
that you test them before using those vector extensions, in software
intended solely for MacOS X for Intel. (SSE is not available in
any format for MacOS X for PowerPC and AltiVec is not available
for MacOS X for Intel. When writing code for Universal Binaries
to run on MacOS X, you should conditionalize your code using appropriate
symbols like __VEC__ and __SSE2__ to prevent the compiler from seeing
vector code for unsupported architectures for each fork of the universal
binary.)

[Next](Translating%20Altivec%20to%20SSE.md)[Previous](AltiVec%20to%20SSE%20Migration%20Overview.md)

