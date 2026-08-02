---
title: TheElements
apple_id: DTS40007419
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: null
published: '2015-08-25'
source_url: https://developer.apple.com/library/archive/samplecode/TheElements/Listings/Classes_AtomicElementViewController_h.html
archived_at: '2026-07-18T03:26:45.459736Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TheElements](TheElements.md)


[Next](Classes-AtomicElementView.m.md)[Previous](Classes-ElementsTableViewController.m.md)

# Classes/AtomicElementViewController.h

```objc
/*
Copyright (C) 2015 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Controller that manages the full tile view of the atomic information, creating the reflection, and the flipping of the tile.
*/

@import UIKit;

@class AtomicElement;

@interface AtomicElementViewController : UIViewController

@property (nonatomic,strong) AtomicElement *element;

- (void)flipCurrentView;

@end
```

[Next](Classes-AtomicElementView.m.md)[Previous](Classes-ElementsTableViewController.m.md)

