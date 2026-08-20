---
title: Advanced UISearchBar
apple_id: DTS40013493
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2013-07-24'
source_url: https://developer.apple.com/library/archive/samplecode/AdvancedTableSearch/Listings/AdvancedTableSearch_APLAppDelegate_m.html
archived_at: '2026-07-18T03:00:48.789109Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Advanced UISearchBar](Advanced%20UISearchBar.md)


[Next](AdvancedTableSearch-APLProduct.m.md)[Previous](AdvancedTableSearch-APLProduct.h.md)

# AdvancedTableSearch/APLAppDelegate.m

```objc
/*
 Copyright (C) 2013-2014 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The application delegate.
 */

#import "APLAppDelegate.h"
#import "APLViewController.h"
#import "APLProduct.h"

@implementation APLAppDelegate

- (BOOL)application:(UIApplication *)application willFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
    NSArray *productArray = @[[APLProduct productWithType:ProductTypeDevice
                                                    name:@"iPhone"
                                                    year:[NSNumber numberWithInteger:2007]
                                                   price:[NSNumber numberWithDouble:599.00]],
                             [APLProduct productWithType:ProductTypeDevice
                                                    name:@"iPod"
                                                    year:[NSNumber numberWithInteger:2001]
                                                   price:[NSNumber numberWithDouble:399.00]],
                             [APLProduct productWithType:ProductTypeDevice
                                                    name:@"iPod touch"
                                                    year:[NSNumber numberWithInteger:2007]
                                                   price:[NSNumber numberWithDouble:210.00]],
                             [APLProduct productWithType:ProductTypeDevice
                                                    name:@"iPad"
                                                    year:[NSNumber numberWithInteger:2010]
                                                   price:[NSNumber numberWithDouble:499.00]],
                             [APLProduct productWithType:ProductTypeDevice
                                                    name:@"iPad mini"
                                                    year:[NSNumber numberWithInteger:2012]
                                                   price:[NSNumber numberWithDouble:659.00]],
                             [APLProduct productWithType:ProductTypeDesktop
                                                    name:@"iMac"
                                                    year:[NSNumber numberWithInteger:1997]
                                                   price:[NSNumber numberWithDouble:1299.00]],
                             [APLProduct productWithType:ProductTypeDesktop
                                                    name:@"Mac Pro"
                                                    year:[NSNumber numberWithInteger:2006]
                                                   price:[NSNumber numberWithDouble:2499.00]],
                             [APLProduct productWithType:ProductTypePortable
                                                    name:@"MacBook Air"
                                                    year:[NSNumber numberWithInteger:2008]
                                                   price:[NSNumber numberWithDouble:1799.00]],
                             [APLProduct productWithType:ProductTypePortable
                                                    name:@"MacBook Pro"
                                                    year:[NSNumber numberWithInteger:2006]
                                                   price:[NSNumber numberWithDouble:1499.00]]
                              ];

    UINavigationController *navigationController = (UINavigationController *)[self.window rootViewController];
    APLViewController *viewController = [navigationController.viewControllers objectAtIndex:0];
    viewController.products = productArray;

    return YES;
}

// required for state restoration
- (BOOL)application:(UIApplication *)application shouldSaveApplicationState:(NSCoder *)coder
{
    return YES;
}

// required for state restoration
- (BOOL)application:(UIApplication *)application shouldRestoreApplicationState:(NSCoder *)coder
{
    return YES;
}

@end
```

[Next](AdvancedTableSearch-APLProduct.m.md)[Previous](AdvancedTableSearch-APLProduct.h.md)

