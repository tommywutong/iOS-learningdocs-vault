---
title: UnwindSegue
apple_id: DTS40013644
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2018-03-15'
source_url: https://developer.apple.com/library/archive/samplecode/UnwindSegue/Listings/Shared_Question_h.html
archived_at: '2026-07-18T03:27:36.861281Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [UnwindSegue](UnwindSegue.md)


[Next](Shared-Quiz.m.md)[Previous](Shared-ResultsViewController.m.md)

# Shared/Question.h

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Model class for a single question in the quiz.
 */

@import Foundation;

@interface Question : NSObject

- (instancetype)initWithQuestionDict:(NSDictionary*)questionDict NS_DESIGNATED_INITIALIZER;
- (instancetype)init NS_UNAVAILABLE;

//! The text of the question.
@property (readonly) NSString *text;
//! Possible responses to the question.
@property (readonly) NSArray *responses;
//! The index of the correct response in the responses array.
@property (readonly) NSInteger correctResponse;
//! The index of the user's selected response or NSNotFound if the user has not
//! responded to the question.
@property (readwrite) NSInteger selectedResponse;

@end
```

[Next](Shared-Quiz.m.md)[Previous](Shared-ResultsViewController.m.md)

