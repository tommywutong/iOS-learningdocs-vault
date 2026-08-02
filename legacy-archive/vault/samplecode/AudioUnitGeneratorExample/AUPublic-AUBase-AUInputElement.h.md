---
title: AudioUnitGeneratorExample
apple_id: DTS40008637
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2012-10-08'
source_url: https://developer.apple.com/library/archive/samplecode/AUPinkNoise/Listings/AUPublic_AUBase_AUInputElement_h.html
archived_at: '2026-07-18T02:59:49.146010Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AudioUnitGeneratorExample](AudioUnitGeneratorExample.md)


[Next](AUPublic-AUBase-AUOutputElement.cpp.md)[Previous](AUPublic-AUBase-AUInputElement.cpp.md)

Relevant replacement documents include:

- [http://developer.apple.com/library/mac/samplecode/sc2195/Introduction/Intro.html#//apple_ref/doc/uid/DTS40013969](https://developer.apple.com/library/mac/samplecode/sc2195/Introduction/Intro.html#//apple_ref/doc/uid/DTS40013969)

# AUPublic/AUBase/AUInputElement.h

```c
/*
 <codex> 
 <abstract>Part of CoreAudio Utility Classes</abstract>
 <\codex>
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

[Next](AUPublic-AUBase-AUOutputElement.cpp.md)[Previous](AUPublic-AUBase-AUInputElement.cpp.md)

