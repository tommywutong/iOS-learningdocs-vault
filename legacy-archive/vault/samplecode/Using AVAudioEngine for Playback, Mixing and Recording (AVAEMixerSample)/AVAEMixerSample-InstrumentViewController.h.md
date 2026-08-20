---
title: Using AVAudioEngine for Playback, Mixing and Recording (AVAEMixerSample)
apple_id: TP40015134
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2017-03-23'
source_url: https://developer.apple.com/library/archive/samplecode/AVAEMixerSample/Listings/AVAEMixerSample_InstrumentViewController_h.html
archived_at: '2026-07-18T02:59:59.497979Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Using AVAudioEngine for Playback, Mixing and Recording (AVAEMixerSample)](Using%20AVAudioEngine%20for%20Playback%2C%20Mixing%20and%20Recording%20%28AVAEMixerSample%29.md)


[Next](AVAEMixerSample-CAAVAudioUnitView.h.md)[Previous](AVAEMixerSample-InstrumentViewController.m.md)

# AVAEMixerSample/InstrumentViewController.h

```objc
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    The InstrumentViewController class provides specific UI Elements to interact with the AVAudioSequencer object. The sequencer is not directly part of AVAudioEngine.

                        UISlider *samplerDirectVolumeSlider;    Sets the volume of the instrument using AVAudioMixingDestination
                        UISlider *reverbVolumeSlider;           Sets the volume of the instrument using AVAudioMixingDestination
*/

#import "AudioViewController.h"

@interface InstrumentViewController : AudioViewController

@end
```

[Next](AVAEMixerSample-CAAVAudioUnitView.h.md)[Previous](AVAEMixerSample-InstrumentViewController.m.md)

