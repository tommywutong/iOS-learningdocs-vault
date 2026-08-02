---
title: CollectionView-Simple
apple_id: DTS40012860
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2015-10-22'
source_url: https://developer.apple.com/library/archive/samplecode/CollectionView-Simple/Listings/CollectionView_Cell_h.html
archived_at: '2026-07-18T03:03:52.063417Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CollectionView-Simple](CollectionView-Simple.md)


[Next](CollectionView-DetailViewController.m.md)[Previous](CollectionView-AppDelegate.h.md)

# CollectionView/Cell.h

```objc
/*
Copyright (C) 2015 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Custom collection view cell for image and its label.
*/

@import UIKit;

@interface Cell : UICollectionViewCell

@property (strong, nonatomic) IBOutlet UIImageView *image;
@property (strong, nonatomic) IBOutlet UILabel *label;

@end
```

[Next](CollectionView-DetailViewController.m.md)[Previous](CollectionView-AppDelegate.h.md)

