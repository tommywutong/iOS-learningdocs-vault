---
title: 'Tic Tac Toe: Creating Accessible Apps with Custom UI'
apple_id: TP40014589
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2016-02-18'
source_url: https://developer.apple.com/library/archive/samplecode/AccessibleTicTacToe/Listings/TicTacToe_AAPLTicTacToeAIEngine_m.html
archived_at: '2026-07-18T03:00:39.441211Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Tic Tac Toe: Creating Accessible Apps with Custom UI](Tic%20Tac%20Toe-%20Creating%20Accessible%20Apps%20with%20Custom%20UI.md)


[Next](TicTacToe-AAPLAppDelegate.h.md)[Previous](TicTacToe-AAPLTicTacToeBoardViewDelegate.h.md)

# TicTacToe/AAPLTicTacToeAIEngine.m

```objc
/*

 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 AI engine that calculates a move for the computer opponent from the current board state.

 */

#import "AAPLTicTacToeAIEngine.h"

@implementation AAPLTicTacToeAIEngine

- (instancetype)init
{
    self = [super init];

    if ( self != nil )
    {
        _difficulty = 5;
    }

    return self;
}

- (NSPoint)moveForBoard:(AAPLTicTacToeBoard *)board
{
    // pick a random open location

    NSPoint move = NSZeroPoint;

    if ( !board.isFull )
    {
        int row;
        int column;
        do
        {
            row = arc4random() % board.numRows;
            column = arc4random() % board.numColumns;
        }
        while ( ![board squareAtRow:row column:column].isEmpty );

        move = NSMakePoint(row, column);
    }

    return move;
}

@end
```

[Next](TicTacToe-AAPLAppDelegate.h.md)[Previous](TicTacToe-AAPLTicTacToeBoardViewDelegate.h.md)

