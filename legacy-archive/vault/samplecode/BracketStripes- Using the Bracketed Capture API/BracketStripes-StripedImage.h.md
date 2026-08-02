---
title: 'BracketStripes: Using the Bracketed Capture API'
apple_id: TP40014579
resource_type: Sample Code
platform: iOS
topic: null
technology: AVFoundation
published: '2016-09-28'
source_url: https://developer.apple.com/library/archive/samplecode/BracketStripes/Listings/BracketStripes_StripedImage_h.html
archived_at: '2026-07-18T03:02:17.300614Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [BracketStripes: Using the Bracketed Capture API](BracketStripes-%20Using%20the%20Bracketed%20Capture%20API.md)


[Next](README.md.md)[Previous](BracketStripes-BracketStripesZoomImageView.m.md)

# BracketStripes/StripedImage.h

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Implements a composite image constructed of CMSampleBuffer stripes.
 */

@import CoreMedia;

@interface StripedImage : NSObject

// Designated initializer
- (instancetype)initForSize:(CGSize)size stripWidth:(CGFloat)stripWidth stride:(NSUInteger)stride;

// Add an image to the strip
// sampleBuffer must be a JPEG or BGRA image
- (void)addSampleBuffer:(CMSampleBufferRef)sampleBuffer;

// The final rendered strip
- (UIImage *)imageWithOrientation:(UIImageOrientation)orientation;

@end
```

[Next](README.md.md)[Previous](BracketStripes-BracketStripesZoomImageView.m.md)

