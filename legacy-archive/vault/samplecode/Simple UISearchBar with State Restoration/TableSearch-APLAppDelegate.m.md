---
title: Simple UISearchBar with State Restoration
apple_id: DTS40007848
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2013-05-23'
source_url: https://developer.apple.com/library/archive/samplecode/TableSearch/Listings/TableSearch_APLAppDelegate_m.html
archived_at: '2026-07-18T03:26:12.271591Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Simple UISearchBar with State Restoration](Simple%20UISearchBar%20with%20State%20Restoration.md)


[Next](TableSearch-APLProduct.m.md)[Previous](TableSearch-APLProduct.h.md)

# TableSearch/APLAppDelegate.m

```objc

/*
 Copyright (C) 2013-2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The application delegate.
 */

#import "APLAppDelegate.h"

#import "APLViewController.h"
#import "APLProduct.h"

@implementation APLAppDelegate;

-(BOOL)application:(UIApplication *)application willFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
    NSArray *productArray = @[[APLProduct productWithType:ProductTypeDevice name:@"iPhone"],
                         [APLProduct productWithType:ProductTypeDevice name:@"iPod"],
                         [APLProduct productWithType:ProductTypeDevice name:@"iPod touch"],
                         [APLProduct productWithType:ProductTypeDevice name:@"iPad"],
                         [APLProduct productWithType:ProductTypeDevice name:@"iPad mini"],
                         [APLProduct productWithType:ProductTypeDesktop name:@"iMac"],
                         [APLProduct productWithType:ProductTypeDesktop name:@"Mac Pro"],
                         [APLProduct productWithType:ProductTypePortable name:@"MacBook Air"],
                         [APLProduct productWithType:ProductTypePortable name:@"MacBook Pro"]];

    UINavigationController *navigationController = (UINavigationController *)[self.window rootViewController];
    APLViewController *viewController = [navigationController.viewControllers objectAtIndex:0];
    viewController.products = productArray;

    return YES;
}



-(BOOL)application:(UIApplication *)application shouldSaveApplicationState:(NSCoder *)coder
{
    return YES;
}

-(BOOL)application:(UIApplication *)application shouldRestoreApplicationState:(NSCoder *)coder
{
    return YES;
}


@end
```

[Next](TableSearch-APLProduct.m.md)[Previous](TableSearch-APLProduct.h.md)

