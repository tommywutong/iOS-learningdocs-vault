---
title: DeferredShading
apple_id: DTS40010088
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2015-07-08'
source_url: https://developer.apple.com/library/archive/samplecode/DeferredShading/Listings/GLView_mm.html
archived_at: '2026-07-18T03:06:11.291693Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DeferredShading](DeferredShading.md)


[Next](vectorUtil.c.md)[Previous](main.m.md)

# GLView.mm

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The OpenGL view. It delegates to the renderer class for drawing.
 */


#import "GLView.h"
#include "renderer.h"

#define k1KeyCode 18
#define k2KeyCode 19
#define k3KeyCode 20
#define k4KeyCode 21
#define kSpacebarKeyCode 49

static CVReturn Heartbeat (     CVDisplayLinkRef displayLink,
                                const CVTimeStamp *inNow,
                                const CVTimeStamp *inOutputTime,
                                CVOptionFlags flagsIn,
                                CVOptionFlags *flagsOut,
                                void *displayLinkContext)
{
    CallbackContext* ctx = (CallbackContext*) displayLinkContext;
    CGLSetCurrentContext((CGLContextObj) [ctx->ctx CGLContextObj]);
    ctx->renderer->draw();
    CGLFlushDrawable((CGLContextObj) [ctx->ctx CGLContextObj]);
    return kCVReturnSuccess;
}

@implementation GLView

- (instancetype)initWithFrame:(NSRect)frame {
    NSOpenGLPixelFormatAttribute attrs[] = {
        NSOpenGLPFADoubleBuffer,
        NSOpenGLPFADepthSize, 24,
        NSOpenGLPFAStencilSize, 8,
        NSOpenGLPFAOpenGLProfile, NSOpenGLProfileVersion3_2Core, //Core Profile
        0
    };

    cbCtx = (CallbackContext*) malloc(sizeof(CallbackContext));

    NSOpenGLPixelFormat*    pixelFormat = [[[NSOpenGLPixelFormat alloc] initWithAttributes:attrs]autorelease];

    self = [super initWithFrame:frame pixelFormat: pixelFormat];
    if (self) 
    {
        self.wantsBestResolutionOpenGLSurface = YES;
        pf = pixelFormat;
        [self setFrame:frame];
        cbCtx->ctx = [self openGLContext];
        [cbCtx->ctx makeCurrentContext];
        const char* pathToResources = [[[NSBundle mainBundle] resourcePath] cStringUsingEncoding:NSASCIIStringEncoding];
        cbCtx->renderer = new OpenGLRenderer(pathToResources, strlen(pathToResources));
        NSRect bounds = [self bounds];
        NSRect pixels = [self convertRectToBacking:bounds];
        cbCtx->renderer->resizeViewport(pixels.size.width,pixels.size.height);
    }
    return self;
}

- (void)prepareOpenGL
{
    [super prepareOpenGL];

    if(!cbCtx->renderer->setupGL())
    {
        NSLog(@"Could not set up GL context");
        assert(0);
    }

    CVDisplayLinkCreateWithActiveCGDisplays(&displayLink);
    CVDisplayLinkSetCurrentCGDisplayFromOpenGLContext(displayLink, (CGLContextObj) [cbCtx->ctx CGLContextObj], (CGLPixelFormatObj) [pf CGLPixelFormatObj]);

    CVDisplayLinkSetOutputCallback(displayLink, &Heartbeat, cbCtx);
    CVDisplayLinkStart(displayLink);

    // Register to be notified when the window closes so we can stop the displaylink
    [[NSNotificationCenter defaultCenter] addObserver:self
                                             selector:@selector(windowWillClose:)
                                                 name:NSWindowWillCloseNotification
                                               object:[self window]];

}

- (BOOL)acceptsFirstResponder
{
    return YES;
}

- (BOOL)becomeFirstResponder
{
    return YES;
}

- (void)dealloc
{
    CVDisplayLinkStop(displayLink);
    CVDisplayLinkRelease(displayLink);
    [pf release];
    [cbCtx->ctx release];   
    delete cbCtx->renderer;
    free(cbCtx);
    [super dealloc];
}

- (void)drawRect:(NSRect)dirtyRect 
{
    if(CVDisplayLinkIsRunning(displayLink))
        return;
    cbCtx->renderer->draw();
    [[self openGLContext] flushBuffer];
}

- (void)keyDown:(NSEvent *)theEvent
{
    switch ([theEvent keyCode]) {
        case k1KeyCode:
            cbCtx->renderer->setShowBuffer(kFinalImage);
            break;
        case k2KeyCode:
            cbCtx->renderer->setShowBuffer(kPositionBuffer);
            break;
        case k3KeyCode:
            cbCtx->renderer->setShowBuffer(kAlbedoBuffer);
            break;
        case k4KeyCode:
            cbCtx->renderer->setShowBuffer(kNormalBuffer);
            break;
        case kSpacebarKeyCode:
            cbCtx->renderer->toggleAnimation();
            break;
        default:
            break;
    }
}

- (void) windowWillClose:(NSNotification*)notification
{
    // Stop the display link when the window is closing because default
    // OpenGL render buffers will be destroyed.  If display link continues to
    // fire without renderbuffers, OpenGL draw calls will set errors.

    CVDisplayLinkStop(displayLink);
}

@end
```

[Next](vectorUtil.c.md)[Previous](main.m.md)

