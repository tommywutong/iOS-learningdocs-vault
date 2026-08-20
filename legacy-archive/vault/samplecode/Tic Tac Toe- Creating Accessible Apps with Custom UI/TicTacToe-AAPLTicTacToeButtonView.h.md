---
title: 'Tic Tac Toe: Creating Accessible Apps with Custom UI'
apple_id: TP40014589
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2016-02-18'
source_url: https://developer.apple.com/library/archive/samplecode/AccessibleTicTacToe/Listings/TicTacToe_AAPLTicTacToeButtonView_h.html
archived_at: '2026-07-18T03:00:39.728422Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Tic Tac Toe: Creating Accessible Apps with Custom UI](Tic%20Tac%20Toe-%20Creating%20Accessible%20Apps%20with%20Custom%20UI.md)


[Next](TicTacToe-AAPLTicTacToeBoard.m.md)[Previous](TicTacToe-AAPLTicTacToeCirclePlusButtonView.h.md)

# TicTacToe/AAPLTicTacToeButtonView.h

```objc
/*

 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 An example demonstrating adding accessibility to an NSView subclass that behaves like a button by implementing the NSAccessibilityButton protocol.

 */

@import Cocoa;

@protocol AAPLTicTacToeButtonDelegate <NSObject>
- (void)buttonPressed:(id)sender;
@end

IB_DESIGNABLE
@interface AAPLTicTacToeButtonView : NSView <NSAccessibilityButton>

@property (nonatomic, weak) id <AAPLTicTacToeButtonDelegate> delegate;

@end
```

[Next](TicTacToe-AAPLTicTacToeBoard.m.md)[Previous](TicTacToe-AAPLTicTacToeCirclePlusButtonView.h.md)

