---
title: Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor
  and Offline)
apple_id: DTS40013969
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-02-19'
source_url: https://developer.apple.com/library/archive/samplecode/sc2195/Listings/AUPublic_AUBase_AUInputElement_h.html
archived_at: '2026-07-26T19:54:12.120217Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor and Offline)](Audio%20Unit%20Examples%20%28AudioUnit%20Effect%2C%20Generator%2C%20Instrument%2C%20MIDI%20Processor%20and.md)


[Next](AUPublic-AUBase-ComponentBase.cpp.md)[Previous](AUPublic-AUBase-AUDispatch.h.md)

# AUPublic/AUBase/AUInputElement.h

```swift
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Part of Core Audio AUBase Classes
*/

#ifndef __AUInput_h__
#define __AUInput_h__

#include "AUScopeElement.h"
#include "AUBuffer.h"

/*! @class AUInputElement */
class AUInputElement : public AUIOElement {
public:

    /*! @ctor AUInputElement */
                        AUInputElement(AUBase *audioUnit);
    /*! @dtor ~AUInputElement */
    virtual             ~AUInputElement() { }

    // AUElement override
    /*! @method SetStreamFormat */
    virtual OSStatus    SetStreamFormat(const CAStreamBasicDescription &desc);
    /*! @method NeedsBufferSpace */
    virtual bool        NeedsBufferSpace() const { return IsCallback(); }

    /*! @method SetConnection */
    void                SetConnection(const AudioUnitConnection &conn);
    /*! @method SetInputCallback */
    void                SetInputCallback(AURenderCallback proc, void *refCon);

    /*! @method IsActive */
    bool                IsActive() const { return mInputType != kNoInput; }
    /*! @method IsCallback */
    bool                IsCallback() const { return mInputType == kFromCallback; }
    /*! @method HasConnection */
    bool                HasConnection() const { return mInputType == kFromConnection; }

    /*! @method PullInput */
    OSStatus            PullInput(  AudioUnitRenderActionFlags &    ioActionFlags,
                                    const AudioTimeStamp &          inTimeStamp,
                                    AudioUnitElement                inElement,
                                    UInt32                          inNumberFrames);

    /*! @method PullInputWithBufferList */
    OSStatus            PullInputWithBufferList(    AudioUnitRenderActionFlags &    ioActionFlags,
                                                    const AudioTimeStamp &          inTimeStamp,
                                                    AudioUnitElement                inElement,
                                                    UInt32                          nFrames,
                                                    AudioBufferList *               inBufferList);
protected:
    /*! @method Disconnect */
    void                Disconnect();

    enum EInputType { kNoInput, kFromConnection, kFromCallback };

    /*! @var mInputType */
    EInputType                  mInputType;

    // if from callback:
    /*! @var mInputProc */
    AURenderCallback            mInputProc;
    /*! @var mInputProcRefCon */
    void *                      mInputProcRefCon;

    // if from connection:
    /*! @var mConnection */
    AudioUnitConnection         mConnection;
#if !CA_USE_AUDIO_PLUGIN_ONLY
    /*! @var mConnRenderProc */
    AudioUnitRenderProc         mConnRenderProc;
#endif
    /*! @var mConnInstanceStorage */
    void *                      mConnInstanceStorage;       // for the input component
};

#endif // __AUInput_h__
```

[Next](AUPublic-AUBase-ComponentBase.cpp.md)[Previous](AUPublic-AUBase-AUDispatch.h.md)

