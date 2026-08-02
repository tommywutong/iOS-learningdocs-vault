---
title: Using AVAudioEngine for Playback, Mixing and Recording (AVAEMixerSample)
apple_id: TP40015134
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2017-03-23'
source_url: https://developer.apple.com/library/archive/samplecode/AVAEMixerSample/Listings/AVAEMixerSample_PlayerViewController_m.html
archived_at: '2026-07-18T02:59:59.788457Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Using AVAudioEngine for Playback, Mixing and Recording (AVAEMixerSample)](Using%20AVAudioEngine%20for%20Playback%2C%20Mixing%20and%20Recording%20%28AVAEMixerSample%29.md)


[Next](AVAEMixerSample-MixerViewController.m.md)[Previous](AVAEMixerSample-AudioEngine.h.md)

# AVAEMixerSample/PlayerViewController.m

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The PlayerViewController class provides specific UI Elements to interact with the PlayerNode.

             UISlider            *playerVolumeSlider;    Sets the volume on the player
             UISlider            *playerPanSlider;       Sets the pan on the player
             UIButton            *playerPlayButton;      Toggles the player state
             UISegmentedControl  *playerSegmentControl;  Provides a selection for different buffers/files
*/

#import "PlayerViewController.h"

@interface PlayerViewController ()

@property (unsafe_unretained, nonatomic) IBOutlet UISlider *playerVolumeSlider;
@property (unsafe_unretained, nonatomic) IBOutlet UISlider *playerPanSlider;
@property (unsafe_unretained, nonatomic) IBOutlet UIButton *playerPlayButton;
@property (unsafe_unretained, nonatomic) IBOutlet UISegmentedControl *playerSegmentControl;

@end

@implementation PlayerViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view.

    [[NSNotificationCenter defaultCenter] addObserver:self selector:@selector(enableToggle:) name:kRecordingCompletedNotification object:nil];
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

- (IBAction)toggleBuffer:(id)sender
{
    [self.audioEngine toggleBuffer:((UISegmentedControl *)sender).selectedSegmentIndex];
}

- (IBAction)togglePlay:(id)sender
{
    [self.audioEngine togglePlayer];
    [self styleButton: _playerPlayButton isPlaying: self.audioEngine.playerIsPlaying];
}

- (IBAction)setVolume:(id)sender
{
    self.audioEngine.playerVolume = ((UISlider *)sender).value;
}

- (IBAction)setPan:(id)sender
{
    self.audioEngine.playerPan = ((UISlider *)sender).value;
}

- (void)enableToggle:(NSNotification*)notification
{
    [self.playerSegmentControl setEnabled:YES forSegmentAtIndex:1];
}

- (void)updateUIElements
{
    [self styleButton: _playerPlayButton isPlaying: self.audioEngine.playerIsPlaying];
}


@end
```

[Next](AVAEMixerSample-MixerViewController.m.md)[Previous](AVAEMixerSample-AudioEngine.h.md)

