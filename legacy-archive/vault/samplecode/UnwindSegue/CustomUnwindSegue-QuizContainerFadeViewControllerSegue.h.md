---
title: UnwindSegue
apple_id: DTS40013644
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2018-03-15'
source_url: https://developer.apple.com/library/archive/samplecode/UnwindSegue/Listings/CustomUnwindSegue_QuizContainerFadeViewControllerSegue_h.html
archived_at: '2026-07-18T03:27:36.229109Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [UnwindSegue](UnwindSegue.md)


[Next](CustomUnwindSegue-QuizContainerViewController.h.md)[Previous](CustomUnwindSegue-QuizContainerRootViewControllerSegue.h.md)

# CustomUnwindSegue/QuizContainerFadeViewControllerSegue.h

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Custom segue for pushing new view controllers onto the
  navigation stack of a QuizContainerViewController.
 */

@import UIKit;

@interface QuizContainerFadeViewControllerSegue : UIStoryboardSegue

//! If the value of this property is YES, the destinationViewController will
//! be pushed onto the navigation stack (equivalent to calling
//! -pushViewController:.  If the value of this property is NO, the
//! navigation stack is popped until the destinationViewController is the top
//! view controller (equivalent to calling -popToViewController:).
@property (nonatomic) BOOL unwind;

@end
```

[Next](CustomUnwindSegue-QuizContainerViewController.h.md)[Previous](CustomUnwindSegue-QuizContainerRootViewControllerSegue.h.md)

