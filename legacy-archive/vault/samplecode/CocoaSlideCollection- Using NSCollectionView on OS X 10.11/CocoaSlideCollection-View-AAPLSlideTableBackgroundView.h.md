---
title: 'CocoaSlideCollection: Using NSCollectionView on OS X 10.11'
apple_id: TP40016149
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/samplecode/CocoaSlideCollection/Listings/CocoaSlideCollection_View_AAPLSlideTableBackgroundView_h.html
archived_at: '2026-07-18T03:03:44.330670Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CocoaSlideCollection: Using NSCollectionView on OS X 10.11](CocoaSlideCollection-%20Using%20NSCollectionView%20on%20OS%20X%2010.11.md)


[Next](CocoaSlideCollection-View-AAPLSlideCarrierView.m.md)[Previous](CocoaSlideCollection-View-AAPLSlide.m.md)

# CocoaSlideCollection/View/AAPLSlideTableBackgroundView.h

```objc
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This is the "SlideTableBackgroundView" class declaration.
*/

#import <Cocoa/Cocoa.h>

// A simple background view for our NSCollectionView, that draws a subtle radial gradient using NSGradient, or an NSImage scaled to cover the entire background.
@interface AAPLSlideTableBackgroundView : NSView
{
    NSGradient *gradient;
    NSImage *image;
}
@property(strong) NSImage *image;
@end
```

[Next](CocoaSlideCollection-View-AAPLSlideCarrierView.m.md)[Previous](CocoaSlideCollection-View-AAPLSlide.m.md)

