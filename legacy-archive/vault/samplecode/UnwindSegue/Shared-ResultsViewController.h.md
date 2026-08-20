---
title: UnwindSegue
apple_id: DTS40013644
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2018-03-15'
source_url: https://developer.apple.com/library/archive/samplecode/UnwindSegue/Listings/Shared_ResultsViewController_h.html
archived_at: '2026-07-18T03:27:37.070677Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [UnwindSegue](UnwindSegue.md)


[Next](Shared-Quiz.h.md)[Previous](Shared-QuestionViewController.h.md)

# Shared/ResultsViewController.h

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 View controller for the results screen, including the quiz score.
  From this view controller, the user can restart the quiz or return to the
  main menu.
 */

@import UIKit;

@class Quiz;

@interface ResultsViewController : UITableViewController

//! The Quiz to source the results from.
@property (strong) Quiz *currentQuiz;

@end
```

[Next](Shared-Quiz.h.md)[Previous](Shared-QuestionViewController.h.md)

