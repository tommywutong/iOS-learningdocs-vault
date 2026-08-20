---
title: OpenCL N-Body Simulation
apple_id: TP40016610
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_NBody_Simulation/Listings/Sources_Model_Foundation_CPU_Load_CFCPULoad_h.html
archived_at: '2026-07-18T03:17:35.999172Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL N-Body Simulation](OpenCL%20N-Body%20Simulation.md)


[Next](Sources-Model-Foundation-CPU-Load-CFCPULoad.mm.md)[Previous](Sources-Model-Foundation-CPU-HostInfo-CFCPUHostInfo.h.md)

# Sources/Model/Foundation/CPU/Load/CFCPULoad.h

```objc
/*
 <codex>
 <abstract>
 Utility class for calculating load on CPU cores.
 </abstract>
 </codex>
 */

#ifndef _CORE_FOUNDATION_CPU_LOAD_H_
#define _CORE_FOUNDATION_CPU_LOAD_H_

#import <cstdlib>

#ifdef __cplusplus

namespace CF
{
    namespace CPU
    {
        class Load
        {
        public:
            Load();

            Load(const Load& rLoad);

            virtual ~Load();

            Load& operator=(const Load& rLoad);

            const size_t total() const;
            const size_t user()  const;

            double percentage();

        private:
            size_t mnTotalTime;
            size_t mnUserTime;
        }; // Load
    } // CPU
} // CF

#endif

#endif
```

[Next](Sources-Model-Foundation-CPU-Load-CFCPULoad.mm.md)[Previous](Sources-Model-Foundation-CPU-HostInfo-CFCPUHostInfo.h.md)

