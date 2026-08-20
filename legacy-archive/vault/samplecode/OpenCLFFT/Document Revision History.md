---
title: OpenCL_FFT
apple_id: DTS40009395
resource_type: Sample Code
platform: macOS
topic: Mathematical Computation
technology: OpenCL
published: '2012-06-26'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_FFT/History/History.html
archived_at: '2026-07-18T03:17:33.553067Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL_FFT](OpenCLFFT.md)


[Previous](procs.h.md)

# Document Revision History

This table describes the changes to _OpenCL_FFT_.

| __Date__ | __Notes__ |
| 2012-06-26 | Fix build warnings |
| 2010-08-18 | Fix a bug where results were wrong if max work group size was restricted to <= 64 |
| 2010-02-10 | Fix a bug in the Twist kernel where global and local work dimension calculations were swapped. |
| 2010-01-29 | Fixed a warning in fft_execute.cpp where the ‘inPlaceDone’ flag may be used before it is initialized. |
| 2009-12-07 | Fix a failures due to the requested local dimension exceeding the value returned by clGetKernelWorkGroupInfo on some GPUs. |
| 2009-11-16 | This sample demonstrates how to use OpenCL and the GPU to compute Fast Fourier Transforms. |

[Previous](procs.h.md)

