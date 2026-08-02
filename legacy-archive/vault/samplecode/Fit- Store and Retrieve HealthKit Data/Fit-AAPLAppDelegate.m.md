---
title: 'Fit: Store and Retrieve HealthKit Data'
apple_id: TP40014583
resource_type: Sample Code
platform: iOS
topic: null
technology: HealthKit
published: '2016-10-25'
source_url: https://developer.apple.com/library/archive/samplecode/Fit/Listings/Fit_AAPLAppDelegate_m.html
archived_at: '2026-07-18T03:08:45.323467Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Fit: Store and Retrieve HealthKit Data](Fit-%20Store%20and%20Retrieve%20HealthKit%20Data.md)


[Next](Fit-AAPLFoodItem.m.md)[Previous](Fit-AAPLEnergyViewController.m.md)

# Fit/AAPLAppDelegate.m

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    The main application delegate.
*/

#import "AAPLAppDelegate.h"
#import "AAPLProfileViewController.h"
#import "AAPLJournalViewController.h"
#import "AAPLEnergyViewController.h"
@import HealthKit;

@interface AAPLAppDelegate()

@property (nonatomic) HKHealthStore *healthStore;

@end


@implementation AAPLAppDelegate

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    self.healthStore = [[HKHealthStore alloc] init];

    [self setUpHealthStoreForTabBarControllers];

    return YES;
}

#pragma mark - Convenience

// Set the healthStore property on each view controller that will be presented to the user. The root view controller is a tab
// bar controller. Each tab of the root view controller is a navigation controller which contains its root view controller—
// these are the subclasses of the view controller that present HealthKit information to the user.
- (void)setUpHealthStoreForTabBarControllers {
    UITabBarController *tabBarController = (UITabBarController *)[self.window rootViewController];

    for (UINavigationController *navigationController in tabBarController.viewControllers) {
        id viewController = navigationController.topViewController;

        if ([viewController respondsToSelector:@selector(setHealthStore:)]) {
            [viewController setHealthStore:self.healthStore];
        }
    }
}

@end
```

[Next](Fit-AAPLFoodItem.m.md)[Previous](Fit-AAPLEnergyViewController.m.md)

