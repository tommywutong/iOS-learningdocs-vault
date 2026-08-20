---
title: Using an AUGraph with the Multi-Channel Mixer and Remote I/O Audio Unit
apple_id: TP40016060
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: CoreAudio
published: '2015-06-19'
source_url: https://developer.apple.com/library/archive/samplecode/iOSMultichannelMixerTest/Listings/PublicUtility_CAComponentDescription_cpp.html
archived_at: '2026-07-18T03:29:36.499981Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Using an AUGraph with the Multi-Channel Mixer and Remote I/O Audio Unit](Using%20an%20AUGraph%20with%20the%20Multi-Channel%20Mixer%20and%20Remote%20I-O%20Audio%20Unit.md)


[Next](PublicUtility-CADebugMacros.h.md)[Previous](PublicUtility-CAComponentDescription.h.md)

# PublicUtility/CAComponentDescription.cpp

```c
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Part of CoreAudio Utility Classes
*/

#include "CAComponentDescription.h"
#include <ctype.h>

/* !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
This file has been MODIFIED from what is available as part of the Core Audio Utility Classes
< https://developer.apple.com/library/ios/samplecode/CoreAudioUtilityClasses/Introduction/Intro.html>

We have removed the need for CAStreamBasicDescription.h simply for the CAStringForOSType function which
also elimitates all the deprecation warnings due to AudioSampleType, AudioUnitSampleType etc.

Use AVAudioFormat as the replacement for CAStreamBasicDescription
*/

// added from CAStreamBasicDescription class
char *CAStringForOSType (OSType t, char *writeLocation)
{
    char *p = writeLocation;
    unsigned char str[4] = {0}, *q = str;
    *(UInt32 *)str = CFSwapInt32HostToBig(t);

    bool hasNonPrint = false;
    for (int i = 0; i < 4; ++i) {
        if (!(isprint(*q) && *q != '\\')) {
            hasNonPrint = true;
            break;
        }
        q++;
    }
    q = str;

    if (hasNonPrint)
        p += sprintf (p, "0x");
    else
        *p++ = '\'';

    for (int i = 0; i < 4; ++i) {
        if (hasNonPrint) {
            p += sprintf(p, "%02X", *q++);
        } else {
            *p++ = *q++;
        }
    }
    if (!hasNonPrint)
        *p++ = '\'';
    *p = '\0';
    return writeLocation;
}

void CAShowComponentDescription(const AudioComponentDescription *desc)
{
    CAComponentDescription::_CAShowComponentDescription (desc, stdout);
}

void    CAComponentDescription::_CAShowComponentDescription(const AudioComponentDescription *desc, FILE* file)
{
    if (desc)
    {
        char str[24];
        fprintf (file, "AudioComponentDescription: %s - ", CAStringForOSType(desc->componentType, str));
        fprintf (file, "%s - ", CAStringForOSType(desc->componentSubType, str));
        fprintf (file, "%s", CAStringForOSType(desc->componentManufacturer, str));      
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

[Next](PublicUtility-CADebugMacros.h.md)[Previous](PublicUtility-CAComponentDescription.h.md)

