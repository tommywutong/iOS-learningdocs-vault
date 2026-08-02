---
title: 'AVFoundationSimplePlayer-iOS: Using AVFoundation to Play Media'
apple_id: TP40016103
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/AVFoundationSimplePlayer-iOS/Listings/Objective_C_AVFoundationSimplePlayer_iOS_AAPLPlayerView_m.html
archived_at: '2026-07-18T03:00:15.677863Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVFoundationSimplePlayer-iOS: Using AVFoundation to Play Media](AVFoundationSimplePlayer-iOS-%20Using%20AVFoundation%20to%20Play%20Media.md)


[Next](Objective-C-AVFoundationSimplePlayer-iOS-AAPLPlayerViewController.m.md)[Previous](Objective-C-AVFoundationSimplePlayer-iOS-AAPLAppDelegate.m.md)

# Objective-C/AVFoundationSimplePlayer-iOS/AAPLPlayerView.m

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    View containing an AVPlayerLayer.
*/

@import Foundation;
@import AVFoundation;
#import "AAPLPlayerView.h"


@implementation AAPLPlayerView

- (AVPlayer *)player {
    return self.playerLayer.player;
}

- (void)setPlayer:(AVPlayer *)player {
    self.playerLayer.player = player;
}

// override UIView
+ (Class)layerClass {
    return [AVPlayerLayer class];
}

- (AVPlayerLayer *)playerLayer {
    return (AVPlayerLayer *)self.layer;
}

@end
```

[Next](Objective-C-AVFoundationSimplePlayer-iOS-AAPLPlayerViewController.m.md)[Previous](Objective-C-AVFoundationSimplePlayer-iOS-AAPLAppDelegate.m.md)

