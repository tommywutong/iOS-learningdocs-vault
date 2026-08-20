---
title: StitchedStreamPlayer
apple_id: DTS40010092
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2016-07-14'
source_url: https://developer.apple.com/library/archive/samplecode/StitchedStreamPlayer/Listings/Classes_MyPlayerLayerView_m.html
archived_at: '2026-07-18T03:25:45.662173Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [StitchedStreamPlayer](StitchedStreamPlayer.md)


[Next](Classes-MoviePlayerAppDelegate.m.md)[Previous](Classes-MyPlayerLayerView.h.md)

# Classes/MyPlayerLayerView.m

```objc
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Abstract: A UIView subclass that contains an AVPlayerLayer.
*/

#import "MyPlayerLayerView.h"

@import AVFoundation;

/* ---------------------------------------------------------
**  To play the visual component of an asset, you need a view 
**  containing an AVPlayerLayer layer to which the output of an 
**  AVPlayer object can be directed. You can create a simple 
**  subclass of UIView to accommodate this. Use the view’s Core 
**  Animation layer (see the 'layer' property) for rendering.  
**  This class is a subclass of UIView that is used for this 
**  purpose.
** ------------------------------------------------------- */

@implementation MyPlayerLayerView


+ (Class)layerClass
{
    return [AVPlayerLayer class];
}

- (AVPlayerLayer *)playerLayer
{
    return (AVPlayerLayer *)self.layer;
}

- (void)setPlayer:(AVPlayer*)player
{
    [(AVPlayerLayer*)[self layer] setPlayer:player];
}

/* Specifies how the video is displayed within a player layer’s bounds. 
 (AVLayerVideoGravityResizeAspect is default) */
- (void)setVideoFillMode:(NSString *)fillMode
{
    AVPlayerLayer *playerLayer = (AVPlayerLayer*)[self layer];
    playerLayer.videoGravity = fillMode;
}


@end
```

[Next](Classes-MoviePlayerAppDelegate.m.md)[Previous](Classes-MyPlayerLayerView.h.md)

