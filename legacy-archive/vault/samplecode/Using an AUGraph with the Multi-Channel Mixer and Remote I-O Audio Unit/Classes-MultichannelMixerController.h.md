---
title: Using an AUGraph with the Multi-Channel Mixer and Remote I/O Audio Unit
apple_id: TP40016060
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: CoreAudio
published: '2015-06-19'
source_url: https://developer.apple.com/library/archive/samplecode/iOSMultichannelMixerTest/Listings/Classes_MultichannelMixerController_h.html
archived_at: '2026-07-18T03:29:35.909756Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Using an AUGraph with the Multi-Channel Mixer and Remote I/O Audio Unit](Using%20an%20AUGraph%20with%20the%20Multi-Channel%20Mixer%20and%20Remote%20I-O%20Audio%20Unit.md)


[Next](Classes-MyViewController.h.md)[Previous](Classes-MultichannelMixerController.mm.md)

# Classes/MultichannelMixerController.h

```objc
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    The Controller Class for the AUGraph.
*/

#import <AudioToolbox/AudioToolbox.h>
#import <AudioUnit/AudioUnit.h>
#import <AVFoundation/AVAudioFormat.h>

#import "CAComponentDescription.h"

#define MAXBUFS  2
#define NUMFILES 2

typedef struct {
    AudioStreamBasicDescription asbd;
    Float32 *data;
    UInt32 numFrames;
    UInt32 sampleNum;
} SoundBuffer, *SoundBufferPtr;

@interface MultichannelMixerController : NSObject
{
    CFURLRef sourceURL[2];

    AVAudioFormat *mAudioFormat;

    AUGraph   mGraph;
    AudioUnit mMixer;
    AudioUnit mOutput;

    SoundBuffer mSoundBuffer[MAXBUFS];

    Boolean isPlaying;
}

@property (readonly, nonatomic) Boolean isPlaying;

- (void)initializeAUGraph;

- (void)enableInput:(UInt32)inputNum isOn:(AudioUnitParameterValue)isONValue;
- (void)setInputVolume:(UInt32)inputNum value:(AudioUnitParameterValue)value;
- (void)setOutputVolume:(AudioUnitParameterValue)value;

- (void)startAUGraph;
- (void)stopAUGraph;

@end
```

[Next](Classes-MyViewController.h.md)[Previous](Classes-MultichannelMixerController.mm.md)

