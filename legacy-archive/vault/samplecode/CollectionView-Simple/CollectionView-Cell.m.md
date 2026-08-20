---
title: CollectionView-Simple
apple_id: DTS40012860
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2015-10-22'
source_url: https://developer.apple.com/library/archive/samplecode/CollectionView-Simple/Listings/CollectionView_Cell_m.html
archived_at: '2026-07-18T03:03:52.088546Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CollectionView-Simple](CollectionView-Simple.md)


[Next](CollectionView-AppDelegate.h.md)[Previous](CollectionView-DetailViewController.h.md)

# CollectionView/Cell.m

```objc
/*
Copyright (C) 2015 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Custom collection view cell for image and its label.
*/

#import "Cell.h"
#import "CustomCellBackground.h"

@implementation Cell

- (instancetype)initWithCoder:(NSCoder *)aDecoder
{
    self = [super initWithCoder:aDecoder];
    if (self)
    {
        // change to our custom selected background view
        CustomCellBackground *backgroundView = [[CustomCellBackground alloc] initWithFrame:CGRectZero];
        self.selectedBackgroundView = backgroundView;
    }
    return self;
}

@end
```

[Next](CollectionView-AppDelegate.h.md)[Previous](CollectionView-DetailViewController.h.md)

