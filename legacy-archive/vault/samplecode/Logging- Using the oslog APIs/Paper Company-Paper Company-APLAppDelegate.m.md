---
title: 'Logging: Using the os_log APIs'
apple_id: TP40017510
resource_type: Sample Code
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/Logging/Listings/Paper_Company_Paper_Company_APLAppDelegate_m.html
archived_at: '2026-07-18T03:13:47.350723Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Logging: Using the os_log APIs](Logging-%20Using%20the%20oslog%20APIs.md)


[Next](Paper%20Company-Paper%20Company-APLPaperCompany.h.md)[Previous](Paper%20Company-Paper%20Company-APLPaperCompany.m.md)

# Paper Company/Paper Company/APLAppDelegate.m

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Basically the default AppDelegate implementation.
 */

#import "APLAppDelegate.h"


@implementation APLAppDelegate

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

[Next](Paper%20Company-Paper%20Company-APLPaperCompany.h.md)[Previous](Paper%20Company-Paper%20Company-APLPaperCompany.m.md)

