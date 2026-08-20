---
title: Using AVAudioEngine for Playback, Mixing and Recording (AVAEMixerSample)
apple_id: TP40015134
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2017-03-23'
source_url: https://developer.apple.com/library/archive/samplecode/AVAEMixerSample/Listings/AVAEMixerSample_ReverbViewController_m.html
archived_at: '2026-07-18T02:59:59.871948Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Using AVAudioEngine for Playback, Mixing and Recording (AVAEMixerSample)](Using%20AVAudioEngine%20for%20Playback%2C%20Mixing%20and%20Recording%20%28AVAEMixerSample%29.md)


[Next](AVAEMixerSample-InstrumentViewController.m.md)[Previous](AVAEMixerSample-CAUITransportButton.h.md)

# AVAEMixerSample/ReverbViewController.m

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The ReverbViewController class provides specific UI Elements to interact with the AVAudioUnitReverb object.

                 UISlider *reverbWetDrySlider;   Set the wet/dry mix of the current reverb preset
                 UIPickerView *reverbTypePicker; Select a preset for the unit
*/

@import AudioToolbox;

#import "ReverbViewController.h"

@interface ReverbViewController ()

@property (unsafe_unretained, nonatomic) IBOutlet UISlider *reverbWetDrySlider;

@end

@implementation ReverbViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view.
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

- (void)updateUIElements
{
    self.reverbWetDrySlider.value = self.audioEngine.reverbWetDryMix;
}

- (IBAction)setWetDryMix:(id)sender {
    self.audioEngine.reverbWetDryMix = ((UISlider *)sender).value;
}

@end
```

[Next](AVAEMixerSample-InstrumentViewController.m.md)[Previous](AVAEMixerSample-CAUITransportButton.h.md)

