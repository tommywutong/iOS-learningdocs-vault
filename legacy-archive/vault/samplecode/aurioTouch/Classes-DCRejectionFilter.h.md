---
title: aurioTouch
apple_id: DTS40007770
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-08-12'
source_url: https://developer.apple.com/library/archive/samplecode/aurioTouch/Listings/Classes_DCRejectionFilter_h.html
archived_at: '2026-07-18T03:28:52.533890Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [aurioTouch](aurioTouch.md)


[Next](Classes-aurioTouchAppDelegate.h.md)[Previous](Classes-BufferManager.h.md)

# Classes/DCRejectionFilter.h

```c
/*

 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 This class implements a DC Rejection Filter which is used to get rid of the DC component in an audio signal

 */

#ifndef __aurioTouch3__DCRejectionFilter__
#define __aurioTouch3__DCRejectionFilter__


#include <AudioToolbox/AudioToolbox.h>


class DCRejectionFilter
{
public:
    DCRejectionFilter();
    ~DCRejectionFilter();

    void ProcessInplace(Float32* ioData, UInt32 numFrames);

private:
    Float32 mY1;
    Float32 mX1;
};

#endif /* defined(__aurioTouch3__DCRejectionFilter__) */
```

[Next](Classes-aurioTouchAppDelegate.h.md)[Previous](Classes-BufferManager.h.md)

