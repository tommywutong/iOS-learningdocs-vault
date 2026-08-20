---
title: AudioUnitGeneratorExample
apple_id: DTS40008637
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2012-10-08'
source_url: https://developer.apple.com/library/archive/samplecode/AUPinkNoise/Listings/AUPinkNoise_h.html
archived_at: '2026-07-18T02:59:47.936320Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AudioUnitGeneratorExample](AudioUnitGeneratorExample.md)


[Next](AUPinkNoise.r.md)[Previous](AUPinkNoise.cpp.md)

Relevant replacement documents include:

- [http://developer.apple.com/library/mac/samplecode/sc2195/Introduction/Intro.html#//apple_ref/doc/uid/DTS40013969](https://developer.apple.com/library/mac/samplecode/sc2195/Introduction/Intro.html#//apple_ref/doc/uid/DTS40013969)

# AUPinkNoise.h

```c
/*
 <codex>
 <abstract>AUPinkNoise.h</abstract>
 <\codex>
*/
#include "AUBase.h"
#include "CAAudioChannelLayout.h"
#include "Pink.h"
#include <Carbon/Carbon.h>

#ifndef __AUPinkNoise_h__
#define __AUPinkNoise_h__

#include "AUPinkNoiseVersion.h"

#pragma mark ____AUPinkNoise Parameters

// parameters
static const float kDefaultValue_Volume = 0.7071;

static CFStringRef kParameterVolumeName = CFSTR("Volume");
static CFStringRef kParameterOnName = CFSTR("On/Off");

enum {
    kParam_Volume =0,
    kParam_On=1,
    kNumberOfParameters=2
};

#pragma mark ____AUPinkNoise
class AUPinkNoise : public AUBase
{
public:
                                AUPinkNoise(AudioUnit component);

    virtual void                Cleanup();

    virtual OSStatus            Initialize();

    virtual OSStatus            GetPropertyInfo(    AudioUnitPropertyID             inID,
                                                    AudioUnitScope                  inScope,
                                                    AudioUnitElement                inElement,
                                                    UInt32 &                        outDataSize,
                                                    Boolean &                       outWritable);

    virtual OSStatus            GetProperty(    AudioUnitPropertyID         inID,
                                                AudioUnitScope              inScope,
                                                AudioUnitElement            inElement,
                                                void *                      outData);

    virtual OSStatus            GetParameterInfo(   AudioUnitScope          inScope,
                                                    AudioUnitParameterID    inParameterID,
                                                    AudioUnitParameterInfo  &outParameterInfo);

    virtual OSStatus    Render( AudioUnitRenderActionFlags &ioActionFlags,
                                        const AudioTimeStamp &      inTimeStamp,
                                        UInt32                      nFrames);

    virtual bool                StreamFormatWritable(   AudioUnitScope                  scope,
                                                        AudioUnitElement                element);

    virtual UInt32              SupportedNumChannels(   const AUChannelInfo**           outInfo);

    virtual UInt32              GetChannelLayoutTags(   AudioUnitScope              scope,
                                                        AudioUnitElement            element,
                                                        AudioChannelLayoutTag *     outLayoutTags);

    virtual UInt32              GetAudioChannelLayout(  AudioUnitScope              scope,
                                                        AudioUnitElement            element,
                                                        AudioChannelLayout *        outLayoutPtr,
                                                        Boolean &                   outWritable);

    virtual OSStatus            SetAudioChannelLayout(  AudioUnitScope              scope, 
                                                        AudioUnitElement            element,
                                                        const AudioChannelLayout *  inLayout);

    virtual OSStatus            RemoveAudioChannelLayout(AudioUnitScope scope, AudioUnitElement element);

    virtual bool                SupportsTail () { return false; }

    /*! @method Version */
    virtual OSStatus            Version() { return kAUPinkNoiseVersion; }

private:
    PinkNoiseGenerator *mPink;

    CAAudioChannelLayout mOutputChannelLayout;
};

#endif
```

[Next](AUPinkNoise.r.md)[Previous](AUPinkNoise.cpp.md)

