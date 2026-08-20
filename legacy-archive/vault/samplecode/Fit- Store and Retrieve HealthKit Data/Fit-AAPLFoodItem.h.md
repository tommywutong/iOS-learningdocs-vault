---
title: 'Fit: Store and Retrieve HealthKit Data'
apple_id: TP40014583
resource_type: Sample Code
platform: iOS
topic: null
technology: HealthKit
published: '2016-10-25'
source_url: https://developer.apple.com/library/archive/samplecode/Fit/Listings/Fit_AAPLFoodItem_h.html
archived_at: '2026-07-18T03:08:45.511738Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Fit: Store and Retrieve HealthKit Data](Fit-%20Store%20and%20Retrieve%20HealthKit%20Data.md)


[Next](Fit-AAPLJournalViewController.m.md)[Previous](Fit-AAPLProfileViewController.h.md)

# Fit/AAPLFoodItem.h

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A simple model class to represent food and its associated energy.
*/

@import Foundation;
@import HealthKit;

@interface AAPLFoodItem : NSObject

// Creates a new food item.
+ (instancetype)foodItemWithName:(NSString *)name joules:(double)joules;

// \c AAPLFoodItem properties are immutable.
@property (nonatomic, readonly, copy) NSString *name;
@property (nonatomic, readonly) double joules;

@end
```

[Next](Fit-AAPLJournalViewController.m.md)[Previous](Fit-AAPLProfileViewController.h.md)

