---
title: UnwindSegue
apple_id: DTS40013644
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2018-03-15'
source_url: https://developer.apple.com/library/archive/samplecode/UnwindSegue/Listings/CustomUnwindSegue_QuizContainerFadeViewControllerSegue_m.html
archived_at: '2026-07-18T03:27:36.271303Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [UnwindSegue](UnwindSegue.md)


[Next](CustomUnwindSegue-QuizContainerRootViewControllerSegue.h.md)[Previous](CustomUnwindSegue-QuizContainerViewController.m.md)

# CustomUnwindSegue/QuizContainerFadeViewControllerSegue.m

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Custom segue for pushing new view controllers onto the
  navigation stack of a QuizContainerViewController.
 */

#import "QuizContainerFadeViewControllerSegue.h"
#import "QuizContainerViewController.h"


@implementation QuizContainerFadeViewControllerSegue

//| ----------------------------------------------------------------------------
//  This segue does not implement the transition animation.  Instead, it calls
//  -pushViewController: or -popToViewController: of the parent
//  QuizContainerViewController, which actually performs the transition.
//
- (void)perform
{
    if (self.unwind)
    {
        // Access the destinationViewController's parent to aquire a reference
        // to QuizContainerViewController.  The sourceViewController may not be
        // a direct child of the QuizContainerViewController in which case its
        // parent would not be a reference to the QuizContainerViewController.
        QuizContainerViewController *containerVC = (QuizContainerViewController*)(self.destinationViewController).parentViewController;
        [containerVC popToViewController:self.destinationViewController animated:YES];
    }
    else
    {
        QuizContainerViewController *containerVC = (QuizContainerViewController*)(self.sourceViewController).parentViewController;
        [containerVC pushViewController:self.destinationViewController animated:YES];
    }

}

@end
```

[Next](CustomUnwindSegue-QuizContainerRootViewControllerSegue.h.md)[Previous](CustomUnwindSegue-QuizContainerViewController.m.md)

