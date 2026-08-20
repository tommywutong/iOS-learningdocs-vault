---
title: OpenCL N-Body Simulation
apple_id: TP40016610
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_NBody_Simulation/Listings/Sources_Model_Foundation_CPU_InfoArray_CFProcessorInfoArray_h.html
archived_at: '2026-07-18T03:17:35.887675Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL N-Body Simulation](OpenCL%20N-Body%20Simulation.md)


[Next](Sources-Model-Foundation-CPU-InfoArray-CFProcessorInfoArray.mm.md)[Previous](Sources-Model-Foundation-Frame-CTFrame.mm.md)

# Sources/Model/Foundation/CPU/InfoArray/CFProcessorInfoArray.h

```objc
/*
 <codex>
 <abstract>
 Utility methods for processor info array management.
 </abstract>
 </codex>
 */

#ifndef _CORE_FOUNDATION_PROCESSOR_INFO_ARRAY_H_
#define _CORE_FOUNDATION_PROCESSOR_INFO_ARRAY_H_

#import <mach/mach.h>

#ifdef __cplusplus

namespace CF
{
    processor_info_array_t ProcessorInfoArrayCreate(const natural_t& nSize,
                                                    kern_return_t& err);

    processor_info_array_t ProcessorInfoArrayCreateCopy(const natural_t& nSizeDst,
                                                        processor_info_array_t pInfoSrc,
                                                        kern_return_t& err);

    kern_return_t ProcessorInfoArrayCopy(const natural_t& nSize,
                                         processor_info_array_t pInfoSrc,
                                         processor_info_array_t pInfoDst);

    kern_return_t ProcessorInfoArrayDelete(const natural_t& nSize,
                                           processor_info_array_t pInfo);
} // CF

#endif

#endif
```

[Next](Sources-Model-Foundation-CPU-InfoArray-CFProcessorInfoArray.mm.md)[Previous](Sources-Model-Foundation-Frame-CTFrame.mm.md)

