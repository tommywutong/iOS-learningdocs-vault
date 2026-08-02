---
title: OpenCL Parallel Prefix Sum (aka Scan) Example
apple_id: DTS40008183
resource_type: Sample Code
platform: macOS
topic: Performance
technology: OpenCL
published: '2017-09-19'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_Parallel_Prefix_Sum_Example/Introduction/Intro.html
archived_at: '2026-07-18T03:17:50.578790Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](scankernel.cl.md)

# OpenCL Parallel Prefix Sum (aka Scan) Example

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.5, 2017-09-19 Fix path issue that prevented loading the input code. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqmjygmwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Mac OS X v10.6 or later, Xcode 3.2 or later. |
| __Runtime Requirements:__ | Mac OS X v10.6 or later |

This example shows how to perform an efficient parallel prefix sum (aka Scan) using OpenCL. Scan is a common data parallel primitive which can be used for variety of different operations -- this example uses local memory for storing partial sums and avoids memory bank conflicts on architectures which serialize memory operations that are serviced on the same memory bank by offsetting the loads and stores based on the size of the local group and the number of memory banks (see appropriate macro definition). As a result, this example requires that the local group size > 1.

[Next](scankernel.cl.md)

