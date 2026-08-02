---
title: Test64BitMultiprec
apple_id: DTS10003947
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2006-06-09'
source_url: https://developer.apple.com/library/archive/samplecode/Test64BitMultiprec/Introduction/Intro.html
archived_at: '2026-07-18T03:26:25.367906Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# Test64BitMultiprec

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2006-06-09 Implements (PPC) A\*Y+B where A & B are arrays of 64-bit words and Y is a 64-bit integer |
| __Build Requirements:__ | Xcode 2.x or GCC 3.0 (makefile included) |
| __Runtime Requirements:__ | Mac OS X |

The samples in this project are explained by "Special applications of 64-bit arithetic: Acceleration on the Apple G5." (enclosed as: 64bit_multiprec.pdf).
addmul3asm.S, addmul4asm.S are two different 64-bit PowerPC G5 implementations of the operation A\*Y+B, where A and B are arrays of 64-bit words and Y is a 64-bit integer. These routines are described in more detail in the paper.
addmulv2.c illustrates using vecLib as a straightforward alternative to the 64-bit optimized multi-precision multiplication routine described in the paper.
modmul64asm_2.S is a 64-bit routine to compute A\*B (mod C) where A, B, and C are 64-bit quantities and a reciprocal for C has been precomputed.

[Next](ReadMe.txt.md)

