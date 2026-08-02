---
title: UnwindSegue
apple_id: DTS40013644
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2018-03-15'
source_url: https://developer.apple.com/library/archive/samplecode/UnwindSegue/Listings/Shared_Question_m.html
archived_at: '2026-07-18T03:27:36.904344Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [UnwindSegue](UnwindSegue.md)


[Next](Shared-QuestionViewController.h.md)[Previous](Shared-QuestionViewController.m.md)

# Shared/Question.m

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Model class for a single question in the quiz.
 */

#import "Question.h"
#import "Quiz.h"

@implementation Question

//| ----------------------------------------------------------------------------
//! Initializes and returns a newly created Question.
//
//! @param  questionDict
//!         The dictionary from which to retrieve the data for the question.
//
- (instancetype)initWithQuestionDict:(NSDictionary*)questionDict
{
    self = [super init];
    if (self)
    {
        _text = questionDict[QuestionTextKey];
        _responses = questionDict[AnswerTextKey];
        _correctResponse = [questionDict[AnswerKey] integerValue];
        _selectedResponse = NSNotFound;
    }
    return self;
}

@end
```

[Next](Shared-QuestionViewController.h.md)[Previous](Shared-QuestionViewController.m.md)

