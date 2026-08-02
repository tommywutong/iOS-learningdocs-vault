---
title: Using AVAudioEngine for Playback, Mixing and Recording (AVAEMixerSample)
apple_id: TP40015134
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2017-03-23'
source_url: https://developer.apple.com/library/archive/samplecode/AVAEMixerSample/Listings/AVAEMixerSample_ReverbViewController_h.html
archived_at: '2026-07-18T02:59:59.841108Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Using AVAudioEngine for Playback, Mixing and Recording (AVAEMixerSample)](Using%20AVAudioEngine%20for%20Playback%2C%20Mixing%20and%20Recording%20%28AVAEMixerSample%29.md)


[Next](AVAEMixerSample-AudioEngineViewController.h.md)[Previous](AVAEMixerSample-SequencerViewController.m.md)

# AVAEMixerSample/ReverbViewController.h

```objc
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    The ReverbViewController class provides specific UI Elements to interact with the AVAudioUnitReverb object.

                    UISlider *reverbWetDrySlider;   Set the wet/dry mix of the current reverb preset
                    UIPickerView *reverbTypePicker; Select a preset for the unit
*/

#import "AudioViewController.h"

@interface ReverbViewController : AudioViewController

@end
```

[Next](AVAEMixerSample-AudioEngineViewController.h.md)[Previous](AVAEMixerSample-SequencerViewController.m.md)

