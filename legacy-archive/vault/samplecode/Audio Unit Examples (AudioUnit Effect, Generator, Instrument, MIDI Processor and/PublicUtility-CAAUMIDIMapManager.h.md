---
title: Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor
  and Offline)
apple_id: DTS40013969
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-02-19'
source_url: https://developer.apple.com/library/archive/samplecode/sc2195/Listings/PublicUtility_CAAUMIDIMapManager_h.html
archived_at: '2026-07-26T19:54:11.776089Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor and Offline)](Audio%20Unit%20Examples%20%28AudioUnit%20Effect%2C%20Generator%2C%20Instrument%2C%20MIDI%20Processor%20and.md)


[Next](PublicUtility-CAAUMIDIMap.h.md)[Previous](PublicUtility-CAAudioChannelLayout.cpp.md)

# PublicUtility/CAAUMIDIMapManager.h

```swift
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Part of Core Audio Public Utility Classes
*/

#ifndef __CAAUMIDIMapManager_h_
#define __CAAUMIDIMapManager_h_

#include "AUBase.h"
#include "CAAUMIDIMap.h"
#include <vector>
#include <AudioToolbox/AudioUnitUtilities.h>

class CAAUMIDIMapManager {

protected:

    typedef std::vector<CAAUMIDIMap>    ParameterMaps;
    ParameterMaps                       mParameterMaps;

    bool                                hotMapping;
    AUParameterMIDIMapping              mHotMap;

public:

                            CAAUMIDIMapManager();

    UInt32                  NumMaps(){return static_cast<UInt32>(mParameterMaps.size());}
    void                    GetMaps(AUParameterMIDIMapping* maps);

    int                     FindParameterIndex(AUParameterMIDIMapping &map);

    void                    GetHotParameterMap(AUParameterMIDIMapping &outMap);

    void                    SortedRemoveFromParameterMaps   (AUParameterMIDIMapping *maps, UInt32 inNumMaps, bool &outMapDidChange);
    OSStatus                SortedInsertToParamaterMaps (AUParameterMIDIMapping *maps, UInt32 inNumMaps, AUBase &That);

    void                    ReplaceAllMaps (AUParameterMIDIMapping* inMappings, UInt32 inNumMaps, AUBase &That);

    bool                    IsHotMapping(){return hotMapping;}
    void                    SetHotMapping (AUParameterMIDIMapping &inMap){hotMapping = true; mHotMap = inMap; }

    bool                    HandleHotMapping(   UInt8   inStatus,
                                                UInt8   inChannel,
                                                UInt8   inData1,
                                                AUBase  &That);

    bool                    FindParameterMapEventMatch(UInt8    inStatus,
                                                       UInt8    inChannel,
                                                       UInt8    inData1,
                                                       UInt8    inData2,
                                                       UInt32   inBufferOffset,
                                                       AUBase&  inAUBase);
#if DEBUG
    void                    Print();
#endif
};

#endif
```

[Next](PublicUtility-CAAUMIDIMap.h.md)[Previous](PublicUtility-CAAudioChannelLayout.cpp.md)

