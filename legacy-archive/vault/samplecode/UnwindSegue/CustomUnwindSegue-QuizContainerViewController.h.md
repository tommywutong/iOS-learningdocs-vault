---
title: UnwindSegue
apple_id: DTS40013644
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2018-03-15'
source_url: https://developer.apple.com/library/archive/samplecode/UnwindSegue/Listings/CustomUnwindSegue_QuizContainerViewController_h.html
archived_at: '2026-07-18T03:27:36.384566Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [UnwindSegue](UnwindSegue.md)


[Next](CustomUnwindSegue-AppDelegate.h.md)[Previous](CustomUnwindSegue-QuizContainerFadeViewControllerSegue.h.md)

# CustomUnwindSegue/QuizContainerViewController.h

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 A custom container view controller that is functionally similar to a 
  UINavigationController.
 */

@import UIKit;

@interface QuizContainerViewController : UIViewController 

//! The view controller at the top of the navigation stack (on screen).
@property (nonatomic, readonly) UIViewController *topViewController;
@property (nonatomic, copy) NSArray *viewControllers;

- (void)setViewControllers:(NSArray *)viewControllers animated:(BOOL)animated;
- (void)pushViewController:(UIViewController *)viewController animated:(BOOL)animated;
- (NSArray *)popToViewController:(UIViewController *)viewController animated:(BOOL)animated;

@end
```

[Next](CustomUnwindSegue-AppDelegate.h.md)[Previous](CustomUnwindSegue-QuizContainerFadeViewControllerSegue.h.md)

