---
title: 'HelloGoodbye: Using the Accessibility API to Widen Your User Base'
apple_id: TP40014593
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/HelloGoodbye/Listings/HelloGoodbye_AAPLAppDelegate_m.html
archived_at: '2026-07-18T03:11:49.674196Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [HelloGoodbye: Using the Accessibility API to Widen Your User Base](HelloGoodbye-%20Using%20the%20Accessibility%20API%20to%20Widen%20Your%20User%20Base.md)


[Next](HelloGoodbye-AAPLPreviewLabel.h.md)[Previous](HelloGoodbye-AAPLPerson.h.md)

# HelloGoodbye/AAPLAppDelegate.m

```objc
/*
 Copyright (C) 2014 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:

  The delegate for the application.

 */

#import "AAPLAppDelegate.h"
#import "AAPLStartViewController.h"
#import "AAPLStyleUtilities.h"

@implementation AAPLAppDelegate

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    self.window = [[UIWindow alloc] initWithFrame:[[UIScreen mainScreen] bounds]];

    AAPLStartViewController *startViewController = [[AAPLStartViewController alloc] init];

    UINavigationController *navigationController = [[UINavigationController alloc] initWithRootViewController:startViewController];
    navigationController.navigationBar.tintColor = [AAPLStyleUtilities foregroundColor];
    self.window.rootViewController = navigationController;

    [self.window makeKeyAndVisible];
    return YES;
}

@end
```

[Next](HelloGoodbye-AAPLPreviewLabel.h.md)[Previous](HelloGoodbye-AAPLPerson.h.md)

