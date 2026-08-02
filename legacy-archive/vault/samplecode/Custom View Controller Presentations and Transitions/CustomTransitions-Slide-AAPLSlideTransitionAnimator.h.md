---
title: Custom View Controller Presentations and Transitions
apple_id: TP40015158
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: UIKit
published: '2016-01-28'
source_url: https://developer.apple.com/library/archive/samplecode/CustomTransitions/Listings/CustomTransitions_Slide_AAPLSlideTransitionAnimator_h.html
archived_at: '2026-07-18T03:05:42.335285Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Custom View Controller Presentations and Transitions](Custom%20View%20Controller%20Presentations%20and%20Transitions.md)


[Next](CustomTransitions-Slide-AAPLSlideTransitionInteractionController.h.md)[Previous](CustomTransitions-Slide-AAPLSlideTransitionDelegate.m.md)

# CustomTransitions/Slide/AAPLSlideTransitionAnimator.h

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 A transition animator that transitions between two view controllers in
  a tab bar controller by sliding both view controllers in a given
  direction.
 */

@import UIKit;

@interface AAPLSlideTransitionAnimator : NSObject <UIViewControllerAnimatedTransitioning>

- (instancetype)initWithTargetEdge:(UIRectEdge)targetEdge;

//! The value for this property determines which direction the view controllers
//! slide during the transition.  This must be one of UIRectEdgeLeft or
//! UIRectEdgeRight.
@property (nonatomic, readwrite) UIRectEdge targetEdge;

@end
```

[Next](CustomTransitions-Slide-AAPLSlideTransitionInteractionController.h.md)[Previous](CustomTransitions-Slide-AAPLSlideTransitionDelegate.m.md)

