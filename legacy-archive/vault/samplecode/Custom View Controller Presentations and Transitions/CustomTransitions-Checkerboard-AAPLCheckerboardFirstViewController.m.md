---
title: Custom View Controller Presentations and Transitions
apple_id: TP40015158
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: UIKit
published: '2016-01-28'
source_url: https://developer.apple.com/library/archive/samplecode/CustomTransitions/Listings/CustomTransitions_Checkerboard_AAPLCheckerboardFirstViewController_m.html
archived_at: '2026-07-18T03:05:41.548069Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Custom View Controller Presentations and Transitions](Custom%20View%20Controller%20Presentations%20and%20Transitions.md)


[Next](CustomTransitions-AAPLAppDelegate.m.md)[Previous](CustomTransitions-Checkerboard-AAPLCheckerboardTransitionAnimator.m.md)

# CustomTransitions/Checkerboard/AAPLCheckerboardFirstViewController.m

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The initial view controller for the Checkerboard demo.
 */

#import "AAPLCheckerboardFirstViewController.h"
#import "AAPLCheckerboardTransitionAnimator.h"

@interface AAPLCheckerboardFirstViewController () <UINavigationControllerDelegate>
@end


@implementation AAPLCheckerboardFirstViewController

//| ----------------------------------------------------------------------------
- (void)viewDidLoad
{
    [super viewDidLoad];

    self.navigationController.delegate = self;
}

#pragma mark -
#pragma mark UINavigationControllerDelegate

//| ----------------------------------------------------------------------------
//  The navigation controller tries to invoke this method on its delegate to
//  retrieve an animator object to be used for animating the transition to the
//  incoming view controller.  Your implementation is expected to return an
//  object that conforms to the UIViewControllerAnimatedTransitioning protocol,
//  or nil if the transition should use the navigation controller's default
//  push/pop animation.
//
- (id<UIViewControllerAnimatedTransitioning>)navigationController:(UINavigationController *)navigationController animationControllerForOperation:(UINavigationControllerOperation)operation fromViewController:(UIViewController *)fromVC toViewController:(UIViewController *)toVC
{
    return [AAPLCheckerboardTransitionAnimator new];
}

@end
```

[Next](CustomTransitions-AAPLAppDelegate.m.md)[Previous](CustomTransitions-Checkerboard-AAPLCheckerboardTransitionAnimator.m.md)

