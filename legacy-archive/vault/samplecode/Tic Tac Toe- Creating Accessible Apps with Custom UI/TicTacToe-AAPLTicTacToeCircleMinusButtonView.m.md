---
title: 'Tic Tac Toe: Creating Accessible Apps with Custom UI'
apple_id: TP40014589
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2016-02-18'
source_url: https://developer.apple.com/library/archive/samplecode/AccessibleTicTacToe/Listings/TicTacToe_AAPLTicTacToeCircleMinusButtonView_m.html
archived_at: '2026-07-18T03:00:40.077813Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Tic Tac Toe: Creating Accessible Apps with Custom UI](Tic%20Tac%20Toe-%20Creating%20Accessible%20Apps%20with%20Custom%20UI.md)


[Next](TicTacToe-AAPLTicTacToeCircleButtonView.m.md)[Previous](TicTacToe-AAPLTicTacToeBoardView.h.md)

# TicTacToe/AAPLTicTacToeCircleMinusButtonView.m

```objc
/*

 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 NSButton subclass demonstrating accessibility provided by AppKit.

 */

#import "AAPLTicTacToeCircleMinusButtonView.h"

@implementation AAPLTicTacToeCircleMinusButtonView

- (void)drawRect:(NSRect)dirtyRect
{
    [super drawRect:dirtyRect];

    NSPoint centerPoint = self.centerPoint;

    [NSBezierPath strokeLineFromPoint:NSMakePoint(2 * self.inset, centerPoint.y)
                              toPoint:NSMakePoint(2 * self.radius, centerPoint.y)];
}

@end
```

[Next](TicTacToe-AAPLTicTacToeCircleButtonView.m.md)[Previous](TicTacToe-AAPLTicTacToeBoardView.h.md)

