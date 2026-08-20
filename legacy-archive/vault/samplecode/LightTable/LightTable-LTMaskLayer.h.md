---
title: LightTable
apple_id: DTS40008927
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: AppKit
published: '2017-08-17'
source_url: https://developer.apple.com/library/archive/samplecode/LightTable/Listings/LightTable_LTMaskLayer_h.html
archived_at: '2026-07-18T03:13:31.040934Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [LightTable](LightTable.md)


[Next](LightTable-LTViewController.m.md)[Previous](LightTable-ClickTracker.h.md)

# LightTable/LTMaskLayer.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
  See LICENSE.txt for this sample’s licensing information

  Abstract:
  The LTMaskLayer is a CALayer that is used by  LTView to draw a single slide in the LTView. It acts as the frame and masking layer for its one child layer that is the image for the slide. 
*/

@import Cocoa;
@import QuartzCore;

@interface LTMaskLayer : CALayer

// The source object who's properties we display.
@property(strong, nonatomic) id source;

// The image to draw.
@property(strong, nonatomic) id photo;

// The sublayer the actually contains the image.
@property(strong, nonatomic, readonly) CALayer* photoLayer;

// The frame and position of the photoLayer in the same coordinate space as this layer's frame. These are just convience methods so we only have to do the conversion in one place.
@property (assign, nonatomic) CGRect photoFrame;
@property (assign, nonatomic) CGPoint photoPosition;

@end
```

[Next](LightTable-LTViewController.m.md)[Previous](LightTable-ClickTracker.h.md)

