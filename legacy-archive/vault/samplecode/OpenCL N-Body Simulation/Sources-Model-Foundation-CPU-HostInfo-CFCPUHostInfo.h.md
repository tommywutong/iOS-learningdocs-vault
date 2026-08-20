---
title: OpenCL N-Body Simulation
apple_id: TP40016610
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_NBody_Simulation/Listings/Sources_Model_Foundation_CPU_HostInfo_CFCPUHostInfo_h.html
archived_at: '2026-07-18T03:17:35.773125Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL N-Body Simulation](OpenCL%20N-Body%20Simulation.md)


[Next](Sources-Model-Foundation-CPU-Load-CFCPULoad.h.md)[Previous](Sources-Model-Foundation-CPU-HostInfo-CFCPUHostInfo.mm.md)

# Sources/Model/Foundation/CPU/HostInfo/CFCPUHostInfo.h

```objc
/*
 <codex>
 <abstract>
 Utility class for acquiring host (cpu) info array.
 </abstract>
 </codex>
 */

#ifndef _CORE_FOUNDATION_CPU_HOST_INFO_H_
#define _CORE_FOUNDATION_CPU_HOST_INFO_H_

#import <mach/mach.h>

#ifdef __cplusplus

namespace CF
{
    namespace CPU
    {
        class HostInfo
        {
        public:
            HostInfo();

            HostInfo(const HostInfo& rHostInfo);

            virtual ~HostInfo();

            HostInfo& operator=(const HostInfo& rHostInfo);

            const kern_return_t error() const;

            const processor_flavor_t flavor() const;

            const natural_t cpus() const;
            const natural_t size() const;

            const natural_t user(const uint32_t& i)   const;
            const natural_t system(const uint32_t& i) const;
            const natural_t idle(const uint32_t& i)   const;
            const natural_t nice(const uint32_t& i)   const;

            const size_t total(const uint32_t& i) const;

        private:
            natural_t              mnCount;
            natural_t              mnSize;
            processor_flavor_t     mnFlavor;
            kern_return_t          mnError;
            processor_info_array_t mpInfo;
            mach_msg_type_number_t mnInfo;
        }; // HostInfo
    } // CPU
} // CF

#endif

#endif
```

[Next](Sources-Model-Foundation-CPU-Load-CFCPULoad.h.md)[Previous](Sources-Model-Foundation-CPU-HostInfo-CFCPUHostInfo.mm.md)

