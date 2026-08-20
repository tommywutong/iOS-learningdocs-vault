---
title: 'Tic Tac Toe: Creating Accessible Apps with Custom UI'
apple_id: TP40014589
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2016-02-18'
source_url: https://developer.apple.com/library/archive/samplecode/AccessibleTicTacToe/Listings/TicTacToe_AAPLTicTacToeBoardView_h.html
archived_at: '2026-07-18T03:00:39.521299Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Tic Tac Toe: Creating Accessible Apps with Custom UI](Tic%20Tac%20Toe-%20Creating%20Accessible%20Apps%20with%20Custom%20UI.md)


[Next](TicTacToe-AAPLTicTacToeCircleMinusButtonView.m.md)[Previous](TicTacToe-AAPLTicTacToeSquare.h.md)

# TicTacToe/AAPLTicTacToeBoardView.h

```objc
/*

 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 An example demonstrating adding accessibility to an NSView subclass that behaves like a group by implementing the NSAccessibilityGroup protocol
  and using NSAccessibilityElement to represent each of the items the view draws.

 */

@import Cocoa;
#import "AAPLTicTacToeGame.h"
#import "AAPLTicTacToeBoardViewDelegate.h"

IB_DESIGNABLE
@interface AAPLTicTacToeBoardView : NSView <NSAccessibilityGroup>

@property (nonatomic, weak) id <AAPLTicTacToeBoardViewDelegate> delegate;
@property (nonatomic, strong) AAPLTicTacToeGame *game;

@end
```

[Next](TicTacToe-AAPLTicTacToeCircleMinusButtonView.m.md)[Previous](TicTacToe-AAPLTicTacToeSquare.h.md)

