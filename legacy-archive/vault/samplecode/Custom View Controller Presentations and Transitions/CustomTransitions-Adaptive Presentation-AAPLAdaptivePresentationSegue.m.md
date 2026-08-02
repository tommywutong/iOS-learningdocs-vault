---
title: Custom View Controller Presentations and Transitions
apple_id: TP40015158
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: UIKit
published: '2016-01-28'
source_url: https://developer.apple.com/library/archive/samplecode/CustomTransitions/Listings/CustomTransitions_Adaptive_Presentation_AAPLAdaptivePresentationSegue_m.html
archived_at: '2026-07-18T03:05:41.467981Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Custom View Controller Presentations and Transitions](Custom%20View%20Controller%20Presentations%20and%20Transitions.md)


[Next](CustomTransitions-Adaptive%20Presentation-AAPLAdaptivePresentationController.m.md)[Previous](CustomTransitions-Adaptive%20Presentation-AAPLAdaptivePresentationFirstViewControl-2.md)

# CustomTransitions/Adaptive Presentation/AAPLAdaptivePresentationSegue.m

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 */

#import "AAPLAdaptivePresentationSegue.h"
#import "AAPLAdaptivePresentationController.h"

@implementation AAPLAdaptivePresentationSegue

//| ----------------------------------------------------------------------------
- (void)perform
{
    UIViewController *sourceViewController = self.destinationViewController;
    UIViewController *destinationViewController = self.destinationViewController;

    // For presentations which will use a custom presentation controller,
    // it is possible for that presentation controller to also be the
    // transitioningDelegate.
    //
    // transitioningDelegate does not hold a strong reference to its
    // destination object.  To prevent presentationController from being
    // released prior to calling -presentViewController:animated:completion:
    // the NS_VALID_UNTIL_END_OF_SCOPE attribute is appended to the declaration.
    AAPLAdaptivePresentationController *presentationController NS_VALID_UNTIL_END_OF_SCOPE;

    presentationController = [[AAPLAdaptivePresentationController alloc] initWithPresentedViewController:destinationViewController presentingViewController:sourceViewController];

    destinationViewController.transitioningDelegate = presentationController;

    [self.sourceViewController presentViewController:destinationViewController animated:YES completion:NULL];
}

@end
```

[Next](CustomTransitions-Adaptive%20Presentation-AAPLAdaptivePresentationController.m.md)[Previous](CustomTransitions-Adaptive%20Presentation-AAPLAdaptivePresentationFirstViewControl-2.md)

