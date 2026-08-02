---
title: 'LaunchMe: Using a custom URL scheme to interact with your application'
apple_id: DTS40007417
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: null
published: '2017-02-11'
source_url: https://developer.apple.com/library/archive/samplecode/LaunchMe/Listings/LaunchMe_Classes_LaunchMeAppDelegate_h.html
archived_at: '2026-07-18T03:13:27.426924Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [LaunchMe: Using a custom URL scheme to interact with your application](LaunchMe-%20Using%20a%20custom%20URL%20scheme%20to%20interact%20with%20your%20application.md)


[Next](LaunchMe-Classes-ResultsViewController.m.md)[Previous](LaunchMe-Classes-RootViewController.m.md)

# LaunchMe/Classes/LaunchMeAppDelegate.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The application's delegate class. Handles incoming URL requests.
 */

// Keys to each parameter value in the URL
// (shared between App Delegate and RootViewController)
//
#define ColorKey @"color"
#define TextKey @"text"

@import UIKit;

@interface LaunchMeAppDelegate : NSObject <UIApplicationDelegate>

@end
```

[Next](LaunchMe-Classes-ResultsViewController.m.md)[Previous](LaunchMe-Classes-RootViewController.m.md)

