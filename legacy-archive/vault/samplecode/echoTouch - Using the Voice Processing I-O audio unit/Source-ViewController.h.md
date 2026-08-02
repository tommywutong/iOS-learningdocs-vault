---
title: echoTouch - Using the Voice Processing I/O audio unit
apple_id: TP40017575
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AudioToolbox
published: '2016-11-29'
source_url: https://developer.apple.com/library/archive/samplecode/echoTouch/Listings/Source_ViewController_h.html
archived_at: '2026-07-18T03:29:08.489248Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [echoTouch - Using the Voice Processing I/O audio unit](echoTouch%20-%20Using%20the%20Voice%20Processing%20I-O%20audio%20unit.md)


[Next](Source-echoTouchHelper.h.md)[Previous](README.md.md)

# Source/ViewController.h

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The main controller class.
*/

#import <UIKit/UIKit.h>
#import <Foundation/Foundation.h>
#import <AVFoundation/AVFoundation.h>
#import <AVFoundation/AVAudioSession.h>
#import <AudioToolbox/AudioToolbox.h>

#import "AUOutputBL.h"
#import "AVLevelMeter.h"
#import "AULevelMeter.h"

@interface ViewController : UIViewController <AVAudioPlayerDelegate> {
IBOutlet AVLevelMeter       *fxMeter;
IBOutlet AULevelMeter       *speechMeter;
IBOutlet AULevelMeter       *voiceUnitMeter;

IBOutlet UIBarButtonItem    *playButton;
IBOutlet UIBarButtonItem    *recordButton;
IBOutlet UISwitch           *fxSwitch;
IBOutlet UISwitch           *voiceSwitch;
IBOutlet UISwitch           *bypassSwitch;

AVAudioPlayer               *fxPlayer;

BOOL                        recording;
UInt32                      bypassState;

AUOutputBL                  *inputBL;

CFURLRef                    fileURL;
ExtAudioFileRef             fileRef;
AVAudioPlayer               *filePlayer;
AVAudioFormat               *fileFormat;

void                        *speechData;
UInt64                      speechDataSize;
UInt64                      speechDataOffset;
BOOL                        playSpeech;

AudioUnit                   voiceUnit;
CAStreamBasicDescription    voiceIOFormat;
}

- (IBAction)fxSwitchPressed:(UISwitch*)sender;
- (IBAction)voiceSwitchPressed:(UISwitch*)sender;
- (IBAction)bypassSwitchPressed:(UISwitch*)sender;
- (IBAction)playPressed:(UIBarButtonItem*)sender;
- (IBAction)recordPressed:(UIBarButtonItem*)sender;

@property (nonatomic, retain)   AVLevelMeter*               fxMeter;
@property (nonatomic, retain)   AULevelMeter*               speechMeter;
@property (nonatomic, retain)   AULevelMeter*               voiceUnitMeter;

@property (nonatomic, retain)   AVAudioPlayer*              fxPlayer;
@property (nonatomic, assign)   AudioUnit                   voiceUnit;
@property (nonatomic, assign)   AUOutputBL*                 inputBL;
@property (assign)              BOOL                        recording;
@property (assign)              UInt32                      bypassState;
@property (nonatomic, assign)   ExtAudioFileRef             fileRef;

@property (nonatomic, assign)   void*                       speechData;
@property (nonatomic, assign)   UInt64                      speechDataSize;
@property (nonatomic, assign)   UInt64                      speechDataOffset;
@property (nonatomic)           BOOL                        playSpeech;
@property (nonatomic, assign)   CAStreamBasicDescription    voiceIOFormat;

@end
```

[Next](Source-echoTouchHelper.h.md)[Previous](README.md.md)

