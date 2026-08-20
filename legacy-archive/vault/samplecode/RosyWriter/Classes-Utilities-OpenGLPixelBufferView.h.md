---
title: RosyWriter
apple_id: DTS40011110
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/RosyWriter/Listings/Classes_Utilities_OpenGLPixelBufferView_h.html
archived_at: '2026-07-18T03:22:21.708075Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [RosyWriter](RosyWriter.md)


[Next](Classes-Utilities-MovieRecorder.m.md)[Previous](Classes-Utilities-MovieRecorder.h.md)

# Classes/Utilities/OpenGLPixelBufferView.h

```objc

/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The OpenGL ES view
 */

#import <Foundation/Foundation.h>
#import <UIKit/UIKit.h>
#import <CoreVideo/CoreVideo.h>

@interface OpenGLPixelBufferView : UIView

- (void)displayPixelBuffer:(CVPixelBufferRef)pixelBuffer;
- (void)flushPixelBufferCache;
- (void)reset;

@end
```

[Next](Classes-Utilities-MovieRecorder.m.md)[Previous](Classes-Utilities-MovieRecorder.h.md)

