---
title: TheElements
apple_id: DTS40007419
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: null
published: '2015-08-25'
source_url: https://developer.apple.com/library/archive/samplecode/TheElements/Listings/Classes_ElementsTableViewController_h.html
archived_at: '2026-07-18T03:26:46.257282Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TheElements](TheElements.md)


[Next](Classes-AtomicElementViewController.m.md)[Previous](Classes-AtomicElement.h.md)

# Classes/ElementsTableViewController.h

```objc
/*
Copyright (C) 2015 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Coordinates the tableviews and element data sources. It also responds to changes of selection in the table view and provides the cells.
*/

@import UIKit;
#import "ElementsDataSourceProtocol.h"

@interface ElementsTableViewController : UITableViewController

@property (nonatomic,strong) id<ElementsDataSource, UITableViewDataSource> dataSource;

@end
```

[Next](Classes-AtomicElementViewController.m.md)[Previous](Classes-AtomicElement.h.md)

