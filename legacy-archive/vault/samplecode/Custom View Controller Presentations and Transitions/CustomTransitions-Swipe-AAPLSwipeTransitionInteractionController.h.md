---
title: Custom View Controller Presentations and Transitions
apple_id: TP40015158
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: UIKit
published: '2016-01-28'
source_url: https://developer.apple.com/library/archive/samplecode/CustomTransitions/Listings/CustomTransitions_Swipe_AAPLSwipeTransitionInteractionController_h.html
archived_at: '2026-07-18T03:05:43.148542Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Custom View Controller Presentations and Transitions](Custom%20View%20Controller%20Presentations%20and%20Transitions.md)


[Next](CustomTransitions-Swipe-AAPLSwipeTransitionDelegate.h.md)[Previous](CustomTransitions-Swipe-AAPLSwipeFirstViewController.h.md)

# CustomTransitions/Swipe/AAPLSwipeTransitionInteractionController.h

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The interaction controller for the Swipe demo.  Tracks a UIScreenEdgePanGestureRecognizer
  from a specified screen edge and derives the completion percentage for the
  transition.
 */

@import UIKit;

@interface AAPLSwipeTransitionInteractionController : UIPercentDrivenInteractiveTransition

- (instancetype)initWithGestureRecognizer:(UIScreenEdgePanGestureRecognizer*)gestureRecognizer edgeForDragging:(UIRectEdge)edge NS_DESIGNATED_INITIALIZER;

- (instancetype)init NS_UNAVAILABLE;

@end
```

[Next](CustomTransitions-Swipe-AAPLSwipeTransitionDelegate.h.md)[Previous](CustomTransitions-Swipe-AAPLSwipeFirstViewController.h.md)

