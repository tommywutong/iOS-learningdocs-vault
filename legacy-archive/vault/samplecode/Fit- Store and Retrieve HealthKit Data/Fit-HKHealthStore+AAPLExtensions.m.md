---
title: 'Fit: Store and Retrieve HealthKit Data'
apple_id: TP40014583
resource_type: Sample Code
platform: iOS
topic: null
technology: HealthKit
published: '2016-10-25'
source_url: https://developer.apple.com/library/archive/samplecode/Fit/Listings/Fit_HKHealthStore_AAPLExtensions_m.html
archived_at: '2026-07-18T03:08:46.078725Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Fit: Store and Retrieve HealthKit Data](Fit-%20Store%20and%20Retrieve%20HealthKit%20Data.md)


[Next](Fit-AAPLJournalViewController.h.md)[Previous](LICENSE.txt.md)

# Fit/HKHealthStore+AAPLExtensions.m

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Contains shared helper methods on HKHealthStore that are specific to Fit's use cases.
*/

#import "HKHealthStore+AAPLExtensions.h"

@implementation HKHealthStore (AAPLExtensions)

- (void)aapl_mostRecentQuantitySampleOfType:(HKQuantityType *)quantityType predicate:(NSPredicate *)predicate completion:(void (^)(HKQuantity *, NSError *))completion {
    NSSortDescriptor *timeSortDescriptor = [[NSSortDescriptor alloc] initWithKey:HKSampleSortIdentifierEndDate ascending:NO];

    // Since we are interested in retrieving the user's latest sample, we sort the samples in descending order, and set the limit to 1. We are not filtering the data, and so the predicate is set to nil.
    HKSampleQuery *query = [[HKSampleQuery alloc] initWithSampleType:quantityType predicate:nil limit:1 sortDescriptors:@[timeSortDescriptor] resultsHandler:^(HKSampleQuery *query, NSArray *results, NSError *error) {
        if (!results) {
            if (completion) {
                completion(nil, error);
            }

            return;
        }

        if (completion) {
            // If quantity isn't in the database, return nil in the completion block.
            HKQuantitySample *quantitySample = results.firstObject;
            HKQuantity *quantity = quantitySample.quantity;

            completion(quantity, error);
        }
    }];

    [self executeQuery:query];
}

@end
```

[Next](Fit-AAPLJournalViewController.h.md)[Previous](LICENSE.txt.md)

