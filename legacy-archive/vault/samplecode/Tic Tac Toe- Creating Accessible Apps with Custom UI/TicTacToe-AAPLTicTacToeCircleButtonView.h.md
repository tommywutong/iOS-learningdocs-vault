---
title: 'Tic Tac Toe: Creating Accessible Apps with Custom UI'
apple_id: TP40014589
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2016-02-18'
source_url: https://developer.apple.com/library/archive/samplecode/AccessibleTicTacToe/Listings/TicTacToe_AAPLTicTacToeCircleButtonView_h.html
archived_at: '2026-07-18T03:00:39.934251Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Tic Tac Toe: Creating Accessible Apps with Custom UI](Tic%20Tac%20Toe-%20Creating%20Accessible%20Apps%20with%20Custom%20UI.md)


[Next](TicTacToe-AAPLTicTacToeSquare.m.md)[Previous](TicTacToe-AAPLTicTacToeCheckboxView.m.md)

# TicTacToe/AAPLTicTacToeCircleButtonView.h

```objc
/*

 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 NSButton subclass demonstrating accessibility provided by AppKit.

 */

@import Cocoa;

IB_DESIGNABLE
@interface AAPLTicTacToeCircleButtonView : NSButton

@property (nonatomic, readonly) CGFloat lineWidth;
@property (nonatomic, readonly) NSColor *color;
@property (nonatomic, readonly) NSColor *backgroundColor;
@property (nonatomic, readonly) NSColor *backgroundDepressedColor;
@property (nonatomic, readonly) CGFloat inset;

@property (NS_NONATOMIC_IOSONLY, readonly) NSPoint centerPoint;
@property (NS_NONATOMIC_IOSONLY, readonly) CGFloat radius;

@end
```

[Next](TicTacToe-AAPLTicTacToeSquare.m.md)[Previous](TicTacToe-AAPLTicTacToeCheckboxView.m.md)

