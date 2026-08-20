---
title: UnwindSegue
apple_id: DTS40013644
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2018-03-15'
source_url: https://developer.apple.com/library/archive/samplecode/UnwindSegue/Listings/Shared_QuestionViewController_h.html
archived_at: '2026-07-18T03:27:36.739590Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [UnwindSegue](UnwindSegue.md)


[Next](Shared-ResultsViewController.h.md)[Previous](Shared-Question.m.md)

# Shared/QuestionViewController.h

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 View controller for displaying a Question.
 */

@import UIKit;

@class Quiz;

@interface QuestionViewController : UITableViewController

//! The Quiz to source the question from.
@property (strong) Quiz *currentQuiz;
//! Index of the Question in the Quiz to display.
@property (readwrite) NSUInteger questionIndex;

@end
```

[Next](Shared-ResultsViewController.h.md)[Previous](Shared-Question.m.md)

