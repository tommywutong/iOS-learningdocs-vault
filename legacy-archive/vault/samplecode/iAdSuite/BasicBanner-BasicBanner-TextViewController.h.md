---
title: iAdSuite
apple_id: DTS40010198
resource_type: Sample Code
platform: iOS
topic: null
technology: iAd
published: '2013-05-28'
source_url: https://developer.apple.com/library/archive/samplecode/iAdSuite/Listings/BasicBanner_BasicBanner_TextViewController_h.html
archived_at: '2026-07-18T03:29:30.114328Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [iAdSuite](iAdSuite.md)


[Next](BasicBanner-BasicBanner-TextViewController.m.md)[Previous](BasicBanner-BasicBanner-AppDelegate.h.md)

# BasicBanner/BasicBanner/TextViewController.h

```objc
/*
Copyright (C) 2013-2015 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
A simple view controller that manages a content view and an ADBannerView
*/

#import <UIKit/UIKit.h>
#import <iAd/iAd.h>

@interface TextViewController : UIViewController <ADBannerViewDelegate>

@property (nonatomic, copy) NSString *text;

@end
```

[Next](BasicBanner-BasicBanner-TextViewController.m.md)[Previous](BasicBanner-BasicBanner-AppDelegate.h.md)

