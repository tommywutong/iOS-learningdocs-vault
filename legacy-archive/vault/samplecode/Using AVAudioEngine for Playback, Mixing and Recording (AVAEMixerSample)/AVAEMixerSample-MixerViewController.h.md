---
title: Using AVAudioEngine for Playback, Mixing and Recording (AVAEMixerSample)
apple_id: TP40015134
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2017-03-23'
source_url: https://developer.apple.com/library/archive/samplecode/AVAEMixerSample/Listings/AVAEMixerSample_MixerViewController_h.html
archived_at: '2026-07-18T02:59:59.576713Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Using AVAudioEngine for Playback, Mixing and Recording (AVAEMixerSample)](Using%20AVAudioEngine%20for%20Playback%2C%20Mixing%20and%20Recording%20%28AVAEMixerSample%29.md)


[Next](AVAEMixerSample-AudioViewController.m.md)[Previous](AVAEMixerSample-main.m.md)

# AVAEMixerSample/MixerViewController.h

```objc
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    The MixerViewController class provides specific UI Elements to interact with the AVAudioEngine mainMixerNode object.

                    CAUITransportButton *recordButton;          Installs a tap on the output bus for the mixer and records to a file
                    UISlider            *masterVolumeSlider;    Sets the output volume of the mixer
*/

#import "AudioViewController.h"

@interface MixerViewController : AudioViewController

@end
```

[Next](AVAEMixerSample-AudioViewController.m.md)[Previous](AVAEMixerSample-main.m.md)

