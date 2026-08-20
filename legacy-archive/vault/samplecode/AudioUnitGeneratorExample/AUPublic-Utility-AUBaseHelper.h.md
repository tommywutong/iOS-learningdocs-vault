---
title: AudioUnitGeneratorExample
apple_id: DTS40008637
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2012-10-08'
source_url: https://developer.apple.com/library/archive/samplecode/AUPinkNoise/Listings/AUPublic_Utility_AUBaseHelper_h.html
archived_at: '2026-07-18T02:59:50.213156Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AudioUnitGeneratorExample](AudioUnitGeneratorExample.md)


[Next](AUPublic-Utility-AUBuffer.cpp.md)[Previous](AUPublic-Utility-AUBaseHelper.cpp.md)

Relevant replacement documents include:

- [http://developer.apple.com/library/mac/samplecode/sc2195/Introduction/Intro.html#//apple_ref/doc/uid/DTS40013969](https://developer.apple.com/library/mac/samplecode/sc2195/Introduction/Intro.html#//apple_ref/doc/uid/DTS40013969)

# AUPublic/Utility/AUBaseHelper.h

```c
/*
 <codex> 
 <abstract>Part of CoreAudio Utility Classes</abstract>
 <\codex>
*/
#ifndef __AUBaseHelper_h__
#define __AUBaseHelper_h__

#if !defined(__COREAUDIO_USE_FLAT_INCLUDES__)
    #include <CoreFoundation/CoreFoundation.h>
    #include <AudioUnit/AUComponent.h>
#else
    #include <CoreFoundation.h>
    #include <AUComponent.h>
#endif

#include "AUBase.h"


UInt32 FindInvalidSamples(Float32 *inSource, UInt32 inFramesToProcess, bool &hasNonZero, bool zapInvalidSamples);


// helpers for dealing with the file-references dictionary in an AUPreset

extern "C" OSStatus 
GetFileRefPath (CFDictionaryRef parent, CFStringRef frKey, CFStringRef * fPath);

// if fileRefDict is NULL, this call creates one
// if not NULL, then the key value is added to it
extern "C" CFMutableDictionaryRef 
CreateFileRefDict (CFStringRef fKey, CFStringRef fPath, CFMutableDictionaryRef fileRefDict);

#if DEBUG
    void PrintAUParamEvent (AudioUnitParameterEvent& event, FILE* f);
#endif



#endif // __AUBaseHelper_h__
```

[Next](AUPublic-Utility-AUBuffer.cpp.md)[Previous](AUPublic-Utility-AUBaseHelper.cpp.md)

