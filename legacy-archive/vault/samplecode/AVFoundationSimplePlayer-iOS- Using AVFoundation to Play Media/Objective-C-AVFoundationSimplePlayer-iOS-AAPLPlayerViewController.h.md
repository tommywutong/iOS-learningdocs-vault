---
title: 'AVFoundationSimplePlayer-iOS: Using AVFoundation to Play Media'
apple_id: TP40016103
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/AVFoundationSimplePlayer-iOS/Listings/Objective_C_AVFoundationSimplePlayer_iOS_AAPLPlayerViewController_h.html
archived_at: '2026-07-18T03:00:15.453712Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVFoundationSimplePlayer-iOS: Using AVFoundation to Play Media](AVFoundationSimplePlayer-iOS-%20Using%20AVFoundation%20to%20Play%20Media.md)


[Next](Objective-C-AVFoundationSimplePlayer-iOS-AAPLPlayerView.h.md)[Previous](Objective-C-AVFoundationSimplePlayer-iOS-main.m.md)

# Objective-C/AVFoundationSimplePlayer-iOS/AAPLPlayerViewController.h

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    View controller containing a player view and basic playback controls.
*/

@import UIKit;


@class AAPLPlayerView;

@interface AAPLPlayerViewController : UIViewController

@property (readonly) AVPlayer *player;
@property AVURLAsset *asset;

@property CMTime currentTime;
@property (readonly) CMTime duration;
@property float rate;

@property (weak) IBOutlet UISlider *timeSlider;
@property (weak) IBOutlet UILabel *startTimeLabel;
@property (weak) IBOutlet UILabel *durationLabel;
@property (weak) IBOutlet UIButton *rewindButton;
@property (weak) IBOutlet UIButton *playPauseButton;
@property (weak) IBOutlet UIButton *fastForwardButton;
@property (weak) IBOutlet AAPLPlayerView *playerView;

@end
```

[Next](Objective-C-AVFoundationSimplePlayer-iOS-AAPLPlayerView.h.md)[Previous](Objective-C-AVFoundationSimplePlayer-iOS-main.m.md)

