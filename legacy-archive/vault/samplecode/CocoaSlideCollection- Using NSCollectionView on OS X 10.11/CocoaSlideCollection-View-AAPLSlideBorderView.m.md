---
title: 'CocoaSlideCollection: Using NSCollectionView on OS X 10.11'
apple_id: TP40016149
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/samplecode/CocoaSlideCollection/Listings/CocoaSlideCollection_View_AAPLSlideBorderView_m.html
archived_at: '2026-07-18T03:03:44.072009Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CocoaSlideCollection: Using NSCollectionView on OS X 10.11](CocoaSlideCollection-%20Using%20NSCollectionView%20on%20OS%20X%2010.11.md)


[Next](CocoaSlideCollection-View-AAPLSlideImageView.h.md)[Previous](CocoaSlideCollection-View-AAPLFooterView.m.md)

# CocoaSlideCollection/View/AAPLSlideBorderView.m

```objc
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This is the "SlideBorderView" class implementation.
*/

#import "AAPLSlideBorderView.h"
#import "AAPLSlideCarrierView.h"

@implementation AAPLSlideBorderView

#pragma mark Property Accessors

- (NSColor *)borderColor {
    return borderColor;
}

- (void)setBorderColor:(NSColor *)newBorderColor {
    if (borderColor != newBorderColor) {
        borderColor = [newBorderColor copy];
        [self setNeedsDisplay:YES];
    }
}

#pragma mark Visual State

// A AAPLSlideCarrierView wants to receive -updateLayer so it can set its backing layer's contents property, instead of being sent -drawRect: to draw its content procedurally.
- (BOOL)wantsUpdateLayer {
    return YES;
}

- (void)updateLayer {
    CALayer *layer = self.layer;
    layer.borderColor = borderColor.CGColor;
    layer.borderWidth = (borderColor ? SLIDE_BORDER_WIDTH : 0.0);
    layer.cornerRadius = SLIDE_CORNER_RADIUS;
}

@end
```

[Next](CocoaSlideCollection-View-AAPLSlideImageView.h.md)[Previous](CocoaSlideCollection-View-AAPLFooterView.m.md)

