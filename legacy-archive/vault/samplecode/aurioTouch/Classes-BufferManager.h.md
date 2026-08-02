---
title: aurioTouch
apple_id: DTS40007770
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-08-12'
source_url: https://developer.apple.com/library/archive/samplecode/aurioTouch/Listings/Classes_BufferManager_h.html
archived_at: '2026-07-18T03:28:52.450693Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [aurioTouch](aurioTouch.md)


[Next](Classes-DCRejectionFilter.h.md)[Previous](Classes-FFTHelper.cpp.md)

# Classes/BufferManager.h

```c
/*

 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 This class handles buffering of audio data that is shared between the view and audio controller

 */

#ifndef __aurioTouch3__BufferManager__
#define __aurioTouch3__BufferManager__

#include <AudioToolbox/AudioToolbox.h>
#include <libkern/OSAtomic.h>

#include "FFTHelper.h"


const UInt32 kNumDrawBuffers = 12;
const UInt32 kDefaultDrawSamples = 1024;


class BufferManager
{
public:
    BufferManager( UInt32 inMaxFramesPerSlice );
    ~BufferManager();

    void            SetDisplayMode ( UInt32 inDisplayMode ) { mDisplayMode = inDisplayMode; }
    UInt32          GetDisplayMode () { return mDisplayMode; }

    Float32**       GetDrawBuffers ()  { return mDrawBuffers; }
    void            CopyAudioDataToDrawBuffer( Float32* inData, UInt32 numFrames );
    void            CycleDrawBuffers();

    void            SetCurrentDrawBufferLength ( UInt32 inDrawBufferLen ) { mCurrentDrawBufferLen = inDrawBufferLen; }
    UInt32          GetCurrentDrawBufferLength ()   { return mCurrentDrawBufferLen; }

    bool            HasNewFFTData()     { return static_cast<bool>(mHasNewFFTData); };
    bool            NeedsNewFFTData()   { return static_cast<bool>(mNeedsNewFFTData); };

    void            CopyAudioDataToFFTInputBuffer( Float32* inData, UInt32 numFrames );
    UInt32          GetFFTOutputBufferLength() { return mFFTInputBufferLen / 2; }
    void            GetFFTOutput ( Float32* outFFTData );

private:
    UInt32          mDisplayMode;

    Float32*        mDrawBuffers[kNumDrawBuffers];
    UInt32          mDrawBufferIndex;
    UInt32          mCurrentDrawBufferLen;

    Float32*        mFFTInputBuffer;
    UInt32          mFFTInputBufferFrameIndex;
    UInt32          mFFTInputBufferLen;
    volatile int32_t mHasNewFFTData;
    volatile int32_t mNeedsNewFFTData;

    FFTHelper*      mFFTHelper;
};

#endif /* defined(__aurioTouch3__BufferManager__) */
```

[Next](Classes-DCRejectionFilter.h.md)[Previous](Classes-FFTHelper.cpp.md)

