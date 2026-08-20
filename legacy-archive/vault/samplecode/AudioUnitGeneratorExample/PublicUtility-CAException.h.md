---
title: AudioUnitGeneratorExample
apple_id: DTS40008637
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2012-10-08'
source_url: https://developer.apple.com/library/archive/samplecode/AUPinkNoise/Listings/PublicUtility_CAException_h.html
archived_at: '2026-07-18T02:59:51.794393Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AudioUnitGeneratorExample](AudioUnitGeneratorExample.md)


[Next](PublicUtility-CAGuard.cpp.md)[Previous](PublicUtility-CADebugPrintf.h.md)

Relevant replacement documents include:

- [http://developer.apple.com/library/mac/samplecode/sc2195/Introduction/Intro.html#//apple_ref/doc/uid/DTS40013969](https://developer.apple.com/library/mac/samplecode/sc2195/Introduction/Intro.html#//apple_ref/doc/uid/DTS40013969)

# PublicUtility/CAException.h

```c
/*
 <codex> 
 <abstract>Part of CoreAudio Utility Classes</abstract>
 <\codex>
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

[Next](PublicUtility-CAGuard.cpp.md)[Previous](PublicUtility-CADebugPrintf.h.md)

