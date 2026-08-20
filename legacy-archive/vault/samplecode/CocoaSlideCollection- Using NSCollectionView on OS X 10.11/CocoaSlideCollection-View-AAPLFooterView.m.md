---
title: 'CocoaSlideCollection: Using NSCollectionView on OS X 10.11'
apple_id: TP40016149
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/samplecode/CocoaSlideCollection/Listings/CocoaSlideCollection_View_AAPLFooterView_m.html
archived_at: '2026-07-18T03:03:43.905196Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CocoaSlideCollection: Using NSCollectionView on OS X 10.11](CocoaSlideCollection-%20Using%20NSCollectionView%20on%20OS%20X%2010.11.md)


[Next](CocoaSlideCollection-View-AAPLSlideBorderView.m.md)[Previous](CocoaSlideCollection-View-AAPLSlideImageView.m.md)

# CocoaSlideCollection/View/AAPLFooterView.m

```objc
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This is the "SlideCarrierView" class implementation.
*/

#import "AAPLFooterView.h"

@implementation AAPLFooterView

- (void)drawRect:(NSRect)dirtyRect {
    [[NSColor colorWithCalibratedWhite:0.85 alpha:0.8] set];
    NSRectFillUsingOperation(dirtyRect, NSCompositeSourceOver);
}

@end
```

[Next](CocoaSlideCollection-View-AAPLSlideBorderView.m.md)[Previous](CocoaSlideCollection-View-AAPLSlideImageView.m.md)

