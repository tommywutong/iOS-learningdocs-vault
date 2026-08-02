---
title: 'Tic Tac Toe: Creating Accessible Apps with Custom UI'
apple_id: TP40014589
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2016-02-18'
source_url: https://developer.apple.com/library/archive/samplecode/AccessibleTicTacToe/Listings/TicTacToe_AAPLTicTacToeBoardView_m.html
archived_at: '2026-07-18T03:00:39.550822Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Tic Tac Toe: Creating Accessible Apps with Custom UI](Tic%20Tac%20Toe-%20Creating%20Accessible%20Apps%20with%20Custom%20UI.md)


[Next](TicTacToe-AAPLTicTacToeCheckboxView.h.md)[Previous](TicTacToe-AAPLAppDelegate.m.md)

# TicTacToe/AAPLTicTacToeBoardView.m

```objc
/*

 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 An example demonstrating adding accessibility to an NSView subclass that behaves like a group by implementing the NSAccessibilityGroup protocol
  and using NSAccessibilityElement to represent each of the items the view draws.

 */

#import "AAPLTicTacToeBoardView.h"
#import "AAPLTicTacToeSquareAccessibilityElement.h"

@implementation AAPLTicTacToeBoardView

@synthesize accessibilityChildren = _accessibilityChildren;

- (NSRect)squareRectforRow:(NSUInteger)row column:(NSUInteger)column
{
    AAPLTicTacToeBoard *board = self.game.board;
    NSRect bounds = self.bounds;
    CGFloat height = bounds.size.height;

    CGFloat squareWidth = bounds.size.width / board.numColumns;
    CGFloat squareHeight = height / board.numRows;

    CGFloat inset = squareWidth / 5.0;
    NSRect squareRect = NSZeroRect;

    if ( row < board.numRows && column < board.numColumns )
    {
            squareRect = NSMakeRect(column * squareWidth + inset,
                                   height - (row + 1) * squareHeight + inset,
                                   squareWidth - 2 * inset,
                                   squareHeight - 2 * inset);
    }

    return squareRect;
}

#pragma mark - Mouse Event Handling

- (void)mouseUp:(NSEvent *)mouseEvent
{
    NSPoint localPoint = [self convertPoint:mouseEvent.locationInWindow fromView:nil];
    CGFloat row = floor((self.bounds.size.height - localPoint.y) / (self.bounds.size.height / 3.0));
    CGFloat column = floor(localPoint.x / (self.bounds.size.width / 3.0));
    [self.delegate playSquareAtRow:row column:column];
    [self setNeedsDisplay:YES];
}

#pragma mark - Drawing

- (void)drawRect:(NSRect)dirtyRect
{
    [super drawRect:dirtyRect];

    [self drawGrid];
    [self drawSquares];
    [self drawWinLine];
}

- (void)drawGrid
{
    NSRect bounds = self.bounds;
    CGFloat width = bounds.size.width;
    CGFloat height = bounds.size.height;

    [[NSColor blackColor] set];
    [NSBezierPath setDefaultLineWidth:1.0];

    [NSBezierPath strokeLineFromPoint:NSMakePoint(width / 3.0, 0.0) toPoint:NSMakePoint(width / 3.0, height)];
    [NSBezierPath strokeLineFromPoint:NSMakePoint(2.0 * width / 3.0, 0.0) toPoint:NSMakePoint(2.0 * width / 3.0, height)];
    [NSBezierPath strokeLineFromPoint:NSMakePoint(0.0, height / 3.0) toPoint:NSMakePoint(width, height/ 3.0)];
    [NSBezierPath strokeLineFromPoint:NSMakePoint(0.0, 2.0 * height / 3.0 ) toPoint:NSMakePoint(width, 2.0 * height / 3.0)];
}

- (void)drawSquares
{
    [NSBezierPath setDefaultLineWidth:3.0];
    AAPLTicTacToeGame *game = self.game;
    AAPLTicTacToeBoard *board = game.board;
    AAPLTicTacToeSquare *square;
    NSUInteger numRows = board.numRows;
    NSUInteger numColumns = board.numColumns;

    for ( NSUInteger row = 0; row < numRows; row++ )
    {
        for ( NSUInteger column = 0; column < numColumns; column++ )
        {
            square = [board squareAtRow:row column:column];
            if ( square.isX )
            {
                [self drawXAtRow:row column:column];
            }
            else if ( square.isO )
            {
                [self drawOAtRow:row column:column];
            }
        }
    }
}

- (void)drawXAtRow:(NSUInteger)row column:(NSUInteger)column
{
    NSRect squareRect = [self squareRectforRow:row column:column];
    NSPoint topLeft = NSMakePoint(NSMinX(squareRect), NSMaxY(squareRect));
    NSPoint topRight = NSMakePoint(NSMaxX(squareRect), NSMaxY(squareRect));
    NSPoint bottomLeft = NSMakePoint(NSMinX(squareRect), NSMinY(squareRect));
    NSPoint bottomRight = NSMakePoint(NSMaxX(squareRect), NSMinY(squareRect));

    [NSBezierPath strokeLineFromPoint:topLeft toPoint:bottomRight];
    [NSBezierPath strokeLineFromPoint:topRight toPoint:bottomLeft];
}

- (void)drawOAtRow:(NSUInteger)row column:(NSUInteger)column
{
    NSRect squareRect = [self squareRectforRow:row column:column];
    NSPoint center = NSMakePoint(NSMidX(squareRect), NSMidY(squareRect));
    NSBezierPath *circlePath = [[NSBezierPath alloc] init];
    [circlePath appendBezierPathWithArcWithCenter:center radius:squareRect.size.height / 2.0  startAngle:0 endAngle:360.0];
    [circlePath stroke];
}


- (void)drawWinLine
{
    AAPLTicTacToeGame *game = self.game;
    NSUInteger height = self.bounds.size.height;
    NSUInteger width = self.bounds.size.width;

    switch ( game.winType )
    {
        case AAPLTicTacToeGameWinTypeRow:
            [NSBezierPath setDefaultLineWidth:4];
            [[NSColor redColor] set];
            [NSBezierPath strokeLineFromPoint:NSMakePoint(0.0, height - (2 * game.winningRow + 1) * (height / 6.0))
                                      toPoint:NSMakePoint(width, height - (2 * game.winningRow + 1) * (height / 6.0))];
            break;
        case AAPLTicTacToeGameWinTypeColumn:
            [NSBezierPath setDefaultLineWidth:4];
            [[NSColor redColor] set];
            [NSBezierPath strokeLineFromPoint:NSMakePoint((2 * game.winningColumn + 1) * (width / 6.0), 0.0)
                                      toPoint:NSMakePoint((2 * game.winningColumn + 1) * (width / 6.0), height)];
            break;
        case AAPLTicTacToeGameWinTypeTopLeftDiagonal:
            [NSBezierPath setDefaultLineWidth:4];
            [[NSColor redColor] set];
            [NSBezierPath strokeLineFromPoint:NSMakePoint(0.0, height)
                                      toPoint:NSMakePoint(width, 0.0)];
            break;
        case AAPLTicTacToeGameWinTypeTopRightDiagonal:
            [NSBezierPath setDefaultLineWidth:4];
            [[NSColor redColor] set];
            [NSBezierPath strokeLineFromPoint:NSMakePoint(0.0, 0.0)
                                      toPoint:NSMakePoint(width, height)];
            break;
        default:
            break;
    }
}

#pragma mark - Accessibility

- (NSString *)accessibilityLabel
{
    return NSLocalizedString(@"tic tac toe board", nil);
}

// This view draws all of its elements (the tic tac toe squares) itself.
// NSAccessibilityElement is used to make these squares individually available to accessibility clients
// by returning an element for each square from -(NSArray *)accessibilityChildren
- (NSArray *)accessibilityChildren
{
    // if the children haven't been created yet
    if ( _accessibilityChildren == nil )
    {
        // make an array to hold them
        NSMutableArray *accessibilityChildren = [NSMutableArray new];

        AAPLTicTacToeBoard *board = self.game.board;
        AAPLTicTacToeSquareAccessibilityElement *squareAccessibilityElement;

        // for each square of the board
        for ( NSUInteger row = 0; row < board.numRows; row++ )
        {
            for ( NSUInteger column = 0; column < board.numColumns; column++ )
            {
                // create an accessibility element for the square
                squareAccessibilityElement = [[AAPLTicTacToeSquareAccessibilityElement alloc] initWithRow:row
                                                                                                   column:column
                                                                                                 delegate:self.delegate];

                // set the parent and frame
                squareAccessibilityElement.accessibilityParent = self;
                squareAccessibilityElement.accessibilityFrameInParentSpace = [self squareRectforRow:row column:column];

                // and add it to the array
                [accessibilityChildren addObject:squareAccessibilityElement];
            }
        }

        // hold onto the accessibility elements the entire time they are shown in the UI
        _accessibilityChildren = accessibilityChildren;
    }

    return _accessibilityChildren;
}

#pragma mark - Support IB_DESIGNABLE

// Executed when your view is being prepared for display in Interface Builder.
- (void)prepareForInterfaceBuilder
{
    // Add visual interest in Interface Builder by instantiating a game and playing two moves.
    self.game = [AAPLTicTacToeGame new];
    [self.game playSquareAtRow:0 column:0];
    [self.game playSquareAtRow:1 column:1];
}

@end
```

[Next](TicTacToe-AAPLTicTacToeCheckboxView.h.md)[Previous](TicTacToe-AAPLAppDelegate.m.md)

