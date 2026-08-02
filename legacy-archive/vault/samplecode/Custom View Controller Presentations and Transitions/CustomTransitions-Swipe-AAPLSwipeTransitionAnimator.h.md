---
title: Custom View Controller Presentations and Transitions
apple_id: TP40015158
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: UIKit
published: '2016-01-28'
source_url: https://developer.apple.com/library/archive/samplecode/CustomTransitions/Listings/CustomTransitions_Swipe_AAPLSwipeTransitionAnimator_h.html
archived_at: '2026-07-18T03:05:42.924682Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Custom View Controller Presentations and Transitions](Custom%20View%20Controller%20Presentations%20and%20Transitions.md)


[Next](CustomTransitions-Swipe-AAPLSwipeSecondViewController.h.md)[Previous](CustomTransitions-Swipe-AAPLSwipeTransitionInteractionController.m.md)

# CustomTransitions/Swipe/AAPLSwipeTransitionAnimator.h

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 A transition animator that slides the incoming view controller over the
  presenting view controller.
 */

@import UIKit;

@interface AAPLSwipeTransitionAnimator : NSObject <UIViewControllerAnimatedTransitioning>

- (instancetype)initWithTargetEdge:(UIRectEdge)targetEdge;

@property (nonatomic, readwrite) UIRectEdge targetEdge;

@end
```

[Next](CustomTransitions-Swipe-AAPLSwipeSecondViewController.h.md)[Previous](CustomTransitions-Swipe-AAPLSwipeTransitionInteractionController.m.md)

