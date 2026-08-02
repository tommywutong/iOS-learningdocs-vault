---
title: 'CocoaSlideCollection: Using NSCollectionView on OS X 10.11'
apple_id: TP40016149
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/samplecode/CocoaSlideCollection/Listings/CocoaSlideCollection_View_Layouts_AAPLWrappedLayout_m.html
archived_at: '2026-07-18T03:03:44.918162Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CocoaSlideCollection: Using NSCollectionView on OS X 10.11](CocoaSlideCollection-%20Using%20NSCollectionView%20on%20OS%20X%2010.11.md)


[Next](CocoaSlideCollection-View-Layouts-AAPLCircularLayout.m.md)[Previous](CocoaSlideCollection-View-Layouts-AAPLScatterLayout.m.md)

# CocoaSlideCollection/View/Layouts/AAPLWrappedLayout.m

```objc
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This is the "WrappedLayout" class implementation.
*/

#import "AAPLWrappedLayout.h"
#import "AAPLSlideLayout.h"         // for X_PADDING, Y_PADDING
#import "AAPLSlideCarrierView.h"    // for SLIDE_WIDTH, SLIDE_HEGIHT

@implementation AAPLWrappedLayout

- (instancetype)init {
    self = [super init];
    if (self) {
        [self setItemSize:NSMakeSize(SLIDE_WIDTH, SLIDE_HEIGHT)];
        [self setMinimumInteritemSpacing:X_PADDING];
        [self setMinimumLineSpacing:Y_PADDING];
        [self setSectionInset:NSEdgeInsetsMake(Y_PADDING, X_PADDING, Y_PADDING, X_PADDING)];
    }
    return self;
}

- (NSCollectionViewLayoutAttributes *)layoutAttributesForItemAtIndexPath:(NSIndexPath *)indexPath {
    NSCollectionViewLayoutAttributes *attributes = [super layoutAttributesForItemAtIndexPath:indexPath];
    [attributes setZIndex:[indexPath item]];
    return attributes;
}

- (NSArray *)layoutAttributesForElementsInRect:(NSRect)rect {
    NSArray *layoutAttributesArray = [super layoutAttributesForElementsInRect:rect];
    for (NSCollectionViewLayoutAttributes *attributes in layoutAttributesArray) {
        [attributes setZIndex:[[attributes indexPath] item]];
    }
    return layoutAttributesArray;
}

@end
```

[Next](CocoaSlideCollection-View-Layouts-AAPLCircularLayout.m.md)[Previous](CocoaSlideCollection-View-Layouts-AAPLScatterLayout.m.md)

