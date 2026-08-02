---
title: 'FourInARow: Using the GameplayKit Minmax Strategist for Opponent AI'
apple_id: TP40016142
resource_type: Sample Code
platform: iOS
topic: General
technology: GameplayKit
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/samplecode/FourInARow/Listings/FourInARowTests_FourInARowTests_m.html
archived_at: '2026-07-18T03:08:51.264832Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [FourInARow: Using the GameplayKit Minmax Strategist for Opponent AI](FourInARow-%20Using%20the%20GameplayKit%20Minmax%20Strategist%20for%20Opponent%20AI.md)


[Next](README.md.md)[Previous](FourInARow-AAPLViewController.m.md)

# FourInARowTests/FourInARowTests.m

```objc
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This file contains tests for board logic.
*/

@import UIKit;
@import XCTest;

#import "AAPLBoard.h"

@interface FourInARowTests : XCTestCase
@end

@implementation FourInARowTests

- (void)testHorizontalWin1 {
    AAPLBoard *board = [[AAPLBoard alloc] init];
    [board addChip:AAPLChipRed   inColumn:0];
    [board addChip:AAPLChipBlack inColumn:0];
    [board addChip:AAPLChipRed   inColumn:1];
    [board addChip:AAPLChipBlack inColumn:1];
    [board addChip:AAPLChipRed   inColumn:2];
    [board addChip:AAPLChipBlack inColumn:2];
    [board addChip:AAPLChipRed   inColumn:3];

    XCTAssertEqualObjects(board.debugDescription, @" . . . . . . \n . . . . . . \n . . . . . . \n . . . . . . \nO.O.O. . . . \nX.X.X.X. . . ");

    XCTAssert([board isWinForPlayer:[AAPLPlayer redPlayer]]);
}

- (void)testHorizontalWin2 {
    AAPLBoard *board = [[AAPLBoard alloc] init];
    [board addChip:AAPLChipRed   inColumn:6];
    [board addChip:AAPLChipBlack inColumn:5];
    [board addChip:AAPLChipRed   inColumn:4];
    [board addChip:AAPLChipBlack inColumn:3];
    [board addChip:AAPLChipRed   inColumn:2];
    [board addChip:AAPLChipBlack inColumn:3];
    [board addChip:AAPLChipRed   inColumn:0];
    [board addChip:AAPLChipBlack inColumn:4];
    [board addChip:AAPLChipRed   inColumn:0];
    [board addChip:AAPLChipBlack inColumn:5];
    [board addChip:AAPLChipRed   inColumn:0];
    [board addChip:AAPLChipBlack inColumn:6];

    XCTAssertEqualObjects(board.debugDescription, @" . . . . . . \n . . . . . . \n . . . . . . \nX. . . . . . \nX. . .O.O.O.O\nX. .X.O.X.O.X");

    XCTAssert([board isWinForPlayer:[AAPLPlayer blackPlayer]]);
}

- (void)testVerticalWin1 {
    AAPLBoard *board = [[AAPLBoard alloc] init];
    [board addChip:AAPLChipRed   inColumn:0];
    [board addChip:AAPLChipBlack inColumn:5];
    [board addChip:AAPLChipRed   inColumn:0];
    [board addChip:AAPLChipBlack inColumn:3];
    [board addChip:AAPLChipRed   inColumn:0];
    [board addChip:AAPLChipBlack inColumn:3];
    [board addChip:AAPLChipRed   inColumn:0];

    XCTAssertEqualObjects(board.debugDescription, @" . . . . . . \n . . . . . . \nX. . . . . . \nX. . . . . . \nX. . .O. . . \nX. . .O. .O. ");

    XCTAssert([board isWinForPlayer:[AAPLPlayer redPlayer]]);
}

- (void)testVerticalWin2 {
    AAPLBoard *board = [[AAPLBoard alloc] init];
    [board addChip:AAPLChipRed   inColumn:6];
    [board addChip:AAPLChipBlack inColumn:5];
    [board addChip:AAPLChipRed   inColumn:4];
    [board addChip:AAPLChipBlack inColumn:3];
    [board addChip:AAPLChipRed   inColumn:2];
    [board addChip:AAPLChipBlack inColumn:3];
    [board addChip:AAPLChipRed   inColumn:0];
    [board addChip:AAPLChipBlack inColumn:3];
    [board addChip:AAPLChipRed   inColumn:0];
    [board addChip:AAPLChipBlack inColumn:3];

    XCTAssertEqualObjects(board.debugDescription, @" . . . . . . \n . . . . . . \n . . .O. . . \n . . .O. . . \nX. . .O. . . \nX. .X.O.X.O.X");

    XCTAssert([board isWinForPlayer:[AAPLPlayer blackPlayer]]);
}

- (AAPLBoard *)diagonalWinBase {
    AAPLBoard *board = [[AAPLBoard alloc] init];
    [board addChip:AAPLChipRed   inColumn:0];
    [board addChip:AAPLChipBlack inColumn:1];
    [board addChip:AAPLChipRed   inColumn:2];
    [board addChip:AAPLChipBlack inColumn:3];
    [board addChip:AAPLChipRed   inColumn:1];
    [board addChip:AAPLChipBlack inColumn:2];
    [board addChip:AAPLChipRed   inColumn:3];
    [board addChip:AAPLChipBlack inColumn:0];
    [board addChip:AAPLChipRed   inColumn:0];
    [board addChip:AAPLChipBlack inColumn:1];
    [board addChip:AAPLChipRed   inColumn:2];
    [board addChip:AAPLChipBlack inColumn:3];

    XCTAssertEqualObjects(board.debugDescription, @" . . . . . . \n . . . . . . \n . . . . . . \nX.O.X.O. . . \nO.X.O.X. . . \nX.O.X.O. . . ");

    return board;
}

- (void)testNortheastWin {
    AAPLBoard *board = [self diagonalWinBase];

    [board addChip:AAPLChipRed inColumn:3];

    XCTAssertEqualObjects(board.debugDescription, @" . . . . . . \n . . . . . . \n . . .X. . . \nX.O.X.O. . . \nO.X.O.X. . . \nX.O.X.O. . . ");

    XCTAssert([board isWinForPlayer:[AAPLPlayer redPlayer]]);
}

- (void)testSoutheastWin {
    AAPLBoard *board = [self diagonalWinBase];

    [board addChip:AAPLChipRed inColumn:4];

    [board addChip:AAPLChipBlack inColumn:0];

    XCTAssertEqualObjects(board.debugDescription, @" . . . . . . \n . . . . . . \nO. . . . . . \nX.O.X.O. . . \nO.X.O.X. . . \nX.O.X.O.X. . ");
    XCTAssert([board isWinForPlayer:[AAPLPlayer blackPlayer]]);
}

- (void)testFull {
    AAPLBoard *board = [[AAPLBoard alloc] init];
    for (NSInteger column = 0; column < AAPLBoard.width; column++) {
        for (NSInteger i = 0; i < AAPLBoard.height; i++) {
            [board addChip:(i % 2 + 1) inColumn:column];
        }
    }
    XCTAssert(board.isFull);
}

@end
```

[Next](README.md.md)[Previous](FourInARow-AAPLViewController.m.md)

