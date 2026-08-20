---
title: iAdSuite
apple_id: DTS40010198
resource_type: Sample Code
platform: iOS
topic: null
technology: iAd
published: '2013-05-28'
source_url: https://developer.apple.com/library/archive/samplecode/iAdSuite/Listings/MediumRectBanner_MediumRectBanner_AppDelegate_m.html
archived_at: '2026-07-18T03:29:30.620563Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [iAdSuite](iAdSuite.md)


[Next](MediumRectBanner-MediumRectBanner-CollectionViewController.m.md)[Previous](MediumRectBanner-MediumRectBanner-CollectionViewController.h.md)

# MediumRectBanner/MediumRectBanner/AppDelegate.m

```objc
/*
Copyright (C) 2013-2015 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Application delegate
*/

#import "AppDelegate.h"
#import "CollectionViewController.h"

@implementation AppDelegate {
    CollectionViewController *_viewController;
}

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
    self.window = [[UIWindow alloc] initWithFrame:[[UIScreen mainScreen] bounds]];
    self.window.backgroundColor = [UIColor whiteColor];

    _viewController = [[CollectionViewController alloc] initWithNibName:@"CollectionViewController" bundle:nil];
    self.window.rootViewController = _viewController;
    [self.window makeKeyAndVisible];
    return YES;
}

@end
```

[Next](MediumRectBanner-MediumRectBanner-CollectionViewController.m.md)[Previous](MediumRectBanner-MediumRectBanner-CollectionViewController.h.md)

