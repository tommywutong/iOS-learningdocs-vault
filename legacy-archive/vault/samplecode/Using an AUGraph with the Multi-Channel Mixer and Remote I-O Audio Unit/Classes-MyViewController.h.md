---
title: Using an AUGraph with the Multi-Channel Mixer and Remote I/O Audio Unit
apple_id: TP40016060
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: CoreAudio
published: '2015-06-19'
source_url: https://developer.apple.com/library/archive/samplecode/iOSMultichannelMixerTest/Listings/Classes_MyViewController_h.html
archived_at: '2026-07-18T03:29:36.175352Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Using an AUGraph with the Multi-Channel Mixer and Remote I/O Audio Unit](Using%20an%20AUGraph%20with%20the%20Multi-Channel%20Mixer%20and%20Remote%20I-O%20Audio%20Unit.md)


[Next](Resources-info.html.md)[Previous](Classes-MultichannelMixerController.h.md)

# Classes/MyViewController.h

```objc
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    The main view controller of this app
*/

#import <UIKit/UIKit.h>
#import <Foundation/Foundation.h>
#import <AVFoundation/AVFoundation.h>
#import <AudioToolbox/AudioToolbox.h>

#import "MultichannelMixerController.h"

@interface MyViewController : UIViewController
{
    IBOutlet UIView     *instructionsView;
    IBOutlet UIWebView  *webView;
    IBOutlet UIView     *contentView;

    UIBarButtonItem     *flipButton;
    UIBarButtonItem     *doneButton;

    IBOutlet UIButton   *startButton;

    IBOutlet UISwitch   *bus0Switch;
    IBOutlet UISlider   *bus0VolumeSlider;
    IBOutlet UISwitch   *bus1Switch;
    IBOutlet UISlider   *bus1VolumeSlider;
    IBOutlet UISlider   *outputVolumeSlider;

    IBOutlet MultichannelMixerController *mixerController;
}

@property (readonly, nonatomic) UIView    *instructionsView;
@property (readonly, nonatomic) UIWebView *webView;
@property (readonly, nonatomic) UIView    *contentView;

@property (nonatomic, retain) UIBarButtonItem *flipButton;
@property (nonatomic, retain) UIBarButtonItem *doneButton;

@property (readonly, nonatomic) UIButton *startButton;

@property (readonly, nonatomic) UISwitch *bus0Switch;
@property (readonly, nonatomic) UISlider *bus0VolumeSlider;
@property (readonly, nonatomic) UISwitch *bus1Switch;
@property (readonly, nonatomic) UISlider *bus1VolumeSlider;
@property (readonly, nonatomic) UISlider *outputVolumeSlider;

@property (readonly, nonatomic)MultichannelMixerController *mixerController;

- (void)setUIDefaults;
- (void)stopForInterruption;

- (IBAction)enableInput:(UISwitch *)sender;
- (IBAction)setInputVolume:(UISlider *)sender;
- (IBAction)setOutputVolume:(UISlider *)sender;

- (IBAction)doSomethingAction:(id)sender;

@end
```

[Next](Resources-info.html.md)[Previous](Classes-MultichannelMixerController.h.md)

