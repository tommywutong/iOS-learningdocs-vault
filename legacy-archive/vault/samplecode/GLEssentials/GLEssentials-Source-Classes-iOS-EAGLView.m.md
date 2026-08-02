---
title: GLEssentials
apple_id: DTS40010104
resource_type: Sample Code
platform: iOS|macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-08-07'
source_url: https://developer.apple.com/library/archive/samplecode/GLEssentials/Listings/GLEssentials_Source_Classes_iOS_EAGLView_m.html
archived_at: '2026-07-18T03:10:03.189516Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GLEssentials](GLEssentials.md)


[Next](GLEssentials-Source-Classes-OpenGLRenderer.h.md)[Previous](GLEssentials-Source-Classes-iOS-ES2Renderer.m.md)

# GLEssentials/Source/Classes/iOS/EAGLView.m

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The EAGLView class is a UIView subclass that renders OpenGL scene.
*/

#import "EAGLView.h"

#import "ES2Renderer.h"
@interface EAGLView ()
{
    ES2Renderer* _renderer;
    EAGLContext* _context;
    NSInteger _animationFrameInterval;
    CADisplayLink* _displayLink;
}
@end

@implementation EAGLView

// Must return the CAEAGLLayer class so that CA allocates an EAGLLayer backing for this view
+ (Class) layerClass
{
    return [CAEAGLLayer class];
}

// The GL view is stored in the storyboard file. When it's unarchived it's sent -initWithCoder:
- (instancetype) initWithCoder:(NSCoder*)coder
{    
    if ((self = [super initWithCoder:coder]))
    {
        // Get the layer
        CAEAGLLayer *eaglLayer = (CAEAGLLayer *)self.layer;

        eaglLayer.opaque = TRUE;
        eaglLayer.drawableProperties = [NSDictionary dictionaryWithObjectsAndKeys:
                                        [NSNumber numberWithBool:FALSE], kEAGLDrawablePropertyRetainedBacking, kEAGLColorFormatRGBA8, kEAGLDrawablePropertyColorFormat, nil];


        _context = [[EAGLContext alloc] initWithAPI:kEAGLRenderingAPIOpenGLES2];

        if (!_context || ![EAGLContext setCurrentContext:_context])
        {
            return nil;
        }

        _renderer = [[ES2Renderer alloc] initWithContext:_context AndDrawable:(id<EAGLDrawable>)self.layer];

        if (!_renderer)
        {
            return nil;
        }

        _animating = FALSE;
        _animationFrameInterval = 1;
        _displayLink = nil;
    }

    return self;
}

- (void) drawView:(id)sender
{   
    [EAGLContext setCurrentContext:_context];
    [_renderer render];
}

- (void) layoutSubviews
{
    [_renderer resizeFromLayer:(CAEAGLLayer*)self.layer];
    [self drawView:nil];
}

- (NSInteger) animationFrameInterval
{
    return _animationFrameInterval;
}

- (void) setAnimationFrameInterval:(NSInteger)frameInterval
{
    // Frame interval defines how many display frames must pass between each time the
    // display link fires. The display link will only fire 30 times a second when the
    // frame internal is two on a display that refreshes 60 times a second. The default
    // frame interval setting of one will fire 60 times a second when the display refreshes
    // at 60 times a second. A frame interval setting of less than one results in undefined
    // behavior.
    if (frameInterval >= 1)
    {
        _animationFrameInterval = frameInterval;

        if (_animating)
        {
            [self stopAnimation];
            [self startAnimation];
        }
    }
}

- (void) startAnimation
{
    if (!_animating)
    {
        // Create the display link and set the callback to our drawView method
        _displayLink = [CADisplayLink displayLinkWithTarget:self selector:@selector(drawView:)];

        // Set it to our _animationFrameInterval
        [_displayLink setFrameInterval:_animationFrameInterval];

        // Have the display link run on the default runn loop (and the main thread)
        [_displayLink addToRunLoop:[NSRunLoop currentRunLoop] forMode:NSDefaultRunLoopMode];

        _animating = TRUE;
    }
}

- (void)stopAnimation
{
    if (_animating)
    {
        [_displayLink invalidate];
        _displayLink = nil;     
        _animating = FALSE;
    }
}

- (void) dealloc
{
    // tear down context
    if ([EAGLContext currentContext] == _context)
        [EAGLContext setCurrentContext:nil];
}

@end
```

[Next](GLEssentials-Source-Classes-OpenGLRenderer.h.md)[Previous](GLEssentials-Source-Classes-iOS-ES2Renderer.m.md)

