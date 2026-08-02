---
title: 'AVTimedAnnotationWriter: Using Custom Annotation Metadata for Movie Writing
  and Playback'
apple_id: TP40014496
resource_type: Sample Code
platform: iOS
topic: null
technology: AVFoundation
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/AVTimedAnnotationWriter/Listings/AVTimedAnnotationWriter_AAPLPlayerView_m.html
archived_at: '2026-07-18T03:00:31.943464Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVTimedAnnotationWriter: Using Custom Annotation Metadata for Movie Writing and Playback](AVTimedAnnotationWriter-%20Using%20Custom%20Annotation%20Metadata%20for%20Movie%20Writing%20and.md)


[Next](Document%20Revision%20History.md)[Previous](AVTimedAnnotationWriter-AAPLPlayerView.h.md)

# AVTimedAnnotationWriter/AAPLPlayerView.m

```objc
/*
 Copyright (C) 2014 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:

  Player view backed by an AVPlayerLayer.

 */
@import AVFoundation;

#import "AAPLPlayerView.h"

@implementation AAPLPlayerView

+ (Class)layerClass
{
    return [AVPlayerLayer class];
}

- (AVPlayer *)player
{
    return [(AVPlayerLayer *)[self layer] player];
}

- (void)setPlayer:(AVPlayer *)player
{
    [(AVPlayerLayer *)[self layer] setPlayer:player];
}

@end
```

[Next](Document%20Revision%20History.md)[Previous](AVTimedAnnotationWriter-AAPLPlayerView.h.md)

