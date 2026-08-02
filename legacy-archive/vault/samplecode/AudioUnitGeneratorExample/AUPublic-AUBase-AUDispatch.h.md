---
title: AudioUnitGeneratorExample
apple_id: DTS40008637
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2012-10-08'
source_url: https://developer.apple.com/library/archive/samplecode/AUPinkNoise/Listings/AUPublic_AUBase_AUDispatch_h.html
archived_at: '2026-07-18T02:59:49.061830Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AudioUnitGeneratorExample](AudioUnitGeneratorExample.md)


[Next](AUPublic-AUBase-AUInputElement.cpp.md)[Previous](AUPublic-AUBase-AUDispatch.cpp.md)

Relevant replacement documents include:

- [http://developer.apple.com/library/mac/samplecode/sc2195/Introduction/Intro.html#//apple_ref/doc/uid/DTS40013969](https://developer.apple.com/library/mac/samplecode/sc2195/Introduction/Intro.html#//apple_ref/doc/uid/DTS40013969)

# AUPublic/AUBase/AUDispatch.h

```c
/*
 <codex> 
 <abstract>Part of CoreAudio Utility Classes</abstract>
 <\codex>
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

[Next](AUPublic-AUBase-AUInputElement.cpp.md)[Previous](AUPublic-AUBase-AUDispatch.cpp.md)

