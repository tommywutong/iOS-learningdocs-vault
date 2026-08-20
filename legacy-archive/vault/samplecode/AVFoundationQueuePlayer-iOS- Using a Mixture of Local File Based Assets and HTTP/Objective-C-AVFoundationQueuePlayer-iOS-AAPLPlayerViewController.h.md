---
title: 'AVFoundationQueuePlayer-iOS: Using a Mixture of Local File Based Assets and
  HTTP Live Streaming Assets with AVFoundation'
apple_id: TP40016104
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/AVFoundationQueuePlayer-iOS/Listings/Objective_C_AVFoundationQueuePlayer_iOS_AAPLPlayerViewController_h.html
archived_at: '2026-07-18T03:00:14.453483Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVFoundationQueuePlayer-iOS: Using a Mixture of Local File Based Assets and HTTP Live Streaming Assets with AVFoundation](AVFoundationQueuePlayer-iOS-%20Using%20a%20Mixture%20of%20Local%20File%20Based%20Assets%20and%20HTTP.md)


[Next](Objective-C-AVFoundationQueuePlayer-iOS-AAPLPlayerView.h.md)[Previous](Objective-C-AVFoundationQueuePlayer-iOS-main.m.md)

# Objective-C/AVFoundationQueuePlayer-iOS/AAPLPlayerViewController.h

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

@property (readonly) AVQueuePlayer *player;

/*
    @{
        NSURL(asset URL) : @{
            NSString(title) : NSString,
            NSString(thumbnail) : UIImage
        }
    }
*/
@property NSMutableDictionary *loadedAssets;

@property CMTime currentTime;
@property (readonly) CMTime duration;
@property float rate;

@end
```

[Next](Objective-C-AVFoundationQueuePlayer-iOS-AAPLPlayerView.h.md)[Previous](Objective-C-AVFoundationQueuePlayer-iOS-main.m.md)

