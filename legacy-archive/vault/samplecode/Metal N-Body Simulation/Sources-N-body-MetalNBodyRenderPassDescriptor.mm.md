---
title: Metal N-Body Simulation
apple_id: TP40016621
resource_type: Sample Code
platform: iOS
topic: General
technology: Metal
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/Metal_NBody_Simulation/Listings/Sources_N_body_MetalNBodyRenderPassDescriptor_mm.html
archived_at: '2026-07-18T03:14:57.739379Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Metal N-Body Simulation](Metal%20N-Body%20Simulation.md)


[Next](Sources-N-body-NBodyPreferences.h.md)[Previous](Sources-N-body-NBodyURDGenerator.h.md)

# Sources/N-body/MetalNBodyRenderPassDescriptor.mm

```objc
/*
 Copyright (C) 2015-2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Utility class for creating a render pass descriptor.
 */

#import "MetalNBodyRenderPassDescriptor.h"

@implementation MetalNBodyRenderPassDescriptor
{
@private
    BOOL _haveTexture;

    MTLLoadAction  _load;
    MTLStoreAction _store;
    MTLClearColor  _color;

    MTLRenderPassDescriptor* _descriptor;
}

- (nullable MTLRenderPassDescriptor *) _newDescriptor
{
    MTLRenderPassDescriptor* pDescriptor = [MTLRenderPassDescriptor renderPassDescriptor];

    if(pDescriptor)
    {
        pDescriptor.colorAttachments[0].loadAction  = _load;
        pDescriptor.colorAttachments[0].storeAction = _store;
        pDescriptor.colorAttachments[0].clearColor  = _color;
    } // if
    else
    {
        NSLog(@">> ERROR:  Failed to instantiate a Metal render pass decriptor!");
    } // else

    return pDescriptor;
} // _newDescriptor

- (instancetype) init
{
    self = [super init];

    if(self)
    {
        _load        = MTLLoadActionClear;
        _store       = MTLStoreActionStore;
        _color       = MTLClearColorMake(0.0f, 0.0f, 0.0f, 0.0f);
        _haveTexture = NO;
        _descriptor  = [self _newDescriptor];
    } // if

    return self;
} // init

- (void) setColor:(MTLClearColor)color
{
    _color = color;

    if(_descriptor)
    {
        _descriptor.colorAttachments[0].clearColor = _color;
    } // if
} // setColor

- (void) setDrawable:(nullable id<CAMetalDrawable>)drawable
{
    _haveTexture = NO;

    if(drawable && _descriptor)
    {
        id<MTLTexture> texture = drawable.texture;

        if(texture)
        {
            _descriptor.colorAttachments[0].texture = texture;

            _haveTexture = YES;
        } // if
    } // if
} // setDrawable

@end
```

[Next](Sources-N-body-NBodyPreferences.h.md)[Previous](Sources-N-body-NBodyURDGenerator.h.md)

