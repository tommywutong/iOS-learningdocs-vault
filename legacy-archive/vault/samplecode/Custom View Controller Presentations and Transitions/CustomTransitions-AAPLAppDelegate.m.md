---
title: Custom View Controller Presentations and Transitions
apple_id: TP40015158
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: UIKit
published: '2016-01-28'
source_url: https://developer.apple.com/library/archive/samplecode/CustomTransitions/Listings/CustomTransitions_AAPLAppDelegate_m.html
archived_at: '2026-07-18T03:05:40.914254Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Custom View Controller Presentations and Transitions](Custom%20View%20Controller%20Presentations%20and%20Transitions.md)


[Next](CustomTransitions-Swipe-AAPLSwipeSecondViewController.m.md)[Previous](CustomTransitions-Checkerboard-AAPLCheckerboardFirstViewController.m.md)

# CustomTransitions/AAPLAppDelegate.m

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The application delegate.
 */

#import "AAPLAppDelegate.h"

@implementation AAPLAppDelegate

//| ----------------------------------------------------------------------------
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
    // Override point for customization after application launch.
    return YES;
}


//| ----------------------------------------------------------------------------
#ifdef __IPHONE_9_0
- (UIInterfaceOrientationMask)application:(UIApplication *)application supportedInterfaceOrientationsForWindow:(UIWindow *)window
#else
- (NSUInteger)application:(UIApplication *)application supportedInterfaceOrientationsForWindow:(UIWindow *)window
#endif
{
    if ([UIDevice currentDevice].systemVersion.floatValue < 8.f)
        return UIInterfaceOrientationMaskPortrait;
    else
        return UIInterfaceOrientationMaskAll;
}

@end
```

[Next](CustomTransitions-Swipe-AAPLSwipeSecondViewController.m.md)[Previous](CustomTransitions-Checkerboard-AAPLCheckerboardFirstViewController.m.md)

