---
title: dist_fft
apple_id: DTS10003377
resource_type: Sample Code
platform: macOS
topic: Mathematical Computation
technology: Accelerate
published: '2004-08-23'
source_url: https://developer.apple.com/library/archive/samplecode/dist_fft/Introduction/Intro.html
archived_at: '2026-07-18T03:29:03.695404Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](distfft.c.md)

# dist_fft

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2004-08-23 Gigaelement FFTs on Apple G5 clusters |
| __Build Requirements:__ | Xcode 1.5 |
| __Runtime Requirements:__ | Mac OS X AltiVec G5 |

The paper gives explicit recipes for 1-dim. (length 2^30), 2-dim. (2^15-by-2^15), and 3-dim. (2^10-by-2^10-by- 2^10) FFTs, each of these involving a gigaelement of (complex) data. Each such FFT is performed via tight coupling, with "all-to-all" machine communication, as befits an essentially "holographic" algorithm like the FFT.

[Next](distfft.c.md)

