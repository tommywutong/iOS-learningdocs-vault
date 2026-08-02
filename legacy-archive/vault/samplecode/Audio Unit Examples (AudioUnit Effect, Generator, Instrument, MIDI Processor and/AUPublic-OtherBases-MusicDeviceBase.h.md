---
title: Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor
  and Offline)
apple_id: DTS40013969
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-02-19'
source_url: https://developer.apple.com/library/archive/samplecode/sc2195/Listings/AUPublic_OtherBases_MusicDeviceBase_h.html
archived_at: '2026-07-26T19:54:12.525977Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor and Offline)](Audio%20Unit%20Examples%20%28AudioUnit%20Effect%2C%20Generator%2C%20Instrument%2C%20MIDI%20Processor%20and.md)


[Next](AUPublic-OtherBases-AUMIDIEffectBase.h.md)[Previous](AUPublic-AUBase-AUBase.h.md)

# AUPublic/OtherBases/MusicDeviceBase.h

```swift
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Part of Core Audio AUBase Classes
*/

#ifndef __MusicDeviceBase_h__
#define __MusicDeviceBase_h__

#include "AUMIDIBase.h"

// ________________________________________________________________________
//  MusicDeviceBase
//

/*! @class MusicDeviceBase */
class MusicDeviceBase : public AUBase, public AUMIDIBase {
public:
    /*! @ctor MusicDeviceBase */
                                MusicDeviceBase(        AudioComponentInstance          inInstance,
                                                        UInt32                          numInputs,
                                                        UInt32                          numOutputs,
                                                        UInt32                          numGroups = 0);

    virtual OSStatus    MIDIEvent(      UInt32                      inStatus,
                                        UInt32                      inData1,
                                        UInt32                      inData2,
                                        UInt32                      inOffsetSampleFrame)
    {
        return AUMIDIBase::MIDIEvent (inStatus, inData1, inData2, inOffsetSampleFrame);
    }

    /*! @method SysEx */
    virtual OSStatus    SysEx(          const UInt8 *               inData,
                                        UInt32                      inLength)
    {
        return AUMIDIBase::SysEx (inData, inLength);
    }

    /*! @method GetPropertyInfo */
    virtual OSStatus            GetPropertyInfo(AudioUnitPropertyID         inID,
                                                AudioUnitScope              inScope,
                                                AudioUnitElement            inElement,
                                                UInt32 &                    outDataSize,
                                                Boolean &                   outWritable);

    /*! @method GetProperty */
    virtual OSStatus            GetProperty(    AudioUnitPropertyID         inID,
                                                AudioUnitScope              inScope,
                                                AudioUnitElement            inElement,
                                                void *                      outData);

    /*! @method SetProperty */
    virtual OSStatus            SetProperty(            AudioUnitPropertyID             inID,
                                                        AudioUnitScope                  inScope,
                                                        AudioUnitElement                inElement,
                                                        const void *                    inData,
                                                        UInt32                          inDataSize);

    /*! @method HandleNoteOn */
    virtual OSStatus            HandleNoteOn(   UInt8   inChannel,
                                                UInt8   inNoteNumber,
                                                UInt8   inVelocity,
                                                UInt32  inStartFrame);

    /*! @method HandleNoteOff */
    virtual OSStatus            HandleNoteOff(  UInt8   inChannel,
                                                UInt8   inNoteNumber,
                                                UInt8   inVelocity,
                                                UInt32  inStartFrame);

    /*! @method GetInstrumentCount */
    virtual OSStatus            GetInstrumentCount (    UInt32 &outInstCount) const;

#if !CA_USE_AUDIO_PLUGIN_ONLY
    // component dispatcher
    /*! @method ComponentEntryDispatch */
    static OSStatus         ComponentEntryDispatch( ComponentParameters *           params,
                                                        MusicDeviceBase *               This);
#endif
private:
    OSStatus                HandleStartNoteMessage (MusicDeviceInstrumentID inInstrument, MusicDeviceGroupID inGroupID, NoteInstanceID *outNoteInstanceID, UInt32 inOffsetSampleFrame, const MusicDeviceNoteParams *inParams);
};

#endif // __MusicDeviceBase_h__
```

[Next](AUPublic-OtherBases-AUMIDIEffectBase.h.md)[Previous](AUPublic-AUBase-AUBase.h.md)

