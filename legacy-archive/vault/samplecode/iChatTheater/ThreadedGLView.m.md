---
title: iChatTheater
apple_id: DTS10004197
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: InstantMessage
published: '2012-08-27'
source_url: https://developer.apple.com/library/archive/samplecode/iChatTheater/Listings/ThreadedGLView_m.html
archived_at: '2026-07-18T03:29:35.187356Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [iChatTheater](iChatTheater.md)


[Next](Document%20Revision%20History.md)[Previous](ThreadedGLView.h.md)

# ThreadedGLView.m

```objc
/*

 File: ThreadedGLView.m

 Abstract: To render simultaneously on two different threads, this
           class creates a secondary context shared with its main
           context. By importing the <OpenGL/CGLMacro.h> header, it
           is able to send OpenGL commands to the correct context for
           each thread: the CGLContextObj called CGL_MACRO_CONTEXT in the
           -_renderInContext: method.

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

#import "ThreadedGLView.h"
#import <OpenGL/CGLMacro.h>

#define kNoTime UINT64_MAX

@implementation ThreadedGLView

- (void) dealloc {
    if (_alternateContext != NULL) {
        CGLDestroyContext(_alternateContext);
        CGLDestroyPixelFormat(_alternatePixelFormat);
    }

    [super dealloc];
}

#pragma mark -
#pragma mark Rendering

#define kBarWidth 0.84
#define kBarHeight 0.10
#define kBarLeft ((1.0 - kBarWidth) / 2.0)
#define kBarBottom ((1.0 - kBarHeight) / 2.0)

static float kBGGradientColor1[]  = {  65.0,  65.0,  75.0 };
static float kBGGradientColor2[]  = { 115.0, 120.0, 135.0 };
static float kBarGradientColor1[] = {  20.0,  35.0, 100.0 };
static float kBarGradientColor2[] = {  70.0, 100.0, 175.0 };

#define SET_COLOR(rgb) glColor3f(rgb[0] / 255.0, rgb[1] / 255.0, rgb[2] / 255.0)

// Render our scene. Takes a CGLContextObj to say which GL context to render into.
- (void) _renderProgress:(float)progress inContext:(CGLContextObj)CGL_MACRO_CONTEXT {
    // Get rendering destination's dimensions.
    GLint viewport[4];
    glGetIntegerv(GL_VIEWPORT, viewport);

    // Projection.
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    glOrtho(viewport[0], viewport[2], viewport[1], viewport[3], -1.0, 1.0);

    // Model.
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();

    float barLeft = viewport[0] + kBarLeft * viewport[2];
    float barRight = barLeft + kBarWidth * viewport[2];
    float barFill = barLeft + kBarWidth * progress * viewport[2];
    float barBottom = viewport[1] + kBarBottom * viewport[3];
    float barTop = barBottom + kBarHeight * viewport[3];

    glBegin(GL_QUADS);

    // bg
    SET_COLOR(kBGGradientColor1);
    glVertex2f(viewport[0], viewport[1]);
    glVertex2f(viewport[2], viewport[1]);
    SET_COLOR(kBGGradientColor2);
    glVertex2f(viewport[2], viewport[3]);
    glVertex2f(viewport[0], viewport[3]);

    // fill
    SET_COLOR(kBarGradientColor1);
    glVertex2f(barLeft, barBottom);
    glVertex2f(barFill, barBottom);
    SET_COLOR(kBarGradientColor2);
    glVertex2f(barFill, barTop);
    glVertex2f(barLeft, barTop);

    // remaining
    SET_COLOR(kBGGradientColor2);
    glVertex2f(barFill, barBottom);
    glVertex2f(barRight, barBottom);
    SET_COLOR(kBGGradientColor1);
    glVertex2f(barRight, barTop);
    glVertex2f(barFill, barTop);

    glEnd();

    glFlush();
}

- (void) _renderInContext:(CGLContextObj)CGL_MACRO_CONTEXT forTime:(uint64_t)time {
    double elapsed = (_startTime == kNoTime) ? 0.0 : ((double)(time - _startTime) / CVGetHostClockFrequency());
    float phase = (elapsed - floor(elapsed / 10.0) * 10.0) / 10.0;

    [self _renderProgress:phase inContext:CGL_MACRO_CONTEXT];
}

- (void) drawRect:(NSRect)rect {
    // Render in the normal context.
    [self _renderInContext:[[self openGLContext] CGLContextObj] forTime:CVGetCurrentHostTime()];
}

- (void) reshape {
    // The NSOpenGLView has resized.
    // Update the viewport (this doesn't affect the _alternateContext used to 
    // send frames to the IMAVManager).
    CGLContextObj CGL_MACRO_CONTEXT = [[self openGLContext] CGLContextObj];

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
        _startTime = CVGetCurrentHostTime();
        _redrawTimer = [[NSTimer scheduledTimerWithTimeInterval:(1.0 / 30.0)
                                                        target:self
                                                      selector:@selector(_frameTimerFired:)
                                                      userInfo:nil
                                                       repeats:YES] retain];
        [self _frameTimerFired:nil];

    } else {
        // Stop the timer.
        [_redrawTimer invalidate];
        [_redrawTimer release];
        _redrawTimer = nil;
        _startTime = kNoTime;
    }
}

#pragma mark -
#pragma mark IMAVManager Call-backs

// The IMAVManager will call this to ask for the context we'll be providing frames with.
- (void) getOpenGLBufferContext:(CGLContextObj *)contextOut pixelFormat:(CGLPixelFormatObj *)pixelFormatOut {
    if (_alternateContext == NULL) {
        // Create a shared GL context.  We will use this context to render with
        // when we're sending frames to the IMAVManager.
        long npix = 0;
        CGLPixelFormatAttribute attributes[] = {
            kCGLPFADoubleBuffer,
            kCGLPFAColorSize, 24,
            0
        };
        CGLChoosePixelFormat(attributes, &_alternatePixelFormat, (void*)&npix);
        CGLCreateContext(_alternatePixelFormat, [[self openGLContext] CGLContextObj], &_alternateContext);
    }

    *contextOut = _alternateContext;
    *pixelFormatOut = _alternatePixelFormat;
}

// The IMAVManager will call this when it wants a frame.
// Note that this will be called on a non-main thread.
- (BOOL) renderIntoOpenGLBuffer:(CVOpenGLBufferRef)buffer onScreen:(int *)screenInOut forTime:(CVTimeStamp*)timeStamp {
    // Get the screen ID for our context.
    CGLContextObj CGL_MACRO_CONTEXT = _alternateContext;

    // Attach the OpenGLBuffer and render into the _alternateContext.
    if (CVOpenGLBufferAttach(buffer, CGL_MACRO_CONTEXT, 0, 0, *screenInOut) == kCVReturnSuccess) {
        // In case the buffers have changed in size, reset the viewport.
        CGRect cleanRect = CVImageBufferGetCleanRect(buffer);
        glViewport(CGRectGetMinX(cleanRect), CGRectGetMinY(cleanRect), CGRectGetWidth(cleanRect), CGRectGetHeight(cleanRect));

        // Render. Our image is constantly changing, so use the supplied timestamp.
        [self _renderInContext:CGL_MACRO_CONTEXT forTime:timeStamp->hostTime];
        return YES;
    } else {
        // This should never happen.  The safest thing to do if it does it return
        // 'NO' (signifying that the frame has not changed).
        return NO;
    }
}

@end
```

[Next](Document%20Revision%20History.md)[Previous](ThreadedGLView.h.md)

