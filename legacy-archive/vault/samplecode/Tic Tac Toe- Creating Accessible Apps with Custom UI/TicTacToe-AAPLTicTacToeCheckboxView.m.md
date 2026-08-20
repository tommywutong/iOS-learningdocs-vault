---
title: 'Tic Tac Toe: Creating Accessible Apps with Custom UI'
apple_id: TP40014589
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2016-02-18'
source_url: https://developer.apple.com/library/archive/samplecode/AccessibleTicTacToe/Listings/TicTacToe_AAPLTicTacToeCheckboxView_m.html
archived_at: '2026-07-18T03:00:39.871816Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Tic Tac Toe: Creating Accessible Apps with Custom UI](Tic%20Tac%20Toe-%20Creating%20Accessible%20Apps%20with%20Custom%20UI.md)


[Next](TicTacToe-AAPLTicTacToeCircleButtonView.h.md)[Previous](TicTacToe-AAPLTicTacToeCircleMinusButtonView.h.md)

# TicTacToe/AAPLTicTacToeCheckboxView.m

```objc
/*

 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 An example demonstrating adding accessibility to an NSView subclass that behaves like a checkbox by implementing the NSAccessibilityCheckBox protocol.

 */

#import "AAPLTicTacToeCheckboxView.h"

static NSString * const AAPLCheckboxSelected = @"CustomCheckboxSelected";
static NSString * const AAPLCheckboxUnselected = @"CustomCheckboxUnselected";
static const CGFloat AAPLCheckboxWidth = 12.0;
static const CGFloat AAPLCheckboxHeight = AAPLCheckboxWidth;
static const CGFloat AAPLCheckboxTextSpacing = 8.0; // spacing between box and text

@interface AAPLTicTacToeCheckboxView ()

@property (nonatomic, strong) IBInspectable NSString *checkboxText;
@property (nonatomic) BOOL checked;

@end

@implementation AAPLTicTacToeCheckboxView

- (BOOL)acceptsFirstResponder
{
    return YES;
}

- (BOOL)becomeFirstResponder
{
    BOOL didBecomeFirstResponder = [super becomeFirstResponder];
    [self setNeedsDisplay:YES];
    return didBecomeFirstResponder;
}

- (BOOL)resignFirstResponder
{
    BOOL didResignFirstResponder = [super resignFirstResponder];
    [self setNeedsDisplay:YES];
    return didResignFirstResponder;
}

- (void)mouseUp:(NSEvent *)mouseEvent
{
    [self toggleCheckedState];
}

- (void)toggleCheckedState
{
    self.checked = !self.checked;
    [self.delegate checkboxCheckedStateChanged:self];

    // Whenever the value of the checkbox changes, let accessibility clients know
    NSAccessibilityPostNotification(self, NSAccessibilityValueChangedNotification);

    [self setNeedsDisplay:YES];
}

- (void)keyDown:(NSEvent *)keyEvent
{
    int spacebarKeyCode = 49;

    if ( [keyEvent keyCode] == spacebarKeyCode )
    {
        [self toggleCheckedState];
    }
    else
    {
        [super keyDown:keyEvent];
    }
}

- (void)drawRect:(NSRect)dirtyRect
{
    NSRect bounds = self.bounds;
    NSRect boxRect = NSMakeRect(bounds.origin.x,
                                bounds.origin.y + 5,
                                AAPLCheckboxWidth,
                                AAPLCheckboxHeight);

    NSRect textRect = NSMakeRect(bounds.origin.x + AAPLCheckboxWidth + AAPLCheckboxTextSpacing,
                                 bounds.origin.y,
                                 bounds.size.width,
                                 bounds.size.height);

    // Draw the checkbox box

    // Obtain the bundle based on our class in order to support `IB_DESIGNABLE`.
    NSBundle *bundle = [NSBundle bundleForClass:[self class]];
    NSImage *boxImage = nil;

    if ( self.checked )
    {
        boxImage = [bundle imageForResource:AAPLCheckboxSelected];
    }
    else
    {
        boxImage = [bundle imageForResource:AAPLCheckboxUnselected];
    }

    [boxImage drawInRect:boxRect fromRect:NSZeroRect operation:NSCompositeSourceOver fraction:1.0];

    // Draw the checkbox text
    NSDictionary *textAttributes = @{ NSFontAttributeName : [NSFont fontWithName:@"Andale Mono" size:16.0f],
                                      NSForegroundColorAttributeName : [NSColor blackColor] };
    [self.checkboxText drawInRect:textRect withAttributes:textAttributes];

    // Draw the focus ring
    BOOL isFirstResponder = [[[NSApp mainWindow] firstResponder] isEqual:self];
    if ( isFirstResponder )
    {
        [NSGraphicsContext saveGraphicsState];
        NSSetFocusRingStyle(NSFocusRingOnly);
        [[NSBezierPath bezierPathWithRect:boxRect] fill];
        [NSGraphicsContext restoreGraphicsState];
    }
}

#pragma mark Accessibility

- (NSString *)accessibilityLabel
{
    return self.checkboxText;
}

- (NSNumber *)accessibilityValue
{
    return self.checked ? @YES : @NO;
}

- (BOOL)accessibilityPerformPress
{
    [self toggleCheckedState];
    return YES;
}

@end
```

[Next](TicTacToe-AAPLTicTacToeCircleButtonView.h.md)[Previous](TicTacToe-AAPLTicTacToeCircleMinusButtonView.h.md)

