---
title: iAdSuite
apple_id: DTS40010198
resource_type: Sample Code
platform: iOS
topic: null
technology: iAd
published: '2013-05-28'
source_url: https://developer.apple.com/library/archive/samplecode/iAdSuite/Listings/SplitNavigationBanner_SplitNavigationBanner_AppDelegate_m.html
archived_at: '2026-07-18T03:29:30.871957Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [iAdSuite](iAdSuite.md)


[Next](SplitNavigationBanner-SplitNavigationBanner-BannerViewController.m.md)[Previous](ReadMe.md.md)

# SplitNavigationBanner/SplitNavigationBanner/AppDelegate.m

```objc
/*
Copyright (C) 2013-2015 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Application delegate
*/

#import "AppDelegate.h"
#import "MasterViewController.h"
#import "TextViewController.h"
#import "BannerViewController.h"

@interface AppDelegate () <UISplitViewControllerDelegate>

@end

@implementation AppDelegate {
    UINavigationController *_navigationController;
    UISplitViewController *_splitViewController;
    BannerViewController *_bannerViewController;
}

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
    self.window = [[UIWindow alloc] initWithFrame:[[UIScreen mainScreen] bounds]];
    self.window.backgroundColor = [UIColor whiteColor];

    if ([[UIDevice currentDevice] userInterfaceIdiom] == UIUserInterfaceIdiomPhone) {
        // On iPhone we use a UINavigationController as our primary user interface.
        // In that configuration, the master view controller won't have a detail view controller.
        MasterViewController *masterViewController = [[MasterViewController alloc] initWithStyle:UITableViewStyleGrouped];
        _navigationController = [[UINavigationController alloc] initWithRootViewController:masterViewController];
        _bannerViewController = [[BannerViewController alloc] initWithContentViewController:_navigationController];
    } else {
        // On iPad we use a UISplitViewController as our primary user interface.
        // In this configuration, the master view controller has a detail view controller that it will update as the selection changes.
        MasterViewController *masterViewController = [[MasterViewController alloc] initWithStyle:UITableViewStylePlain];
        TextViewController *detailViewController = [[TextViewController alloc] init];
        masterViewController.detailViewController = detailViewController;

        _splitViewController = [[UISplitViewController alloc] init];
        _splitViewController.viewControllers = @[
            [[UINavigationController alloc] initWithRootViewController:masterViewController],
            [[UINavigationController alloc] initWithRootViewController:detailViewController]
        ];
        _splitViewController.delegate = self;
        _bannerViewController = [[BannerViewController alloc] initWithContentViewController:_splitViewController];
    }
    self.window.rootViewController = _bannerViewController;
    [self.window makeKeyAndVisible];
    return YES;
}

- (BOOL)splitViewController:(UISplitViewController *)svc shouldHideViewController:(UIViewController *)vc inOrientation:(UIInterfaceOrientation)orientation
{
    return NO;
}

@end
```

[Next](SplitNavigationBanner-SplitNavigationBanner-BannerViewController.m.md)[Previous](ReadMe.md.md)

