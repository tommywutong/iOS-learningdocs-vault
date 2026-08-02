---
title: Offline Compilation Using the OpenCL Compiler
apple_id: DTS40011196
resource_type: Sample Code
platform: macOS
topic: null
technology: OpenCL
published: '2014-03-11'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCLOfflineCompilation/History/History.html
archived_at: '2026-07-18T03:17:32.973997Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Offline Compilation Using the OpenCL Compiler](Offline%20Compilation%20Using%20the%20OpenCL%20Compiler.md)


[Previous](kernel.cl.md)

# Document Revision History

This table describes the changes to _Offline Compilation Using the OpenCL Compiler_.

| __Date__ | __Notes__ |
| 2014-03-11 | 1. Modified the Makefile to use the new -arch flags. 2. Added an option to run the test on a 64bit GPU. 3. Added a check for whether the current architecture is compatible with the specified test option (cpu32|cpu64|gpu32|gpu64). If there is a mismatch, the test now prints a warning. 4. Added a '-h/--help' argument. |
| 2011-08-23 | Demonstrates using the OpenCL offline compiler to produce and utilize bitcode for CPU and GPU devices. |

[Previous](kernel.cl.md)

