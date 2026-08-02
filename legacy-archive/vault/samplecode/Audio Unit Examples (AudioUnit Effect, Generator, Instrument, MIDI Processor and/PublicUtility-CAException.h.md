---
title: Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor
  and Offline)
apple_id: DTS40013969
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-02-19'
source_url: https://developer.apple.com/library/archive/samplecode/sc2195/Listings/PublicUtility_CAException_h.html
archived_at: '2026-07-26T19:54:11.656381Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor and Offline)](Audio%20Unit%20Examples%20%28AudioUnit%20Effect%2C%20Generator%2C%20Instrument%2C%20MIDI%20Processor%20and.md)


[Next](PublicUtility-CAHostTimeBase.h.md)[Previous](PublicUtility-CADebugMacros.cpp.md)

# PublicUtility/CAException.h

```swift
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Part of Core Audio Public Utility Classes
*/

#if !defined(__CAException_h__)
#define __CAException_h__

//=============================================================================
//  Includes
//=============================================================================

#if !defined(__COREAUDIO_USE_FLAT_INCLUDES__)
    #include <CoreAudio/CoreAudioTypes.h>
#else
    #include "CoreAudioTypes.h"
#endif

//=============================================================================
//  CAException
//=============================================================================

class CAException
{

public:
                    CAException(OSStatus inError) : mError(inError) {}
                    CAException(const CAException& inException) : mError(inException.mError) {}
    CAException&    operator=(const CAException& inException) { mError = inException.mError; return *this; }
                    ~CAException() {}

    OSStatus        GetError() const { return mError; }

protected:
    OSStatus        mError;
};

#define CATry                               try{
#define CACatch                             } catch(...) {}
#define CASwallowException(inExpression)    try { inExpression; } catch(...) {}

#endif
```

[Next](PublicUtility-CAHostTimeBase.h.md)[Previous](PublicUtility-CADebugMacros.cpp.md)

