---
title: 'LookInside: Presentation Controllers, Adaptivity, and Custom Animator Objects'
apple_id: TP40014643
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/LookInside/Listings/LookInside_AAPLCoolTransitioner_m.html
archived_at: '2026-07-18T03:13:49.181452Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [LookInside: Presentation Controllers, Adaptivity, and Custom Animator Objects](LookInside-%20Presentation%20Controllers%2C%20Adaptivity%2C%20and%20Custom%20Animator%20Objects.md)


[Next](LookInside-AAPLCoolPresentationController.h.md)[Previous](LookInside-AAPLOverlayPresentationController.m.md)

# LookInside/AAPLCoolTransitioner.m

```objc
/*
 Copyright (C) 2014 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:

  AAPLCoolAnimatedTransitioning and AAPLCoolTransitioningDelegate implementations.

 */

#import "AAPLCoolTransitioner.h"
#import "AAPLCoolPresentationController.h"

@implementation AAPLCoolTransitioningDelegate

- (UIPresentationController *)presentationControllerForPresentedViewController:(UIViewController *)presented presentingViewController:(UIViewController *)presenting sourceViewController:(UIViewController *)source
{
    // Provide our Cool presentation controller
    return [[AAPLCoolPresentationController alloc] initWithPresentedViewController:presented presentingViewController:presenting];
}

- (AAPLCoolAnimatedTransitioning *)animationController
{
    // Provide our Cool animation controller
    AAPLCoolAnimatedTransitioning *animationController = [[AAPLCoolAnimatedTransitioning alloc] init];
    return animationController;
}

- (id <UIViewControllerAnimatedTransitioning>)animationControllerForPresentedController:(UIViewController *)presented presentingController:(UIViewController *)presenting sourceController:(UIViewController *)source
{
    AAPLCoolAnimatedTransitioning *animationController = [self animationController];
    [animationController setIsPresentation:YES];

    return animationController;
}

- (id <UIViewControllerAnimatedTransitioning>)animationControllerForDismissedController:(UIViewController *)dismissed
{
    AAPLCoolAnimatedTransitioning *animationController = [self animationController];
    [animationController setIsPresentation:NO];

    return animationController;
}

@end

@implementation AAPLCoolAnimatedTransitioning

- (NSTimeInterval)transitionDuration:(id <UIViewControllerContextTransitioning>)transitionContext
{
    return 0.5;
}

- (void)animateTransition:(id <UIViewControllerContextTransitioning>)transitionContext
{
    UIViewController *fromVC = [transitionContext viewControllerForKey:UITransitionContextFromViewControllerKey];
    UIView *fromView = [fromVC view];
    UIViewController *toVC   = [transitionContext viewControllerForKey:UITransitionContextToViewControllerKey];
    UIView *toView = [toVC view];

    UIView *containerView = [transitionContext containerView];

    BOOL isPresentation = [self isPresentation];

    if(isPresentation)
    {
        [containerView addSubview:toView];
    }

    UIViewController *animatingVC = isPresentation? toVC : fromVC;
    UIView *animatingView = [animatingVC view];

    [animatingView setFrame:[transitionContext finalFrameForViewController:animatingVC]];

    CGAffineTransform presentedTransform = CGAffineTransformIdentity;
    CGAffineTransform dismissedTransform = CGAffineTransformConcat(CGAffineTransformMakeScale(0.001, 0.001), CGAffineTransformMakeRotation(8 * M_PI));

    [animatingView setTransform:isPresentation ? dismissedTransform : presentedTransform];

    [UIView animateWithDuration:[self transitionDuration:transitionContext]
                          delay:0
         usingSpringWithDamping:300.0
          initialSpringVelocity:5.0
                        options:UIViewAnimationOptionAllowUserInteraction | UIViewAnimationOptionBeginFromCurrentState
                     animations:^{
                         [animatingView setTransform:isPresentation ? presentedTransform : dismissedTransform];
                     }
                     completion:^(BOOL finished){
                         if(![self isPresentation])
                         {
                             [fromView removeFromSuperview];
                         }
                         [transitionContext completeTransition:YES];
                     }];
}

@end
```

[Next](LookInside-AAPLCoolPresentationController.h.md)[Previous](LookInside-AAPLOverlayPresentationController.m.md)

