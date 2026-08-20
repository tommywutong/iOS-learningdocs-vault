---
title: UnwindSegue
apple_id: DTS40013644
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2018-03-15'
source_url: https://developer.apple.com/library/archive/samplecode/UnwindSegue/Listings/Shared_ResultsViewController_m.html
archived_at: '2026-07-18T03:27:37.106730Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [UnwindSegue](UnwindSegue.md)


[Next](Shared-Question.h.md)[Previous](Shared-Quiz.h.md)

# Shared/ResultsViewController.m

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 View controller for the results screen, including the quiz score.
  From this view controller, the user can restart the quiz or return to the
  main menu.
 */

#import "ResultsViewController.h"
#import "Quiz.h"

@interface ResultsViewController ()
//! Table view cell that displays the user's percentage qyuiz score.
@property (nonatomic, weak) IBOutlet UITableViewCell *resultsCell;
@end


@implementation ResultsViewController

//| ----------------------------------------------------------------------------
- (void)viewDidLoad
{
    [super viewDidLoad];

    self.navigationItem.hidesBackButton = YES;
}


//| ----------------------------------------------------------------------------
- (void)viewWillAppear:(BOOL)animated
{
    [super viewWillAppear:animated];

    self.resultsCell.textLabel.text = [NSString stringWithFormat:@"You answered %lu of %lu questions correctly for a score of %.0f%%!",
                                       (unsigned long)self.currentQuiz.correctlyAnsweredQuestions,
                                       (unsigned long)self.currentQuiz.totalQuestions,
                                       self.currentQuiz.percentageScore * 100];
}

@end
```

[Next](Shared-Question.h.md)[Previous](Shared-Quiz.h.md)

