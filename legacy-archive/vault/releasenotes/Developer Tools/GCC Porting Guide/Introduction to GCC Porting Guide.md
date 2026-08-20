---
title: GCC Porting Guide
apple_id: TP40002069
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/releasenotes/DeveloperTools/GCC40PortingReleaseNotes/Introduction.html
archived_at: '2026-07-26T19:54:15.350312Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md)



# Retired Document

__Important:__
Xcode 4.2 and later do not support GCC. You should use the Clang compiler instead.

# Introduction to GCC Porting Guide

__Important__ Xcode 4.2 and later do not support GCC. You should use the Clang compiler instead.

Mac OS X v10.4 introduced a new version of the GCC compiler: version 4.0. This new compiler provided significant improvements for the compilation of C, C++, Objective-C, and Objective-C++. With these improvements, though, came stricter rules and better conformance to the C and C++ standards. As a result, developers may have encountered errors when compiling code that had previously compiled without error under GCC 3.3.

__Important:__ This document offers only guidance and tips on how to move your code to the newest revisions of the GCC compiler and is not the definitive reference for the compiler itself. If you need more information about GCC than is provided in this document, see _GNU C/C++/Objective-C 4.0.1 Compiler User Guide_. For a summary of compiler options, you can also consult the `gcc` man page.

This document provides advice for how to modify your code in ways that make it more compatible with the latest versions of GCC. Because of its improved support for uniform coding standards, compiling your code under GCC 4.0 or later should make it easier to develop code that compiles successfully on other platforms and with other compilers.

## Organization of This Document

This document includes the following articles:

- [General Guidelines for Using GCC](General%20Guidelines%20for%20Using%20GCC.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdsojyfvjvomi) offers general porting advice for developers coming to GCC 4.0 for the first time. It also discusses issues related to universal binaries and CodeWarrior migration.
- [Porting from GCC 3.3 to GCC 4.0](Porting%20from%20GCC%203.3%20to%20GCC%204.0.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanzrfvbeeq2ci5eegsq) provides specific information on how to migrate your code from GCC 3.3 to GCC 4.0.

## See Also

For reference information on the GCC compiler, see the following documents:

- _GNU C/C++/Objective-C 4.0.1 Compiler User Guide_
- `gcc` man page
