---
title: StitchedStreamPlayer
apple_id: DTS40010092
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2016-07-14'
source_url: https://developer.apple.com/library/archive/samplecode/StitchedStreamPlayer/Listings/Classes_MyPlayerLayerView_h.html
archived_at: '2026-07-18T03:25:45.621402Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [StitchedStreamPlayer](StitchedStreamPlayer.md)


[Next](Classes-MyPlayerLayerView.m.md)[Previous](Classes-MyStreamingMovieViewController.h.md)

# Classes/MyPlayerLayerView.h

```objc
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Abstract: A UIView subclass that contains an AVPlayerLayer.
*/

@import UIKit;

@class AVPlayerLayer;

@interface MyPlayerLayerView : UIView {

}

@property (nonatomic, readonly) AVPlayerLayer *playerLayer;

- (void)setVideoFillMode:(NSString *)fillMode;

@end
```

[Next](Classes-MyPlayerLayerView.m.md)[Previous](Classes-MyStreamingMovieViewController.h.md)

