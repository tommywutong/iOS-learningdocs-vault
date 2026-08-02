---
title: Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor
  and Offline)
apple_id: DTS40013969
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-02-19'
source_url: https://developer.apple.com/library/archive/samplecode/sc2195/Listings/AUPublic_Utility_AUBaseHelper_h.html
archived_at: '2026-07-26T19:54:12.067603Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor and Offline)](Audio%20Unit%20Examples%20%28AudioUnit%20Effect%2C%20Generator%2C%20Instrument%2C%20MIDI%20Processor%20and.md)


[Next](AUPublic-AUBase-AUScopeElement.cpp.md)[Previous](AUPublic-Utility-AUBuffer.h.md)

# AUPublic/Utility/AUBaseHelper.h

```c
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Part of Core Audio AUBase Classes
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

// helpers for dealing with the file-references dictionary in an AUPreset
OSStatus GetFileRefPath (CFDictionaryRef parent, CFStringRef frKey, CFStringRef * fPath);

// if fileRefDict is NULL, this call creates one
// if not NULL, then the key value is added to it
CFMutableDictionaryRef CreateFileRefDict (CFStringRef fKey, CFStringRef fPath, CFMutableDictionaryRef fileRefDict);

int AccessURLAsset(const CFURLRef inURL, int mode);

#if DEBUG
    void PrintAUParamEvent (AudioUnitParameterEvent& event, FILE* f);
#endif

#endif // __AUBaseHelper_h__
```

[Next](AUPublic-AUBase-AUScopeElement.cpp.md)[Previous](AUPublic-Utility-AUBuffer.h.md)

