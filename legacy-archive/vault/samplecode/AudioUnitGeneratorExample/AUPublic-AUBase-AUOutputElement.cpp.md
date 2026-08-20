---
title: AudioUnitGeneratorExample
apple_id: DTS40008637
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2012-10-08'
source_url: https://developer.apple.com/library/archive/samplecode/AUPinkNoise/Listings/AUPublic_AUBase_AUOutputElement_cpp.html
archived_at: '2026-07-18T02:59:49.200743Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AudioUnitGeneratorExample](AudioUnitGeneratorExample.md)


[Next](AUPublic-AUBase-AUOutputElement.h.md)[Previous](AUPublic-AUBase-AUInputElement.h.md)

Relevant replacement documents include:

- [http://developer.apple.com/library/mac/samplecode/sc2195/Introduction/Intro.html#//apple_ref/doc/uid/DTS40013969](https://developer.apple.com/library/mac/samplecode/sc2195/Introduction/Intro.html#//apple_ref/doc/uid/DTS40013969)

# AUPublic/AUBase/AUOutputElement.cpp

```c
/*
 <codex> 
 <abstract>AUOutputElement.h</abstract>
 <\codex>
*/
#include "AUOutputElement.h"
#include "AUBase.h"

AUOutputElement::AUOutputElement(AUBase *audioUnit) : 
    AUIOElement(audioUnit)
{
    AllocateBuffer();
}

OSStatus    AUOutputElement::SetStreamFormat(const CAStreamBasicDescription &desc)
{
    OSStatus result = AUIOElement::SetStreamFormat(desc);   // inherited
    if (result == AUBase::noErr)
        AllocateBuffer();
    return result;
}
```

[Next](AUPublic-AUBase-AUOutputElement.h.md)[Previous](AUPublic-AUBase-AUInputElement.h.md)

