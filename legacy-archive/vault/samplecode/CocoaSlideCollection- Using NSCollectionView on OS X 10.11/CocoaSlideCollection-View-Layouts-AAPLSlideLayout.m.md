---
title: 'CocoaSlideCollection: Using NSCollectionView on OS X 10.11'
apple_id: TP40016149
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/samplecode/CocoaSlideCollection/Listings/CocoaSlideCollection_View_Layouts_AAPLSlideLayout_m.html
archived_at: '2026-07-18T03:03:44.845222Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CocoaSlideCollection: Using NSCollectionView on OS X 10.11](CocoaSlideCollection-%20Using%20NSCollectionView%20on%20OS%20X%2010.11.md)


[Next](CocoaSlideCollection-View-Layouts-AAPLLoopLayout.m.md)[Previous](CocoaSlideCollection-View-Layouts-AAPLLoopLayout.h.md)

# CocoaSlideCollection/View/Layouts/AAPLSlideLayout.m

```objc
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This is the "SlideLayout" class implementation.
*/

#import "AAPLSlideLayout.h"
#import "AAPLSlideCarrierView.h"    // for SLIDE_WIDTH, SLIDE_HEGIHT

@implementation AAPLSlideLayout

- (instancetype)init {
    self = [super init];
    if (self) {
        itemSize = NSMakeSize(SLIDE_WIDTH, SLIDE_HEIGHT);
    }
    return self;
}

- (NSSize)collectionViewContentSize {
    NSRect clipBounds = [[[self collectionView] superview] bounds];
    return clipBounds.size; // Lay our slides out within the available area.
}

- (BOOL)shouldInvalidateLayoutForBoundsChange:(NSRect)newBounds {
    return YES; // Our custom SlideLayouts show all items within the CollectionView's visible rect, and must recompute their layouts for a good fit when that rect changes.
}

- (void)prepareLayout {
    [super prepareLayout];

    // Inset by (X_PADDING,Y_PADDING) to precompute the box we need to fix the slides in.
    CGSize collectionViewContentSize = [self collectionViewContentSize];
    box = NSInsetRect(NSMakeRect(0, 0, collectionViewContentSize.width, collectionViewContentSize.height), X_PADDING, Y_PADDING);
}

// A layout derived from this base class always displays all items, within the visible rectangle.  So we can implement -layoutAttributesForElementsInRect: quite simply, by enumerating all item index paths and obtaining the -layoutAttributesForItemAtIndexPath: for each.  Our subclasses then just have to implement -layoutAttributesForItemAtIndexPath:.
- (NSArray *)layoutAttributesForElementsInRect:(NSRect)rect {
    NSInteger itemCount = [[self collectionView] numberOfItemsInSection:0];
    NSMutableArray *layoutAttributesArray = [NSMutableArray arrayWithCapacity:itemCount];
    for (NSInteger index = 0; index < itemCount; index++) {
        NSIndexPath *indexPath = [NSIndexPath indexPathForItem:index inSection:0];
        NSCollectionViewLayoutAttributes *layoutAttributes = [self layoutAttributesForItemAtIndexPath:indexPath];
        if (layoutAttributes) {
            [layoutAttributesArray addObject:layoutAttributes];
        }
    }
    return layoutAttributesArray;
}

@end
```

[Next](CocoaSlideCollection-View-Layouts-AAPLLoopLayout.m.md)[Previous](CocoaSlideCollection-View-Layouts-AAPLLoopLayout.h.md)

