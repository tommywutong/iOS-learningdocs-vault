---
title: OpenCL N-Body Simulation
apple_id: TP40016610
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_NBody_Simulation/Listings/Sources_Model_Foundation_Queue_CFQueue_mm.html
archived_at: '2026-07-18T03:17:37.259842Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL N-Body Simulation](OpenCL%20N-Body%20Simulation.md)


[Next](Sources-Model-Foundation-Hardware-CFQueryHardware.mm.md)[Previous](Sources-Model-Foundation-Queue-CFQueue.h.md)

# Sources/Model/Foundation/Queue/CFQueue.mm

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Utility functor for creating dispatch queues with a unique identifier
 */

#import <strstream>

#include "CFQueue.h"

CF::Queue::Queue(const dispatch_queue_attr_t& attrib)
{
    attribute = attrib;
    m_SQID    = "";
} // Constructor

CF::Queue::~Queue()
{
    attribute = nullptr;
    m_SQID    = "";
} // Destructor

const std::string CF::Queue::identifier() const
{
    return m_SQID;
} // identifier

dispatch_queue_t CF::Queue::operator()(const std::string& label)
{
    uint64_t qid = m_Device();

    std::strstream sqid;

    sqid << qid;

    if(label.empty())
    {
        m_SQID = sqid.str();
    } // if
    else
    {
        m_SQID  = label + ".";
        m_SQID += sqid.str();
    } // else

    m_SQID += "\0";

    return dispatch_queue_create(m_SQID.c_str(), attribute);
} // Operator()
```

[Next](Sources-Model-Foundation-Hardware-CFQueryHardware.mm.md)[Previous](Sources-Model-Foundation-Queue-CFQueue.h.md)

