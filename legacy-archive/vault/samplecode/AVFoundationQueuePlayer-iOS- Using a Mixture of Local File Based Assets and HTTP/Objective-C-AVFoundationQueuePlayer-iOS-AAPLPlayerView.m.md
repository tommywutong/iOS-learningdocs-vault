---
title: 'AVFoundationQueuePlayer-iOS: Using a Mixture of Local File Based Assets and
  HTTP Live Streaming Assets with AVFoundation'
apple_id: TP40016104
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/AVFoundationQueuePlayer-iOS/Listings/Objective_C_AVFoundationQueuePlayer_iOS_AAPLPlayerView_m.html
archived_at: '2026-07-18T03:00:14.748618Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVFoundationQueuePlayer-iOS: Using a Mixture of Local File Based Assets and HTTP Live Streaming Assets with AVFoundation](AVFoundationQueuePlayer-iOS-%20Using%20a%20Mixture%20of%20Local%20File%20Based%20Assets%20and%20HTTP.md)


[Next](Objective-C-AVFoundationQueuePlayer-iOS-AAPLPlayerViewController.m.md)[Previous](Objective-C-AVFoundationQueuePlayer-iOS-AAPLQueuedItemCollectionViewCell.h.md)

# Objective-C/AVFoundationQueuePlayer-iOS/AAPLPlayerView.m

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

[Next](Objective-C-AVFoundationQueuePlayer-iOS-AAPLPlayerViewController.m.md)[Previous](Objective-C-AVFoundationQueuePlayer-iOS-AAPLQueuedItemCollectionViewCell.h.md)

