---
title: 64-Bit Transition Guide for Cocoa
apple_id: TP40004247
resource_type: Guide
platform: macOS
topic: General
technology: null
published: '2013-09-17'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Cocoa64BitGuide/Introduction/Introduction.html
archived_at: '2026-07-15T07:11:59.016177Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Moving%20to%2064-Bit%20Addressing.md)

# Introduction to 64-Bit Transition Guide For Cocoa

OS X is undergoing a gradual transition to a 64-bit model. An 64-bit executable is a process that can support a 64-bit address space. In a 64-bit world pointers are 64 bits (eight bytes) and some integer types, once 32 bits, are now 64 bits. These fundamental changes required for 64-bit processes impact the programmatic interfaces of many of the frameworks of OS X, including Cocoa, in various ways.

This document explains the rationale for the 64-bit transition and describes the 64-bit related changes to the Cocoa API. It also discusses the steps you must take to convert existing Cocoa applications to a 64-bit model.

This document has the following chapters:

- [Moving to 64-Bit Addressing](Moving%20to%2064-Bit%20Addressing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denbxfvbuqmznknltc) provides background information about the 64-bit initiative for OS X and offers general advice for developers thinking about moving their Cocoa projects to 64-bit addressing.
- [64-Bit Changes To the Cocoa API](64-Bit%20Changes%20To%20the%20Cocoa%20API.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denbxfvbuqnbnknlts) describes the changes to data types for integers, floating-point values, enumeration constants, and other types of values in the Cocoa API.
- [Converting an Existing Application to 64-Bit](Converting%20an%20Existing%20Application%20to%2064-Bit.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denbxfvbuqnjnknltc) explains how to run the script for converting a Cocoa code base to 64-bit and describes modifications you may have to perform manually after the script is run.
- [Optimizing Memory Performance](Optimizing%20Memory%20Performance.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denbxfvbuqnrnknltc) describes common memory usage patterns in 64-bit applications and how to profile your application to find them.

As a prerequisite to this document, read _[64-Bit Transition Guide](../../Darwin/64-Bit%20Transition%20Guide/Introduction%20to%2064-Bit%20Transition%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanru)_, which describes in full detail the reasons for the 64-bit transition, the fundamental changes to OS X to support 64-bit addressing, and the general requirements and procedure for building 64-bit executables.

[Next](Moving%20to%2064-Bit%20Addressing.md)

