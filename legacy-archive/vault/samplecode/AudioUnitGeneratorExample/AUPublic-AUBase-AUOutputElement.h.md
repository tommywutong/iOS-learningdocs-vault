---
title: AudioUnitGeneratorExample
apple_id: DTS40008637
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2012-10-08'
source_url: https://developer.apple.com/library/archive/samplecode/AUPinkNoise/Listings/AUPublic_AUBase_AUOutputElement_h.html
archived_at: '2026-07-18T02:59:49.246218Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AudioUnitGeneratorExample](AudioUnitGeneratorExample.md)


[Next](AUPublic-AUBase-AUPlugInDispatch.cpp.md)[Previous](AUPublic-AUBase-AUOutputElement.cpp.md)

Relevant replacement documents include:

- [http://developer.apple.com/library/mac/samplecode/sc2195/Introduction/Intro.html#//apple_ref/doc/uid/DTS40013969](https://developer.apple.com/library/mac/samplecode/sc2195/Introduction/Intro.html#//apple_ref/doc/uid/DTS40013969)

# AUPublic/AUBase/AUOutputElement.h

```c
/*
 <codex> 
 <abstract>Part of CoreAudio Utility Classes</abstract>
 <\codex>
*/
#ifndef __AUOutput_h__
#define __AUOutput_h__

#include "AUScopeElement.h"
#include "AUBuffer.h"

    /*! @class AUOutputElement */
class AUOutputElement : public AUIOElement {
public:
    /*! @ctor AUOutputElement */
                        AUOutputElement(AUBase *audioUnit);

    // AUElement override
    /*! @method SetStreamFormat */
    virtual OSStatus    SetStreamFormat(const CAStreamBasicDescription &desc);
    /*! @method NeedsBufferSpace */
    virtual bool        NeedsBufferSpace() const { return true; }
};

#endif // __AUOutput_h__
```

[Next](AUPublic-AUBase-AUPlugInDispatch.cpp.md)[Previous](AUPublic-AUBase-AUOutputElement.cpp.md)

