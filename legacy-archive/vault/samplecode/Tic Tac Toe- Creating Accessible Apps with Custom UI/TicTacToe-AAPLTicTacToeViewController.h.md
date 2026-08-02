---
title: 'Tic Tac Toe: Creating Accessible Apps with Custom UI'
apple_id: TP40014589
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2016-02-18'
source_url: https://developer.apple.com/library/archive/samplecode/AccessibleTicTacToe/Listings/TicTacToe_AAPLTicTacToeViewController_h.html
archived_at: '2026-07-18T03:00:40.655802Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Tic Tac Toe: Creating Accessible Apps with Custom UI](Tic%20Tac%20Toe-%20Creating%20Accessible%20Apps%20with%20Custom%20UI.md)


[Next](TicTacToe-AAPLTicTacToeBoard.h.md)[Previous](TicTacToe-AAPLTicTacToeSquareAccessibilityElement.m.md)

# TicTacToe/AAPLTicTacToeViewController.h

```objc
/*

 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 View controller for a tic-tac-toe game demonstrating accessible custom controls using the accessibility methods of NSControl subclasses, accessibility protocols, and NSAccessibilityElement.

 */

@import Cocoa;
#import "AAPLTicTacToeBoardView.h"
#import "AAPLTicTacToeButtonView.h"
#import "AAPLTicTacToeCircleMinusButtonView.h"
#import "AAPLTicTacToeCirclePlusButtonView.h"
#import "AAPLTicTacToeCheckboxView.h"

@interface AAPLTicTacToeViewController : NSViewController <AAPLTicTacToeButtonDelegate, AAPLTicTacToeBoardViewDelegate, AAPLTicTacToeCheckboxDelegate>

@property (weak) IBOutlet AAPLTicTacToeBoardView *boardView;
@property (weak) IBOutlet AAPLTicTacToeButtonView *resetGameButton;
@property (weak) IBOutlet NSTextField *statusText;
@property (weak) IBOutlet NSTextField *difficultyText;
@property (weak) IBOutlet AAPLTicTacToeCheckboxView *playAICheckbox;
@property (weak) IBOutlet AAPLTicTacToeCircleMinusButtonView *decreaseDifficultyButton;
@property (weak) IBOutlet AAPLTicTacToeCirclePlusButtonView *increaseDifficultyButton;

- (IBAction)decreaseDifficulty:(id)sender;
- (IBAction)increaseDifficulty:(id)sender;

- (IBAction)playTopLeft:(id)sender;
- (IBAction)playTop:(id)sender;
- (IBAction)playTopRight:(id)sender;
- (IBAction)playLeft:(id)sender;
- (IBAction)playCenter:(id)sender;
- (IBAction)playRight:(id)sender;
- (IBAction)playBottomLeft:(id)sender;
- (IBAction)playBottom:(id)sender;
- (IBAction)playBottomRight:(id)sender;

@end
```

[Next](TicTacToe-AAPLTicTacToeBoard.h.md)[Previous](TicTacToe-AAPLTicTacToeSquareAccessibilityElement.m.md)

