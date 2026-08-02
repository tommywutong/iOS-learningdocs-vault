---
title: 'CocoaSlideCollection: Using NSCollectionView on OS X 10.11'
apple_id: TP40016149
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/samplecode/CocoaSlideCollection/Listings/CocoaSlideCollection_View_AAPLSlideImageView_m.html
archived_at: '2026-07-18T03:03:44.283950Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CocoaSlideCollection: Using NSCollectionView on OS X 10.11](CocoaSlideCollection-%20Using%20NSCollectionView%20on%20OS%20X%2010.11.md)


[Next](CocoaSlideCollection-View-AAPLFooterView.m.md)[Previous](CocoaSlideCollection-View-AAPLSlideCarrierView.h.md)

# CocoaSlideCollection/View/AAPLSlideImageView.m

```objc
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This is the "SlideCarrierView" class implementation.
*/

#import "AAPLSlideImageView.h"

@implementation AAPLSlideImageView

// Fill in semitransparent gray bands in any areas that the image doesn't cover, to give a more slide-like appearance.
- (void)drawRect:(NSRect)rect {
    NSImage *image = [self image];
    if (image != nil && [self imageScaling] == NSImageScaleProportionallyUpOrDown) {
        NSSize imageSize = [image size];
        NSSize viewSize = [self bounds].size;
        if (imageSize.height > 0.0 && viewSize.height > 0.0) {
            CGFloat imageAspectRatio = imageSize.width / imageSize.height;
            CGFloat viewAspectRatio = viewSize.width / viewSize.height;
            [[NSColor colorWithCalibratedWhite:0.0 alpha:0.2] set];
            if (imageAspectRatio > viewAspectRatio) {
                // Fill in bands at top and bottom.
                CGFloat thumbnailHeight = viewSize.width / imageAspectRatio;
                CGFloat bandHeight = 0.5 * (viewSize.height - thumbnailHeight);
                NSRectFillUsingOperation(NSMakeRect(0, 0, viewSize.width, bandHeight), NSCompositeSourceOver);
                NSRectFillUsingOperation(NSMakeRect(0, viewSize.height - bandHeight, viewSize.width, bandHeight), NSCompositeSourceOver);
            } else if (imageAspectRatio < viewAspectRatio) {
                // Fill in bands at left and right.
                CGFloat thumbnailWidth = viewSize.height * imageAspectRatio;
                CGFloat bandWidth = 0.5 * (viewSize.width - thumbnailWidth);
                NSRectFillUsingOperation(NSMakeRect(0, 0, bandWidth, viewSize.height), NSCompositeSourceOver);
                NSRectFillUsingOperation(NSMakeRect(viewSize.width - bandWidth, 0, bandWidth, viewSize.height), NSCompositeSourceOver);
            }
        }
    }

    // Now let NSImageView do its drawing.
    [super drawRect:rect];
}

@end
```

[Next](CocoaSlideCollection-View-AAPLFooterView.m.md)[Previous](CocoaSlideCollection-View-AAPLSlideCarrierView.h.md)

