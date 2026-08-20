---
title: Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor
  and Offline)
apple_id: DTS40013969
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-02-19'
source_url: https://developer.apple.com/library/archive/samplecode/sc2195/Listings/PublicUtility_CAAudioChannelLayout_cpp.html
archived_at: '2026-07-26T19:54:11.769259Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor and Offline)](Audio%20Unit%20Examples%20%28AudioUnit%20Effect%2C%20Generator%2C%20Instrument%2C%20MIDI%20Processor%20and.md)


[Next](PublicUtility-CAAUMIDIMapManager.h.md)[Previous](PublicUtility-CAXException.cpp.md)

# PublicUtility/CAAudioChannelLayout.cpp

```c
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Part of Core Audio Public Utility Classes
*/

//=============================================================================
//  Includes
//=============================================================================

//  Self Include
#include "CAAudioChannelLayout.h"
#include "CAAutoDisposer.h"
#include <stdlib.h>
#include <string.h>

//=============================================================================
//  CAAudioChannelLayout
//=============================================================================

AudioChannelLayout* CAAudioChannelLayout::Create(UInt32 inNumberChannelDescriptions)
{
    UInt32 theSize = CalculateByteSize(inNumberChannelDescriptions);
    AudioChannelLayout* theAnswer = static_cast<AudioChannelLayout*>(CA_calloc(1, theSize));
    if(theAnswer != NULL)
    {
        SetAllToUnknown(*theAnswer, inNumberChannelDescriptions);
    }
    return theAnswer;
}

void    CAAudioChannelLayout::Destroy(AudioChannelLayout* inChannelLayout)
{
    free(inChannelLayout);
}

void    CAAudioChannelLayout::SetAllToUnknown(AudioChannelLayout& outChannelLayout, UInt32 inNumberChannelDescriptions)
{
    outChannelLayout.mChannelLayoutTag = kAudioChannelLayoutTag_UseChannelDescriptions;
    outChannelLayout.mChannelBitmap = 0;
    outChannelLayout.mNumberChannelDescriptions = inNumberChannelDescriptions;
    for(UInt32 theChannelIndex = 0; theChannelIndex < inNumberChannelDescriptions; ++theChannelIndex)
    {
        outChannelLayout.mChannelDescriptions[theChannelIndex].mChannelLabel = kAudioChannelLabel_Unknown;
        outChannelLayout.mChannelDescriptions[theChannelIndex].mChannelFlags = 0;
        outChannelLayout.mChannelDescriptions[theChannelIndex].mCoordinates[0] = 0;
        outChannelLayout.mChannelDescriptions[theChannelIndex].mCoordinates[1] = 0;
        outChannelLayout.mChannelDescriptions[theChannelIndex].mCoordinates[2] = 0;
    }
}

bool    operator== (const AudioChannelLayout &x, const AudioChannelLayout &y)
{
    // compare based on the number of channel descriptions present
    // (this may be too strict a comparison if all you care about are matching layout tags)
    UInt32 theSize1 = CAAudioChannelLayout::CalculateByteSize(x.mNumberChannelDescriptions);
    UInt32 theSize2 = CAAudioChannelLayout::CalculateByteSize(y.mNumberChannelDescriptions);

    if (theSize1 != theSize2)
        return false;

    return !memcmp (&x, &y, theSize1);
}

bool    operator!= (const AudioChannelLayout &x, const AudioChannelLayout &y)
{
    return !(x == y);
}

// counting the one bits in a word
inline UInt32 CountOnes(UInt32 x)
{
    // secret magic algorithm for counting bits in a word.
    UInt32 t;
    x = x - ((x >> 1) & 0x55555555);
    t = ((x >> 2) & 0x33333333);
    x = (x & 0x33333333) + t;
    x = (x + (x >> 4)) & 0x0F0F0F0F;
    x = x + (x << 8);
    x = x + (x << 16);
    return x >> 24;
}

UInt32  CAAudioChannelLayout::NumberChannels (const AudioChannelLayout& inLayout)
{
    if (inLayout.mChannelLayoutTag == kAudioChannelLayoutTag_UseChannelDescriptions)
        return inLayout.mNumberChannelDescriptions;

    if (inLayout.mChannelLayoutTag == kAudioChannelLayoutTag_UseChannelBitmap)
        return CountOnes (inLayout.mChannelBitmap);

    return AudioChannelLayoutTag_GetNumberOfChannels(inLayout.mChannelLayoutTag);
}

void    CAShowAudioChannelLayout (FILE* file, const AudioChannelLayout *layout)
{
    if (layout == NULL)
    {
        fprintf (file, "\tNULL layout\n");
        return;
    }
    fprintf (file, "\tTag=0x%X, ", (int)layout->mChannelLayoutTag);
    if (layout->mChannelLayoutTag == kAudioChannelLayoutTag_UseChannelBitmap)
        fprintf (file, "Using Bitmap:0x%X\n", (int)layout->mChannelBitmap);
    else {
        fprintf (file, "Num Chan Descs=%d\n", (int)layout->mNumberChannelDescriptions);
        const AudioChannelDescription *desc = layout->mChannelDescriptions;
        for (unsigned int i = 0; i < layout->mNumberChannelDescriptions; ++i, ++desc) {
            fprintf (file, "\t\tLabel=%d, Flags=0x%X, ", (int)desc->mChannelLabel, (int)desc->mChannelFlags);
            fprintf (file, "[az=%f,el=%f,dist=%f]\n", desc->mCoordinates[0], desc->mCoordinates[1], desc->mCoordinates[2]);
        }
    }
}
```

[Next](PublicUtility-CAAUMIDIMapManager.h.md)[Previous](PublicUtility-CAXException.cpp.md)

