---
title: OpenCL_OceanWave
apple_id: DTS40009447
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2011-04-13'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_OceanWave/Introduction/Intro.html
archived_at: '2026-07-18T03:17:44.018663Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

Current information on this Developer Library topic can be found here:

- [Performance > Multiprocessing](https://developer.apple.com/referencelibrary/Performance/idxMultiprocessing-date.html)

# OpenCL_OceanWave

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.1, 2011-04-13 Fixed the issue were if CL initialization failed, we were not propagating error upstream correctly and thus not terminating the application, resulting in crash later. glUniform4fv was not getting correct count parameter. Build issue on Lion. Demo now links against 10.6 sdk. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnbug4wvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Mac OS X 10.6 |
| __Runtime Requirements:__ | Mac OS X 10.6 OpenCL 1.0 compliant hardware |

Demonstrates animating ocean water wave using attenuated random fourier spectrum and FFT

[Next](ReadMe.txt.md)

