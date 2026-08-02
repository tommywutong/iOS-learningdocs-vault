---
title: Custom View Controller Presentations and Transitions
apple_id: TP40015158
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: UIKit
published: '2016-01-28'
source_url: https://developer.apple.com/library/archive/samplecode/CustomTransitions/Listings/CustomTransitions_Adaptive_Presentation_AAPLAdaptivePresentationSecondViewController_m.html
archived_at: '2026-07-18T03:05:41.396911Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Custom View Controller Presentations and Transitions](Custom%20View%20Controller%20Presentations%20and%20Transitions.md)


[Next](CustomTransitions-Adaptive%20Presentation-AAPLAdaptivePresentationFirstViewControl-2.md)[Previous](CustomTransitions-Adaptive%20Presentation-AAPLAdaptivePresentationFirstViewControl.md)

# CustomTransitions/Adaptive Presentation/AAPLAdaptivePresentationSecondViewController.m

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The second view controller for the Adaptive Presentation demo.
 */

#import "AAPLAdaptivePresentationSecondViewController.h"
#import "AAPLAdaptivePresentationController.h"

@interface AAPLAdaptivePresentationSecondViewController () <UIAdaptivePresentationControllerDelegate>
@end


@implementation AAPLAdaptivePresentationSecondViewController

//| ----------------------------------------------------------------------------
- (void)viewDidLoad
{
    [super viewDidLoad];

    // In the regular environment, AAPLAdaptivePresentationController displays
    // a close button for the presented view controller.  For the compact
    // environment, a 'dismiss' button is added to this view controller's
    // navigationItem.  This button will be picked up and displayed in the
    // navigation bar of the navigation controller returned by
    // -presentationController:viewControllerForAdaptivePresentationStyle:
    UIBarButtonItem *dismissButton = [[UIBarButtonItem alloc] initWithTitle:@"Dismiss" style:UIBarButtonItemStylePlain target:self action:@selector(dismissButtonAction:)];
    self.navigationItem.leftBarButtonItem = dismissButton;
}


//| ----------------------------------------------------------------------------
- (void)setTransitioningDelegate:(id<UIViewControllerTransitioningDelegate>)transitioningDelegate
{
    [super setTransitioningDelegate:transitioningDelegate];

    // For an adaptive presentation, the presentation controller's delegate
    // must be configured prior to invoking
    // -presentViewController:animated:completion:.  This ensures the
    // presentation is able to properly adapt if the initial presentation
    // environment is compact.
    self.presentationController.delegate = self;
}


//| ----------------------------------------------------------------------------
- (IBAction)dismissButtonAction:(UIBarButtonItem *)sender
{
    [self performSegueWithIdentifier:@"unwindToFirstViewController" sender:sender];
}

#pragma mark -
#pragma mark UIAdaptivePresentationControllerDelegate

//| ----------------------------------------------------------------------------
- (UIModalPresentationStyle)adaptivePresentationStyleForPresentationController:(UIPresentationController *)controller
{
    // An adaptive presentation may only fallback to
    // UIModalPresentationFullScreen or UIModalPresentationOverFullScreen
    // in the horizontally compact environment.  Other presentation styles
    // are interpreted as UIModalPresentationNone - no adaptation occurs.
    return UIModalPresentationFullScreen;
}


//| ----------------------------------------------------------------------------
- (UIViewController*)presentationController:(UIPresentationController *)controller viewControllerForAdaptivePresentationStyle:(UIModalPresentationStyle)style
{
    return [[UINavigationController alloc] initWithRootViewController:controller.presentedViewController];
}

@end
```

[Next](CustomTransitions-Adaptive%20Presentation-AAPLAdaptivePresentationFirstViewControl-2.md)[Previous](CustomTransitions-Adaptive%20Presentation-AAPLAdaptivePresentationFirstViewControl.md)

