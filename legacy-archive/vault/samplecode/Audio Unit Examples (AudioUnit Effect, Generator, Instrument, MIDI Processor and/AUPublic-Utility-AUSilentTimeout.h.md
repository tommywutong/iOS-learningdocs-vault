---
title: Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor
  and Offline)
apple_id: DTS40013969
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-02-19'
source_url: https://developer.apple.com/library/archive/samplecode/sc2195/Listings/AUPublic_Utility_AUSilentTimeout_h.html
archived_at: '2026-07-26T19:54:12.027946Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor and Offline)](Audio%20Unit%20Examples%20%28AudioUnit%20Effect%2C%20Generator%2C%20Instrument%2C%20MIDI%20Processor%20and.md)


[Next](AUPublic-Utility-AUMIDIDefs.h.md)[Previous](AUPublic-Utility-AUBuffer.cpp.md)

# AUPublic/Utility/AUSilentTimeout.h

```swift
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Part of Core Audio AUBase Classes
*/

#ifndef __AUSilentTimeout
#define __AUSilentTimeout

class AUSilentTimeout
{
public:
    AUSilentTimeout()
        :   mTimeoutCounter(0),
            mResetTimer(true)
                {};

    void                Process(UInt32 inFramesToProcess, UInt32 inTimeoutLimit, bool &ioSilence )
    {
        if(ioSilence )
        {
            if(mResetTimer )
            {
                mTimeoutCounter = inTimeoutLimit;
                mResetTimer = false;
            }

            if(mTimeoutCounter > 0 )
            {
                mTimeoutCounter -= inFramesToProcess;
                ioSilence = false;
            }
        }
        else
        {
            // signal to reset the next time we receive silence
            mResetTimer = true;
        }
    }

    void                Reset()
    {
        mResetTimer = true;
    };

private:
    SInt32              mTimeoutCounter;
    bool                mResetTimer;
};

#endif // __AUSilentTimeout
```

[Next](AUPublic-Utility-AUMIDIDefs.h.md)[Previous](AUPublic-Utility-AUBuffer.cpp.md)

