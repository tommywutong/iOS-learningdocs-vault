---
title: 'Regions: region monitoring, significant location changes, background location
  service, location service authorization'
apple_id: DTS40010726
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2016-02-11'
source_url: https://developer.apple.com/library/archive/samplecode/Regions/Listings/Regions_RegionsAppDelegate_m.html
archived_at: '2026-07-18T03:22:05.462941Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Regions: region monitoring, significant location changes, background location service, location service authorization](Regions-%20region%20monitoring%2C%20significant%20location%20changes%2C%20background%20location%20se.md)


[Next](Regions-RegionsViewController.m.md)[Previous](Regions-RegionAnnotation.m.md)

# Regions/RegionsAppDelegate.m

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The application delegate which creates the window and root view controller.
 */

#import "RegionsAppDelegate.h"
#import "RegionsViewController.h"

@interface RegionsAppDelegate()

@property (strong, nonatomic) CLLocationManager *locationManager;
@property (nonatomic, readonly) RegionsViewController *viewController;

@end

@implementation RegionsAppDelegate

@synthesize viewController = _viewController;

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    // Override point for customization after application launch.

    return YES;
}

// Custom getter for the read-only property viewController.
- (RegionsViewController *)viewController {

    // lazy accessor implementation
    if (!_viewController) {
        _viewController = (RegionsViewController *)self.window.rootViewController;
    }

    return _viewController;
}

- (void)applicationDidEnterBackground:(UIApplication *)application {
    /*
     Use this method to release shared resources, save user data, invalidate timers, and store enough application state information to restore your application to its current state in case it is terminated later. 
     If your application supports background execution, called instead of applicationWillTerminate: when the user quits.
     */

    // Reset the icon badge number to zero.
    [UIApplication sharedApplication].applicationIconBadgeNumber = 0;

}


- (void)applicationWillEnterForeground:(UIApplication *)application {
    /*
     Called as part of  transition from the background to the inactive state: here you can undo many of the changes made on entering the background.
     */
}


- (void)applicationDidBecomeActive:(UIApplication *)application {
    /*
     Restart any tasks that were paused (or not yet started) while the application was inactive. If the application was previously in the background, optionally refresh the user interface.
     */
}


- (void)applicationWillResignActive:(UIApplication *)application {
    /*
     Sent when the application is about to move from active to inactive state. This can occur for certain types of temporary interruptions (such as an incoming phone call or SMS message) or when the user quits the application and it begins the transition to the background state.
     Use this method to pause ongoing tasks, disable timers, and throttle down OpenGL ES frame rates. Games should use this method to pause the game.
     */
}


- (void)applicationWillTerminate:(UIApplication *)application {
    // Save data if appropriate.
}



@end
```

[Next](Regions-RegionsViewController.m.md)[Previous](Regions-RegionAnnotation.m.md)

