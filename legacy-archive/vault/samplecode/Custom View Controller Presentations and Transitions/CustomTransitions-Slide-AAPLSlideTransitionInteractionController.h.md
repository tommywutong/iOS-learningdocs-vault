---
title: Custom View Controller Presentations and Transitions
apple_id: TP40015158
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: UIKit
published: '2016-01-28'
source_url: https://developer.apple.com/library/archive/samplecode/CustomTransitions/Listings/CustomTransitions_Slide_AAPLSlideTransitionInteractionController_h.html
archived_at: '2026-07-18T03:05:42.586285Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Custom View Controller Presentations and Transitions](Custom%20View%20Controller%20Presentations%20and%20Transitions.md)


[Next](CustomTransitions-Slide-AAPLSlideTransitionInteractionController.m.md)[Previous](CustomTransitions-Slide-AAPLSlideTransitionAnimator.h.md)

# CustomTransitions/Slide/AAPLSlideTransitionInteractionController.h

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The interaction controller for the Slide demo.
 */

@import UIKit;

@interface AAPLSlideTransitionInteractionController : UIPercentDrivenInteractiveTransition

- (instancetype)initWithGestureRecognizer:(UIPanGestureRecognizer *)gestureRecognizer NS_DESIGNATED_INITIALIZER;

- (instancetype)init NS_UNAVAILABLE;

@end
```

[Next](CustomTransitions-Slide-AAPLSlideTransitionInteractionController.m.md)[Previous](CustomTransitions-Slide-AAPLSlideTransitionAnimator.h.md)

