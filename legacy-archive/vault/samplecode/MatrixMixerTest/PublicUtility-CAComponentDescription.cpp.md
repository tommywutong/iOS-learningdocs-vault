---
title: MatrixMixerTest
apple_id: DTS40008645
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-02-11'
source_url: https://developer.apple.com/library/archive/samplecode/MatrixMixerTest/Listings/PublicUtility_CAComponentDescription_cpp.html
archived_at: '2026-07-18T03:14:32.357827Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MatrixMixerTest](MatrixMixerTest.md)


[Next](PublicUtility-MatrixMixerVolumes.cpp.md)[Previous](PublicUtility-CAStreamBasicDescription.h.md)

# PublicUtility/CAComponentDescription.cpp

```c
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Part of CoreAudio Utility Classes
*/

#include "CAComponentDescription.h"
#include "CAStreamBasicDescription.h"
#include <ctype.h>

void CAShowComponentDescription(const AudioComponentDescription *desc)
{
    CAComponentDescription::_CAShowComponentDescription (desc, stdout);
}

void    CAComponentDescription::_CAShowComponentDescription(const AudioComponentDescription *desc, FILE* file)
{
    if (desc)
    {
        char str[24];
        fprintf (file, "AudioComponentDescription: %s - ", CAStringForOSType(desc->componentType, str, sizeof(str)));
        fprintf (file, "%s - ", CAStringForOSType(desc->componentSubType, str, sizeof(str)));
        fprintf (file, "%s", CAStringForOSType(desc->componentManufacturer, str, sizeof(str)));     
        fprintf (file, ", 0x%X, 0x%X\n", (int)desc->componentFlags, (int)desc->componentFlagsMask);
    }
}

CAComponentDescription::CAComponentDescription (OSType inType, OSType inSubtype, OSType inManu)
{
    componentType = inType;
    componentSubType = inSubtype;
    componentManufacturer = inManu;
    componentFlags = 0;
    componentFlagsMask = 0;
}

bool    CAComponentDescription::IsAU () const 
{ 
    bool flag = IsEffect() || IsMusicDevice() || IsOffline();
    if (flag) return true;

    switch (componentType) {
        case kAudioUnitType_Output:
        case kAudioUnitType_FormatConverter:
        case kAudioUnitType_Mixer:
            return true;
    }
    return false;
}

inline bool _MatchTest (const OSType &inTypeA, const OSType &inTypeB)
{
    return ((inTypeA == inTypeB) || (!inTypeA && !inTypeB) || (inTypeA && !inTypeB) || (!inTypeA && inTypeB)); 
}

bool    CAComponentDescription::Matches (const AudioComponentDescription &desc) const
{
    bool matches = false;

        // see if the type matches
    matches = _MatchTest (componentType, desc.componentType);

    if (matches)
        matches = _MatchTest (componentSubType, desc.componentSubType);

    if (matches)
        matches = _MatchTest (componentManufacturer, desc.componentManufacturer);

    return matches;
}
```

[Next](PublicUtility-MatrixMixerVolumes.cpp.md)[Previous](PublicUtility-CAStreamBasicDescription.h.md)

