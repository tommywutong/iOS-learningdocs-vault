---
title: Offline Compilation Using the OpenCL Compiler
apple_id: DTS40011196
resource_type: Sample Code
platform: macOS
topic: null
technology: OpenCL
published: '2014-03-11'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCLOfflineCompilation/Introduction/Intro.html
archived_at: '2026-07-18T03:17:33.118640Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# Offline Compilation Using the OpenCL Compiler

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.1, 2014-03-11 1. Modified the Makefile to use the new -arch flags. 2. Added an option to run the test on a 64bit GPU. 3. Added a check for whether the current architecture is compatible with the specified test option (cpu32|cpu64|gpu32|gpu64). If there is a mismatch, the test now prints a warning. 4. Added a '-h/--help' argument. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmjzgywvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode 4.0 or later, Mac OS X v10.7 or later |
| __Runtime Requirements:__ | Mac OS X v10.7 or later |

This sample demonstrates how developers can utilize the OpenCL offline compiler to transform their human-readable OpenCL source files into shippable bitcode. It includes an example Makefile that demonstrates how to invoke the compiler, and a self-contained OpenCL program that shows how to build a program from the generated bitcode. The sample covers the case of using bitcode on 64 and 32 bit CPU devices, as well as 32 bit GPU devices.

[Next](ReadMe.txt.md)

