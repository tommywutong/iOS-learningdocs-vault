---
title: 'AVTimedAnnotationWriter: Using Custom Annotation Metadata for Movie Writing
  and Playback'
apple_id: TP40014496
resource_type: Sample Code
platform: iOS
topic: null
technology: AVFoundation
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/AVTimedAnnotationWriter/Listings/AVTimedAnnotationWriter_AAPLPlayerViewController_h.html
archived_at: '2026-07-18T03:00:31.742044Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVTimedAnnotationWriter: Using Custom Annotation Metadata for Movie Writing and Playback](AVTimedAnnotationWriter-%20Using%20Custom%20Annotation%20Metadata%20for%20Movie%20Writing%20and.md)


[Next](AVTimedAnnotationWriter-AAPLAppDelegate.m.md)[Previous](AVTimedAnnotationWriter-main.m.md)

# AVTimedAnnotationWriter/AAPLPlayerViewController.h

```objc
/*
 Copyright (C) 2014 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:

  Player view controller which sets up playback of movie file with metadata and uses AVPlayerItemMetadataOutput to render circle and text annotation during playback.

 */

@import UIKit;
@import AVKit;

@interface AAPLPlayerViewController : AVPlayerViewController

- (void)setupPlaybackWithURL:(NSURL *)movieURL;

@end
```

[Next](AVTimedAnnotationWriter-AAPLAppDelegate.m.md)[Previous](AVTimedAnnotationWriter-main.m.md)

