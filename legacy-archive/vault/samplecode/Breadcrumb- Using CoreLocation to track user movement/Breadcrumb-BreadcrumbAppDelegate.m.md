---
title: 'Breadcrumb: Using CoreLocation to track user movement'
apple_id: DTS40010048
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: CoreLocation
published: '2018-05-17'
source_url: https://developer.apple.com/library/archive/samplecode/Breadcrumb/Listings/Breadcrumb_BreadcrumbAppDelegate_m.html
archived_at: '2026-07-27T06:57:01.927809Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Breadcrumb: Using CoreLocation to track user movement](Breadcrumb-%20Using%20CoreLocation%20to%20track%20user%20movement.md)


[Next](Breadcrumb-CrumbPath.h.md)[Previous](Breadcrumb-SettingsViewController.m.md)

# Breadcrumb/BreadcrumbAppDelegate.m

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Template delegate for the application.
 */

#import "BreadcrumbAppDelegate.h"
#import "SettingsKeys.h"
@import MapKit; // for kCLLocationAccuracyBest

@implementation BreadcrumbAppDelegate

// The app delegate must implement the window @property
// from UIApplicationDelegate @protocol to use a main storyboard file.
//
@synthesize window;

- (BOOL)application:(UIApplication *)application willFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
    // It is important to registerDefaults as soon as possible,
    // because it can change so much of how your app behaves.
    //
    NSMutableDictionary *defaultsDictionary = [NSMutableDictionary dictionary];

    // By default we track the user location while in the background.
    defaultsDictionary[TrackLocationInBackgroundPrefsKey] = @YES;

    // By default we use the best accuracy setting (kCLLocationAccuracyBest).
    defaultsDictionary[LocationTrackingAccuracyPrefsKey] = @(kCLLocationAccuracyBest);

    // By default we play a sound in the background to signify a location change.
    defaultsDictionary[PlaySoundOnLocationUpdatePrefsKey] = @YES;

    [[NSUserDefaults standardUserDefaults] registerDefaults:defaultsDictionary];

    return YES;
}

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
    //..
    return YES;
}

@end
```

[Next](Breadcrumb-CrumbPath.h.md)[Previous](Breadcrumb-SettingsViewController.m.md)
