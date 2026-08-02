---
title: iAdSuite
apple_id: DTS40010198
resource_type: Sample Code
platform: iOS
topic: null
technology: iAd
published: '2013-05-28'
source_url: https://developer.apple.com/library/archive/samplecode/iAdSuite/Listings/SplitNavigationBanner_SplitNavigationBanner_BannerViewController_h.html
archived_at: '2026-07-18T03:29:30.920971Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [iAdSuite](iAdSuite.md)


[Next](SplitNavigationBanner-SplitNavigationBanner-AppDelegate.h.md)[Previous](SplitNavigationBanner-SplitNavigationBanner-BannerViewController.m.md)

# SplitNavigationBanner/SplitNavigationBanner/BannerViewController.h

```objc
/*
Copyright (C) 2013-2015 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
A container view controller that manages an ADBannerView and a content view controller
*/

#import <UIKit/UIKit.h>
#import <iAd/iAd.h>

extern NSString * const BannerViewActionWillBegin;
extern NSString * const BannerViewActionDidFinish;

@interface BannerViewController : UIViewController <ADBannerViewDelegate>

- (instancetype)initWithContentViewController:(UIViewController *)contentController;

@end
```

[Next](SplitNavigationBanner-SplitNavigationBanner-AppDelegate.h.md)[Previous](SplitNavigationBanner-SplitNavigationBanner-BannerViewController.m.md)

