---
title: 'Tic Tac Toe: Creating Accessible Apps with Custom UI'
apple_id: TP40014589
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2016-02-18'
source_url: https://developer.apple.com/library/archive/samplecode/AccessibleTicTacToe/Listings/TicTacToe_AAPLTicTacToeSquare_h.html
archived_at: '2026-07-18T03:00:40.548473Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Tic Tac Toe: Creating Accessible Apps with Custom UI](Tic%20Tac%20Toe-%20Creating%20Accessible%20Apps%20with%20Custom%20UI.md)


[Next](TicTacToe-AAPLTicTacToeBoardView.h.md)[Previous](TicTacToe-AAPLTicTacToePiece.m.md)

# TicTacToe/AAPLTicTacToeSquare.h

```objc
/*

 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Square class encapsulates a single square on the board.

 */

@import Foundation;

typedef NS_ENUM (NSUInteger, AAPLTicTacToeSquareType)
{
    AAPLTicTacToeSquareTypeEmpty,
    AAPLTicTacToeSquareTypeX,
    AAPLTicTacToeSquareTypeO,
};

@interface AAPLTicTacToeSquare : NSObject

@property (nonatomic) AAPLTicTacToeSquareType type;

+ (AAPLTicTacToeSquare *)X;
+ (AAPLTicTacToeSquare *)O;
+ (AAPLTicTacToeSquare *)Empty;

@property (NS_NONATOMIC_IOSONLY, getter=isX, readonly) BOOL x;
@property (NS_NONATOMIC_IOSONLY, getter=isO, readonly) BOOL o;
@property (NS_NONATOMIC_IOSONLY, getter=isEmpty, readonly) BOOL empty;

- (BOOL)sameTypeAs:(AAPLTicTacToeSquare *)square;

@property (NS_NONATOMIC_IOSONLY, readonly, copy) NSString *description;

@end
```

[Next](TicTacToe-AAPLTicTacToeBoardView.h.md)[Previous](TicTacToe-AAPLTicTacToePiece.m.md)

