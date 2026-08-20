---
title: Custom View Controller Presentations and Transitions
apple_id: TP40015158
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: UIKit
published: '2016-01-28'
source_url: https://developer.apple.com/library/archive/samplecode/CustomTransitions/Listings/CustomTransitions_Custom_Presentation_AAPLCustomPresentationFirstViewController_m.html
archived_at: '2026-07-18T03:05:42.186390Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Custom View Controller Presentations and Transitions](Custom%20View%20Controller%20Presentations%20and%20Transitions.md)


[Next](CustomTransitions-Custom%20Presentation-AAPLCustomPresentationController.m.md)[Previous](CustomTransitions-Custom%20Presentation-AAPLCustomPresentationController.h.md)

# CustomTransitions/Custom Presentation/AAPLCustomPresentationFirstViewController.m

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The initial view controller for the Custom Presentation demo.
 */

#import "AAPLCustomPresentationFirstViewController.h"
#import "AAPLCustomPresentationController.h"

@implementation AAPLCustomPresentationFirstViewController

#pragma mark -
#pragma mark Presentation

//| ----------------------------------------------------------------------------
- (IBAction)buttonAction:(UIButton*)sender
{
    UIViewController *secondViewController = [self.storyboard instantiateViewControllerWithIdentifier:@"SecondViewController"];

    // For presentations which will use a custom presentation controller,
    // it is possible for that presentation controller to also be the
    // transitioningDelegate.  This avoids introducing another object
    // or implementing <UIViewControllerTransitioningDelegate> in the
    // source view controller.
    //
    // transitioningDelegate does not hold a strong reference to its
    // destination object.  To prevent presentationController from being
    // released prior to calling -presentViewController:animated:completion:
    // the NS_VALID_UNTIL_END_OF_SCOPE attribute is appended to the declaration.
    AAPLCustomPresentationController *presentationController NS_VALID_UNTIL_END_OF_SCOPE;

    presentationController = [[AAPLCustomPresentationController alloc] initWithPresentedViewController:secondViewController presentingViewController:self];

    secondViewController.transitioningDelegate = presentationController;

    [self presentViewController:secondViewController animated:YES completion:NULL];
}

@end
```

[Next](CustomTransitions-Custom%20Presentation-AAPLCustomPresentationController.m.md)[Previous](CustomTransitions-Custom%20Presentation-AAPLCustomPresentationController.h.md)

