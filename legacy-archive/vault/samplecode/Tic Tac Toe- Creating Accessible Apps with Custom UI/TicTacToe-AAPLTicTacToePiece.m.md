---
title: 'Tic Tac Toe: Creating Accessible Apps with Custom UI'
apple_id: TP40014589
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2016-02-18'
source_url: https://developer.apple.com/library/archive/samplecode/AccessibleTicTacToe/Listings/TicTacToe_AAPLTicTacToePiece_m.html
archived_at: '2026-07-18T03:00:40.355950Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Tic Tac Toe: Creating Accessible Apps with Custom UI](Tic%20Tac%20Toe-%20Creating%20Accessible%20Apps%20with%20Custom%20UI.md)


[Next](TicTacToe-AAPLTicTacToeSquare.h.md)[Previous](LICENSE.txt.md)

# TicTacToe/AAPLTicTacToePiece.m

```objc
/*

 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Piece class encapsulates a single space on the board.

 */

#import "AAPLTicTacToePiece.h"

@implementation AAPLTicTacToePiece

+ (AAPLTicTacToePiece *)X
{
    return [[self alloc] initWithType:AAPLTicTacToePieceTypeX];
}

+ (AAPLTicTacToePiece *)O
{
    return [[self alloc] initWithType:AAPLTicTacToePieceTypeO];
}

+ (AAPLTicTacToePiece *)Empty
{
    return [[self alloc] initWithType:AAPLTicTacToePieceTypeEmpty];
}

- (instancetype)initWithType:(AAPLTicTacToePieceType)type
{
    self = [super init];

    if ( self != nil )
    {
        _type = type;
    }

    return self;
}

- (BOOL)isX
{
    return self.type == AAPLTicTacToePieceTypeX;
}

- (BOOL)isO
{
    return self.type == AAPLTicTacToePieceTypeO;
}

- (BOOL)isEmpty
{
    return self.type == AAPLTicTacToePieceTypeEmpty;
}

- (void)makeX
{
    self.type = AAPLTicTacToePieceTypeX;
}

- (void)makeO
{
    self.type = AAPLTicTacToePieceTypeO;
}

- (void)makeEmpty
{
    self.type = AAPLTicTacToePieceTypeEmpty;
}

- (BOOL)sameTypeAs:(AAPLTicTacToePiece *)piece
{
    return piece.type == self.type;
}

- (NSString *)description
{
    if ( self.isX )
    {
        return NSLocalizedString(@"X", nil);
    }
    else if ( self.isO )
    {
        return NSLocalizedString(@"O", nil);
    }
    else
    {
        return  NSLocalizedString(@"empty", nil);
    }
}

@end
```

[Next](TicTacToe-AAPLTicTacToeSquare.h.md)[Previous](LICENSE.txt.md)

