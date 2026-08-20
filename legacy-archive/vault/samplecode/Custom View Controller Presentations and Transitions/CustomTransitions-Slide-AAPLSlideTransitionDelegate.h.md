---
title: Custom View Controller Presentations and Transitions
apple_id: TP40015158
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: UIKit
published: '2016-01-28'
source_url: https://developer.apple.com/library/archive/samplecode/CustomTransitions/Listings/CustomTransitions_Slide_AAPLSlideTransitionDelegate_h.html
archived_at: '2026-07-18T03:05:42.491919Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Custom View Controller Presentations and Transitions](Custom%20View%20Controller%20Presentations%20and%20Transitions.md)


[Next](CustomTransitions-Slide-AAPLSlideTransitionAnimator.m.md)[Previous](CustomTransitions-Slide-AAPLSlideTransitionInteractionController.m.md)

# CustomTransitions/Slide/AAPLSlideTransitionDelegate.h

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The delegate of the tab bar controller for the Slide demo.  Manages the
  gesture recognizer used for the interactive transition.  Vends
  instances of AAPLSlideTransitionAnimator and 
  AAPLSlideTransitionInteractionController.
 */

@import UIKit;

@interface AAPLSlideTransitionDelegate : NSObject <UITabBarControllerDelegate>

//! The UITabBarController instance for which this object is the delegate of.
@property (nonatomic, weak) IBOutlet UITabBarController *tabBarController;

//! The gesture recognizer used for driving the interactive transition
//! between view controllers.  AAPLSlideTransitionDelegate installs this
//! gesture recognizer on the tab bar controller's view.
@property (nonatomic, strong, readonly) UIPanGestureRecognizer *panGestureRecongizer;

@end
```

[Next](CustomTransitions-Slide-AAPLSlideTransitionAnimator.m.md)[Previous](CustomTransitions-Slide-AAPLSlideTransitionInteractionController.m.md)

