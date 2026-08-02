---
title: OS X ABI Function Call Guide
apple_id: TP40002521
resource_type: Guide
platform: macOS
topic: General
technology: null
published: '2010-11-17'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/LowLevelABI/000-Introduction/introduction.html
archived_at: '2026-07-15T07:25:12.868265Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](32-bit%20PowerPC%20Function%20Calling%20Conventions.md)

# Introduction to OS X ABI Function Call Guide

This document describes the function-calling conventions used in the OS X ABI on the architectures on which OS X can run. Specifically, 32-bit PowerPC, 64-bit PowerPC, and IA-32.

The information in this document is based on OS X v10.4 and later, and Xcode Tools 2.2 and later.

This document is intended for developers interested in the calling conventions used in the OS X ABI on each of the supported architectures. This information is especially useful to developers of development tools.

This document contains the following articles:

- [32-bit PowerPC Function Calling Conventions](32-bit%20PowerPC%20Function%20Calling%20Conventions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdimzyfvjvomrq)
- [64-bit PowerPC Function Calling Conventions](64-bit%20PowerPC%20Function%20Calling%20Conventions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdinzrfvjvomju)
- [IA-32 Function Calling Conventions](IA-32%20Function%20Calling%20Conventions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdiojsfvjvona)
- [x86-64 Function Calling Conventions](x86-64%20Function%20Calling%20Conventions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tamzvfvjvomi)

Each of these articles describes the data types that can be used to manipulate the arguments and results of function calls, how routines pass arguments to the functions they call, and how functions pass results to their callers. They also list the registers available in each architecture and whether their value is preserved after a function call.

The following documents contain information related to function calls in OS X.

- _PowerPC Numerics_ in Performance Documentation. Describes how floating-point operations are implemented in OS X.
- _System V Application Binary Interface: Intel386 Architecture Processor Supplement_. Describes the data representation, register usage, stack management, and function-calling sequence the System V ABI uses in the IA-32 architecture. This document is located at [http://www.sco.com/developers/devspecs/abi386-4.pdf](http://www.sco.com/developers/devspecs/abi386-4.pdf).
- _System V Application Binary Interface AMD64 Architecture Processor Supplement_. Describes the System V x86-64 ABI, on which the function calling conventions used in the OS X x86-64 environment are based.
[Next](32-bit%20PowerPC%20Function%20Calling%20Conventions.md)

