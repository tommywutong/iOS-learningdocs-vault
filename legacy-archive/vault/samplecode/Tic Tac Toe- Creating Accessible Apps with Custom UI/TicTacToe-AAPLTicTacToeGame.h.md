---
title: 'Tic Tac Toe: Creating Accessible Apps with Custom UI'
apple_id: TP40014589
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2016-02-18'
source_url: https://developer.apple.com/library/archive/samplecode/AccessibleTicTacToe/Listings/TicTacToe_AAPLTicTacToeGame_h.html
archived_at: '2026-07-18T03:00:40.212795Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Tic Tac Toe: Creating Accessible Apps with Custom UI](Tic%20Tac%20Toe-%20Creating%20Accessible%20Apps%20with%20Custom%20UI.md)


[Next](TicTacToe-AAPLTicTacToeCirclePlusButtonView.h.md)[Previous](TicTacToe-AAPLTicTacToeCirclePlusButtonView.m.md)

# TicTacToe/AAPLTicTacToeGame.h

```objc
/*

 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Game state class encapsulates the current board state, player turn, and game rules (e.g. win conditions, playing a square).

 */

@import Foundation;
#import "AAPLTicTacToeBoard.h"

typedef NS_ENUM(NSUInteger, AAPLTicTacToeGameState)
{
    AAPLTicTacToeGameStateXTurn,
    AAPLTicTacToeGameStateOTurn,
    AAPLTicTacToeGameStateXWin,
    AAPLTicTacToeGameStateOWin,
    AAPLTicTacToeGameStateTie
};

typedef NS_ENUM(NSUInteger, AAPLTicTacToeGameWinType)
{
    AAPLTicTacToeGameWinTypeNone,
    AAPLTicTacToeGameWinTypeRow,
    AAPLTicTacToeGameWinTypeColumn,
    AAPLTicTacToeGameWinTypeTopLeftDiagonal,
    AAPLTicTacToeGameWinTypeTopRightDiagonal,
};

@interface AAPLTicTacToeGame : NSObject

@property (nonatomic, strong, readonly) AAPLTicTacToeBoard *board;
@property (nonatomic, readonly) AAPLTicTacToeGameState state;
@property (nonatomic, readonly) AAPLTicTacToeGameWinType winType;
@property (nonatomic, readonly) NSUInteger winningRow;
@property (nonatomic, readonly) NSUInteger winningColumn;

- (AAPLTicTacToeSquare *)playSquareAtRow:(NSUInteger)row column:(NSUInteger)column;
- (void)reset;

@end
```

[Next](TicTacToe-AAPLTicTacToeCirclePlusButtonView.h.md)[Previous](TicTacToe-AAPLTicTacToeCirclePlusButtonView.m.md)

