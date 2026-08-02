---
title: Custom View Controller Presentations and Transitions
apple_id: TP40015158
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: UIKit
published: '2016-01-28'
source_url: https://developer.apple.com/library/archive/samplecode/CustomTransitions/Listings/CustomTransitions_Swipe_AAPLSwipeSecondViewController_m.html
archived_at: '2026-07-18T03:05:42.855622Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Custom View Controller Presentations and Transitions](Custom%20View%20Controller%20Presentations%20and%20Transitions.md)


[Next](CustomTransitions-Swipe-AAPLSwipeTransitionInteractionController.m.md)[Previous](CustomTransitions-AAPLAppDelegate.m.md)

# CustomTransitions/Swipe/AAPLSwipeSecondViewController.m

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The presented view controller for the Swipe demo.
 */

#import "AAPLSwipeSecondViewController.h"
#import "AAPLSwipeTransitionDelegate.h"

@interface AAPLSwipeSecondViewController ()
@end


@implementation AAPLSwipeSecondViewController

//| ----------------------------------------------------------------------------
- (void)viewDidLoad
{
    [super viewDidLoad];

    // This gesture recognizer could be defined in the storyboard but is
    // instead created in code for clarity.
    UIScreenEdgePanGestureRecognizer *interactiveTransitionRecognizer;
    interactiveTransitionRecognizer = [[UIScreenEdgePanGestureRecognizer alloc] initWithTarget:self action:@selector(interactiveTransitionRecognizerAction:)];
    interactiveTransitionRecognizer.edges = UIRectEdgeLeft;
    [self.view addGestureRecognizer:interactiveTransitionRecognizer];
}


//| ----------------------------------------------------------------------------
//! Action method for the interactiveTransitionRecognizer.
//
- (IBAction)interactiveTransitionRecognizerAction:(UIScreenEdgePanGestureRecognizer *)sender
{
    if (sender.state == UIGestureRecognizerStateBegan) {
        // "BackToFirstViewController" is the identifier of the unwind segue
        // back to AAPLSwipeFirstViewController.  Triggering it will dismiss
        // this view controller.
        [self performSegueWithIdentifier:@"BackToFirstViewController" sender:sender];
    }
}


//| ----------------------------------------------------------------------------
- (void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender
{
    if ([segue.identifier isEqualToString:@"BackToFirstViewController"])
    {
        // Check if we were presented with our custom transition delegate.
        // If we were, update the configuration of the
        // AAPLSwipeTransitionDelegate with the gesture recognizer and
        // targetEdge for this view controller.
        if ([self.transitioningDelegate isKindOfClass:AAPLSwipeTransitionDelegate.class])
        {
            AAPLSwipeTransitionDelegate *transitionDelegate = self.transitioningDelegate;

            // If this will be an interactive presentation, pass the gesture
            // recognizer along to our AAPLSwipeTransitionDelegate instance
            // so it can return the necessary
            // <UIViewControllerInteractiveTransitioning> for the presentation.
            if ([sender isKindOfClass:UIGestureRecognizer.class])
                transitionDelegate.gestureRecognizer = sender;
            else
                transitionDelegate.gestureRecognizer = nil;

            // Set the edge of the screen to dismiss this view controller
            // from.  This will match the edge we configured the
            // UIScreenEdgePanGestureRecognizer with previously.
            //
            // NOTE: We can not retrieve the value of our gesture recognizer's
            //       configured edges because prior to iOS 8.3
            //       UIScreenEdgePanGestureRecognizer would always return
            //       UIRectEdgeNone when querying its edges property.
            transitionDelegate.targetEdge = UIRectEdgeLeft;
        }
    }
}

@end
```

[Next](CustomTransitions-Swipe-AAPLSwipeTransitionInteractionController.m.md)[Previous](CustomTransitions-AAPLAppDelegate.m.md)

