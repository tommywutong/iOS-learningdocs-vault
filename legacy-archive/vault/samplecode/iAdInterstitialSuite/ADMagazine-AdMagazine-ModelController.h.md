---
title: iAdInterstitialSuite
apple_id: DTS40010627
resource_type: Sample Code
platform: iOS
topic: null
technology: iAd
published: '2015-08-13'
source_url: https://developer.apple.com/library/archive/samplecode/iAdInterstitialSuite/Listings/ADMagazine_AdMagazine_ModelController_h.html
archived_at: '2026-07-18T03:29:29.566181Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [iAdInterstitialSuite](iAdInterstitialSuite.md)


[Next](ADMagazine-AdMagazine-AppDelegate.m.md)[Previous](ADMagazine-AdMagazine-DataViewController.h.md)

# ADMagazine/AdMagazine/ModelController.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The data model controller that manages our view controller pages.
 */

@import UIKit;

@class DataViewController;

@interface ModelController : NSObject <UIPageViewControllerDataSource>

- (DataViewController *)viewControllerAtIndex:(NSUInteger)index storyboard:(UIStoryboard *)storyboard;
- (NSUInteger)indexOfViewController:(DataViewController *)viewController;

@end
```

[Next](ADMagazine-AdMagazine-AppDelegate.m.md)[Previous](ADMagazine-AdMagazine-DataViewController.h.md)

