---
title: UnwindSegue
apple_id: DTS40013644
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2018-03-15'
source_url: https://developer.apple.com/library/archive/samplecode/UnwindSegue/Listings/CustomUnwindSegue_QuizContainerRootViewControllerSegue_m.html
archived_at: '2026-07-18T03:27:36.344114Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [UnwindSegue](UnwindSegue.md)


[Next](CustomUnwindSegue-AppDelegate.m.md)[Previous](CustomUnwindSegue-main.m.md)

# CustomUnwindSegue/QuizContainerRootViewControllerSegue.m

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Custom segue for setting the root view controller of a
  QuizContainerViewController.
 */

#import "QuizContainerRootViewControllerSegue.h"
#import "QuizContainerViewController.h"
#import "Quiz.h"

@implementation QuizContainerRootViewControllerSegue

//| ----------------------------------------------------------------------------
//  Replaces the viewControllers array of the sourceViewController (which must 
//  be a QuizContainerViewController) with an array containing only the
//  destinationViewController.  Visually, it causes the
//  QuizContainerViewController to immediately display the
//  destinationViewController with no animated transition.
//
- (void)perform
{
    QuizContainerViewController *containerVC = (QuizContainerViewController*)self.sourceViewController;

    NSArray *viewControllers = @[self.destinationViewController];

    // For our custom segue we can set the quiz here
    // as the destinationViewController is now instantiated
    [Quiz setQuizOnQuestionViewController:(QuestionViewController *)self.destinationViewController];

    containerVC.viewControllers = viewControllers;
}

@end
```

[Next](CustomUnwindSegue-AppDelegate.m.md)[Previous](CustomUnwindSegue-main.m.md)

