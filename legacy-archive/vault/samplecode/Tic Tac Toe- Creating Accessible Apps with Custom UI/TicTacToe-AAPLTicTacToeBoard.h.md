---
title: 'Tic Tac Toe: Creating Accessible Apps with Custom UI'
apple_id: TP40014589
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2016-02-18'
source_url: https://developer.apple.com/library/archive/samplecode/AccessibleTicTacToe/Listings/TicTacToe_AAPLTicTacToeBoard_h.html
archived_at: '2026-07-18T03:00:39.615785Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Tic Tac Toe: Creating Accessible Apps with Custom UI](Tic%20Tac%20Toe-%20Creating%20Accessible%20Apps%20with%20Custom%20UI.md)


[Next](TicTacToe-AAPLTicTacToeCirclePlusButtonView.m.md)[Previous](TicTacToe-AAPLTicTacToeViewController.h.md)

# TicTacToe/AAPLTicTacToeBoard.h

```objc
/*

 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Board class encapsulates the nine grid.

 */

@import Foundation;
#import "AAPLTicTacToeSquare.h"

@interface AAPLTicTacToeBoard : NSObject

+ (NSString *)descriptionForSquare:(AAPLTicTacToeSquare *)square row:(NSUInteger)row column:(NSUInteger)column;

- (AAPLTicTacToeSquare *)squareAtRow:(NSUInteger)row column:(NSUInteger)column;
- (NSArray *)squaresInRow:(NSUInteger)row;
- (NSArray *)squaresInColumn:(NSUInteger)column;
@property (NS_NONATOMIC_IOSONLY, readonly) NSUInteger numRows;
@property (NS_NONATOMIC_IOSONLY, readonly) NSUInteger numColumns;
@property (NS_NONATOMIC_IOSONLY, getter=isFull, readonly) BOOL full;

- (void)reset;

@end
```

[Next](TicTacToe-AAPLTicTacToeCirclePlusButtonView.m.md)[Previous](TicTacToe-AAPLTicTacToeViewController.h.md)

