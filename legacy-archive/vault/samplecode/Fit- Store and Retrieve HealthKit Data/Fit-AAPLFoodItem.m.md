---
title: 'Fit: Store and Retrieve HealthKit Data'
apple_id: TP40014583
resource_type: Sample Code
platform: iOS
topic: null
technology: HealthKit
published: '2016-10-25'
source_url: https://developer.apple.com/library/archive/samplecode/Fit/Listings/Fit_AAPLFoodItem_m.html
archived_at: '2026-07-18T03:08:45.555100Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Fit: Store and Retrieve HealthKit Data](Fit-%20Store%20and%20Retrieve%20HealthKit%20Data.md)


[Next](Fit-AAPLEnergyViewController.h.md)[Previous](Fit-AAPLAppDelegate.m.md)

# Fit/AAPLFoodItem.m

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A simple model class to represent food and its associated energy.
*/

#import "AAPLFoodItem.h"

@interface AAPLFoodItem ()

@property (nonatomic, readwrite) double joules;
@property (nonatomic, readwrite, copy) NSString *name;

@end

@implementation AAPLFoodItem

+ (instancetype)foodItemWithName:(NSString *)name joules:(double)joules {
    AAPLFoodItem *foodItem = [[self alloc] init];

    foodItem.name = name;
    foodItem.joules = joules;

    return foodItem;
}

- (BOOL)isEqual:(id)object {
    if ([object isKindOfClass:[AAPLFoodItem class]]) {
        return [object joules] == self.joules && [self.name isEqualToString:[object name]];
    }

    return NO;
}

- (NSString *)description {
    return [@{
        @"name": self.name,
        @"joules": @(self.joules)
    } description];
}

@end
```

[Next](Fit-AAPLEnergyViewController.h.md)[Previous](Fit-AAPLAppDelegate.m.md)

