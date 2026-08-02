---
title: 'Tic Tac Toe: Creating Accessible Apps with Custom UI'
apple_id: TP40014589
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2016-02-18'
source_url: https://developer.apple.com/library/archive/samplecode/AccessibleTicTacToe/Listings/TicTacToe_AAPLTicTacToeAIEngine_h.html
archived_at: '2026-07-18T03:00:39.410703Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Tic Tac Toe: Creating Accessible Apps with Custom UI](Tic%20Tac%20Toe-%20Creating%20Accessible%20Apps%20with%20Custom%20UI.md)


[Next](TicTacToe-AAPLTicTacToeSquareAccessibilityElement.h.md)[Previous](TicTacToe-AAPLTicTacToeSquare.m.md)

# TicTacToe/AAPLTicTacToeAIEngine.h

```objc
/*

 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 AI engine that calculates a move for the computer opponent from the current board state.

 */

@import Foundation;
#import "AAPLTicTacToeBoard.h"

@interface AAPLTicTacToeAIEngine : NSObject

@property (nonatomic) NSInteger difficulty;

// Returns a point whose x coordinate represents the row
// and y coordinate represents the column for the move
- (NSPoint)moveForBoard:(AAPLTicTacToeBoard *)board;

@end
```

[Next](TicTacToe-AAPLTicTacToeSquareAccessibilityElement.h.md)[Previous](TicTacToe-AAPLTicTacToeSquare.m.md)

