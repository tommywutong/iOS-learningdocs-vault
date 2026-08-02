---
title: MetalShaderShowcase
apple_id: TP40014696
resource_type: Sample Code
platform: iOS
topic: null
technology: Metal
published: '2016-06-13'
source_url: https://developer.apple.com/library/archive/samplecode/MetalShaderShowcase/Listings/MetalShaderShowcase_AAPLRenderer_h.html
archived_at: '2026-07-18T03:14:52.506286Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MetalShaderShowcase](MetalShaderShowcase.md)


[Next](MetalShaderShowcase-AAPLAppDelegate.mm.md)[Previous](MetalShaderShowcase-AAPLParticleSystemRenderer.h.md)

# MetalShaderShowcase/AAPLRenderer.h

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Metal Renderer for Metal Shader Showpiece. Acts as the update and render delegate for the view controller and performs rendering. In MetalShaderShowpiece, the renderer draws a few objects using different shaders.
 */

#import "AAPLView.h"
#import "AAPLViewController.h"
#import "AAPLMesh.h"
#import "AAPLTexture.h"
#import <Metal/Metal.h>
#import "AAPLSharedTypes.h"

static const long kMaxBufferBytesPerFrame = 1024*1024;
static const long kInFlightCommandBuffers = 3;
static const simd::float3 kEye    = {0.0f, 0.0f, 0.0f};
static const simd::float3 kCenter = {0.0f, 0.0f, 1.0f};
static const simd::float3 kUp     = {0.0f, 1.0f, 0.0f};
static const float kFOVY          = 65.0f;

@interface AAPLRenderer : NSObject <AAPLViewControllerDelegate, AAPLViewDelegate>
{
    @protected
        // Global transform data
        id <MTLBuffer> _dynamicConstantBuffer;
        float _rotation;

        BOOL _blending;
        BOOL _depthWriteEnabled;

        id <MTLRenderPipelineState> _pipelineState;
        MTLRenderPipelineReflection *_reflection;
}

// renderer will create a default device at init time.
@property (nonatomic) id <MTLDevice> device;

//  These queries exist so the View can initialize a framebuffer that matches the expectations of the renderer
@property (nonatomic) MTLPixelFormat depthPixelFormat;
@property (nonatomic) MTLPixelFormat stencilPixelFormat;
@property (nonatomic) NSUInteger sampleCount;

@property (nonatomic) NSString *name;

- (instancetype)initWithName:(NSString*)name vertexShader:(NSString*)vertexShaderName fragmentShader:(NSString*)fragmentShaderName mesh:(AAPLMesh*)mesh;

- (instancetype)initWithName:(NSString*)name vertexShader:(NSString*)vertexShaderName fragmentShader:(NSString*)fragmentShaderName mesh:(AAPLMesh*)mesh texture:(AAPLTexture*)texture;

// load all assets before triggering rendering
- (void)configure:(AAPLView *)view;

- (void)initializePipelineStateWithVertexShader:(NSString*)vertexShaderName fragmentShader:(NSString*)fragmentShaderName blending:(BOOL)blending;

- (void)reshape:(AAPLView *)view;

@end
```

[Next](MetalShaderShowcase-AAPLAppDelegate.mm.md)[Previous](MetalShaderShowcase-AAPLParticleSystemRenderer.h.md)

