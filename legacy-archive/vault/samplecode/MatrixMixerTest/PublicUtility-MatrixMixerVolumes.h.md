---
title: MatrixMixerTest
apple_id: DTS40008645
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-02-11'
source_url: https://developer.apple.com/library/archive/samplecode/MatrixMixerTest/Listings/PublicUtility_MatrixMixerVolumes_h.html
archived_at: '2026-07-18T03:14:33.251405Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MatrixMixerTest](MatrixMixerTest.md)


[Next](PublicUtility-CADebugMacros.h.md)[Previous](PublicUtility-CACFDictionary.h.md)

# PublicUtility/MatrixMixerVolumes.h

```c
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Part of CoreAudio Utility Classes
*/

#ifndef __MatrixMixerVolumes_h__
#define __MatrixMixerVolumes_h__

#if !defined(__COREAUDIO_USE_FLAT_INCLUDES__)
    #include <AudioUnit/AudioUnit.h>
#else
    #include <AudioUnit.h>
#endif

#if defined(__cplusplus)
extern "C"
{
#endif

// prints the matrix mixer volumes of a specific audio unit to the given file
void     PrintMatrixMixerVolumes (FILE* file, AudioUnit au);                

// prints the mixer volumes for the specific scope of the audio unit
// results will be printed to the speficied file "file" with identifiying string tag "str"      
OSStatus PrintBuses (FILE* file, const char* str, AudioUnit au, AudioUnitScope inScope);
#if defined(__cplusplus)
}
#endif

#endif
```

[Next](PublicUtility-CADebugMacros.h.md)[Previous](PublicUtility-CACFDictionary.h.md)

