---
title: CocoaSpeechSynthesisExample
apple_id: DTS10001089
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: ApplicationServices
published: '2015-07-10'
source_url: https://developer.apple.com/library/archive/samplecode/CocoaSpeechSynthesisExample/Listings/CocoaSpeechSynthesisExample_SpeakingCharacterView_h.html
archived_at: '2026-07-18T03:03:47.057661Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CocoaSpeechSynthesisExample](CocoaSpeechSynthesisExample.md)


[Next](CocoaSpeechSynthesisExample-SpeakingTextWindow.h.md)[Previous](LICENSE.txt.md)

# CocoaSpeechSynthesisExample/SpeakingCharacterView.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The custom view holding the speaking character.
 */

@import Cocoa;

extern NSString *kCharacterExpressionIdentifierSleep;
extern NSString *kCharacterExpressionIdentifierIdle;

@interface SpeakingCharacterView : NSView

- (void)setExpressionForPhoneme:(NSNumber *)phoneme;
- (void)setExpression:(NSString *)expression;

@end
```

[Next](CocoaSpeechSynthesisExample-SpeakingTextWindow.h.md)[Previous](LICENSE.txt.md)

