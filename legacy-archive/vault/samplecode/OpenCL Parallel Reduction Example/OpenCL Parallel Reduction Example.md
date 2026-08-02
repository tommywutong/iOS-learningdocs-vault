---
title: OpenCL Parallel Reduction Example
apple_id: DTS40008188
resource_type: Sample Code
platform: macOS
topic: Performance
technology: OpenCL
published: '2009-09-30'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_Parallel_Reduction_Example/Introduction/Intro.html
archived_at: '2026-07-18T03:17:51.174894Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# OpenCL Parallel Reduction Example

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.3, 2009-09-30 Corrected usage of barriers to comply with the OpenCL specification. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqmjyhawvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Mac OS X v10.6, Xcode 3.2 |
| __Runtime Requirements:__ | Mac OS X v10.6 |

This example shows how to perform an efficient parallel reduction using OpenCL. Reduce is a common data parallel primitive which can be used for variety of different operations -- this example computes the global sum for a large number of values, and includes kernels for integer and floating point vector types.

[Next](ReadMe.txt.md)

