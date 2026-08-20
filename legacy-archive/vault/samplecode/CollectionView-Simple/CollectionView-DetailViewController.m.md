---
title: CollectionView-Simple
apple_id: DTS40012860
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2015-10-22'
source_url: https://developer.apple.com/library/archive/samplecode/CollectionView-Simple/Listings/CollectionView_DetailViewController_m.html
archived_at: '2026-07-18T03:03:52.230602Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CollectionView-Simple](CollectionView-Simple.md)


[Next](CollectionView-CustomCellBackground.m.md)[Previous](CollectionView-Cell.h.md)

# CollectionView/DetailViewController.m

```objc
/*
Copyright (C) 2015 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
The secondary detailed view controller for this app.
*/

#import "DetailViewController.h"


@interface DetailViewController ()

@property (nonatomic, weak) IBOutlet UIImageView *imageView;

@end

@implementation DetailViewController

- (void)viewWillAppear:(BOOL)animated
{
    [super viewWillAppear:animated];
    self.imageView.image = self.image;
}

@end
```

[Next](CollectionView-CustomCellBackground.m.md)[Previous](CollectionView-Cell.h.md)

