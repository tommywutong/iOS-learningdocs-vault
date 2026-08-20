---
title: MetalArrayTexture
apple_id: TP40016608
resource_type: Sample Code
platform: iOS|macOS
topic: null
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/samplecode/MetalArrayTexture/Listings/MetalArrayTexture_AAPLMtkView_m.html
archived_at: '2026-07-18T03:14:46.181911Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MetalArrayTexture](MetalArrayTexture.md)


[Next](MetalArrayTexture-AAPLViewController.h.md)[Previous](MetalArrayTexture-AAPLTransforms.h.md)

# MetalArrayTexture/AAPLMtkView.m

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 A MTKView subclass. Handles camera movement. Delegates to the AAPLRenderer object for actual rendering and resizing.
 */

#import "AAPLMtkView.h"

@implementation AAPLMtkView
{
#ifdef TARGET_IOS
    UIPanGestureRecognizer *_panRecognizer;
    UIPinchGestureRecognizer *_pinchRecognizer;
#else
    CGPoint _lastPoint;
    BOOL _dragBegan;
#endif

    CGFloat _zoomScale;
}

- (void)initView
{
#ifdef TARGET_IOS
    _panRecognizer = [[UIPanGestureRecognizer alloc] initWithTarget:self action:@selector(handlePan:)];
    [self addGestureRecognizer:_panRecognizer];

    _pinchRecognizer = [[UIPinchGestureRecognizer alloc] initWithTarget:self action:@selector(handlePinch:)];
    [self addGestureRecognizer:_pinchRecognizer];
#endif

    _zoomScale = 1.0;
}

- (id)initWithFrame:(CGRect)frame
{
    self = [super initWithFrame:frame];

    if(self)
    {
        [self initView];
    }

    return self;
}

- (instancetype)initWithCoder:(NSCoder *)coder
{
    self = [super initWithCoder:coder];

    if(self)
    {
        [self initView];
    }
    return self;
}

- (void)drawRect:(CGRect)dirtyRect
{
    // delegate to the renderer object for drawing
    [_renderer drawView:self];
}

#ifdef TARGET_IOS
-(void)layoutSubviews
{
    [super layoutSubviews];

    // delegate to the renderer object for resizing
    [_renderer reshapeView:self];
}
#else

-(void) setFrameSize:(NSSize)newSize
{
    [super setFrameSize:newSize];

    // delegate to the renderer object for resizing
    [_renderer reshapeView:self];
}
#endif


#pragma mark Camera Movements

#ifdef TARGET_IOS
- (void)handlePan:(UIPanGestureRecognizer *)pan
{
    CGPoint p = [pan velocityInView:self];
    CGSize viewSize = self.bounds.size;

    [_renderer rotateCameraWithDx:p.x/viewSize.width dy:p.y/viewSize.height scale:10.0];
}

- (void)handlePinch:(UIPinchGestureRecognizer *)pinch
{
    CGFloat s = [pinch scale];

    [_renderer zoomCameraWithScale:_zoomScale*s];

    if (pinch.state == UIGestureRecognizerStateEnded) {
        _zoomScale *= s;
    }
}

- (void)dealloc
{
    [self removeGestureRecognizer:_panRecognizer];
    [self removeGestureRecognizer:_pinchRecognizer];
}
#else

- (BOOL)acceptsFirstResponder
{
    return YES;
}

- (void)keyDown:(NSEvent *)theEvent
{
    unichar c = [[theEvent charactersIgnoringModifiers] characterAtIndex:0];
    switch (c)
    {
        case '-':
        case '_':
            [_renderer zoomCameraWithScale:_renderer.zoomFactor * 0.8];
            break;

        case '+':
        case '=':
            [_renderer zoomCameraWithScale:_renderer.zoomFactor * 1.2];
            break;

        default:
            break;
    }
}

- (void)mouseDown:(NSEvent *)theEvent
{
    _lastPoint = [self convertPoint:[theEvent locationInWindow] fromView:nil];
    _dragBegan = YES;
}

- (void)mouseDragged:(NSEvent *)theEvent
{
    // eat the first event so the camera doesn't go crazy
    if (_dragBegan)  {
        _dragBegan = NO;
    }
    else {
        NSPoint p = [self convertPoint:[theEvent locationInWindow] fromView:nil];
        float dx = _lastPoint.x - p.x;
        float dy = _lastPoint.y - p.y;

        [_renderer rotateCameraWithDx:dx dy:dy scale:0.33];

        _lastPoint = p;
    }
}
#endif

@end
```

[Next](MetalArrayTexture-AAPLViewController.h.md)[Previous](MetalArrayTexture-AAPLTransforms.h.md)

