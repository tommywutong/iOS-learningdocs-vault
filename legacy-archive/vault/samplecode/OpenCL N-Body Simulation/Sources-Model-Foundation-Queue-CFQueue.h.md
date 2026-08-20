---
title: OpenCL N-Body Simulation
apple_id: TP40016610
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_NBody_Simulation/Listings/Sources_Model_Foundation_Queue_CFQueue_h.html
archived_at: '2026-07-18T03:17:37.217887Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL N-Body Simulation](OpenCL%20N-Body%20Simulation.md)


[Next](Sources-Model-Foundation-Queue-CFQueue.mm.md)[Previous](Sources-Model-Foundation-CPU-Load-CFCPULoad.mm.md)

# Sources/Model/Foundation/Queue/CFQueue.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Utility functor for creating dispatch queues with a unique identifier
 */


#ifndef _CORE_FOUNDATION_QUEUE_H_
#define _CORE_FOUNDATION_QUEUE_H_

#import <random>
#import <string>

#import <Foundation/Foundation.h>

#ifdef __cplusplus

namespace CF
{
    class Queue
    {
    public:
        Queue(const dispatch_queue_attr_t& attribute = DISPATCH_QUEUE_SERIAL);

        virtual ~Queue();

        const std::string identifier() const;

        dispatch_queue_t operator()(const std::string& label);

    public:
        dispatch_queue_attr_t attribute;  // Dispatch queue attribute

    private:

        std::string        m_SQID;      // Dispatch queue label plus an attched id
        std::random_device m_Device;    // A device for random number generation
    };
} // Queue

#endif

#endif
```

[Next](Sources-Model-Foundation-Queue-CFQueue.mm.md)[Previous](Sources-Model-Foundation-CPU-Load-CFCPULoad.mm.md)

