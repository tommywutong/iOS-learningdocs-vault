---
title: GeekGameBoard
apple_id: DTS10004548
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: QuartzCore
published: '2007-12-19'
source_url: https://developer.apple.com/library/archive/samplecode/GeekGameBoard/Listings/Source_BoardView_h.html
archived_at: '2026-07-18T03:10:38.976464Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GeekGameBoard](GeekGameBoard.md)


[Next](Source-BoardView.m.md)[Previous](Source-BitHolder.m.md)

# Source/BoardView.h

```objc
/*

File: BoardView.h

Abstract: NSView that hosts a game.

Version: 1.0

Disclaimer: IMPORTANT:  This Apple software is supplied to you by 
Apple Inc. ("Apple") in consideration of your agreement to the
following terms, and your use, installation, modification or
redistribution of this Apple software constitutes acceptance of these
terms.  If you do not agree with these terms, please do not use,
install, modify or redistribute this Apple software.

In consideration of your agreement to abide by the following terms, and
subject to these terms, Apple grants you a personal, non-exclusive
license, under Apple's copyrights in this original Apple software (the
"Apple Software"), to use, reproduce, modify and redistribute the Apple
Software, with or without modifications, in source and/or binary forms;
provided that if you redistribute the Apple Software in its entirety and
without modifications, you must retain this notice and the following
text and disclaimers in all such redistributions of the Apple Software. 
Neither the name, trademarks, service marks or logos of Apple Inc. 
may be used to endorse or promote products derived from the Apple
Software without specific prior written permission from Apple.  Except
as expressly stated in this notice, no other rights or licenses, express
or implied, are granted by Apple herein, including but not limited to
any patent rights that may be infringed by your derivative works or by
other works in which the Apple Software may be incorporated.

The Apple Software is provided by Apple on an "AS IS" basis.  APPLE
MAKES NO WARRANTIES, EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION
THE IMPLIED WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY AND FITNESS
FOR A PARTICULAR PURPOSE, REGARDING THE APPLE SOFTWARE OR ITS USE AND
OPERATION ALONE OR IN COMBINATION WITH YOUR PRODUCTS.

IN NO EVENT SHALL APPLE BE LIABLE FOR ANY SPECIAL, INDIRECT, INCIDENTAL
OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) ARISING IN ANY WAY OUT OF THE USE, REPRODUCTION,
MODIFICATION AND/OR DISTRIBUTION OF THE APPLE SOFTWARE, HOWEVER CAUSED
AND WHETHER UNDER THEORY OF CONTRACT, TORT (INCLUDING NEGLIGENCE),
STRICT LIABILITY OR OTHERWISE, EVEN IF APPLE HAS BEEN ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.

Copyright © 2007 Apple Inc. All Rights Reserved.

*/


#import <Cocoa/Cocoa.h>
@class Bit, Card, Grid, Game;
@protocol BitHolder;


/** NSView that hosts a game. */
@interface BoardView : NSView
{
    @private
    Game *_game;                                // Current Game
    CALayer *_gameboard;                        // Game's main layer

    // Used during mouse-down tracking:
    NSPoint _dragStartPos;                      // Starting position of mouseDown
    Bit *_dragBit;                              // Bit being dragged
    id<BitHolder> _oldHolder;                   // Bit's original holder
    CALayer *_oldSuperlayer;                    // Bit's original superlayer
    int _oldLayerIndex;                         // Bit's original index in _oldSuperlayer.layers
    CGPoint _oldPos;                            // Bit's original x/y position
    CGPoint _dragOffset;                        // Offset of mouse position from _dragBit's origin
    BOOL _dragMoved;                            // Has the mouse moved more than 3 pixels since mouseDown?
    id<BitHolder> _dropTarget;                  // Current BitHolder the cursor is over

    // Used while handling incoming drags:
    CALayer *_viewDropTarget;                   // Current drop target during an incoming drag-n-drop
    NSDragOperation _viewDropOp;                // Current drag operation
}

- (void) startGameNamed: (NSString*)gameClassName;

- (IBAction) enterFullScreen: (id)sender;

@property (readonly) Game *game;
@property (readonly) CALayer *gameboard;

- (CGRect) gameBoardFrame;

@end
```

[Next](Source-BoardView.m.md)[Previous](Source-BitHolder.m.md)

