---
title: 'Fit: Store and Retrieve HealthKit Data'
apple_id: TP40014583
resource_type: Sample Code
platform: iOS
topic: null
technology: HealthKit
published: '2016-10-25'
source_url: https://developer.apple.com/library/archive/samplecode/Fit/Listings/Fit_AAPLProfileViewController_h.html
archived_at: '2026-07-18T03:08:45.872302Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Fit: Store and Retrieve HealthKit Data](Fit-%20Store%20and%20Retrieve%20HealthKit%20Data.md)


[Next](Fit-AAPLFoodItem.h.md)[Previous](Fit-AAPLFoodPickerViewController.h.md)

# Fit/AAPLProfileViewController.h

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Displays age, height, and weight information retrieved from HealthKit.
*/

@import UIKit;
@import HealthKit;

@interface AAPLProfileViewController : UITableViewController

@property (nonatomic) HKHealthStore *healthStore;

@end
```

[Next](Fit-AAPLFoodItem.h.md)[Previous](Fit-AAPLFoodPickerViewController.h.md)

