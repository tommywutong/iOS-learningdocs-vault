---
title: OpenCL_OceanWave
apple_id: DTS40009447
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2011-04-13'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_OceanWave/History/History.html
archived_at: '2026-07-18T03:17:43.979675Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL_OceanWave](OpenCLOceanWave.md)


[Previous](oceansimulator.h.md)

Current information on this Developer Library topic can be found here:

- [Performance > Multiprocessing](https://developer.apple.com/referencelibrary/Performance/idxMultiprocessing-date.html)

# Document Revision History

This table describes the changes to _OpenCL_OceanWave_.

| __Date__ | __Notes__ |
| 2011-04-13 | Fixed the issue were if CL initialization failed, we were not propagating error upstream correctly and thus not terminating the application, resulting in crash later. glUniform4fv was not getting correct count parameter. Build issue on Lion. Demo now links against 10.6 sdk. |
| 2009-12-18 | Demonstrates animating ocean water wave using attenuated random fourier spectrum and FFT |

[Previous](oceansimulator.h.md)

