---
title: Using AVAudioEngine for Playback, Mixing and Recording (AVAEMixerSample)
apple_id: TP40015134
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2017-03-23'
source_url: https://developer.apple.com/library/archive/samplecode/AVAEMixerSample/Listings/AVAEMixerSample_AudioEngineViewController_m.html
archived_at: '2026-07-18T02:59:58.498730Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Using AVAudioEngine for Playback, Mixing and Recording (AVAEMixerSample)](Using%20AVAudioEngine%20for%20Playback%2C%20Mixing%20and%20Recording%20%28AVAEMixerSample%29.md)


[Next](AVAEMixerSample-AudioEngine.h.md)[Previous](AVAEMixerSample-AudioEngine.m.md)

# AVAEMixerSample/AudioEngineViewController.m

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 AudioEngineViewController hosts the AudioEngine UI as well as the UI for each individual node

             This controller is linked to a size-classes storyboard that supports both iPhone and iPad UI
*/

#import "AudioEngineViewController.h"
#import "AudioViewController.h"

#import "AudioEngine.h"
#import "CAAVAudioUnitView.h"
#import "CAUITransportButton.h"


@interface AudioEngineViewController () <AudioEngineDelegate>

@property (strong) AudioEngine *audioEngine;
@property (unsafe_unretained, nonatomic) IBOutlet UIView *shadowView;

@end

@implementation AudioEngineViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view.
    [self setupUI];

}

- (void)setupUI
{
    //apply a drop shadow to the boxes
    self.shadowView.layer.shadowColor = [UIColor blackColor].CGColor;
    self.shadowView.layer.shadowRadius = 10.0f;
    self.shadowView.layer.shadowOffset = CGSizeMake(0.0f, 5.0f);
    self.shadowView.layer.shadowOpacity = 0.5f;
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

- (void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender
{
    //initialize
    if (!self.audioEngine) {
        self.audioEngine = [[AudioEngine alloc] init];
        self.audioEngine.delegate = self;
    }

    //Pass the audio engine to all the audioviewcontrollers
    if ([[segue.destinationViewController class] isSubclassOfClass:[AudioViewController class]]) {
        AudioViewController *controller = (AudioViewController*)segue.destinationViewController;
        controller.audioEngine = self.audioEngine;
    }

}


#pragma mark AudioEngineDelegate Methods
- (void)engineWasInterrupted
{
    //update the UI elements for all the audioviewcontrollers
    for (UIViewController *controller in self.childViewControllers) {
        if ([[controller class] isSubclassOfClass:[AudioViewController class]]) {
            [((AudioViewController*)controller) updateUIElements];
        }
    }
}

- (void)engineConfigurationHasChanged
{
    //update the UI elements for all the audioviewcontrollers
    for (UIViewController *controller in self.childViewControllers) {
        if ([[controller class] isSubclassOfClass:[AudioViewController class]]) {
            [((AudioViewController*)controller) updateUIElements];
        }
    }
}


@end
```

[Next](AVAEMixerSample-AudioEngine.h.md)[Previous](AVAEMixerSample-AudioEngine.m.md)

