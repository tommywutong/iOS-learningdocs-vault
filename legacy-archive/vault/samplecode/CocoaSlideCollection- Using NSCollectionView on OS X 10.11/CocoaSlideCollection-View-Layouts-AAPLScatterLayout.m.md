---
title: 'CocoaSlideCollection: Using NSCollectionView on OS X 10.11'
apple_id: TP40016149
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/samplecode/CocoaSlideCollection/Listings/CocoaSlideCollection_View_Layouts_AAPLScatterLayout_m.html
archived_at: '2026-07-18T03:03:44.766757Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CocoaSlideCollection: Using NSCollectionView on OS X 10.11](CocoaSlideCollection-%20Using%20NSCollectionView%20on%20OS%20X%2010.11.md)


[Next](CocoaSlideCollection-View-Layouts-AAPLWrappedLayout.m.md)[Previous](CocoaSlideCollection-View-Layouts-AAPLLoopLayout.m.md)

# CocoaSlideCollection/View/Layouts/AAPLScatterLayout.m

```objc
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This is the "ScatterLayout" class implementation.
*/

#import "AAPLScatterLayout.h"

@implementation AAPLScatterLayout

- (instancetype)init {
    self = [super init];
    if (self) {
        cachedItemFrames = [[NSMutableDictionary alloc] init];
    }
    return self;
}

- (NSCollectionViewLayoutAttributes *)layoutAttributesForItemAtIndexPath:(NSIndexPath *)indexPath {
    NSValue *frameValue = [cachedItemFrames objectForKey:indexPath];
    if (frameValue == nil) {
        NSPoint p;
        p.x = box.origin.x + drand48() * (box.size.width - itemSize.width);
        p.y = box.origin.y + drand48() * (box.size.height - itemSize.height);
        frameValue = [NSValue valueWithRect:NSMakeRect(p.x, p.y, itemSize.width, itemSize.height)];
        [cachedItemFrames setObject:frameValue forKey:indexPath];
    }

    NSCollectionViewLayoutAttributes *attributes = [[[self class] layoutAttributesClass] layoutAttributesForItemWithIndexPath:indexPath];
    [attributes setFrame:[frameValue rectValue]];
    [attributes setZIndex:[indexPath item]];
    return attributes;
}

@end
```

[Next](CocoaSlideCollection-View-Layouts-AAPLWrappedLayout.m.md)[Previous](CocoaSlideCollection-View-Layouts-AAPLLoopLayout.m.md)

