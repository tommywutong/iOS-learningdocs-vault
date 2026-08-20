---
title: 'Tic Tac Toe: Creating Accessible Apps with Custom UI'
apple_id: TP40014589
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2016-02-18'
source_url: https://developer.apple.com/library/archive/samplecode/AccessibleTicTacToe/Listings/TicTacToe_AAPLTicTacToeCheckboxView_h.html
archived_at: '2026-07-18T03:00:39.835422Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Tic Tac Toe: Creating Accessible Apps with Custom UI](Tic%20Tac%20Toe-%20Creating%20Accessible%20Apps%20with%20Custom%20UI.md)


[Next](TicTacToe-AAPLTicTacToeViewController.m.md)[Previous](TicTacToe-AAPLTicTacToeBoardView.m.md)

# TicTacToe/AAPLTicTacToeCheckboxView.h

```objc
/*

 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 An example demonstrating adding accessibility to an NSView subclass that behaves like a checkbox by implementing the NSAccessibilityCheckBox protocol.

 */

@import Cocoa;

@protocol AAPLTicTacToeCheckboxDelegate <NSObject>
- (void)checkboxCheckedStateChanged:(id)sender;
@end

IB_DESIGNABLE
@interface AAPLTicTacToeCheckboxView : NSView <NSAccessibilityCheckBox>

@property (nonatomic, readonly) BOOL checked;
@property (nonatomic, weak) id <AAPLTicTacToeCheckboxDelegate> delegate;

@end
```

[Next](TicTacToe-AAPLTicTacToeViewController.m.md)[Previous](TicTacToe-AAPLTicTacToeBoardView.m.md)

