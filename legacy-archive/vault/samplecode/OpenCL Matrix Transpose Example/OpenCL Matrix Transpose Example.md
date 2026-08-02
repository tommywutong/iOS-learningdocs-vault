---
title: OpenCL Matrix Transpose Example
apple_id: DTS40008189
resource_type: Sample Code
platform: macOS
topic: Performance
technology: OpenCL
published: '2009-05-13'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_Matrix_Transpose_Example/Introduction/Intro.html
archived_at: '2026-07-18T03:17:35.198035Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# OpenCL Matrix Transpose Example

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.1, 2009-05-13 Updated to new API. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqmjyhewvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Mac OS X v10.6, Xcode 3.2 |
| __Runtime Requirements:__ | Mac OS X v10.6 |

This example shows how to efficiently perform a transpose of a matrix composed of M x N power-of-two elements for GPU architectures which require specific memory addressing to avoid memory bank conflicts.

Transposing large power-of-two matrices naively can easily cause bank conflicts which can severly affect the performance.

With appropriate padding and choice of local block size, good performance can be ensured.

In this example 64 work items are issued per work-group which individually operate small 32x2 sections to fill a 32x32 sub-matrix (over 8 iterations). The final 32 x 32 sub-matrix is transposed locally using local memory with one column padding to avoid bank conflicts. Performing the transpose in local memory allows the reads and writes to global memory to be coalesced.

The extra column padding is used to offset the write addresses, so that they don't conflict with the read requests.

Using a padding of 32 (or any odd multiple of GROUP_DIMX = 32) ensures that the reads and writes for each element in global memory will be offset and not operate on the same memory bank/channel/port.

This is important for the global memory write operations, since the column major indices are non-sequential and can cause global memory bank conflicts.

Global memory read requests will operate on sequential indices for the row-major elements, and will not conflict.

[Next](ReadMe.txt.md)

