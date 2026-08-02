---
title: AudioUnitGeneratorExample
apple_id: DTS40008637
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2012-10-08'
source_url: https://developer.apple.com/library/archive/samplecode/AUPinkNoise/Listings/AUPublic_AUBase_AUInputElement_cpp.html
archived_at: '2026-07-18T02:59:49.090296Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AudioUnitGeneratorExample](AudioUnitGeneratorExample.md)


[Next](AUPublic-AUBase-AUInputElement.h.md)[Previous](AUPublic-AUBase-AUDispatch.h.md)

Relevant replacement documents include:

- [http://developer.apple.com/library/mac/samplecode/sc2195/Introduction/Intro.html#//apple_ref/doc/uid/DTS40013969](https://developer.apple.com/library/mac/samplecode/sc2195/Introduction/Intro.html#//apple_ref/doc/uid/DTS40013969)

# AUPublic/AUBase/AUInputElement.cpp

```c
/*
 <codex> 
 <abstract>AUInputElement.h</abstract>
 <\codex>
*/
#include "AUBase.h"

inline bool HasGoodBufferPointers(const AudioBufferList &abl, UInt32 nBytes)
{
    const AudioBuffer *buf = abl.mBuffers;
    for (UInt32 i = abl.mNumberBuffers; i--;++buf) {
        if (buf->mData == NULL || buf->mDataByteSize < nBytes)
            return false;
    }
    return true;
}


//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//  AUInputElement::AUInputElement
//
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
AUInputElement::AUInputElement(AUBase *audioUnit) :
    AUIOElement(audioUnit),
    mInputType(kNoInput)
{
}

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//  AUInputElement::SetConnection
//
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
void    AUInputElement::SetConnection(const AudioUnitConnection &conn)
{
    if (conn.sourceAudioUnit == 0) {
        Disconnect();
        return;
    }   

    mInputType = kFromConnection;
    mConnection = conn;
    AllocateBuffer();

    mConnInstanceStorage = NULL;

#if !CA_USE_AUDIO_PLUGIN_ONLY
    mConnRenderProc = NULL;
    UInt32 size = sizeof(AudioUnitRenderProc);
    OSStatus result = AudioUnitGetProperty( conn.sourceAudioUnit,
                            kAudioUnitProperty_FastDispatch,
                            kAudioUnitScope_Global,
                            kAudioUnitRenderSelect,
                            &mConnRenderProc,
                            &size);
    if (result == noErr)
        mConnInstanceStorage = CMgr_GetComponentInstanceStorage (conn.sourceAudioUnit);
    else
        mConnRenderProc = NULL;
#endif
}

void    AUInputElement::Disconnect()
{
    mInputType = kNoInput;
    mIOBuffer.Deallocate();
}



//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//  AUInputElement::SetInputCallback
//
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
void    AUInputElement::SetInputCallback(AURenderCallback proc, void *refCon)
{
    if (proc == NULL)
        Disconnect();
    else {
        mInputType = kFromCallback;
        mInputProc = proc;
        mInputProcRefCon = refCon;
        AllocateBuffer();
    }
}

OSStatus    AUInputElement::SetStreamFormat(const CAStreamBasicDescription &fmt)
{
    OSStatus err = AUIOElement::SetStreamFormat(fmt);
    if (err == AUBase::noErr)
        AllocateBuffer();
    return err;
}

OSStatus        AUInputElement::PullInput(  AudioUnitRenderActionFlags &    ioActionFlags,
                                            const AudioTimeStamp &          inTimeStamp,
                                            AudioUnitElement                inElement,
                                            UInt32                          nFrames)
{   
    if (!IsActive())
        return kAudioUnitErr_NoConnection;

    AudioBufferList *pullBuffer;

    if (HasConnection() || !WillAllocateBuffer())
        pullBuffer = &mIOBuffer.PrepareNullBuffer(mStreamFormat, nFrames);
    else
        pullBuffer = &mIOBuffer.PrepareBuffer(mStreamFormat, nFrames);

    return PullInputWithBufferList (ioActionFlags, inTimeStamp, inElement, nFrames, pullBuffer);
}
```

[Next](AUPublic-AUBase-AUInputElement.h.md)[Previous](AUPublic-AUBase-AUDispatch.h.md)

