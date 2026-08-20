---
title: Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor
  and Offline)
apple_id: DTS40013969
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-02-19'
source_url: https://developer.apple.com/library/archive/samplecode/sc2195/Listings/AUPublic_AUBase_AUDispatch_h.html
archived_at: '2026-07-26T19:54:12.109362Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor and Offline)](Audio%20Unit%20Examples%20%28AudioUnit%20Effect%2C%20Generator%2C%20Instrument%2C%20MIDI%20Processor%20and.md)


[Next](AUPublic-AUBase-AUInputElement.h.md)[Previous](AUPublic-AUBase-AUScopeElement.cpp.md)

# AUPublic/AUBase/AUDispatch.h

```c
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Part of Core Audio AUBase Classes
*/

#ifndef __AUDispatch_h__
#define __AUDispatch_h__

#if !defined(__COREAUDIO_USE_FLAT_INCLUDES__)
    #include <AudioUnit/AudioUnit.h>
#else
    #include "AudioUnit.h"
#endif

#if !CA_USE_AUDIO_PLUGIN_ONLY
/*! @function AudioUnitBaseGetParameter */
OSStatus CMgr_AudioUnitBaseGetParameter(    AUBase *                This,
                                            AudioUnitParameterID    inID,
                                            AudioUnitScope          inScope,
                                            AudioUnitElement        inElement,
                                            float *                 outValue);

/*! @function AudioUnitBaseSetParameter */
OSStatus CMgr_AudioUnitBaseSetParameter(    AUBase *                This,
                                            AudioUnitParameterID    inID,
                                            AudioUnitScope          inScope,
                                            AudioUnitElement        inElement,
                                            float                   inValue,
                                            UInt32                  inBufferOffset);

/*! @function AudioUnitBaseRender */
OSStatus CMgr_AudioUnitBaseRender(          AUBase *                This,
                                            AudioUnitRenderActionFlags *ioActionFlags,
                                            const AudioTimeStamp *  inTimeStamp,
                                            UInt32                  inBusNumber,
                                            UInt32                  inNumberFrames,
                                            AudioBufferList *       ioData);
#endif

#endif // __AUDispatch_h__
```

[Next](AUPublic-AUBase-AUInputElement.h.md)[Previous](AUPublic-AUBase-AUScopeElement.cpp.md)

