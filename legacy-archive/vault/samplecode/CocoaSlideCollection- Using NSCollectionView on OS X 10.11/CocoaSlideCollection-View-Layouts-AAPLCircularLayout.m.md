---
title: 'CocoaSlideCollection: Using NSCollectionView on OS X 10.11'
apple_id: TP40016149
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/samplecode/CocoaSlideCollection/Listings/CocoaSlideCollection_View_Layouts_AAPLCircularLayout_m.html
archived_at: '2026-07-18T03:03:44.608212Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CocoaSlideCollection: Using NSCollectionView on OS X 10.11](CocoaSlideCollection-%20Using%20NSCollectionView%20on%20OS%20X%2010.11.md)


[Next](CocoaSlideCollection-View-Layouts-AAPLSlideLayout.h.md)[Previous](CocoaSlideCollection-View-Layouts-AAPLWrappedLayout.m.md)

# CocoaSlideCollection/View/Layouts/AAPLCircularLayout.m

```objc
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This is the "CircularLayout" class implementation.
*/

#import "AAPLCircularLayout.h"

@implementation AAPLCircularLayout

- (void)prepareLayout {
    [super prepareLayout];

    CGFloat halfItemWidth = 0.5 * itemSize.width;
    CGFloat halfItemHeight = 0.5 * itemSize.height;
    CGFloat radiusInset = sqrt(halfItemWidth * halfItemWidth + halfItemHeight * halfItemHeight);
    circleCenter = NSMakePoint(NSMidX(box), NSMidY(box));
    circleRadius = MIN(box.size.width, box.size.height) * 0.5 - radiusInset;
}

- (NSCollectionViewLayoutAttributes *)layoutAttributesForItemAtIndexPath:(NSIndexPath *)indexPath {
    NSInteger count = [[self collectionView] numberOfItemsInSection:0];
    if (count == 0) {
        return nil;
    }

    NSUInteger itemIndex = [indexPath item];
    CGFloat angleInRadians = ((CGFloat)itemIndex / (CGFloat)count) * (2.0 * M_PI);
    NSPoint subviewCenter;
    subviewCenter.x = circleCenter.x + circleRadius * cos(angleInRadians);
    subviewCenter.y = circleCenter.y + circleRadius * sin(angleInRadians);
    NSRect itemFrame = NSMakeRect(subviewCenter.x - 0.5 * itemSize.width, subviewCenter.y - 0.5 * itemSize.height, itemSize.width, itemSize.height);

    NSCollectionViewLayoutAttributes *attributes = [[[self class] layoutAttributesClass] layoutAttributesForItemWithIndexPath:indexPath];
    [attributes setFrame:NSRectToCGRect(itemFrame)];
    [attributes setZIndex:itemIndex];
    return attributes;
}

@end
```

[Next](CocoaSlideCollection-View-Layouts-AAPLSlideLayout.h.md)[Previous](CocoaSlideCollection-View-Layouts-AAPLWrappedLayout.m.md)

