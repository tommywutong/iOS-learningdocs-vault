---
title: Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor
  and Offline)
apple_id: DTS40013969
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-02-19'
source_url: https://developer.apple.com/library/archive/samplecode/sc2195/Listings/AudioUnitMidiProcessorExample_AUMidiPassThru_h.html
archived_at: '2026-07-26T19:54:11.972866Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor and Offline)](Audio%20Unit%20Examples%20%28AudioUnit%20Effect%2C%20Generator%2C%20Instrument%2C%20MIDI%20Processor%20and.md)


[Next](AudioUnitMidiProcessorExample-AUMidiPassThruVersion.h.md)[Previous](AudioUnitOfflineEffectExample-ReadMe.md.md)

# AudioUnitMidiProcessorExample/AUMidiPassThru.h

```swift
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
MIDI Processor AU
*/

#ifndef __AUMidiPassThru_h__
#define __AUMidiPassThru_h__

#include "AUMidiPassThruVersion.h"
#include <CoreMIDI/CoreMIDI.h>
#include "AUMIDIEffectBase.h"
#include "LockFreeFIFO.h"

#pragma mark - AUMidiPassThru
class AUMidiPassThru : public AUMIDIEffectBase
{
public:
    AUMidiPassThru(AudioUnit component);
    virtual ~AUMidiPassThru();

    virtual OSStatus GetPropertyInfo(AudioUnitPropertyID inID, AudioUnitScope inScope, AudioUnitElement inElement, UInt32& outDataSize, Boolean& outWritable );

    virtual OSStatus GetProperty(AudioUnitPropertyID inID, AudioUnitScope inScope, AudioUnitElement inElement, void* outData);

    virtual OSStatus SetProperty(   AudioUnitPropertyID inID, AudioUnitScope inScope, AudioUnitElement inElement, const void* inData, UInt32 inDataSize);

    virtual bool SupportsTail() { return false; }

    virtual OSStatus Version() { return kAUMidiPassThruVersion; }

    virtual OSStatus HandleMidiEvent(UInt8 status, UInt8 channel, UInt8 data1, UInt8 data2, UInt32 inOffsetSampleFrame);

    virtual OSStatus Render(AudioUnitRenderActionFlags &ioActionFlags, const AudioTimeStamp& inTimeStamp, UInt32 nFrames);

private:
    AUMIDIOutputCallbackStruct mMIDIOutCB;

    LockFreeFIFO<MIDIPacket> mOutputPacketFIFO;

};

#endif
```

[Next](AudioUnitMidiProcessorExample-AUMidiPassThruVersion.h.md)[Previous](AudioUnitOfflineEffectExample-ReadMe.md.md)

