---
title: 'CocoaSlideCollection: Using NSCollectionView on OS X 10.11'
apple_id: TP40016149
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/samplecode/CocoaSlideCollection/Listings/CocoaSlideCollection_View_Layouts_AAPLScatterLayout_h.html
archived_at: '2026-07-18T03:03:44.734046Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CocoaSlideCollection: Using NSCollectionView on OS X 10.11](CocoaSlideCollection-%20Using%20NSCollectionView%20on%20OS%20X%2010.11.md)


[Next](CocoaSlideCollection-View-Layouts-AAPLWrappedLayout.h.md)[Previous](CocoaSlideCollection-View-Layouts-AAPLSlideLayout.h.md)

# CocoaSlideCollection/View/Layouts/AAPLScatterLayout.h

```objc
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This is the "ScatterLayout" class declaration.
*/

#import "AAPLSlideLayout.h"

// Positions items randomly, within the available area.
@interface AAPLScatterLayout : AAPLSlideLayout
{
    NSMutableDictionary *cachedItemFrames;
}
@end
```

[Next](CocoaSlideCollection-View-Layouts-AAPLWrappedLayout.h.md)[Previous](CocoaSlideCollection-View-Layouts-AAPLSlideLayout.h.md)

