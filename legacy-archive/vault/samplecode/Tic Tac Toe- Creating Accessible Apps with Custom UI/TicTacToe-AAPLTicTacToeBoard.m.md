---
title: 'Tic Tac Toe: Creating Accessible Apps with Custom UI'
apple_id: TP40014589
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2016-02-18'
source_url: https://developer.apple.com/library/archive/samplecode/AccessibleTicTacToe/Listings/TicTacToe_AAPLTicTacToeBoard_m.html
archived_at: '2026-07-18T03:00:39.658212Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Tic Tac Toe: Creating Accessible Apps with Custom UI](Tic%20Tac%20Toe-%20Creating%20Accessible%20Apps%20with%20Custom%20UI.md)


[Next](TicTacToe-AAPLTicTacToeCircleMinusButtonView.h.md)[Previous](TicTacToe-AAPLTicTacToeButtonView.h.md)

# TicTacToe/AAPLTicTacToeBoard.m

```objc
/*

 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Board class encapsulates the nine grid.

 */

#import "AAPLTicTacToeBoard.h"

@interface AAPLTicTacToeBoard ()

@property (nonatomic, strong) NSArray *rows;

@end

@implementation AAPLTicTacToeBoard

+ (NSString *)descriptionForSquare:(AAPLTicTacToeSquare *)square row:(NSUInteger)row column:(NSUInteger)column
{
    NSString *location = @"";

    if ( row == 0 && column == 0)
    {
        location = NSLocalizedString(@"top left", nil);
    }
    else if ( row == 1 && column == 0 )
    {
        location = NSLocalizedString(@"left", nil);
    }
    else if ( row == 2 && column == 0 )
    {
        location = NSLocalizedString(@"bottom left", nil);
    }
    else if ( row == 0 && column == 1)
    {
        location = NSLocalizedString(@"top", nil);
    }
    else if ( row == 1 && column == 1 )
    {
        location= NSLocalizedString(@"center", nil);
    }
    else if ( row == 2 && column == 1 )
    {
        location = NSLocalizedString(@"bottom", nil);
    }
    else if ( row == 0 && column == 2 )
    {
        location = NSLocalizedString(@"top right", nil);
    }
    else if ( row == 1 && column == 2 )
    {
        location= NSLocalizedString(@"right", nil);
    }
    else if ( row == 2 && column == 2 )
    {
        location = NSLocalizedString(@"bottom right", nil);
    }

    NSString *descriptionAndLocationFormatter = NSLocalizedString(@"DescriptionAndLocationFormatter", nil);
    return [NSString stringWithFormat:descriptionAndLocationFormatter, [square description], location];
}

- (instancetype)init
{
    self = [super init];

    if ( self != nil )
    {
        NSArray *topRow = @[[AAPLTicTacToeSquare Empty], [AAPLTicTacToeSquare Empty], [AAPLTicTacToeSquare Empty]];
        NSArray *middleRow = @[[AAPLTicTacToeSquare Empty], [AAPLTicTacToeSquare Empty], [AAPLTicTacToeSquare Empty]];
        NSArray *bottomRow = @[[AAPLTicTacToeSquare Empty], [AAPLTicTacToeSquare Empty], [AAPLTicTacToeSquare Empty]];
        _rows = @[topRow, middleRow, bottomRow];
    }

    return self;
}

- (AAPLTicTacToeSquare *)squareAtRow:(NSUInteger)row column:(NSUInteger)column
{
    AAPLTicTacToeSquare *square = nil;

    if ( row < self.numRows && column < self.numColumns )
    {
        NSArray *rowArray = self.rows[row];
        square = rowArray[column];
    }

    return square;
}

- (NSArray *)squaresInRow:(NSUInteger)row
{
    return self.rows[row];
}

- (NSArray *)squaresInColumn:(NSUInteger)column
{
    NSMutableArray *columnSquares = [[NSMutableArray alloc] initWithCapacity:self.numColumns];

    for ( NSUInteger row = 0; row < self.numRows; row++ )
    {
        columnSquares[row] = self.rows[row][column];
    }

    return columnSquares;
}

- (NSUInteger)numRows
{
    return self.rows.count;
}

- (NSUInteger)numColumns
{
    NSMutableArray *firstRow = self.rows[0];
    return firstRow.count;
}

- (BOOL)isFull
{
    for ( NSUInteger row = 0; row < self.numRows; row++ )
    {
        for ( NSUInteger column = 0; column < self.numColumns; column++ )
        {
            AAPLTicTacToeSquare *square = [self squareAtRow:row column:column];
            if ( square.isEmpty )
            {
                return NO;
            }
        }
    }

    return YES;
}

- (void)reset
{
    AAPLTicTacToeSquare *square;
    for ( NSUInteger row = 0; row < self.numRows; row++ )
    {
        for ( NSUInteger column = 0; column < self.numColumns; column++ )
        {
            square = [self squareAtRow:row column:column];
            square.type = AAPLTicTacToeSquareTypeEmpty;
        }
    }
}

- (NSString *)description
{
    NSMutableString *desc = [NSMutableString new];
    AAPLTicTacToeSquare *square;

    for ( int row = 0; row < self.numRows; row++ )
    {
        for ( int column = 0; column < self.numColumns; column++ )
        {
            square = [self squareAtRow:row column:column];
            [desc appendString:[square description]];
            [desc appendString:@" "];
        }
        [desc appendString:@"\n"];
    }
    return desc;
}

@end
```

[Next](TicTacToe-AAPLTicTacToeCircleMinusButtonView.h.md)[Previous](TicTacToe-AAPLTicTacToeButtonView.h.md)

