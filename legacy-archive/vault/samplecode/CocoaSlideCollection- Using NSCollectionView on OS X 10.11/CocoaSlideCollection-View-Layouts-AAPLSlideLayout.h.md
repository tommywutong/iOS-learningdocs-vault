---
title: 'CocoaSlideCollection: Using NSCollectionView on OS X 10.11'
apple_id: TP40016149
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/samplecode/CocoaSlideCollection/Listings/CocoaSlideCollection_View_Layouts_AAPLSlideLayout_h.html
archived_at: '2026-07-18T03:03:44.808621Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CocoaSlideCollection: Using NSCollectionView on OS X 10.11](CocoaSlideCollection-%20Using%20NSCollectionView%20on%20OS%20X%2010.11.md)


[Next](CocoaSlideCollection-View-Layouts-AAPLScatterLayout.h.md)[Previous](CocoaSlideCollection-View-Layouts-AAPLCircularLayout.m.md)

# CocoaSlideCollection/View/Layouts/AAPLSlideLayout.h

```objc
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This is the "SlideLayout" class declaration.
*/

#import <Cocoa/Cocoa.h>

#define X_PADDING        10.0
#define Y_PADDING        10.0

// The base class for our custom slide layouts.  It provides a foundation for layouts that show all of a CollectionView's items within the CollectionView's visibleRect (so that no scrolling is required).
@interface AAPLSlideLayout : NSCollectionViewLayout
{
    NSRect box;
    NSSize itemSize;
}
@end
```

[Next](CocoaSlideCollection-View-Layouts-AAPLScatterLayout.h.md)[Previous](CocoaSlideCollection-View-Layouts-AAPLCircularLayout.m.md)

