---
title: iAdSuite with Storyboards
apple_id: DTS40013458
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2015-10-29'
source_url: https://developer.apple.com/library/archive/samplecode/iAdSuite_Storyboard/Listings/SplitNavigationBanner_SplitNavigationBanner_AppDelegate_m.html
archived_at: '2026-07-18T03:29:32.419406Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [iAdSuite with Storyboards](iAdSuite%20with%20Storyboards.md)


[Next](SplitNavigationBanner-SplitNavigationBanner-BannerViewController.m.md)[Previous](ReadMe.md.md)

# SplitNavigationBanner/SplitNavigationBanner/AppDelegate.m

```objc
/*
Copyright (C) 2015 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Application delegate
*/

#import "AppDelegate.h"

@implementation AppDelegate

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
    return YES;
}

// as a delegate to our UISplitViewController, block from hiding the master view controller for any orientation
- (BOOL)splitViewController:(UISplitViewController *)svc shouldHideViewController:(UIViewController *)vc inOrientation:(UIInterfaceOrientation)orientation
{
    return NO;
}

@end
```

[Next](SplitNavigationBanner-SplitNavigationBanner-BannerViewController.m.md)[Previous](ReadMe.md.md)

