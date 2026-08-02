---
title: 'Tic Tac Toe: Creating Accessible Apps with Custom UI'
apple_id: TP40014589
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2016-02-18'
source_url: https://developer.apple.com/library/archive/samplecode/AccessibleTicTacToe/Listings/TicTacToe_AAPLTicTacToeSquareAccessibilityElement_m.html
archived_at: '2026-07-18T03:00:40.461306Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Tic Tac Toe: Creating Accessible Apps with Custom UI](Tic%20Tac%20Toe-%20Creating%20Accessible%20Apps%20with%20Custom%20UI.md)


[Next](TicTacToe-AAPLTicTacToeViewController.h.md)[Previous](TicTacToe-AAPLTicTacToeViewController.m.md)

# TicTacToe/AAPLTicTacToeSquareAccessibilityElement.m

```objc
/*

 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 An accessibility object representing a single tic tac toe piece.

 */

#import "AAPLTicTacToeSquareAccessibilityElement.h"
#import "AAPLTicTacToeSquare.h"
#import "AAPLTicTacToeBoard.h"

@implementation AAPLTicTacToeSquareAccessibilityElement

- (instancetype)initWithRow:(NSUInteger)row column:(NSUInteger)column delegate:(id <AAPLTicTacToeBoardViewDelegate>)delegate
{
    self = [super init];
    if ( self != nil )
    {
        self.row = row;
        self.column = column;
        self.delegate = delegate;
    }
    return self;
}

- (NSRect)accessibilityFrame
{
    return [super accessibilityFrame];
}

- (id)accessibilityParent
{
    return [super accessibilityParent];
}

- (NSString *)accessibilityLabel
{
    NSUInteger row = self.row;
    NSUInteger column = self.column;

    AAPLTicTacToeSquare *square = [self.delegate squareAtRow:row column:column];
    return [AAPLTicTacToeBoard descriptionForSquare:square row:row column:column];
}

- (BOOL)accessibilityPerformPress
{
    [self.delegate playSquareAtRow:self.row column:self.column];
    return YES;
}

// It is not legal to play in an occupied square or when the game is over, disable the button in these cases.
- (BOOL)isAccessibilityEnabled
{
    AAPLTicTacToeSquare *square = [self.delegate squareAtRow:self.row column:self.column];
    BOOL gameOver = [self.delegate isGameOver];

    return !gameOver && square.isEmpty;
}

@end
```

[Next](TicTacToe-AAPLTicTacToeViewController.h.md)[Previous](TicTacToe-AAPLTicTacToeViewController.m.md)

