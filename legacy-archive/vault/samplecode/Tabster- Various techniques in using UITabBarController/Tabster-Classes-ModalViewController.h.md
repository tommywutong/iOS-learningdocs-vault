---
title: 'Tabster: Various techniques in using UITabBarController'
apple_id: DTS40011213
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2018-02-15'
source_url: https://developer.apple.com/library/archive/samplecode/Tabster/Listings/Tabster_Classes_ModalViewController_h.html
archived_at: '2026-07-18T03:26:20.140914Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Tabster: Various techniques in using UITabBarController](Tabster-%20Various%20techniques%20in%20using%20UITabBarController.md)


[Next](Tabster-Classes-TwoViewController.m.md)[Previous](Tabster-Classes-CrossfadeAnimationController.m.md)

# Tabster/Classes/ModalViewController.h

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The modal view controller for temporary UI interaction.
 */

@import UIKit;

@class SubLevelViewController;

@interface ModalViewController : UIViewController

@property (nonatomic, strong) SubLevelViewController *owningViewController;

@end
```

[Next](Tabster-Classes-TwoViewController.m.md)[Previous](Tabster-Classes-CrossfadeAnimationController.m.md)

