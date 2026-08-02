---
title: 'Tabster: Various techniques in using UITabBarController'
apple_id: DTS40011213
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2018-02-15'
source_url: https://developer.apple.com/library/archive/samplecode/Tabster/Listings/Tabster_Classes_CrossfadeAnimationController_m.html
archived_at: '2026-07-18T03:26:19.656734Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Tabster: Various techniques in using UITabBarController](Tabster-%20Various%20techniques%20in%20using%20UITabBarController.md)


[Next](Tabster-Classes-ModalViewController.h.md)[Previous](Tabster-Classes-ThreeViewController.h.md)

# Tabster/Classes/CrossfadeAnimationController.m

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Animator between the two view controllers by performing a simple cross-fade.
 */

#import "CrossfadeAnimationController.h"

@implementation CrossfadeAnimationController

- (id)init
{
    if (self = [super init])
    {
        _duration = 1.0f;   // Default duration.
    }
    return self;
}

- (NSTimeInterval)transitionDuration:(id<UIViewControllerContextTransitioning>)transitionContext
{
    return self.duration;
}

- (void)animateTransition:(id<UIViewControllerContextTransitioning>)transitionContext
{
    UIViewController *fromVC = [transitionContext viewControllerForKey:UITransitionContextFromViewControllerKey];
    UIViewController *toVC = [transitionContext viewControllerForKey:UITransitionContextToViewControllerKey];
    UIView *toView = toVC.view;
    UIView *fromView = fromVC.view;

    [self animateTransition:transitionContext fromVC:fromVC toVC:toVC fromView:fromView toView:toView];
}

- (void)animateTransition:(id<UIViewControllerContextTransitioning>)transitionContext fromVC:(UIViewController *)fromVC toVC:(UIViewController *)toVC fromView:(UIView *)fromView toView:(UIView *)toView
{
    // Add the toView to the container.
    UIView *containerView = [transitionContext containerView];
    [containerView addSubview:toView];
    [containerView sendSubviewToBack:toView];

    // Do the cross-fade transition.
    NSTimeInterval duration = [self transitionDuration:transitionContext];
    [UIView animateWithDuration:duration animations:^{
        fromView.alpha = 0.0;
    } completion:^(BOOL finished) {
        if ([transitionContext transitionWasCancelled])
        {
            fromView.alpha = 1.0;
        }
        else
        {
            // Reset from- view to its original state.
            [fromView removeFromSuperview];
            fromView.alpha = 1.0;
        }
        [transitionContext completeTransition:![transitionContext transitionWasCancelled]];
    }];
}

@end
```

[Next](Tabster-Classes-ModalViewController.h.md)[Previous](Tabster-Classes-ThreeViewController.h.md)

