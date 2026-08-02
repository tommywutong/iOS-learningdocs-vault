---
title: aurioTouch
apple_id: DTS40007770
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-08-12'
source_url: https://developer.apple.com/library/archive/samplecode/aurioTouch/Listings/Classes_aurioTouchAppDelegate_mm.html
archived_at: '2026-07-18T03:28:53.001516Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [aurioTouch](aurioTouch.md)


[Next](Classes-EAGLView.mm.md)[Previous](Classes-EAGLView.h.md)

# Classes/aurioTouchAppDelegate.mm

```objc
/*

 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 App delegate

 */

#import "aurioTouchAppDelegate.h"
#import "EAGLView.h"

@implementation aurioTouchAppDelegate

@synthesize window;
@synthesize view;

#pragma mark-

- (void)applicationDidFinishLaunching:(UIApplication *)application
{
    CGRect screenBounds = [[UIScreen mainScreen] bounds];
    window = [[UIWindow alloc] initWithFrame:screenBounds];

    UIViewController *myVC = [[UIViewController alloc]initWithNibName:nil bundle:nil];
    myVC.view = view;

    self.window.rootViewController = myVC;
    [myVC release];

    // Turn off the idle timer, since this app doesn't rely on constant touch input
    application.idleTimerDisabled = YES;

    [window makeKeyAndVisible];
}

- (void)applicationDidBecomeActive:(UIApplication *)application {
    //start animation now that we're in the foreground
    view.applicationResignedActive = NO;
    [view startAnimation];
}

- (void)applicationWillResignActive:(UIApplication *)application {
    //stop animation before going into background
    view.applicationResignedActive = YES;
    [view stopAnimation];
}

- (void)applicationDidEnterBackground:(UIApplication *)application {
}

- (void)applicationWillEnterForeground:(UIApplication *)application {
}

- (void)dealloc
{   
    [view release];
    [window release];
    [super dealloc];
}


@end
```

[Next](Classes-EAGLView.mm.md)[Previous](Classes-EAGLView.h.md)

