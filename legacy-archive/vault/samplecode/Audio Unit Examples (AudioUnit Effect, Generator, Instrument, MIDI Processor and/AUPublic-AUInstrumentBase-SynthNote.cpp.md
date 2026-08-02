---
title: Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor
  and Offline)
apple_id: DTS40013969
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-02-19'
source_url: https://developer.apple.com/library/archive/samplecode/sc2195/Listings/AUPublic_AUInstrumentBase_SynthNote_cpp.html
archived_at: '2026-07-26T19:54:12.797978Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor and Offline)](Audio%20Unit%20Examples%20%28AudioUnit%20Effect%2C%20Generator%2C%20Instrument%2C%20MIDI%20Processor%20and.md)


[Next](AUPublic-AUInstrumentBase-SynthNoteList.cpp.md)[Previous](AUPublic-AUInstrumentBase-SynthEvent.h.md)

# AUPublic/AUInstrumentBase/SynthNote.cpp

```c
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Part of Core Audio AUInstrument Base Classes
*/

#include "SynthNote.h"
#include "SynthElement.h"
#include "AUInstrumentBase.h"

bool SynthNote::AttackNote(
            SynthPartElement *              inPart,
            SynthGroupElement *             inGroup,
            NoteInstanceID                  inNoteID,
            UInt64                          inAbsoluteSampleFrame,
            UInt32                          inOffsetSampleFrame,
            const MusicDeviceNoteParams     &inParams)
{
#if DEBUG_PRINT
    printf("SynthNote::AttackNote %lu %lu abs frame %llu rel frame %lu\n", (UInt32)inGroup->GroupID(), (UInt32)inNoteID, inAbsoluteSampleFrame, inOffsetSampleFrame);
#endif
    mPart = inPart;
    mGroup = inGroup;
    mNoteID = inNoteID;

    mAbsoluteStartFrame = inAbsoluteSampleFrame;
    mRelativeStartFrame = inOffsetSampleFrame;
    mRelativeReleaseFrame = -1;
    mRelativeKillFrame = -1;

    mPitch = inParams.mPitch;
    mVelocity = inParams.mVelocity;

    return Attack(inParams);
}

void SynthNote::Reset()
{
    mPart = 0;
    mGroup = 0;
    mAbsoluteStartFrame = 0;
    mRelativeStartFrame = 0;
    mRelativeReleaseFrame = -1;
    mRelativeKillFrame = -1;
}

void SynthNote::Kill(UInt32 inFrame)
{
    mRelativeKillFrame = inFrame;
}

void SynthNote::Release(UInt32 inFrame)
{
    mRelativeReleaseFrame = inFrame;
}

void SynthNote::FastRelease(UInt32 inFrame)
{
    mRelativeReleaseFrame = inFrame;
}

double SynthNote::TuningA() const
{
    return 440.0;
}

double SynthNote::Frequency()
{
    return TuningA() * pow(2., (mPitch - 69. + GetPitchBend()) / 12.);
}

double SynthNote::SampleRate()
{
    return GetAudioUnit()->GetOutput(0)->GetStreamFormat().mSampleRate;
}

AUInstrumentBase* SynthNote::GetAudioUnit() const
{
    return (AUInstrumentBase*)mGroup->GetAudioUnit();
}

Float32 SynthNote::GetGlobalParameter(AudioUnitParameterID inParamID) const
{
    return mGroup->GetAudioUnit()->Globals()->GetParameter(inParamID);
}

void SynthNote::NoteEnded(UInt32 inFrame)
{
    mGroup->NoteEnded(this, inFrame);
    mNoteID = 0xFFFFFFFF;
}

float SynthNote::GetPitchBend() const
{
    return mGroup->GetPitchBend();
}
```

[Next](AUPublic-AUInstrumentBase-SynthNoteList.cpp.md)[Previous](AUPublic-AUInstrumentBase-SynthEvent.h.md)

