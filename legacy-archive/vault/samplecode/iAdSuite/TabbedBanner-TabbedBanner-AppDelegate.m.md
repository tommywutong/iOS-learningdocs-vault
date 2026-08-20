---
title: iAdSuite
apple_id: DTS40010198
resource_type: Sample Code
platform: iOS
topic: null
technology: iAd
published: '2013-05-28'
source_url: https://developer.apple.com/library/archive/samplecode/iAdSuite/Listings/TabbedBanner_TabbedBanner_AppDelegate_m.html
archived_at: '2026-07-18T03:29:31.276426Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [iAdSuite](iAdSuite.md)


[Next](TabbedBanner-TabbedBanner-BannerViewController.m.md)[Previous](BasicBanner-BasicBanner-main.m.md)

# TabbedBanner/TabbedBanner/AppDelegate.m

```objc
/*
Copyright (C) 2013-2015 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Application delegate
*/

#import "AppDelegate.h"
#import "TextViewController.h"
#import "BannerViewController.h"

@implementation AppDelegate {
    UITabBarController *_tabBarController;
}

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
    CGRect bounds = [[UIScreen mainScreen] bounds];
    self.window = [[UIWindow alloc] initWithFrame:bounds];
    self.window.backgroundColor = [UIColor whiteColor];

    NSData *ipsumData = [NSData dataWithContentsOfURL:[[NSBundle mainBundle] URLForResource:@"ipsums" withExtension:@"plist"] options:NSDataReadingMappedIfSafe error:nil];
    NSDictionary *ipsums = [NSPropertyListSerialization propertyListWithData:ipsumData options:NSPropertyListImmutable format:nil error:nil];

    TextViewController *originalIpsumViewController = [[TextViewController alloc] init];
    originalIpsumViewController.title = NSLocalizedString(@"Original", @"Original");
    originalIpsumViewController.text = ipsums[@"Original"];

    TextViewController *meatyIpsumViewController = [[TextViewController alloc] init];
    meatyIpsumViewController.title = NSLocalizedString(@"Meaty", @"Meaty");
    meatyIpsumViewController.text = ipsums[@"Meaty"];

    TextViewController *veganIpsumViewController = [[TextViewController alloc] init];
    veganIpsumViewController.title = NSLocalizedString(@"Vegan", @"Vegan");
    veganIpsumViewController.text = ipsums[@"Vegan"];

    _tabBarController = [[UITabBarController alloc] init];
    _tabBarController.viewControllers = @[
        [[BannerViewController alloc] initWithContentViewController:originalIpsumViewController],
        [[BannerViewController alloc] initWithContentViewController:meatyIpsumViewController],
        [[BannerViewController alloc] initWithContentViewController:veganIpsumViewController],
    ];

    self.window.rootViewController = _tabBarController;
    [self.window makeKeyAndVisible];
    return YES;
}

@end
```

[Next](TabbedBanner-TabbedBanner-BannerViewController.m.md)[Previous](BasicBanner-BasicBanner-main.m.md)

