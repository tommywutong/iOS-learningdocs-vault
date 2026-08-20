---
title: iAdInterstitialSuite
apple_id: DTS40010627
resource_type: Sample Code
platform: iOS
topic: null
technology: iAd
published: '2015-08-13'
source_url: https://developer.apple.com/library/archive/samplecode/iAdInterstitialSuite/Listings/ADMagazine_AdMagazine_AppDelegate_m.html
archived_at: '2026-07-18T03:29:29.447557Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [iAdInterstitialSuite](iAdInterstitialSuite.md)


[Next](ADMagazine-AdMagazine-AppDelegate.h.md)[Previous](ADMagazine-AdMagazine-ModelController.h.md)

# ADMagazine/AdMagazine/AppDelegate.m

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The application delegate class used for setting up our application.
 */

#import "AppDelegate.h"
@import iAd;

@implementation AppDelegate

// The app delegate must implement the window @property
// from UIApplicationDelegate @protocol to use a main storyboard file.
//
@synthesize window;

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
    /* Ads involve network requests, so if an application needs to use interstitial
        ads and wants to ensure early availability, this method can be called to trigger
        a prefetch.
    */
    [UIViewController prepareInterstitialAds];

    return YES;
}

@end
```

[Next](ADMagazine-AdMagazine-AppDelegate.h.md)[Previous](ADMagazine-AdMagazine-ModelController.h.md)

