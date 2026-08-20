---
title: LocateMe
apple_id: DTS40007801
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: CoreLocation
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/LocateMe/Listings/LocateMe_AppDelegate_h.html
archived_at: '2026-07-18T03:13:45.924629Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [LocateMe](LocateMe.md)


[Next](LocateMe-SetupViewController.h.md)[Previous](LocateMe-TrackLocationViewController.h.md)

# LocateMe/AppDelegate.h

```objc
/*
Copyright (C) 2014 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:

The application delegate has a minimal role in this sample: in -applicationDidFinishLaunching: it adds the tab bar controller's view to the window. It also creates a CLLocationManager object to check the locationServicesEnabled property at launch time.

*/

#import <UIKit/UIKit.h>

@interface AppDelegate : UIResponder <UIApplicationDelegate>

@property (strong, nonatomic) UIWindow *window;

@end
```

[Next](LocateMe-SetupViewController.h.md)[Previous](LocateMe-TrackLocationViewController.h.md)

