---
title: AltiVec/SSE Migration Guide
apple_id: TP40002729
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2005-09-08'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/Accelerate_sse_migration/migration_intro/migration_intro.html
archived_at: '2026-07-18T01:39:31.366688Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](AltiVec%20to%20SSE%20Migration%20Overview.md)

# Introduction to AltiVec/SSE Migration Guide

_AltiVec/SSE Migration Guide_ will assist experienced developers who need to migrate their vector-oriented code from the PowerPC AltiVec extensions to the Intel x86 SSE extensions. Both of these are sets of SIMD (single instruction, multiple data) instructions, accessible through C intrinsics. The instructions operate on special sets of 128-bit registers that can be used to hold vectors of smaller-sized data, to be operated on in parallel.

The two sets of instructions serve the same purposes, but are implemented differently; porting of algorithms from one to the other must be done carefully.

Most work involving vector-oriented calculations can be done via Apple’s Accelerate frameworks, which provide higher-level functions for image processing, signal processing, linear algebra, vector math, and operations on large numbers. The advantage of using these frameworks is that the hardware dependencies are abstracted away by highly optimized library code that will be maintained not only for PowerPC and Apple’s initial Intel processors, but also for future processors.

Developers who have already written AltiVec code should consider adopting the Accelerate frameworks, instead of porting to SSE. However, some developers will need to port their code, or to write new AltiVec and SSE versions of new algorithms. Similarly, those who are porting Windows applications to Mac OS X may need to port existing SSE code to AltiVec.

Any developer who needs to port existing AltiVec code to SSE or vice versa, or who needs to write custom-optimized code for both architectures.

This document is organized into the following chapters:

- [AltiVec to SSE Migration Overview](AltiVec%20to%20SSE%20Migration%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdomrzfvbuqmrqgywviucykjcummjqge) This chapter introduces basic information on migrating vector-oriented code from the PowerPC AltiVec extensions to the Intel x86 SSE extensions.
- [Programming SSE in C](Programming%20SSE%20in%20C.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdomrzfvbuqmrug4wviucykjcummjqge) This chapter describes the intrinsics and data types provided for programming SSE in C.
- [Translating Altivec to SSE](Translating%20Altivec%20to%20SSE.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdomrzfvbuqmruhawviucykjcummjqge) This chapter provides in-depth tutorial information on translating AltiVec to to SSE code.

The document assumes the following:

- Your application runs in Mac OS X.

  Your application can use any of the Mac OS X development environments: Carbon, Cocoa, Java, or BSD UNIX.

  If your application runs in a version of the Mac OS that is earlier than Mac OS X version 10.0, you should first read [Carbon Porting Guide](../../Carbon/Carbon%20Porting%20Guide/Introduction%20to%20Carbon%20Porting%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojr) and Technical Note TN2003 [Moving Your Code to Mac OS X](https://developer.apple.com/technotes/tn/tn2003.html).

  If your application runs in the UNIX operating system but not specifically in Mac OS X, you should first read [Porting UNIX/Linux Applications to Mac OS X](../../Porting/Porting%20UNIX-Linux%20Applications%20to%20OS%20X/Introduction%20to%20Porting%20UNIX-Linux%20Applications%20to%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambt).

  If your application runs only in the Windows operating system, you should first read [Porting to Mac OS X from Windows Win32 API](../../Porting/Porting%20to%20Mac%20OS%20X%20from%20Windows%20Win32%20API/Porting%20to%20Mac%20OS%20X%20from%20Windows%20Win32%20API.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge4ta2i).
- You know how to use Xcode.

  Currently Xcode is the only GUI tool available that compiles code to run universally.

  If you are unfamiliar with Xcode, you might want to take a look at Xcode 2.1 User Guide.

  If you have been using CodeWarrior, you should read [Moving Projects from CodeWarrior to Xcode](../../Developer%20Tools/Porting%20CodeWarrior%20Projects%20to%20Xcode/Introduction%20to%20Porting%20CodeWarrior%20Projects%20to%20Xcode.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrg4ydq).

The term _x86_ is a generic term used in some parts of this book to refer to the class of microprocessors manufactured by Intel. This book uses the term x86 as a synonym for IA-32 (Intel Architecture 32-bit).

[Next](AltiVec%20to%20SSE%20Migration%20Overview.md)

