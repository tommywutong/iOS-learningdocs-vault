---
title: Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor
  and Offline)
apple_id: DTS40013969
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-02-19'
source_url: https://developer.apple.com/library/archive/samplecode/sc2195/Listings/AudioUnitInstrumentExample_SinSynth_h.html
archived_at: '2026-07-26T19:54:11.893763Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor and Offline)](Audio%20Unit%20Examples%20%28AudioUnit%20Effect%2C%20Generator%2C%20Instrument%2C%20MIDI%20Processor%20and.md)


[Next](AudioUnitInstrumentExample-ReadMe.md.md)[Previous](AudioUnitInstrumentExample-SinSynthVersion.h.md)

# AudioUnitInstrumentExample/SinSynth.h

```swift
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Instrument AU
*/

#include "AUInstrumentBase.h"
#include "SinSynthVersion.h"

static const UInt32 kNumNotes = 12;

struct TestNote : public SynthNote
{
    virtual                 ~TestNote() {}

    virtual bool            Attack(const MusicDeviceNoteParams &inParams)
                                {
#if DEBUG_PRINT
                                    printf("TestNote::Attack %p %d\n", this, GetState());
#endif
                                    double sampleRate = SampleRate();
                                    phase = 0.;
                                    amp = 0.;
                                    maxamp = 0.4 * pow(inParams.mVelocity/127., 3.);
                                    up_slope = maxamp / (0.1 * sampleRate);
                                    dn_slope = -maxamp / (0.9 * sampleRate);
                                    fast_dn_slope = -maxamp / (0.005 * sampleRate);
                                    return true;
                                }
    virtual void            Kill(UInt32 inFrame); // voice is being stolen.
    virtual void            Release(UInt32 inFrame);
    virtual void            FastRelease(UInt32 inFrame);
    virtual Float32         Amplitude() { return amp; } // used for finding quietest note for voice stealing.
    virtual OSStatus        Render(UInt64 inAbsoluteSampleFrame, UInt32 inNumFrames, AudioBufferList** inBufferList, UInt32 inOutBusCount);

    double phase, amp, maxamp;
    double up_slope, dn_slope, fast_dn_slope;
};

class SinSynth : public AUMonotimbralInstrumentBase
{
public:
                                SinSynth(AudioUnit inComponentInstance);
    virtual                     ~SinSynth();

    virtual OSStatus            Initialize();
    virtual void                Cleanup();
    virtual OSStatus            Version() { return kSinSynthVersion; }

    virtual AUElement*          CreateElement(          AudioUnitScope                  scope,
                                              AudioUnitElement              element);

    virtual OSStatus            GetParameterInfo(       AudioUnitScope                  inScope,
                                                        AudioUnitParameterID            inParameterID,
                                                        AudioUnitParameterInfo &        outParameterInfo);

    MidiControls*               GetControls( MusicDeviceGroupID inChannel)
    {
        SynthGroupElement *group = GetElForGroupID(inChannel);
        return (MidiControls *) group->GetMIDIControlHandler();
    }

private:

    TestNote mTestNotes[kNumNotes];
};
```

[Next](AudioUnitInstrumentExample-ReadMe.md.md)[Previous](AudioUnitInstrumentExample-SinSynthVersion.h.md)

