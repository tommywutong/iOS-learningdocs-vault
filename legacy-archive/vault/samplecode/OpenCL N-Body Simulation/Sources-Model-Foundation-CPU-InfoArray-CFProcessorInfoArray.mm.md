---
title: OpenCL N-Body Simulation
apple_id: TP40016610
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_NBody_Simulation/Listings/Sources_Model_Foundation_CPU_InfoArray_CFProcessorInfoArray_mm.html
archived_at: '2026-07-18T03:17:35.959251Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL N-Body Simulation](OpenCL%20N-Body%20Simulation.md)


[Next](Sources-Model-Foundation-CPU-HostInfo-CFCPUHostInfo.mm.md)[Previous](Sources-Model-Foundation-CPU-InfoArray-CFProcessorInfoArray.h.md)

# Sources/Model/Foundation/CPU/InfoArray/CFProcessorInfoArray.mm

```objc
/*
 <codex>
 <import>CFProcessorInfoArray.h</import>
 </codex>
 */

#include <mach/vm_map.h>

#import "CFProcessorInfoArray.h"

typedef vm_address_t * vm_address_ref;

processor_info_array_t CF::ProcessorInfoArrayCreate(const natural_t& nSize,
                                                    kern_return_t& err)
{
    processor_info_array_t pInfo = nullptr;

    err = (nSize) ? KERN_SUCCESS : KERN_INVALID_ARGUMENT;

    if(err == KERN_SUCCESS)
    {
        err = vm_allocate(mach_task_self(),
                          vm_address_ref(&pInfo),
                          nSize,
                          VM_FLAGS_ANYWHERE);
    } // if

    return pInfo;
} // ProcessorInfoArrayCreate

processor_info_array_t CF::ProcessorInfoArrayCreateCopy(const natural_t& nSizeDst,
                                                        processor_info_array_t pInfoSrc,
                                                        kern_return_t& err)
{
    processor_info_array_t pInfoDst = nullptr;

    err = (nSizeDst) ? KERN_SUCCESS : KERN_INVALID_ARGUMENT;

    if(err == KERN_SUCCESS)
    {
        err = vm_allocate(mach_task_self(),
                          vm_address_ref(&pInfoDst),
                          nSizeDst,
                          VM_FLAGS_ANYWHERE);

        if(err == KERN_SUCCESS)
        {
            err = vm_copy(mach_task_self(),
                          vm_address_t(pInfoSrc),
                          nSizeDst,
                          vm_address_t(pInfoDst));
        } // if
    } // if

    return pInfoDst;
} // ProcessorInfoArrayCreateCopy

kern_return_t CF::ProcessorInfoArrayCopy(const natural_t& nSize,
                                         processor_info_array_t pInfoSrc,
                                         processor_info_array_t pInfoDst)
{
    kern_return_t err = (nSize) ? KERN_SUCCESS : KERN_INVALID_ARGUMENT;

    if(err == KERN_SUCCESS)
    {
        err = vm_copy(mach_task_self(),
                      vm_address_t(pInfoSrc),
                      nSize,
                      vm_address_t(pInfoDst));
    } // if

    return err;
} // ProcessorInfoArrayCopy

kern_return_t CF::ProcessorInfoArrayDelete(const natural_t& nSize,
                                           processor_info_array_t pInfo)
{
    kern_return_t err = (nSize) ? KERN_SUCCESS : KERN_INVALID_ARGUMENT;

    if(err == KERN_SUCCESS)
    {
        err = vm_deallocate(mach_task_self(), vm_address_t(pInfo), nSize);

        pInfo = nullptr;
    } // if

    return err;
} // ProcessorInfoArrayDelete
```

[Next](Sources-Model-Foundation-CPU-HostInfo-CFCPUHostInfo.mm.md)[Previous](Sources-Model-Foundation-CPU-InfoArray-CFProcessorInfoArray.h.md)

