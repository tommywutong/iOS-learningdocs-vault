---
title: 'Tic Tac Toe: Creating Accessible Apps with Custom UI'
apple_id: TP40014589
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2016-02-18'
source_url: https://developer.apple.com/library/archive/samplecode/AccessibleTicTacToe/Listings/TicTacToe_AAPLTicTacToeSquare_m.html
archived_at: '2026-07-18T03:00:40.576697Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Tic Tac Toe: Creating Accessible Apps with Custom UI](Tic%20Tac%20Toe-%20Creating%20Accessible%20Apps%20with%20Custom%20UI.md)


[Next](TicTacToe-AAPLTicTacToeAIEngine.h.md)[Previous](TicTacToe-AAPLTicTacToeCircleButtonView.h.md)

# TicTacToe/AAPLTicTacToeSquare.m

```objc
/*

 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Square class encapsulates a single square on the board.

 */

#import "AAPLTicTacToeSquare.h"

@implementation AAPLTicTacToeSquare

+ (AAPLTicTacToeSquare *)X
{
    return [[self alloc] initWithType:AAPLTicTacToeSquareTypeX];
}

+ (AAPLTicTacToeSquare *)O
{
    return [[self alloc] initWithType:AAPLTicTacToeSquareTypeO];
}

+ (AAPLTicTacToeSquare *)Empty
{
    return [[self alloc] initWithType:AAPLTicTacToeSquareTypeEmpty];
}

- (instancetype)initWithType:(AAPLTicTacToeSquareType)type
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
    return self.type == AAPLTicTacToeSquareTypeX;
}

- (BOOL)isO
{
    return self.type == AAPLTicTacToeSquareTypeO;
}

- (BOOL)isEmpty
{
    return self.type == AAPLTicTacToeSquareTypeEmpty;
}

- (void)makeX
{
    self.type = AAPLTicTacToeSquareTypeX;
}

- (void)makeO
{
    self.type = AAPLTicTacToeSquareTypeO;
}

- (void)makeEmpty
{
    self.type = AAPLTicTacToeSquareTypeEmpty;
}

- (BOOL)sameTypeAs:(AAPLTicTacToeSquare *)square
{
    return square.type == self.type;
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

[Next](TicTacToe-AAPLTicTacToeAIEngine.h.md)[Previous](TicTacToe-AAPLTicTacToeCircleButtonView.h.md)

