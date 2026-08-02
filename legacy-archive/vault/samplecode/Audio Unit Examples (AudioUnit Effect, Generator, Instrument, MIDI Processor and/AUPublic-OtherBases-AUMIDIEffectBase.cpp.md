---
title: Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor
  and Offline)
apple_id: DTS40013969
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-02-19'
source_url: https://developer.apple.com/library/archive/samplecode/sc2195/Listings/AUPublic_OtherBases_AUMIDIEffectBase_cpp.html
archived_at: '2026-07-26T19:54:12.663160Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor and Offline)](Audio%20Unit%20Examples%20%28AudioUnit%20Effect%2C%20Generator%2C%20Instrument%2C%20MIDI%20Processor%20and.md)


[Next](AUPublic-AUInstrumentBase-AUInstrumentBase.h.md)[Previous](AUPublic-OtherBases-MusicDeviceBase.cpp.md)

# AUPublic/OtherBases/AUMIDIEffectBase.cpp

```c
/*
 <codex>
 <abstract>AUMIDIEffectBase.h</abstract>
 </codex>
*/
#include "AUMIDIEffectBase.h"

// compatibility with older OS SDK releases
typedef OSStatus
(*TEMP_MusicDeviceMIDIEventProc)(   void *              inComponentStorage,
                UInt32                  inStatus,
                UInt32                  inData1,
                UInt32                  inData2,
                UInt32                  inOffsetSampleFrame);

#if !CA_USE_AUDIO_PLUGIN_ONLY
static OSStatus     AUMIDIEffectBaseMIDIEvent(void *                inComponentStorage,
                        UInt32                  inStatus,
                        UInt32                  inData1,
                        UInt32                  inData2,
                        UInt32                  inOffsetSampleFrame);
#endif

AUMIDIEffectBase::AUMIDIEffectBase(     AudioComponentInstance              inInstance,
                        bool                        inProcessesInPlace )
    : AUEffectBase(inInstance, inProcessesInPlace),
      AUMIDIBase(this)
{
}

OSStatus            AUMIDIEffectBase::GetPropertyInfo(AudioUnitPropertyID           inID,
                            AudioUnitScope              inScope,
                            AudioUnitElement            inElement,
                            UInt32 &                outDataSize,
                            Boolean &               outWritable)
{
    OSStatus result;

    result = AUEffectBase::GetPropertyInfo (inID, inScope, inElement, outDataSize, outWritable);

    if (result == kAudioUnitErr_InvalidProperty)
        result = AUMIDIBase::DelegateGetPropertyInfo (inID, inScope, inElement, outDataSize, outWritable);

    return result;
}

OSStatus            AUMIDIEffectBase::GetProperty(  AudioUnitPropertyID     inID,
                                                    AudioUnitScope          inScope,
                                                    AudioUnitElement        inElement,
                                                    void *                  outData)
{
    OSStatus result;

#if !CA_USE_AUDIO_PLUGIN_ONLY
    if (inID == kAudioUnitProperty_FastDispatch) {
        if (inElement == kMusicDeviceMIDIEventSelect) {
            *(TEMP_MusicDeviceMIDIEventProc *)outData = AUMIDIEffectBaseMIDIEvent;
            return noErr;
        }
        return kAudioUnitErr_InvalidElement;
    }
#endif

    result = AUEffectBase::GetProperty (inID, inScope, inElement, outData);

    if (result == kAudioUnitErr_InvalidProperty)
        result = AUMIDIBase::DelegateGetProperty (inID, inScope, inElement, outData);

    return result;
}

OSStatus            AUMIDIEffectBase::SetProperty(  AudioUnitPropertyID         inID,
                            AudioUnitScope              inScope,
                            AudioUnitElement            inElement,
                            const void *                inData,
                            UInt32                  inDataSize)
{

    OSStatus result = AUEffectBase::SetProperty (inID, inScope, inElement, inData, inDataSize);

    if (result == kAudioUnitErr_InvalidProperty)
        result = AUMIDIBase::DelegateSetProperty (inID, inScope, inElement, inData, inDataSize);

    return result;
}

#if !CA_USE_AUDIO_PLUGIN_ONLY
#if !TARGET_OS_IPHONE
OSStatus            AUMIDIEffectBase::ComponentEntryDispatch(ComponentParameters *          params,
                                AUMIDIEffectBase *          This)
{
    if (This == NULL) return paramErr;

    OSStatus result;

    switch (params->what) {
    case kMusicDeviceMIDIEventSelect:
    case kMusicDeviceSysExSelect:
        result = AUMIDIBase::ComponentEntryDispatch (params, This);
        break;
    default:
        result = AUEffectBase::ComponentEntryDispatch(params, This);
        break;
    }

    return result;
}
#endif

// fast dispatch
static OSStatus     AUMIDIEffectBaseMIDIEvent(void *                inComponentStorage,
                        UInt32                  inStatus,
                        UInt32                  inData1,
                        UInt32                  inData2,
                        UInt32                  inOffsetSampleFrame)
{
    OSStatus result = noErr;
    try {
        AUMIDIEffectBase *This = static_cast<AUMIDIEffectBase *>(inComponentStorage);
        if (This == NULL) return paramErr;
        result = This->AUMIDIBase::MIDIEvent(inStatus, inData1, inData2, inOffsetSampleFrame);
    }
    COMPONENT_CATCH
    return result;
}
#endif
```

[Next](AUPublic-AUInstrumentBase-AUInstrumentBase.h.md)[Previous](AUPublic-OtherBases-MusicDeviceBase.cpp.md)

