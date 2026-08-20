---
title: iOS ABI Function Call Guide
apple_id: TP40009023
resource_type: Guide
platform: iOS
topic: Languages & Utilities
technology: null
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/Xcode/Conceptual/iPhoneOSABIReference/Introduction/Introduction.html
archived_at: '2026-07-27T06:57:07.423646Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](ARM64%20Function%20Calling%20Conventions.md)

# Introduction

This document describes the function-calling conventions used in the iOS ABI on the architectures on which iOS can run. Specifically, this document covers the ARM64 architecture, as well as the v7 and v6 revisions of the ARM 32-bit architecture.

The information in this document is based on iOS 2.0 and later, and Xcode 3.1 and later.

This document is intended for developers interested in the calling conventions used in the iOS ABI on each of the supported architectures. This information is especially useful to developers of development tools.

## Organization of This Document

This document contains the following articles:

- [ARM64 Function Calling Conventions](ARM64%20Function%20Calling%20Conventions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztombsfvjvomi)
- [ARMv7 Function Calling Conventions](ARMv7%20Function%20Calling%20Conventions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tamrsfvjvomi)
- [ARMv6 Function Calling Conventions](ARMv6%20Function%20Calling%20Conventions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tamrrfvjvomi)

Each of these articles describes how routines pass arguments to the functions they call, how functions pass results to their callers, and the data types that can be used to manipulate the arguments and results of function calls.

[Next](ARM64%20Function%20Calling%20Conventions.md)
