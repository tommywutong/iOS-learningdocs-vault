---
title: TheElements
apple_id: DTS40007419
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: null
published: '2015-08-25'
source_url: https://developer.apple.com/library/archive/samplecode/TheElements/Listings/Classes_ElementsSortedByNameDataSource_h.html
archived_at: '2026-07-18T03:26:45.946488Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TheElements](TheElements.md)


[Next](Classes-AtomicElementTableViewCell.h.md)[Previous](Classes-ElementsSortedByStateDataSource.m.md)

# Classes/ElementsSortedByNameDataSource.h

```objc
/*
Copyright (C) 2015 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Provides the table view data for the elements sorted by name.
*/

@import UIKit;

#import "ElementsDataSourceProtocol.h"

@interface ElementsSortedByNameDataSource : NSObject <UITableViewDataSource, ElementsDataSource> {
}

@end
```

[Next](Classes-AtomicElementTableViewCell.h.md)[Previous](Classes-ElementsSortedByStateDataSource.m.md)

