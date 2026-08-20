---
title: Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor
  and Offline)
apple_id: DTS40013969
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-02-19'
source_url: https://developer.apple.com/library/archive/samplecode/sc2195/Listings/AUPublic_AUBase_AUOutputElement_h.html
archived_at: '2026-07-26T19:54:12.404067Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor and Offline)](Audio%20Unit%20Examples%20%28AudioUnit%20Effect%2C%20Generator%2C%20Instrument%2C%20MIDI%20Processor%20and.md)


[Next](AUPublic-AUBase-AUInputElement.cpp.md)[Previous](AUPublic-AUBase-AUScopeElement.h.md)

# AUPublic/AUBase/AUOutputElement.h

```swift
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Part of Core Audio AUBase Classes
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

[Next](AUPublic-AUBase-AUInputElement.cpp.md)[Previous](AUPublic-AUBase-AUScopeElement.h.md)

