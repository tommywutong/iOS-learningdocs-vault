---
title: Custom View Controller Presentations and Transitions
apple_id: TP40015158
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: UIKit
published: '2016-01-28'
source_url: https://developer.apple.com/library/archive/samplecode/CustomTransitions/Listings/CustomTransitions_Swipe_AAPLSwipeTransitionDelegate_h.html
archived_at: '2026-07-18T03:05:43.077169Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Custom View Controller Presentations and Transitions](Custom%20View%20Controller%20Presentations%20and%20Transitions.md)


[Next](CustomTransitions-Swipe-AAPLSwipeTransitionDelegate.m.md)[Previous](CustomTransitions-Swipe-AAPLSwipeTransitionInteractionController.h.md)

# CustomTransitions/Swipe/AAPLSwipeTransitionDelegate.h

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The transition delegate for the Swipe demo.  Vends instances of 
  AAPLSwipeTransitionAnimator and optionally 
  AAPLSwipeTransitionInteractionController.
 */

@import UIKit;

@interface AAPLSwipeTransitionDelegate : NSObject <UIViewControllerTransitioningDelegate>

//! If this transition will be interactive, this property is set to the
//! gesture recognizer which will drive the interactivity.
@property (nonatomic, strong) UIScreenEdgePanGestureRecognizer *gestureRecognizer;

@property (nonatomic, readwrite) UIRectEdge targetEdge;

@end
```

[Next](CustomTransitions-Swipe-AAPLSwipeTransitionDelegate.m.md)[Previous](CustomTransitions-Swipe-AAPLSwipeTransitionInteractionController.h.md)

