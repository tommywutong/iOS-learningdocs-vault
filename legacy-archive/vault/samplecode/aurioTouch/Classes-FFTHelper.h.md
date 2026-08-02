---
title: aurioTouch
apple_id: DTS40007770
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-08-12'
source_url: https://developer.apple.com/library/archive/samplecode/aurioTouch/Listings/Classes_FFTHelper_h.html
archived_at: '2026-07-18T03:28:52.919734Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [aurioTouch](aurioTouch.md)


[Next](Classes-EAGLView.h.md)[Previous](main.m.md)

# Classes/FFTHelper.h

```c
/*

 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 This class demonstrates how to use the Accelerate framework to take Fast Fourier Transforms (FFT) of the audio data. FFTs are used to perform analysis on the captured audio data

 */

#ifndef __aurioTouch3__FFTHelper__
#define __aurioTouch3__FFTHelper__


#include <Accelerate/Accelerate.h>


class FFTHelper
{
public:
    FFTHelper( UInt32 inMaxFramesPerSlice );
    ~FFTHelper();

    void ComputeFFT ( Float32* inAudioData, Float32* outFFTData );

private:
    FFTSetup            mSpectrumAnalysis;
    DSPSplitComplex     mDspSplitComplex;
    Float32             mFFTNormFactor;
    UInt32              mFFTLength;
    UInt32              mLog2N;
};

#endif /* defined(__aurioTouch3__FFTHelper__) */
```

[Next](Classes-EAGLView.h.md)[Previous](main.m.md)

