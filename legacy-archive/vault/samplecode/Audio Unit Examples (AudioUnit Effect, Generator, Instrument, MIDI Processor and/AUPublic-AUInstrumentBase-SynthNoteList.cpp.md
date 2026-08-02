---
title: Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor
  and Offline)
apple_id: DTS40013969
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-02-19'
source_url: https://developer.apple.com/library/archive/samplecode/sc2195/Listings/AUPublic_AUInstrumentBase_SynthNoteList_cpp.html
archived_at: '2026-07-26T19:54:12.804279Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor and Offline)](Audio%20Unit%20Examples%20%28AudioUnit%20Effect%2C%20Generator%2C%20Instrument%2C%20MIDI%20Processor%20and.md)


[Next](AUPublic-AUInstrumentBase-SynthElement.cpp.md)[Previous](AUPublic-AUInstrumentBase-SynthNote.cpp.md)

# AUPublic/AUInstrumentBase/SynthNoteList.cpp

```c
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Part of Core Audio AUInstrument Base Classes
*/

#include "SynthNoteList.h"
#include <stdexcept>

void SynthNoteList::SanityCheck() const
{
    if (mState >= kNoteState_Unset) {
        throw std::runtime_error("SanityCheck: mState is bad");
    }

    if (mHead == NULL) {
        if (mTail != NULL)
            throw std::runtime_error("SanityCheck: mHead is NULL but not mTail");
        return;
    }
    if (mTail == NULL) {
        throw std::runtime_error("SanityCheck: mTail is NULL but not mHead");
    }

    if (mHead->mPrev) {
        throw std::runtime_error("SanityCheck: mHead has a mPrev");
    }
    if (mTail->mNext) {
        throw std::runtime_error("SanityCheck: mTail has a mNext");
    }

    SynthNote *note = mHead;
    while (note)
    {
        if (note->mState != mState)
            throw std::runtime_error("SanityCheck: note in wrong state");
        if (note->mNext) {
            if (note->mNext->mPrev != note)
                throw std::runtime_error("SanityCheck: bad link 1");
        } else {
            if (mTail != note)
                throw std::runtime_error("SanityCheck: note->mNext is nil, but mTail != note");
        }
        if (note->mPrev) {
            if (note->mPrev->mNext != note)
                throw std::runtime_error("SanityCheck: bad link 2");
        } else {
            if (mHead != note)
                throw std::runtime_error("SanityCheck: note->mPrev is nil, but mHead != note");
        }
        note = note->mNext;
    }
}
```

[Next](AUPublic-AUInstrumentBase-SynthElement.cpp.md)[Previous](AUPublic-AUInstrumentBase-SynthNote.cpp.md)

