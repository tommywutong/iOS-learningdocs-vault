---
title: 'Fit: Store and Retrieve HealthKit Data'
apple_id: TP40014583
resource_type: Sample Code
platform: iOS
topic: null
technology: HealthKit
published: '2016-10-25'
source_url: https://developer.apple.com/library/archive/samplecode/Fit/Listings/Fit_AAPLJournalViewController_h.html
archived_at: '2026-07-18T03:08:45.713867Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Fit: Store and Retrieve HealthKit Data](Fit-%20Store%20and%20Retrieve%20HealthKit%20Data.md)


[Next](Fit-AAPLProfileViewController.m.md)[Previous](Fit-HKHealthStore%2BAAPLExtensions.m.md)

# Fit/AAPLJournalViewController.h

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Displays information retrieved from HealthKit about the food items consumed today.
*/

@import UIKit;
@import HealthKit;

@interface AAPLJournalViewController : UITableViewController

@property (nonatomic) HKHealthStore *healthStore;

@end
```

[Next](Fit-AAPLProfileViewController.m.md)[Previous](Fit-HKHealthStore%2BAAPLExtensions.m.md)

