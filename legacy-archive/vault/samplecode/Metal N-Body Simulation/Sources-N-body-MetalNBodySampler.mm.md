---
title: Metal N-Body Simulation
apple_id: TP40016621
resource_type: Sample Code
platform: iOS
topic: General
technology: Metal
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/Metal_NBody_Simulation/Listings/Sources_N_body_MetalNBodySampler_mm.html
archived_at: '2026-07-18T03:14:58.147147Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Metal N-Body Simulation](Metal%20N-Body%20Simulation.md)


[Next](Sources-N-body-MetalGaussianMap.mm.md)[Previous](Sources-N-body-MetalNBodyRenderStage.mm.md)

# Sources/N-body/MetalNBodySampler.mm

```objc
/*
 Copyright (C) 2015-2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Utility class for creating a sampler.
 */

#import "MetalNBodySampler.h"

@implementation MetalNBodySampler
{
@private
    BOOL _haveSampler;

    id<MTLSamplerState>  _sampler;
}

- (instancetype) init
{
    self = [super init];

    if(self)
    {
        _haveSampler = NO;
        _sampler     = nil;
    } // if

    return self;
} // init

- (BOOL) _acquire:(nullable id<MTLDevice>)device
{
    if(device)
    {
        MTLSamplerDescriptor* pDescriptor = [MTLSamplerDescriptor new];

        if(!pDescriptor)
        {
            NSLog(@">> ERROR: Failed to instantiate sampler descriptor!");

            return NO;
        } // if

        pDescriptor.minFilter             = MTLSamplerMinMagFilterLinear;
        pDescriptor.magFilter             = MTLSamplerMinMagFilterLinear;
        pDescriptor.sAddressMode          = MTLSamplerAddressModeRepeat;
        pDescriptor.tAddressMode          = MTLSamplerAddressModeRepeat;
        pDescriptor.mipFilter             = MTLSamplerMipFilterNotMipmapped;
        pDescriptor.maxAnisotropy         = 1U;
        pDescriptor.normalizedCoordinates = YES;
        pDescriptor.lodMinClamp           = 0.0;
        pDescriptor.lodMaxClamp           = 255.0;

        _sampler = [device newSamplerStateWithDescriptor:pDescriptor];

        if(!_sampler)
        {
            NSLog(@">> ERROR: Failed to instantiate sampler state with descriptor!");

            return NO;
        } // else

        return YES;
    } // else
    else
    {
        NSLog(@">> ERROR: Metal device is nil!");
    } // if

    return NO;
} // _acquire

- (void) acquire:(nullable id<MTLDevice>)device
{
    if(!_haveSampler)
    {
        _haveSampler = [self _acquire:device];
    } // if
} // acquire

@end
```

[Next](Sources-N-body-MetalGaussianMap.mm.md)[Previous](Sources-N-body-MetalNBodyRenderStage.mm.md)

