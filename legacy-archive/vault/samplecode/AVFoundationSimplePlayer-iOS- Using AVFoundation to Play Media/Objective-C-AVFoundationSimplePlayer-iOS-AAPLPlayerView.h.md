---
title: 'AVFoundationSimplePlayer-iOS: Using AVFoundation to Play Media'
apple_id: TP40016103
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/AVFoundationSimplePlayer-iOS/Listings/Objective_C_AVFoundationSimplePlayer_iOS_AAPLPlayerView_h.html
archived_at: '2026-07-18T03:00:15.619300Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVFoundationSimplePlayer-iOS: Using AVFoundation to Play Media](AVFoundationSimplePlayer-iOS-%20Using%20AVFoundation%20to%20Play%20Media.md)


[Next](Objective-C-AVFoundationSimplePlayer-iOS-AAPLAppDelegate.m.md)[Previous](Objective-C-AVFoundationSimplePlayer-iOS-AAPLPlayerViewController.h.md)

# Objective-C/AVFoundationSimplePlayer-iOS/AAPLPlayerView.h

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    View containing an AVPlayerLayer.
*/

@import UIKit;

@class AVPlayer;

@interface AAPLPlayerView : UIView
@property AVPlayer *player;
@property (readonly) AVPlayerLayer *playerLayer;
@end
```

[Next](Objective-C-AVFoundationSimplePlayer-iOS-AAPLAppDelegate.m.md)[Previous](Objective-C-AVFoundationSimplePlayer-iOS-AAPLPlayerViewController.h.md)

