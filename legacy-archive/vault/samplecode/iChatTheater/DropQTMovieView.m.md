---
title: iChatTheater
apple_id: DTS10004197
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: InstantMessage
published: '2012-08-27'
source_url: https://developer.apple.com/library/archive/samplecode/iChatTheater/Listings/DropQTMovieView_m.html
archived_at: '2026-07-18T03:29:34.614761Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [iChatTheater](iChatTheater.md)


[Next](NormalGLView.h.md)[Previous](DropQTMovieView.h.md)

# DropQTMovieView.m

```objc
/*

 File: DropQTMovieView.m

 Abstract: The view will register for drag-and-drop to receive
           QuickTime movie files. It works as a video data source
           via the built-in functionality of NSViews in iChat Theater.

 Version: 2.0

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

 Copyright (C) 2007 - 2008 Apple Inc. All Rights Reserved.

 */

#import "DropQTMovieView.h"
#import "Controller.h"
#import <QTKit/QTMovie.h>

@implementation DropQTMovieView

- (void) _drawDragLabel {
    // Construct message label.
    NSString *messageString = NSLocalizedString(@"Drag a movie here", @"Label: instruction to drag a movie onto the movie view");
    NSDictionary *messageAttributes = [NSDictionary dictionaryWithObjectsAndKeys:
                                       [NSFont systemFontOfSize:[NSFont systemFontSize]], NSFontAttributeName,
                                       [NSColor lightGrayColor], NSForegroundColorAttributeName,
                                       nil];

    NSAttributedString *message = [[NSAttributedString alloc] initWithString:messageString
                                                                  attributes:messageAttributes];

    // Draw in center.
    NSRect bounds = [self bounds];
    NSSize size = [message size];
    [message drawInRect:NSMakeRect(NSMidX(bounds) - floor(size.width  / 2.0),
                                   NSMidY(bounds) - floor(size.height / 2.0),
                                   size.width, size.height)];
}

- (void) drawRect:(NSRect)aRect {
    if ([self movie] == nil) {
        // No movie: fill with black and show message.
        [[NSColor blackColor] set];
        NSRectFill(aRect);
        [self _drawDragLabel];

    } else {
        // Fill margins around movie with gray.
        [[NSColor darkGrayColor] set];
        NSRectFill(aRect);
    }
}

- (void) viewWillMoveToWindow:(NSWindow *)newWindow {
    if ([self window] != nil)
        [self unregisterDraggedTypes];
}

- (void) viewDidMoveToWindow {
    [super viewDidMoveToWindow];
    if ([self window] != nil)
        [self registerForDraggedTypes:[NSArray arrayWithObject:NSFilenamesPboardType]];
}

- (NSDragOperation) draggingEntered:(id < NSDraggingInfo >)sender {
    return [QTMovie canInitWithPasteboard:[sender draggingPasteboard]] ? NSDragOperationCopy : NSDragOperationNone;
}

- (BOOL) performDragOperation:(id < NSDraggingInfo >)sender {

    /*
    QTMovie *movie = [QTMovie movieWithPasteboard:[sender draggingPasteboard] error:NULL];
    if (movie != nil) {
        [_controller setMovie:movie];
        return YES;
    }
    return NO;

     */
    QTMovie *movie = [QTMovie movieWithFile: @"/test.m4v" error: NULL];
    [_controller setMovie: movie];
    return YES;
}

@end
```

[Next](NormalGLView.h.md)[Previous](DropQTMovieView.h.md)

