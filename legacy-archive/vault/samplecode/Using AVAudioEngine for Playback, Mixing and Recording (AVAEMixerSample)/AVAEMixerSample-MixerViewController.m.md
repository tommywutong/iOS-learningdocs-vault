---
title: Using AVAudioEngine for Playback, Mixing and Recording (AVAEMixerSample)
apple_id: TP40015134
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2017-03-23'
source_url: https://developer.apple.com/library/archive/samplecode/AVAEMixerSample/Listings/AVAEMixerSample_MixerViewController_m.html
archived_at: '2026-07-18T02:59:59.648775Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Using AVAudioEngine for Playback, Mixing and Recording (AVAEMixerSample)](Using%20AVAudioEngine%20for%20Playback%2C%20Mixing%20and%20Recording%20%28AVAEMixerSample%29.md)


[Next](AVAEMixerSample-CAAVParameterView.m.md)[Previous](AVAEMixerSample-PlayerViewController.m.md)

# AVAEMixerSample/MixerViewController.m

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The MixerViewController class provides specific UI Elements to interact with the AVAudioEngine mainMixerNode object.

                 CAUITransportButton *recordButton;          Installs a tap on the output bus for the mixer and records to a file
                 UISlider            *masterVolumeSlider;    Sets the output volume of the mixer
*/

#import "MixerViewController.h"
#import "CAUITransportButton.h"

@interface MixerViewController ()

@property (unsafe_unretained, nonatomic) IBOutlet CAUITransportButton *recordButton;
@property (unsafe_unretained, nonatomic) IBOutlet UISlider *masterVolumeSlider;

@property (getter=isRecording) BOOL recording;

@end

@implementation MixerViewController

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
    self.masterVolumeSlider.value   = self.audioEngine.outputVolume;
    self.recordButton.drawingStyle = recordButtonStyle;
    self.recordButton.fillColor = [UIColor colorWithRed:255/255.0 green:102/255.0 blue:102/255.0 alpha:1].CGColor;
}

- (IBAction)setMasterVolume:(id)sender {
    self.audioEngine.outputVolume = ((UISlider *)sender).value;
}

- (IBAction)recordAction:(id)sender {
    self.recording = !self.recording;

    if (self.recording)
        [self.audioEngine startRecordingMixerOutput];
    else
        [self.audioEngine stopRecordingMixerOutput];

    self.recordButton.drawingStyle = self.recording ? recordEnabledButtonStyle : recordButtonStyle;
}


@end
```

[Next](AVAEMixerSample-CAAVParameterView.m.md)[Previous](AVAEMixerSample-PlayerViewController.m.md)

