---
title: VelEng Multiprecision
apple_id: DTS10000459
resource_type: Sample Code
platform: macOS
topic: Mathematical Computation
technology: Accelerate
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/VelEng_Multiprecision/Introduction/Intro.html
archived_at: '2026-07-18T03:27:43.998595Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](vfactor%20source-factor.c.md)

# VelEng Multiprecision

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 An implementation of arbitrary precision arithmetic using the PowerPC Velocity-Engine (G4) vector instructions. |
| __Build Requirements:__ | Xcode v2.1, gcc 3.3 |
| __Runtime Requirements:__ | Mac OS X 10.3, PowerPC Velocity-Engine |

An implementation of arbitrary precision arithmetic using the PowerPC Velocity-Engine (G4) vector instructions. We first define essential digit size of a multiprecision integer to be 128 bits, in view of the Velocity Engine architecture. By designing a general purpose vector library comprised of multiplication, square, bit shift and bitwise comparison, we have achieved significant speedups over PowerPC G3 scalar (base-2^16 ) implementation, or even hand-tuned assembly (base-2^32 ) packages. In particular, vector multiplications enjoy performance improvements ranging from 3:1 to 10:1 over their scalar counterpart, depending on operand bit size. An application for general purpose integer factoring was written and is able to factor large integers with speedups factors roughly in the aforementioned range. A second, large convolution application was written to settle a certain research problem; in this instance a length-2 15 convolution of 512-bit elements is performed. Requirements: G4 Keywords: Velocity Engine, AlitVec, Multiprecision arithmetic, arbitrary precision arithmetic,

[Next](vfactor%20source-factor.c.md)

