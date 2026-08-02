---
title: 'Tic Tac Toe: Creating Accessible Apps with Custom UI'
apple_id: TP40014589
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2016-02-18'
source_url: https://developer.apple.com/library/archive/samplecode/AccessibleTicTacToe/Listings/TicTacToe_AAPLTicTacToeSquareAccessibilityElement_h.html
archived_at: '2026-07-18T03:00:40.421294Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Tic Tac Toe: Creating Accessible Apps with Custom UI](Tic%20Tac%20Toe-%20Creating%20Accessible%20Apps%20with%20Custom%20UI.md)


[Next](TicTacToe-AAPLTicTacToeGame.m.md)[Previous](TicTacToe-AAPLTicTacToeAIEngine.h.md)

# TicTacToe/AAPLTicTacToeSquareAccessibilityElement.h

```objc
/*

 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 An accessibility object representing a single tic tac toe square.

 */

@import Cocoa;
#import "AAPLTicTacToeBoardViewDelegate.h"

@interface AAPLTicTacToeSquareAccessibilityElement : NSAccessibilityElement <NSAccessibilityButton>

- (instancetype)init NS_UNAVAILABLE;

- (instancetype)initWithRow:(NSUInteger)row column:(NSUInteger)column delegate:(id <AAPLTicTacToeBoardViewDelegate>)delegate NS_DESIGNATED_INITIALIZER;

@property (nonatomic, weak) id <AAPLTicTacToeBoardViewDelegate> delegate;
@property (nonatomic) NSUInteger row;
@property (nonatomic) NSUInteger column;

@end
```

[Next](TicTacToe-AAPLTicTacToeGame.m.md)[Previous](TicTacToe-AAPLTicTacToeAIEngine.h.md)

