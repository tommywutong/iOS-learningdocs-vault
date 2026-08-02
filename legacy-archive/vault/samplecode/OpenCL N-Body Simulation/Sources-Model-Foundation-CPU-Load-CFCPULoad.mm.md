---
title: OpenCL N-Body Simulation
apple_id: TP40016610
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_NBody_Simulation/Listings/Sources_Model_Foundation_CPU_Load_CFCPULoad_mm.html
archived_at: '2026-07-18T03:17:36.099762Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL N-Body Simulation](OpenCL%20N-Body%20Simulation.md)


[Next](Sources-Model-Foundation-Queue-CFQueue.h.md)[Previous](Sources-Model-Foundation-CPU-Load-CFCPULoad.h.md)

# Sources/Model/Foundation/CPU/Load/CFCPULoad.mm

```objc
/*
 <codex>
 <import>CFCPULoad.h</import>
 </codex>
 */

#import <iostream>

#import "CFCPUHostInfo.h"
#import "CFCPULoad.h"

using namespace CF::CPU;

Load::Load()
{
    mnTotalTime = 0;
    mnUserTime  = 0;
} // Constructor

Load::Load(const Load& rLoad)
{
    mnTotalTime = rLoad.mnTotalTime;
    mnUserTime  = rLoad.mnUserTime;
} // Copy Constructor

Load::~Load()
{
    mnTotalTime = 0;
    mnUserTime  = 0;
} // Constructor

Load& Load::operator=(const Load& rLoad)
{
    if(this != &rLoad)
    {
        mnTotalTime = rLoad.mnTotalTime;
        mnUserTime  = rLoad.mnUserTime;
    } // if

    return *this;
} // Assignment Operator

const size_t Load::total() const
{
    return mnTotalTime;
} // total

const size_t Load::user() const
{
    return mnUserTime;
} // user

double Load::percentage()
{
    double nResult = 0.0;

    HostInfo hostInfo;

    if(hostInfo.error() == KERN_SUCCESS)
    {
        size_t nTotalTime = 0;
        size_t nUserTime  = 0;

        natural_t nCPU;
        natural_t nCPUMax = hostInfo.cpus();

        for(nCPU = 0; nCPU < nCPUMax; ++nCPU)
        {
            nUserTime  += hostInfo.user(nCPU);
            nTotalTime += hostInfo.total(nCPU);
        } // for

        nResult = 100.0f * double(nUserTime  - mnUserTime) / double(nTotalTime - mnTotalTime);

        mnUserTime  = nUserTime;
        mnTotalTime = nTotalTime;
    } // if

    return nResult;
} // percentage
```

[Next](Sources-Model-Foundation-Queue-CFQueue.h.md)[Previous](Sources-Model-Foundation-CPU-Load-CFCPULoad.h.md)

