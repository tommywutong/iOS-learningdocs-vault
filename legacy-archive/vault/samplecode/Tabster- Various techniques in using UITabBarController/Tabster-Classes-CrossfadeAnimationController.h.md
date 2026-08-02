---
title: 'Tabster: Various techniques in using UITabBarController'
apple_id: DTS40011213
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2018-02-15'
source_url: https://developer.apple.com/library/archive/samplecode/Tabster/Listings/Tabster_Classes_CrossfadeAnimationController_h.html
archived_at: '2026-07-18T03:26:19.616817Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Tabster: Various techniques in using UITabBarController](Tabster-%20Various%20techniques%20in%20using%20UITabBarController.md)


[Next](Tabster-Classes-FourViewController.h.md)[Previous](Tabster-Classes-TwoViewController.h.md)

# Tabster/Classes/CrossfadeAnimationController.h

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Animator between the two view controllers by performing a simple cross-fade.
 */

@import UIKit;

@interface CrossfadeAnimationController : NSObject <UIViewControllerAnimatedTransitioning>

@property (nonatomic, assign) NSTimeInterval duration;

// The direction of the animation.
@property (nonatomic, assign) BOOL reverse;

@end
```

[Next](Tabster-Classes-FourViewController.h.md)[Previous](Tabster-Classes-TwoViewController.h.md)

