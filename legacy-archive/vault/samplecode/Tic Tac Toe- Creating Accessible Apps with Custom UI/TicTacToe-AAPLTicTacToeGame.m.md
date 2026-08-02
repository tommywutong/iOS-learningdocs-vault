---
title: 'Tic Tac Toe: Creating Accessible Apps with Custom UI'
apple_id: TP40014589
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2016-02-18'
source_url: https://developer.apple.com/library/archive/samplecode/AccessibleTicTacToe/Listings/TicTacToe_AAPLTicTacToeGame_m.html
archived_at: '2026-07-18T03:00:40.265339Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Tic Tac Toe: Creating Accessible Apps with Custom UI](Tic%20Tac%20Toe-%20Creating%20Accessible%20Apps%20with%20Custom%20UI.md)


[Next](TicTacToe-AAPLTicTacToeBoardViewDelegate.h.md)[Previous](TicTacToe-AAPLTicTacToeSquareAccessibilityElement.h.md)

# TicTacToe/AAPLTicTacToeGame.m

```objc
/*

 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Game state class encapsulates the current board state, player turn, and game rules (e.g. win conditions, piece placement).

 */

#import "AAPLTicTacToeGame.h"

@interface AAPLTicTacToeGame ()

@property (nonatomic, strong) AAPLTicTacToeBoard *board;
@property (nonatomic) AAPLTicTacToeGameState state;
@property (nonatomic) AAPLTicTacToeGameWinType winType;

@property (nonatomic) NSUInteger winningRow;
@property (nonatomic) NSUInteger winningColumn;

@end

@implementation AAPLTicTacToeGame

- (AAPLTicTacToeSquare *)winner:(AAPLTicTacToeBoard *)board
{
    AAPLTicTacToeSquare *firstSquare;
    AAPLTicTacToeSquare *square;

    NSInteger numRows = board.numRows;
    NSInteger numColumns = board.numColumns;

    // check rows
    for ( NSUInteger row = 0; row < numRows; row++ )
    {
        firstSquare = [board squareAtRow:row column:0];
        NSUInteger column;
        for ( column = 0; column < numColumns; column++ )
        {
            square = [board squareAtRow:row column:column];

            if ( ![square sameTypeAs:firstSquare] || square.isEmpty )
            {
                break;
            }
        }

        if ( column == numColumns )
        {
            self.winType = AAPLTicTacToeGameWinTypeRow;
            self.winningRow = row;
            return square;
        }
    }

    // check columns
    for ( NSUInteger column = 0; column < numColumns; column++ )
    {
        firstSquare = [board squareAtRow:0 column:column];

        NSUInteger row;
        for ( row = 0; row < numRows; row++ )
        {
            square = [board squareAtRow:row column:column];

            if ( ![square sameTypeAs:firstSquare] || square.isEmpty )
            {
                break;
            }
        }

        if ( row == numRows )
        {
            self.winType = AAPLTicTacToeGameWinTypeColumn;
            self.winningColumn = column;
            return square;
        }
    }

    // check top left diagonal
    firstSquare = [board squareAtRow:0 column:0];
    NSUInteger column;
    NSUInteger row;
    for ( column = 0, row = 0; column < numColumns && row < numRows; column++, row++ )
    {
        square = [board squareAtRow:row column:column];

        if ( ![square sameTypeAs:firstSquare] || square.isEmpty )
        {
            break;
        }
    }

    if ( column == numColumns || row == numRows )
    {
        self.winType = AAPLTicTacToeGameWinTypeTopLeftDiagonal;
        return square;
    }

    // check top right diagonal
    firstSquare = [board squareAtRow:0 column:numColumns - 1];
    for ( column = 0, row = 0; column < numColumns && row < numRows; column++, row++ )
    {
        square = [board squareAtRow:row column:numColumns - column - 1];

        if ( ![square sameTypeAs:firstSquare] || square.isEmpty )
        {
            break;
        }
    }

    if ( column == numColumns || row == numRows )
    {
        self.winType = AAPLTicTacToeGameWinTypeTopRightDiagonal;
        return square;
    }

    return [AAPLTicTacToeSquare Empty];
}

- (instancetype)init
{
    self = [super init];

    if ( self != nil )
    {
        self.board = [AAPLTicTacToeBoard new];
        [self reset];
    }

    return self;
}

- (AAPLTicTacToeSquare *)playSquareAtRow:(NSUInteger)row column:(NSUInteger)column
{
    AAPLTicTacToeBoard *board = self.board;
    AAPLTicTacToeSquare *square = [board squareAtRow:row column:column];
    AAPLTicTacToeGameState state = self.state;

    if ( square == nil || !square.isEmpty )
    {
        return NO;
    }

    if ( state == AAPLTicTacToeGameStateXTurn )
    {
        square.type = AAPLTicTacToeSquareTypeX;
    }
    else if ( state == AAPLTicTacToeGameStateOTurn )
    {
        square.type = AAPLTicTacToeSquareTypeO;
    }

    AAPLTicTacToeSquare *winner = [self winner:board];
    if ( winner.isX )
    {
        state = AAPLTicTacToeGameStateXWin;
    }
    else if ( winner.isO )
    {
        state = AAPLTicTacToeGameStateOWin;
    }
    else if ( winner.isEmpty )
    {
        if ( [board isFull] )
        {
            state = AAPLTicTacToeGameStateTie;
        }
        else if ( state == AAPLTicTacToeGameStateXTurn )
        {
            state = AAPLTicTacToeGameStateOTurn;
        }
        else if ( state == AAPLTicTacToeGameStateOTurn )
        {
            state = AAPLTicTacToeGameStateXTurn;
        }
    }

    self.state = state;
    return square;
}

- (void)reset
{
    [self.board reset];
    self.state = AAPLTicTacToeGameStateXTurn;
    self.winType = AAPLTicTacToeGameWinTypeNone;
    self.winningRow = 0;
    self.winningColumn = 0;
}

@end
```

[Next](TicTacToe-AAPLTicTacToeBoardViewDelegate.h.md)[Previous](TicTacToe-AAPLTicTacToeSquareAccessibilityElement.h.md)

