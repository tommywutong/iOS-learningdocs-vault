---
title: MatrixMixerTest
apple_id: DTS40008645
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-02-11'
source_url: https://developer.apple.com/library/archive/samplecode/MatrixMixerTest/Listings/PublicUtility_CAComponentDescription_h.html
archived_at: '2026-07-18T03:14:32.418254Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MatrixMixerTest](MatrixMixerTest.md)


[Next](PublicUtility-CACFDictionary.h.md)[Previous](MeteringView.mm.md)

# PublicUtility/CAComponentDescription.h

```c
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Part of CoreAudio Utility Classes
*/

#ifndef __CAComponentDescription_h__
#define __CAComponentDescription_h__

#if !defined(__COREAUDIO_USE_FLAT_INCLUDES__)
    #include <AudioUnit/AudioUnit.h>
#else
    #include <ConditionalMacros.h>
    #include <AudioUnit.h>
#endif

#include "CACFDictionary.h"
#include <stdio.h>
#include <string.h>

void CAShowComponentDescription(const AudioComponentDescription *desc);

// ____________________________________________________________________________
//
//  CAComponentDescription
class CAComponentDescription : public AudioComponentDescription {
public:
    CAComponentDescription() { memset (this, 0, sizeof (AudioComponentDescription)); }

    CAComponentDescription (OSType inType, OSType inSubtype = 0, OSType inManu = 0);

    CAComponentDescription(const AudioComponentDescription& desc) { memcpy (this, &desc, sizeof (AudioComponentDescription)); }

    // _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    //
    // interrogation

    bool    IsAU () const;

    bool    IsAUFX() const { return componentType == kAudioUnitType_Effect; }
    bool    IsAUFM() const { return componentType == kAudioUnitType_MusicEffect; }

    bool    IsAUMI() const { return componentType == 'aumi' /*kAudioUnitType_MIDIProcessor*/; }

    bool    IsAUAX () const { return componentType == 'auax' /*kAudioUnitType_Auxiliary*/; }

    bool    IsEffect () const { return IsAUFX() || IsAUFM() || IsPanner(); }

    bool    IsOffline () const { return componentType == 'auol' /*kAudioUnitType_Offline*/; }

    bool    IsFConv () const { return componentType == kAudioUnitType_FormatConverter; }

    bool    IsPanner () const { return componentType == kAudioUnitType_Panner; }

    bool    IsMusicDevice () const { return componentType == kAudioUnitType_MusicDevice; }

#ifndef MAC_OS_X_VERSION_10_4
    bool    IsGenerator () const { return componentType =='augn'; }
#else
    bool    IsGenerator () const { return componentType ==kAudioUnitType_Generator; }
#endif

    bool    IsOutput () const { return componentType == kAudioUnitType_Output; }

    bool    IsSource () const { return IsMusicDevice() || IsGenerator(); }

    OSType  Type () const { return componentType; }
    OSType  SubType () const { return componentSubType; }
    OSType  Manu () const { return componentManufacturer; }

    int     Count() const { return AudioComponentCount(const_cast<CAComponentDescription*>(this)); }

        // does a semantic match where "wild card" values for type, subtype, manu will match
    bool    Matches (const AudioComponentDescription &desc) const;

    // _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    //
    //  other

    void    Print(FILE* file = stdout) const    { _CAShowComponentDescription (this, file); }

    OSStatus            Save (CFPropertyListRef *outData) const;
    OSStatus            Restore (CFPropertyListRef &inData);

private:
    static void _CAShowComponentDescription (const AudioComponentDescription *desc, FILE* file);
    friend void CAShowComponentDescription (const AudioComponentDescription *desc);
};

inline bool operator< (const AudioComponentDescription& x, const AudioComponentDescription& y)
{
    return memcmp (&x, &y, offsetof (AudioComponentDescription, componentFlags)) < 0;
}

inline bool operator== (const AudioComponentDescription& x, const AudioComponentDescription& y)
{
    return !memcmp (&x, &y, offsetof (AudioComponentDescription, componentFlags));
}

inline bool operator!= (const AudioComponentDescription& x, const AudioComponentDescription& y)
{
    return !(x == y);
}

#endif
```

[Next](PublicUtility-CACFDictionary.h.md)[Previous](MeteringView.mm.md)

