---
title: Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor
  and Offline)
apple_id: DTS40013969
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-02-19'
source_url: https://developer.apple.com/library/archive/samplecode/sc2195/Listings/AudioUnitGeneratorExample_AUPinkNoise_h.html
archived_at: '2026-07-26T19:54:11.240330Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor and Offline)](Audio%20Unit%20Examples%20%28AudioUnit%20Effect%2C%20Generator%2C%20Instrument%2C%20MIDI%20Processor%20and.md)


[Next](AudioUnitGeneratorExample-ReadMe.md.md)[Previous](AudioUnitGeneratorExample-AUPinkNoise.cpp.md)

# AudioUnitGeneratorExample/AUPinkNoise.h

```swift
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Pink Noise AU
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

    virtual bool                CanScheduleParameters() const { return false; }

private:
    PinkNoiseGenerator *mPink;

    CAAudioChannelLayout mOutputChannelLayout;
};

#endif
```

[Next](AudioUnitGeneratorExample-ReadMe.md.md)[Previous](AudioUnitGeneratorExample-AUPinkNoise.cpp.md)

