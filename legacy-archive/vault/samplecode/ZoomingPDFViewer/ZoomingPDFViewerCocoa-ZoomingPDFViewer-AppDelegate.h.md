---
title: ZoomingPDFViewer
apple_id: DTS40010281
resource_type: Sample Code
platform: iOS
topic: Graphics & Animation
technology: CoreGraphics
published: '2017-04-27'
source_url: https://developer.apple.com/library/archive/samplecode/ZoomingPDFViewer/Listings/ZoomingPDFViewerCocoa_ZoomingPDFViewer_AppDelegate_h.html
archived_at: '2026-07-18T03:28:44.405484Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ZoomingPDFViewer](ZoomingPDFViewer.md)


[Next](ZoomingPDFViewerCocoa-ZoomingPDFViewer-ModelController.m.md)[Previous](ZoomingPDFViewerCocoa-ZoomingPDFViewer-AppDelegate.m.md)

# ZoomingPDFViewerCocoa/ZoomingPDFViewer/AppDelegate.h

```objc
/*
Copyright (C) 2017 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
The App Delegate.
*/

#import <UIKit/UIKit.h>



@interface AppDelegate: UIResponder <UIApplicationDelegate>


@property (strong, nonatomic) UIWindow *window;



- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions;

- (void)applicationWillResignActive:(UIApplication *)application;

- (void)applicationDidEnterBackground:(UIApplication *)application;

- (void)applicationWillEnterForeground:(UIApplication *)application;

- (void)applicationDidBecomeActive:(UIApplication *)application;

- (void)applicationWillTerminate:(UIApplication *)application;

@end
```

[Next](ZoomingPDFViewerCocoa-ZoomingPDFViewer-ModelController.m.md)[Previous](ZoomingPDFViewerCocoa-ZoomingPDFViewer-AppDelegate.m.md)

