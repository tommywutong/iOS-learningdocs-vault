---
title: UnwindSegue
apple_id: DTS40013644
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2018-03-15'
source_url: https://developer.apple.com/library/archive/samplecode/UnwindSegue/Listings/Shared_Quiz_h.html
archived_at: '2026-07-18T03:27:36.941435Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [UnwindSegue](UnwindSegue.md)


[Next](Shared-ResultsViewController.m.md)[Previous](Shared-ResultsViewController.h.md)

# Shared/Quiz.h

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Model class for a Quiz.  Manages loading the quiz 
  data (questions, answers) from a plist file, vending questions, and recording 
  responses.
 */

@import Foundation;
#import "Question.h"

// Structure of the Questions.plist file
// Root
//  - QuestionsList (Array)
//      0 (Dictionary)
//          QuestionText (String): Text of the question.
//          AnswerText (Array): List of responses.
//              0 (String): Text of the response
//              ...
//          Answer (Number): Index in AnswerText of the correct response.
//      ...
extern NSString * const QuestionsListKey;
extern NSString * const QuestionTextKey;
extern NSString * const AnswerTextKey;
extern NSString * const AnswerKey;

@class QuestionViewController;

@interface Quiz : NSObject

- (instancetype)init NS_UNAVAILABLE;

- (Question*)objectAtIndexedSubscript:(NSInteger)idx;
- (Question*)questionAtIndex:(NSUInteger)idx;
- (void)resetQuiz;

// Set the newQuiz as the currentQuiz of the view controller.
+ (void)setQuizOnQuestionViewController:(QuestionViewController *)controller;

#pragma mark - Statistics

//! The number of questions the user has answered correctly.
@property (readonly) NSUInteger correctlyAnsweredQuestions;
//! The number of questions the user has answered.
@property (readonly) NSUInteger answeredQuestions;
//! Total questions in the quiz.
@property (readonly) NSUInteger totalQuestions;
//! Percentage of correctly answered questions of the total questions
//! answered.
@property (readonly) float percentageScore;

@end
```

[Next](Shared-ResultsViewController.m.md)[Previous](Shared-ResultsViewController.h.md)

