---
title: 'Tic Tac Toe: Creating Accessible Apps with Custom UI'
apple_id: TP40014589
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2016-02-18'
source_url: https://developer.apple.com/library/archive/samplecode/AccessibleTicTacToe/Listings/TicTacToe_AAPLTicTacToeViewController_m.html
archived_at: '2026-07-18T03:00:40.718766Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Tic Tac Toe: Creating Accessible Apps with Custom UI](Tic%20Tac%20Toe-%20Creating%20Accessible%20Apps%20with%20Custom%20UI.md)


[Next](TicTacToe-AAPLTicTacToeSquareAccessibilityElement.m.md)[Previous](TicTacToe-AAPLTicTacToeCheckboxView.h.md)

# TicTacToe/AAPLTicTacToeViewController.m

```objc
/*

 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 View controller for a tic-tac-toe game demonstrating accessible custom controls using the accessibility methods of NSControl subclasses, accessibility protocols, and NSAccessibilityElement.

 */

#import "AAPLTicTacToeViewController.h"
#import "AAPLTicTacToeAIEngine.h"
#import "AAPLTicTacToeBoard.h"

static const NSInteger AAPLMaxDifficulty = 10;
static const NSInteger AAPLMinDifficulty = 0;

@interface AAPLTicTacToeViewController ()

@property (nonatomic, strong) AAPLTicTacToeGame *game;
@property (nonatomic, strong) AAPLTicTacToeAIEngine *ai;

@end

@implementation AAPLTicTacToeViewController

- (void)awakeFromNib
{
    if ( self.game == nil )
    {
        self.game = [AAPLTicTacToeGame new];
    }
    self.boardView.game = self.game;

    self.ai = [AAPLTicTacToeAIEngine new];

    self.resetGameButton.delegate = self;
    self.boardView.delegate = self;
    self.playAICheckbox.delegate = self;

    [self refresh];
}

- (void)refresh
{
    [self.boardView setNeedsDisplay:YES];

    switch ( self.game.state )
    {
        case AAPLTicTacToeGameStateXTurn:
            self.statusText.stringValue = NSLocalizedString(@"X's turn", nil);
            break;
        case AAPLTicTacToeGameStateOTurn:
            self.statusText.stringValue = NSLocalizedString(@"O's turn", nil);
            break;
        case AAPLTicTacToeGameStateXWin:
            self.statusText.stringValue = NSLocalizedString(@"X wins!", nil);
            break;
        case AAPLTicTacToeGameStateOWin:
            self.statusText.stringValue = NSLocalizedString(@"O Wins!", nil);
            break;
        case AAPLTicTacToeGameStateTie:
            self.statusText.stringValue = NSLocalizedString(@"It's a tie", nil);
            break;
        default:
            break;
    }

    self.difficultyText.integerValue = self.ai.difficulty;

    self.increaseDifficultyButton.enabled = (self.ai.difficulty != AAPLMaxDifficulty);
    self.decreaseDifficultyButton.enabled = (self.ai.difficulty != AAPLMinDifficulty);
}

- (BOOL)takeAITurn
{
    return self.game.state == AAPLTicTacToeGameStateOTurn && self.playAICheckbox.checked;
}

#pragma mark - Board View Delegate Methods

- (void)playSquareAtRow:(NSUInteger)row column:(NSUInteger)column
{
    [self.game playSquareAtRow:row column:column];

    AAPLTicTacToeSquare *aiSquare = nil;
    NSUInteger aiRow = 0;
    NSUInteger aiColumn = 0;

    if ( [self takeAITurn] )
    {
        NSPoint move = [self.ai moveForBoard:self.game.board];
        aiRow = move.x;
        aiColumn = move.y;
        aiSquare = [self.game playSquareAtRow:aiRow column:aiColumn];
    }

    [self refresh];
    [self announceTurnWithAISquare:aiSquare row:aiRow column:aiColumn];
}

- (AAPLTicTacToeSquare *)squareAtRow:(NSUInteger)row column:(NSUInteger)column
{
    return [self.game.board squareAtRow:row column:column];
}

- (BOOL)isGameOver
{
    return self.game.state != AAPLTicTacToeGameStateOTurn &&
           self.game.state != AAPLTicTacToeGameStateXTurn;
}

#pragma mark - Checkbox Delegate Methods

- (void)checkboxCheckedStateChanged:(id)sender
{
    if ( sender == self.playAICheckbox && [self takeAITurn] )
    {
        NSPoint move = [self.ai moveForBoard:self.game.board];
        NSUInteger row = move.x;
        NSUInteger column = move.y;
        AAPLTicTacToeSquare *square = [self.game playSquareAtRow:row column:column];
        [self announceTurnWithAISquare:square row:row column:column];
    }
}

#pragma mark - Reset Button Delegate Methods

- (void)buttonPressed:(id)sender
{
    if ( sender == self.resetGameButton )
    {
        [self.game reset];
        [self refresh];
    }
}

#pragma mark - Increase/Decrease Difficulty Actions

- (IBAction)decreaseDifficulty:(id)sender
{
    NSInteger difficulty = self.difficultyText.integerValue;
    self.ai.difficulty = MAX(difficulty - 1, AAPLMinDifficulty);
    [self refresh];
}

- (IBAction)increaseDifficulty:(id)sender
{
    NSInteger difficulty = self.difficultyText.integerValue;
    self.ai.difficulty = MIN(difficulty + 1, AAPLMaxDifficulty);
    [self refresh];
}

#pragma mark - Menu Actions

- (IBAction)playTopLeft:(id)sender
{
    [self playSquareAtRow:0 column:0];
}

- (IBAction)playTop:(id)sender
{
    [self playSquareAtRow:0 column:1];
}

- (IBAction)playTopRight:(id)sender
{
    [self playSquareAtRow:0 column:2];
}

- (IBAction)playLeft:(id)sender
{
    [self playSquareAtRow:1 column:0];
}

- (IBAction)playCenter:(id)sender
{
    [self playSquareAtRow:1 column:1];
}

- (IBAction)playRight:(id)sender
{
    [self playSquareAtRow:1 column:2];
}

- (IBAction)playBottomLeft:(id)sender
{
    [self playSquareAtRow:2 column:0];
}

- (IBAction)playBottom:(id)sender
{
    [self playSquareAtRow:2 column:1];
}

- (IBAction)playBottomRight:(id)sender
{
    [self playSquareAtRow:2 column:2];
}

#pragma mark - Accessibility Announcements

// When a square is played, announce the AI player's move (if enabled) and the next player's turn or game outcome.
- (void)announceTurnWithAISquare:(AAPLTicTacToeSquare *)aiSquare row:(NSUInteger)row column:(NSUInteger)column
{
    NSString *announcement;

    NSString *statusText = self.statusText.stringValue;

    if ( aiSquare )
    {
        NSString *computerPlayedFormatter = NSLocalizedString(@"ComputerPlayedFormatter", nil);
        NSString *computerPlayedAndStatusFormatter = NSLocalizedString(@"ComputerPlayerAndStatusFormatter", nil);
        NSString *aiMove = [NSString stringWithFormat:computerPlayedFormatter, [AAPLTicTacToeBoard descriptionForSquare:aiSquare row:row column:column]];
        announcement = [NSString stringWithFormat:computerPlayedAndStatusFormatter, aiMove, statusText];
    }
    else
    {
        announcement = statusText;
    }

    NSDictionary *userInfo = @{NSAccessibilityAnnouncementKey : announcement,
                               NSAccessibilityPriorityKey : @(NSAccessibilityPriorityMedium)};

    NSAccessibilityPostNotificationWithUserInfo(self.boardView, NSAccessibilityAnnouncementRequestedNotification, userInfo);

}

@end
```

[Next](TicTacToe-AAPLTicTacToeSquareAccessibilityElement.m.md)[Previous](TicTacToe-AAPLTicTacToeCheckboxView.h.md)

