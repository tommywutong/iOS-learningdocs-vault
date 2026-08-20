---
title: 'CocoaSlideCollection: Using NSCollectionView on OS X 10.11'
apple_id: TP40016149
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/samplecode/CocoaSlideCollection/Listings/CocoaSlideCollection_View_AAPLSlideBorderView_h.html
archived_at: '2026-07-18T03:03:44.035905Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CocoaSlideCollection: Using NSCollectionView on OS X 10.11](CocoaSlideCollection-%20Using%20NSCollectionView%20on%20OS%20X%2010.11.md)


[Next](CocoaSlideCollection-View-AAPLSlide.m.md)[Previous](CocoaSlideCollection-View-AAPLSlideTableBackgroundView.m.md)

# CocoaSlideCollection/View/AAPLSlideBorderView.h

```objc
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This is the "SlideBorderView" class declaration.
*/

#import <Cocoa/Cocoa.h>

// Added as a subview of a AAPLSlideCarrierView, when we want to frame the slide's shape with a stroked outline to indicate selection or highlighting.
@interface AAPLSlideBorderView : NSView
{
    NSColor *borderColor;
}

@property(copy) NSColor *borderColor;

@end
```

[Next](CocoaSlideCollection-View-AAPLSlide.m.md)[Previous](CocoaSlideCollection-View-AAPLSlideTableBackgroundView.m.md)

