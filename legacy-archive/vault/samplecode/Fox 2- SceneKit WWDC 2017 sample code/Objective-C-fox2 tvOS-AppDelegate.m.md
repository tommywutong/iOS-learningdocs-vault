---
title: 'Fox 2: SceneKit WWDC 2017 sample code'
apple_id: TP40017656
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SceneKit
published: '2018-04-05'
source_url: https://developer.apple.com/library/archive/samplecode/scenekit-2017/Listings/Objective_C_fox2_tvOS_AppDelegate_m.html
archived_at: '2026-07-26T19:54:17.161615Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Fox 2: SceneKit WWDC 2017 sample code](Fox%202-%20SceneKit%20WWDC%202017%20sample%20code.md)


[Next](Objective-C-fox2%20tvOS-AppDelegate.h.md)[Previous](Objective-C-fox2%20tvOS-AAPLGameViewController.m.md)

# Objective-C/fox2 tvOS/AppDelegate.m

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 a standard App Delegate.
 */

#import "AppDelegate.h"

@interface AppDelegate ()

@end

@implementation AppDelegate

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    // Override point for customization after application launch.
    return YES;
}

- (void)applicationWillResignActive:(UIApplication *)application {
    // Sent when the application is about to move from active to inactive state. This can occur for certain types of temporary interruptions (such as an incoming phone call or SMS message) or when the user quits the application and it begins the transition to the background state.
    // Use this method to pause ongoing tasks, disable timers, and throttle down OpenGL ES frame rates. Games should use this method to pause the game.
}

- (void)applicationDidEnterBackground:(UIApplication *)application {
    // Use this method to release shared resources, save user data, invalidate timers, and store enough application state information to restore your application to its current state in case it is terminated later.
    // If your application supports background execution, this method is called instead of applicationWillTerminate: when the user quits.
}

- (void)applicationWillEnterForeground:(UIApplication *)application {
    // Called as part of the transition from the background to the active state; here you can undo many of the changes made on entering the background.
}

- (void)applicationDidBecomeActive:(UIApplication *)application {
    // Restart any tasks that were paused (or not yet started) while the application was inactive. If the application was previously in the background, optionally refresh the user interface.
}

- (void)applicationWillTerminate:(UIApplication *)application {
    // Called when the application is about to terminate. Save data if appropriate. See also applicationDidEnterBackground:.
}

@end
```

[Next](Objective-C-fox2%20tvOS-AppDelegate.h.md)[Previous](Objective-C-fox2%20tvOS-AAPLGameViewController.m.md)

