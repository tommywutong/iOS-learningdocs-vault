---
title: 'Tic Tac Toe: Creating Accessible Apps with Custom UI'
apple_id: TP40014589
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2016-02-18'
source_url: https://developer.apple.com/library/archive/samplecode/AccessibleTicTacToe/Listings/TicTacToe_AAPLTicTacToeBoardViewDelegate_h.html
archived_at: '2026-07-18T03:00:39.479976Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Tic Tac Toe: Creating Accessible Apps with Custom UI](Tic%20Tac%20Toe-%20Creating%20Accessible%20Apps%20with%20Custom%20UI.md)


[Next](TicTacToe-AAPLTicTacToeAIEngine.m.md)[Previous](TicTacToe-AAPLTicTacToeGame.m.md)

# TicTacToe/AAPLTicTacToeBoardViewDelegate.h

```objc
/*

 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Delegate methods for an object that can provide information about the game state.

 */

@import Foundation;
#import "AAPLTicTacToeSquare.h"

@protocol AAPLTicTacToeBoardViewDelegate <NSObject>

- (void)playSquareAtRow:(NSUInteger)row column:(NSUInteger)column;
- (AAPLTicTacToeSquare *)squareAtRow:(NSUInteger)row column:(NSUInteger)column;
- (BOOL)isGameOver;

@end
```

[Next](TicTacToe-AAPLTicTacToeAIEngine.m.md)[Previous](TicTacToe-AAPLTicTacToeGame.m.md)

