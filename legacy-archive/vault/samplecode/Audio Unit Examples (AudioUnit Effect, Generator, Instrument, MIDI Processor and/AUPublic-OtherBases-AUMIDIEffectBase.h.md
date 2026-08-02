---
title: Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor
  and Offline)
apple_id: DTS40013969
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-02-19'
source_url: https://developer.apple.com/library/archive/samplecode/sc2195/Listings/AUPublic_OtherBases_AUMIDIEffectBase_h.html
archived_at: '2026-07-26T19:54:12.532962Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor and Offline)](Audio%20Unit%20Examples%20%28AudioUnit%20Effect%2C%20Generator%2C%20Instrument%2C%20MIDI%20Processor%20and.md)


[Next](AUPublic-OtherBases-AUMIDIBase.h.md)[Previous](AUPublic-OtherBases-MusicDeviceBase.h.md)

# AUPublic/OtherBases/AUMIDIEffectBase.h

```swift
/*
 <codex>
 <abstract>Part of CoreAudio Utility Classes</abstract>
 </codex>
*/
#ifndef __AUMIDIEffectBase_h__
#define __AUMIDIEffectBase_h__

#include "AUMIDIBase.h"
#include "AUEffectBase.h"

// ________________________________________________________________________
//  AUMIDIEffectBase
//
    /*! @class AUMIDIEffectBase */
class AUMIDIEffectBase : public AUEffectBase, public AUMIDIBase {
public:
    /*! @ctor AUMIDIEffectBase */
                                AUMIDIEffectBase(   AudioComponentInstance  inInstance,
                                                    bool                    inProcessesInPlace = false );
    /*! @method MIDIEvent */
    virtual OSStatus            MIDIEvent(UInt32            inStatus,
                                          UInt32            inData1,
                                          UInt32            inData2,
                                          UInt32            inOffsetSampleFrame)
    {
        return AUMIDIBase::MIDIEvent (inStatus, inData1, inData2, inOffsetSampleFrame);
    }

    /*! @method SysEx */
    virtual OSStatus            SysEx(const UInt8 *         inData,
                                      UInt32                inLength)
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
    virtual OSStatus            SetProperty(    AudioUnitPropertyID         inID,
                                                AudioUnitScope              inScope,
                                                AudioUnitElement            inElement,
                                                const void *                inData,
                                                UInt32                      inDataSize);

#if !CA_USE_AUDIO_PLUGIN_ONLY
#if !TARGET_OS_IPHONE
    // component dispatcher
    /*! @method ComponentEntryDispatch */
    static OSStatus         ComponentEntryDispatch( ComponentParameters *           params,
                                                        AUMIDIEffectBase *              This);
#endif
#endif
};

#endif // __AUMIDIEffectBase_h__
```

[Next](AUPublic-OtherBases-AUMIDIBase.h.md)[Previous](AUPublic-OtherBases-MusicDeviceBase.h.md)

