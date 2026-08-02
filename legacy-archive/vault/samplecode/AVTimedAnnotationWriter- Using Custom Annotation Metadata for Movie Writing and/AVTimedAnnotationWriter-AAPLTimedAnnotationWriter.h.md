---
title: 'AVTimedAnnotationWriter: Using Custom Annotation Metadata for Movie Writing
  and Playback'
apple_id: TP40014496
resource_type: Sample Code
platform: iOS
topic: null
technology: AVFoundation
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/AVTimedAnnotationWriter/Listings/AVTimedAnnotationWriter_AAPLTimedAnnotationWriter_h.html
archived_at: '2026-07-18T03:00:31.996355Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVTimedAnnotationWriter: Using Custom Annotation Metadata for Movie Writing and Playback](AVTimedAnnotationWriter-%20Using%20Custom%20Annotation%20Metadata%20for%20Movie%20Writing%20and.md)


[Next](AVTimedAnnotationWriter-AAPLAppDelegate.h.md)[Previous](AVTimedAnnotationWriter-AAPLViewController.h.md)

# AVTimedAnnotationWriter/AAPLTimedAnnotationWriter.h

```objc
/*
 Copyright (C) 2014 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:

  Annotation writer class which writes a given set of timed metadata groups into a movie file.

 */

@import Foundation;
@import AVFoundation;

NSString *const AAPLTimedAnnotationWriterCircleCenterCoordinateIdentifier;
NSString *const AAPLTimedAnnotationWriterCircleRadiusIdentifier;
NSString *const AAPLTimedAnnotationWriterCommentFieldIdentifier;

@interface AAPLTimedAnnotationWriter : NSObject

- (instancetype)initWithAsset:(AVAsset *)asset;
- (void)writeMetadataGroups:(NSArray *)metadataGroups;

@property (readonly) NSURL *outputURL;

@end
```

[Next](AVTimedAnnotationWriter-AAPLAppDelegate.h.md)[Previous](AVTimedAnnotationWriter-AAPLViewController.h.md)

