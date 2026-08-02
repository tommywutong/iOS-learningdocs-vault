---
title: Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor
  and Offline)
apple_id: DTS40013969
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-02-19'
source_url: https://developer.apple.com/library/archive/samplecode/sc2195/Listings/PublicUtility_CAAudioChannelLayoutObject_cpp.html
archived_at: '2026-07-26T19:54:11.745057Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor and Offline)](Audio%20Unit%20Examples%20%28AudioUnit%20Effect%2C%20Generator%2C%20Instrument%2C%20MIDI%20Processor%20and.md)


[Next](PublicUtility-CAMutex.h.md)[Previous](PublicUtility-CAVectorUnit.cpp.md)

# PublicUtility/CAAudioChannelLayoutObject.cpp

```c
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Part of Core Audio Public Utility Classes
*/

#include "CAAudioChannelLayout.h"
#if !defined(__COREAUDIO_USE_FLAT_INCLUDES__)
    #include <AudioToolbox/AudioFormat.h>
#else
    #include <AudioFormat.h>
#endif

CAAudioChannelLayout::CAAudioChannelLayout ()
{
    mLayout = RefCountedLayout::CreateWithNumberChannelDescriptions(0);
}

//=============================================================================
//  CAAudioChannelLayout::CAAudioChannelLayout
//=============================================================================
CAAudioChannelLayout::CAAudioChannelLayout (UInt32 inNumberChannels, bool inChooseSurround)
{
        // this chooses default layouts based on the number of channels...
    AudioChannelLayoutTag tag;

    switch (inNumberChannels)
    {
        default:
            // here we have a "broken" layout, in the sense that we haven't any idea how to lay this out
            mLayout = RefCountedLayout::CreateWithNumberChannelDescriptions(inNumberChannels);
            SetAllToUnknown(*mLayout->GetLayout(), inNumberChannels);
            return; // don't fall into the tag case
        case 1:
            tag = kAudioChannelLayoutTag_Mono;
            break;
        case 2:
            tag = inChooseSurround ? kAudioChannelLayoutTag_Binaural : kAudioChannelLayoutTag_Stereo;
            break;
        case 4:
            tag = inChooseSurround ? kAudioChannelLayoutTag_Ambisonic_B_Format : kAudioChannelLayoutTag_AudioUnit_4;
            break;
        case 5:
            tag = inChooseSurround ? kAudioChannelLayoutTag_AudioUnit_5_0 : kAudioChannelLayoutTag_AudioUnit_5;
            break;
        case 6:
            tag = inChooseSurround ? kAudioChannelLayoutTag_AudioUnit_6_0 : kAudioChannelLayoutTag_AudioUnit_6;
            break;
        case 7:
            tag = kAudioChannelLayoutTag_AudioUnit_7_0;
            break;
        case 8:
            tag = kAudioChannelLayoutTag_AudioUnit_8;
            break;
    }

    mLayout = RefCountedLayout::CreateWithLayoutTag(tag);
}

//=============================================================================
//  CAAudioChannelLayout::CAAudioChannelLayout
//=============================================================================
CAAudioChannelLayout::CAAudioChannelLayout (AudioChannelLayoutTag inLayoutTag)
    : mLayout(NULL)
{
    SetWithTag(inLayoutTag);
}

//=============================================================================
//  CAAudioChannelLayout::CAAudioChannelLayout
//=============================================================================
CAAudioChannelLayout::CAAudioChannelLayout (const CAAudioChannelLayout &c)
    : mLayout(NULL)
{
    *this = c;
}

//=============================================================================
//  CAAudioChannelLayout::AudioChannelLayout
//=============================================================================
CAAudioChannelLayout::CAAudioChannelLayout (const AudioChannelLayout* inChannelLayout)
    : mLayout(NULL)
{
    *this = inChannelLayout;
}

//=============================================================================
//  CAAudioChannelLayout::~CAAudioChannelLayout
//=============================================================================
CAAudioChannelLayout::~CAAudioChannelLayout ()
{
    if (mLayout) {
        mLayout->release();
        mLayout = NULL;
    }
}

//=============================================================================
//  CAAudioChannelLayout::CAAudioChannelLayout
//=============================================================================
CAAudioChannelLayout& CAAudioChannelLayout::operator= (const CAAudioChannelLayout &c)
{
    if (mLayout != c.mLayout) {
        if (mLayout)
            mLayout->release();

        if ((mLayout = c.mLayout) != NULL)
            mLayout->retain();
    }

    return *this;
}

CAAudioChannelLayout&   CAAudioChannelLayout::operator= (const AudioChannelLayout* inChannelLayout)
{
    if (mLayout && &mLayout->Layout() == inChannelLayout)
        return *this;

    if (mLayout)
        mLayout->release();

    if (inChannelLayout == NULL)
    {
        mLayout = RefCountedLayout::CreateWithNumberChannelDescriptions(0);
    }
    else
    {
        mLayout = RefCountedLayout::CreateWithLayout(inChannelLayout);
    }
    return *this;
}

void    CAAudioChannelLayout::SetWithTag(AudioChannelLayoutTag inTag)
{
    if (mLayout)
        mLayout->release();

    mLayout = RefCountedLayout::CreateWithLayoutTag(inTag);
}

//=============================================================================
//  CAAudioChannelLayout::operator==
//=============================================================================
bool        CAAudioChannelLayout::operator== (const CAAudioChannelLayout &c) const
{
    if (mLayout == c.mLayout)
        return true;
    return Layout() == c.Layout();
}

//=============================================================================
//  CAAudioChannelLayout::operator!=
//=============================================================================
bool        CAAudioChannelLayout::operator!= (const CAAudioChannelLayout &c) const
{
    if (mLayout == c.mLayout)
        return false;

    return !(Layout() == c.Layout());
}

//=============================================================================
//  CAAudioChannelLayout::Print
//=============================================================================
void        CAAudioChannelLayout::Print (FILE* file) const
{
    CAShowAudioChannelLayout (file, &Layout());
}
```

[Next](PublicUtility-CAMutex.h.md)[Previous](PublicUtility-CAVectorUnit.cpp.md)

