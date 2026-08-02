---
title: iChatTheater
apple_id: DTS10004197
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: InstantMessage
published: '2012-08-27'
source_url: https://developer.apple.com/library/archive/samplecode/iChatTheater/Listings/NormalGLView_m.html
archived_at: '2026-07-18T03:29:34.716642Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [iChatTheater](iChatTheater.md)


[Next](SlideshowView.h.md)[Previous](NormalGLView.h.md)

# NormalGLView.m

```objc
/*

 File: NormalGLView.m

 Abstract: There is no need to implement the -getOpenGLContext:pixelFormat:
           and -renderIntoOpenGLBuffer:onScreen:forTime: methods, or deal
           with concurrent rendering of the GL scene.

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

#import "NormalGLView.h"

@implementation NormalGLView

#pragma mark -
#pragma mark Rendering

- (void) drawRect:(NSRect)rect {
    [[self openGLContext] makeCurrentContext];

    // Clear.
    glClearColor(0.0, 0.0, 0.0, 1.0);
    glClear(GL_COLOR_BUFFER_BIT);

    // Get rendering destination's dimensions.
    GLint viewport[4];
    glGetIntegerv(GL_VIEWPORT, viewport);
    float width = viewport[2], height = viewport[3];
    float size = MIN(width, height);    // fit figure in viewport

    // Projection.
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    glOrtho(-width, width, -height, height, -1.0, 1.0);

    // Model.
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();

    NSTimeInterval elapsed = (_startTime == nil) ? 0.0 : -[_startTime timeIntervalSinceNow];
    glRotatef(elapsed * 90.0, 0.0, 0.0, 1.0);

    // Render a diamond with red, green, blue and white corners.
    glBegin(GL_QUADS);

    glColor3f(1.0, 0.0, 0.0);
    glVertex2f(-size, 0.0);

    glColor3f(0.0, 1.0, 0.0);
    glVertex2f(0.0, size);

    glColor3f(0.0, 0.0, 1.0);
    glVertex2f(size, 0.0);

    glColor3f(1.0, 1.0, 1.0);
    glVertex2f(0.0, -size);

    glEnd();

    glFlush();
}

- (void) reshape {
    // The NSOpenGLView has resized.
    // Update the viewport.
    [[self openGLContext] makeCurrentContext];

    // Get the view size in screen coordinates.
    NSSize size = [self convertSize:[self bounds].size toView:nil];
    glViewport(0, 0, size.width, size.height);
}

// We need to display a frame of animation
- (void) _frameTimerFired:(NSTimer *)timer {
    [self setNeedsDisplay:YES];
}

- (void) viewDidMoveToWindow {
    [super viewDidMoveToWindow];
    NSWindow *newWindow = [self window];

    if (newWindow != nil) {
        // Start a timer to periodically refresh the scene.
        _startTime = [[NSDate alloc] init];
        _redrawTimer = [[NSTimer scheduledTimerWithTimeInterval:(1.0 / 30.0)
                                                        target:self
                                                      selector:@selector(_frameTimerFired:)
                                                      userInfo:nil
                                                       repeats:YES] retain];
        //[[NSRunLoop currentRunLoop] addTimer:_redrawTimer forMode:NSEventTrackingRunLoopMode];
        [self _frameTimerFired:nil];

    } else {
        // Stop the timer.
        [_redrawTimer invalidate];
        [_redrawTimer release];
        _redrawTimer = nil;
        [_startTime release];
        _startTime = nil;
    }
}

@end
```

[Next](SlideshowView.h.md)[Previous](NormalGLView.h.md)

