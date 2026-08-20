---
title: Using AVAudioEngine for Playback, Mixing and Recording (AVAEMixerSample)
apple_id: TP40015134
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2017-03-23'
source_url: https://developer.apple.com/library/archive/samplecode/AVAEMixerSample/Listings/AVAEMixerSample_AudioViewController_h.html
archived_at: '2026-07-18T02:59:58.854358Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Using AVAudioEngine for Playback, Mixing and Recording (AVAEMixerSample)](Using%20AVAudioEngine%20for%20Playback%2C%20Mixing%20and%20Recording%20%28AVAEMixerSample%29.md)


[Next](AVAEMixerSample-CAUITransportButton.m.md)[Previous](AVAEMixerSample-CAAVParameterView.h.md)

# AVAEMixerSample/AudioViewController.h

```objc
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This class represents a node/sequencer.
                    It contains -
                        A reference to the AudioEngine
                        Basic Views for displaying parameters. Subclasses can provide their own views for customization
*/

@import UIKit;

#import "AudioEngine.h"
#import "CAAVAudioUnitView.h"
#import "CAAVParameterView.h"

@interface AudioViewController : UIViewController

@property (strong) AudioEngine *audioEngine;

@property (weak, nonatomic) IBOutlet UIView *titleView;
@property (weak, nonatomic) IBOutlet UILabel *titleLabel;
@property (weak, nonatomic) IBOutlet UIStackView *stackView;
@property (weak, nonatomic) IBOutlet CAAVParameterView *parameterView;

- (void)updateUIElements;
- (void)styleButton:(UIButton *)button isPlaying:(BOOL)isPlaying;

@end
```

[Next](AVAEMixerSample-CAUITransportButton.m.md)[Previous](AVAEMixerSample-CAAVParameterView.h.md)

