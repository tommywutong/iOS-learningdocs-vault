---
title: Metal N-Body Simulation
apple_id: TP40016621
resource_type: Sample Code
platform: iOS
topic: General
technology: Metal
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/Metal_NBody_Simulation/Listings/Sources_N_body_MetalNBodyRenderPipeline_mm.html
archived_at: '2026-07-18T03:14:57.891438Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Metal N-Body Simulation](Metal%20N-Body%20Simulation.md)


[Next](Sources-N-body-NBodyURDGenerator.mm.md)[Previous](Sources-N-body-NBodyPreferences.h.md)

# Sources/N-body/MetalNBodyRenderPipeline.mm

```objc
/*
 Copyright (C) 2015-2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Utility class for creating a render state pipeline.
 */

#import "MetalNBodyRenderPipeline.h"

@implementation MetalNBodyRenderPipeline
{
@private
    BOOL _blend;
    BOOL _haveDescriptor;

    id<MTLFunction>  _vertex;
    id<MTLFunction>  _fragment;

    id<MTLRenderPipelineState> _render;
}

- (instancetype) init
{
    self = [super init];

    if(self)
    {
        _blend          = NO;
        _haveDescriptor = NO;

        _fragment = nil;
        _vertex   = nil;
        _render   = nil;
    } // if

    return self;
} // init

- (BOOL) _acquire:(nullable id<MTLDevice>) device
{
    if(device)
    {
        if(!_vertex)
        {
            NSLog(@">> ERROR: Vertex stage object is nil!");

            return NO;
        } // if

        if(!_fragment)
        {
            NSLog(@">> ERROR: Fragment stage object is nil!");

            return NO;
        } // if

        MTLRenderPipelineDescriptor* pDescriptor = [MTLRenderPipelineDescriptor new];

        if(!pDescriptor)
        {
            NSLog(@">> ERROR: Failed to instantiate render pipeline descriptor!");

            return NO;
        } // if

        [pDescriptor setVertexFunction:_vertex];
        [pDescriptor setFragmentFunction:_fragment];

        pDescriptor.colorAttachments[0].pixelFormat         = MTLPixelFormatBGRA8Unorm;
        pDescriptor.colorAttachments[0].blendingEnabled     = YES;
        pDescriptor.colorAttachments[0].rgbBlendOperation   = MTLBlendOperationAdd;
        pDescriptor.colorAttachments[0].alphaBlendOperation = MTLBlendOperationAdd;

        if(_blend)
        {
            pDescriptor.colorAttachments[0].sourceRGBBlendFactor        = MTLBlendFactorOne;
            pDescriptor.colorAttachments[0].sourceAlphaBlendFactor      = MTLBlendFactorOne;
            pDescriptor.colorAttachments[0].destinationRGBBlendFactor   = MTLBlendFactorOneMinusSourceAlpha;
            pDescriptor.colorAttachments[0].destinationAlphaBlendFactor = MTLBlendFactorOneMinusSourceAlpha;
        } // if
        else
        {
            pDescriptor.colorAttachments[0].sourceRGBBlendFactor        = MTLBlendFactorSourceAlpha;
            pDescriptor.colorAttachments[0].sourceAlphaBlendFactor      = MTLBlendFactorSourceAlpha;
            pDescriptor.colorAttachments[0].destinationRGBBlendFactor   = MTLBlendFactorOne;
            pDescriptor.colorAttachments[0].destinationAlphaBlendFactor = MTLBlendFactorOne;
        } // else

        NSError* pError = nil;

        _render = [device newRenderPipelineStateWithDescriptor:pDescriptor
                                                         error:&pError];

        if(!_render)
        {
            NSString* pDescription = [pError description];

            if(pDescription)
            {
                NSLog(@">> ERROR: Failed to instantiate render pipeline: {%@}", pDescription);
            } // if
            else
            {
                NSLog(@">> ERROR: Failed to instantiate render pipeline!");
            } // else

            return NO;
        } // if

        return YES;
    } // if
    else
    {
        NSLog(@">> ERROR: Metal device is nil!");
    } // if

    return NO;
} // acquire

// Generate render pipeline state using a default system
// device, fragment and vertex stages
- (void) acquire:(nullable id<MTLDevice>)device
{
    if(!_haveDescriptor)
    {
        _haveDescriptor = [self _acquire:device];
    } // if
} // acquire

@end
```

[Next](Sources-N-body-NBodyURDGenerator.mm.md)[Previous](Sources-N-body-NBodyPreferences.h.md)

