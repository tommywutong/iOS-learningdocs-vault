---
title: TheElements
apple_id: DTS40007419
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: null
published: '2015-08-25'
source_url: https://developer.apple.com/library/archive/samplecode/TheElements/Listings/Classes_AtomicElementTableViewCell_h.html
archived_at: '2026-07-18T03:26:45.309323Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TheElements](TheElements.md)


[Next](Classes-AtomicElement.m.md)[Previous](Classes-ElementsSortedByNameDataSource.h.md)

# Classes/AtomicElementTableViewCell.h

```objc
/*
Copyright (C) 2015 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Draws the tableview cell and lays out the subviews.
*/

@import UIKit;

@class AtomicElement;

@interface AtomicElementTableViewCell : UITableViewCell

@property (nonatomic,strong) AtomicElement *element;

@end
```

[Next](Classes-AtomicElement.m.md)[Previous](Classes-ElementsSortedByNameDataSource.h.md)

