---
title: Using AVAudioEngine for Playback, Mixing and Recording (AVAEMixerSample)
apple_id: TP40015134
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2017-03-23'
source_url: https://developer.apple.com/library/archive/samplecode/AVAEMixerSample/Listings/AVAEMixerSample_SequencerViewController_h.html
archived_at: '2026-07-18T02:59:59.912526Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Using AVAudioEngine for Playback, Mixing and Recording (AVAEMixerSample)](Using%20AVAudioEngine%20for%20Playback%2C%20Mixing%20and%20Recording%20%28AVAEMixerSample%29.md)


[Next](AVAEMixerSample-DistortionViewController.m.md)[Previous](AVAEMixerSample-AppDelegate.m.md)

# AVAEMixerSample/SequencerViewController.h

```objc
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    The SequencerViewController class provides specific UI Elements to interact with the AVAudioSequencer object. The sequencer is not directly part of AVAudioEngine.

                    UISlider *sequencerPlaybackRateSlider;  Set the playback rate for the sequencer
                    UISlider *sequencerPositionSlider;      Set the current position for the current track
                    UIButton *sequencerPlayButton;          Toggle the state of the sequencer
*/

#import "AudioViewController.h"

@interface SequencerViewController : AudioViewController

@end
```

[Next](AVAEMixerSample-DistortionViewController.m.md)[Previous](AVAEMixerSample-AppDelegate.m.md)

