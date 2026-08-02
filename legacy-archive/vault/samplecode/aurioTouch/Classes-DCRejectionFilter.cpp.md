---
title: aurioTouch
apple_id: DTS40007770
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-08-12'
source_url: https://developer.apple.com/library/archive/samplecode/aurioTouch/Listings/Classes_DCRejectionFilter_cpp.html
archived_at: '2026-07-18T03:28:52.492353Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [aurioTouch](aurioTouch.md)


[Next](Classes-FFTHelper.cpp.md)[Previous](Classes-AudioController.mm.md)

# Classes/DCRejectionFilter.cpp

```c
/*

 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 This class implements a DC Rejection Filter which is used to get rid of the DC component in an audio signal

 */

#include "DCRejectionFilter.h"


const Float32 kDefaultPoleDist = 0.975f;


DCRejectionFilter::DCRejectionFilter()
{
    mY1 = mX1 = 0;
}


DCRejectionFilter::~DCRejectionFilter()
{
}


void DCRejectionFilter::ProcessInplace(Float32* ioData, UInt32 numFrames)
{
    for (UInt32 i=0; i < numFrames; i++)
    {
        Float32 xCurr = ioData[i];
        ioData[i] = ioData[i] - mX1 + (kDefaultPoleDist * mY1);
        mX1 = xCurr;
        mY1 = ioData[i];
    }
}
```

[Next](Classes-FFTHelper.cpp.md)[Previous](Classes-AudioController.mm.md)

