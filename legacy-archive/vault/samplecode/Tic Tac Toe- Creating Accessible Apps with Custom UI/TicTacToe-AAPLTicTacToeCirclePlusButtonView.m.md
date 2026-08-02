---
title: 'Tic Tac Toe: Creating Accessible Apps with Custom UI'
apple_id: TP40014589
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2016-02-18'
source_url: https://developer.apple.com/library/archive/samplecode/AccessibleTicTacToe/Listings/TicTacToe_AAPLTicTacToeCirclePlusButtonView_m.html
archived_at: '2026-07-18T03:00:40.165349Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Tic Tac Toe: Creating Accessible Apps with Custom UI](Tic%20Tac%20Toe-%20Creating%20Accessible%20Apps%20with%20Custom%20UI.md)


[Next](TicTacToe-AAPLTicTacToeGame.h.md)[Previous](TicTacToe-AAPLTicTacToeBoard.h.md)

# TicTacToe/AAPLTicTacToeCirclePlusButtonView.m

```objc
/*

 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 NSButton subclass demonstrating accessibility provided by AppKit.

 */

#import "AAPLTicTacToeCirclePlusButtonView.h"

@implementation AAPLTicTacToeCirclePlusButtonView

- (void)drawRect:(NSRect)dirtyRect
{
    [super drawRect:dirtyRect];

    NSPoint centerPoint = self.centerPoint;

    [NSBezierPath strokeLineFromPoint:NSMakePoint(2 * self.inset, centerPoint.y)
                              toPoint:NSMakePoint(2 * self.radius, centerPoint.y)];

    [NSBezierPath strokeLineFromPoint:NSMakePoint(centerPoint.x, 2 * self.inset)
                              toPoint:NSMakePoint(centerPoint.x, 2 * self.radius)];

}

@end
```

[Next](TicTacToe-AAPLTicTacToeGame.h.md)[Previous](TicTacToe-AAPLTicTacToeBoard.h.md)

