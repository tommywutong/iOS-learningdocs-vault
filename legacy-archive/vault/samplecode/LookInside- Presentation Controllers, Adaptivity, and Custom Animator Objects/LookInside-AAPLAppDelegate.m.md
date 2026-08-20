---
title: 'LookInside: Presentation Controllers, Adaptivity, and Custom Animator Objects'
apple_id: TP40014643
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/LookInside/Listings/LookInside_AAPLAppDelegate_m.html
archived_at: '2026-07-18T03:13:48.845436Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [LookInside: Presentation Controllers, Adaptivity, and Custom Animator Objects](LookInside-%20Presentation%20Controllers%2C%20Adaptivity%2C%20and%20Custom%20Animator%20Objects.md)


[Next](LookInside-AAPLCoolPresentationController.m.md)[Previous](LookInside-AAPLOverlayTransitioner.m.md)

# LookInside/AAPLAppDelegate.m

```objc
/*
 Copyright (C) 2014 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:

  Application delegate implementation.

 */

#import "AAPLAppDelegate.h"
#import "AAPLRootViewController.h"

@implementation AAPLAppDelegate

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    self.window = [[UIWindow alloc] initWithFrame:[[UIScreen mainScreen] bounds]];
    self.window.backgroundColor = [UIColor whiteColor];
    [self.window makeKeyAndVisible];

    // Configure the root view controller, and set it as the root of the navigation controller
    AAPLRootViewController* rootViewController = [[AAPLRootViewController alloc] init];

    UINavigationController* navigationController = [[UINavigationController alloc] initWithRootViewController:rootViewController];

    [self.window setRootViewController:navigationController];

    return YES;
}

@end
```

[Next](LookInside-AAPLCoolPresentationController.m.md)[Previous](LookInside-AAPLOverlayTransitioner.m.md)

