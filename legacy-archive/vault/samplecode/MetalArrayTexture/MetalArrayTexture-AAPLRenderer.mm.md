---
title: MetalArrayTexture
apple_id: TP40016608
resource_type: Sample Code
platform: iOS|macOS
topic: null
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/samplecode/MetalArrayTexture/Listings/MetalArrayTexture_AAPLRenderer_mm.html
archived_at: '2026-07-18T03:14:46.323694Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MetalArrayTexture](MetalArrayTexture.md)


[Next](MetalArrayTexture-AAPLMtkView.h.md)[Previous](MetalArrayTexture-GeoUtils.c.md)

# MetalArrayTexture/AAPLRenderer.mm

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Metal Renderer. Acts as the update and render delegate for the MTKView object.
 */

#import <string>

#import <QuartzCore/CAMetalLayer.h>
#import <Metal/Metal.h>
#import <simd/simd.h>

#import "AAPLTransforms.h"
#import "AAPLArrayTexture.h"
#import "AAPLTerrain.h"

#import "AAPLRenderer.h"

static const uint32_t kSzSIMDFloat4x4         = sizeof(simd::float4x4);
static const uint32_t kSzBufferLimitsPerFrame = kSzSIMDFloat4x4;

static const uint32_t kInFlightCommandBuffers = 3;

static const float minZoomFactor = 0.2;
static const float maxZoomFactor = 2.5;

@implementation AAPLRenderer
{
@private
    // Renderer globals
    id <MTLDevice>             m_Device;
    id <MTLCommandQueue>       m_CommandQueue;
    id <MTLLibrary>            m_ShaderLibrary;
    id <MTLDepthStencilState>  m_DepthState;

    // Array texture
    AAPLArrayTexture               *mpInTexture;
    id <MTLRenderPipelineState>    m_PipelineState;

    // Terrain representation
    AAPLTerrain *mpTerrain;

    // App control
    dispatch_semaphore_t  m_InflightSemaphore;

    // Dimensions
    CGSize  m_Size;

    // Viewing matrix is derived from an eye point, a reference point
    // indicating the center of the scene, and an up vector.
    simd::float4x4 m_LookAt;

    // Translate the object in (x,y,z) space.
    simd::float4x4 m_Translate;

    // Transform buffers
    simd::float4x4  m_Transform;
    simd::float4x4  m_perspective;
    id <MTLBuffer> m_TransformBuffer[kInFlightCommandBuffers];

    simd::float4x4  m_TextureMatrix;
    id <MTLBuffer>  m_TextureMatrixBuffer;

    // this value will cycle from 0 to kInFlightCommandBuffers whenever a display completes ensuring renderer clients
    // can synchronize between kInFlightCommandBuffers count buffers, and thus avoiding a constant buffer from being overwritten between draws
    NSUInteger m_ConstantDataBufferIndex;

    float _xAxisAngle;
    float _zAxisAngle;
    float _zoomFactor;

    BOOL _needsToUpdateCameraTransform;
}


- (instancetype)init
{
    self = [super init];

    if (self)
    {
        // initialize properties
        m_ConstantDataBufferIndex = 0;
        m_InflightSemaphore = dispatch_semaphore_create(kInFlightCommandBuffers);
    }

    return self;
}

#pragma mark Setup

- (void)configure:(MTKView *)view
{
    // find a usable Device
    m_Device = view.device;

    view.depthStencilPixelFormat   = MTLPixelFormatDepth32Float_Stencil8;
    view.sampleCount        = 1;

    // create a new command queue
    m_CommandQueue = [m_Device newCommandQueue];

    m_ShaderLibrary = [m_Device newDefaultLibrary];

    [self loadAssets:view];
}

- (void)loadAssets:(MTKView *)view
{
    // get the fragment function from the library
    id <MTLFunction> fragmentProgram = [m_ShaderLibrary newFunctionWithName:@"texturedTerrainFragment"];

    // get the vertex function from the library
    id <MTLFunction> vertexProgram = [m_ShaderLibrary newFunctionWithName:@"texturedTerrainVertex"];

    //  create a pipeline state
    MTLRenderPipelineDescriptor *pPipelineStateDescriptor = [MTLRenderPipelineDescriptor new];

    pPipelineStateDescriptor.depthAttachmentPixelFormat      = view.depthStencilPixelFormat;
    pPipelineStateDescriptor.stencilAttachmentPixelFormat    = view.depthStencilPixelFormat;
    pPipelineStateDescriptor.colorAttachments[0].pixelFormat = MTLPixelFormatBGRA8Unorm;

    pPipelineStateDescriptor.sampleCount      = view.sampleCount;
    pPipelineStateDescriptor.vertexFunction   = vertexProgram;
    pPipelineStateDescriptor.fragmentFunction = fragmentProgram;

    NSError *pError = nil;
    m_PipelineState = [m_Device newRenderPipelineStateWithDescriptor:pPipelineStateDescriptor
                                                               error:&pError];
    if(!m_PipelineState) {
        NSLog(@">> ERROR: Failed acquiring pipeline state descriptor: %@", pError);
    }

    // create a depth stencil state
    MTLDepthStencilDescriptor *pDepthStateDesc = [MTLDepthStencilDescriptor new];

    pDepthStateDesc.depthCompareFunction = MTLCompareFunctionLess;
    pDepthStateDesc.depthWriteEnabled    = YES;

    m_DepthState = [m_Device newDepthStencilStateWithDescriptor:pDepthStateDesc];

    // create our two-dimensional array texture
    mpInTexture = [[AAPLArrayTexture alloc] initWithTextureWidth:128 textureHeight:128 arrayLength:4 device:m_Device];

    BOOL isAcquired = NO;
    isAcquired |= [mpInTexture setSlice:0 withContentsOfFile:[[NSBundle mainBundle] pathForResource:@"rock" ofType:@"jpg"]];
    isAcquired |= [mpInTexture setSlice:1 withContentsOfFile:[[NSBundle mainBundle] pathForResource:@"grass" ofType:@"jpg"]];
    isAcquired |= [mpInTexture setSlice:2 withContentsOfFile:[[NSBundle mainBundle] pathForResource:@"dirt" ofType:@"jpg"]];
    isAcquired |= [mpInTexture setSlice:3 withContentsOfFile:[[NSBundle mainBundle] pathForResource:@"snow" ofType:@"jpg"]];

    if(!isAcquired) {
        NSLog(@">> ERROR: Failed creating array texture!");
    }

    // load our terrain mesh
    mpTerrain = [[AAPLTerrain alloc] initWithDevice:m_Device];

    if(!mpTerrain) {
        NSLog(@">> ERROR: Failed creating a terrain object!");
    }

    // allocate regions of memory for the uniform buffers
    for (int i = 0; i < kInFlightCommandBuffers; i++) {
        m_TransformBuffer[i] = [m_Device newBufferWithLength:kSzBufferLimitsPerFrame options:0];
    }

    m_TextureMatrixBuffer = [m_Device newBufferWithLength:kSzBufferLimitsPerFrame options:0];

    // initialize transform values
    _xAxisAngle = -135.0;
    _zAxisAngle = 160.0;
    _zoomFactor = 1.0;

    [self setupTransform:view];
    [self setupTextureMatrix];
}

- (void)setupTransform:(MTKView *)view
{
    uint32_t heightMapSizeScale = mpTerrain ? mpTerrain.heightMapSize : 64;

    m_perspective = AAPL::Math::perspective_fov(60.0, (float)(view.bounds.size.width)/(float)(view.bounds.size.height), 1.0, 100.0);

    m_Transform = AAPL::Math::translate(0, 0, 5.0) * AAPL::Math::rotate(_xAxisAngle, 1, 0, 0) * AAPL::Math::rotate(_zAxisAngle, 0, 0, 1) * AAPL::Math::scale(2.0/heightMapSizeScale, 2.0/heightMapSizeScale, 4.0/heightMapSizeScale) * AAPL::Math::scale(_zoomFactor, _zoomFactor, _zoomFactor);

    m_Transform = m_perspective * m_Transform;

    // Update the buffer associated with the transformation matrix
    for (int i=0; i<kInFlightCommandBuffers; i++) {
        float *pTransform = (float *)[m_TransformBuffer[i] contents];
        std::memcpy(pTransform, &m_Transform, kSzSIMDFloat4x4);
    }
}

- (void)setupTextureMatrix
{
    uint32_t heightMapSizeScale = mpTerrain ? mpTerrain.heightMapSize : 64;

    m_TextureMatrix = AAPL::Math::translate(0, 0, -0.5) * AAPL::Math::scale(1.0, 1.0, 4.0) * AAPL::Math::scale(1.0/heightMapSizeScale, 1.0/heightMapSizeScale, 1.0/16.0) * AAPL::Math::translate(0, 0, 8.0);

    // Update the buffer associated with the transformation matrix
    float *pTextureMatrix = (float *)[m_TextureMatrixBuffer contents];
    std::memcpy(pTextureMatrix, &m_TextureMatrix, kSzSIMDFloat4x4);
}

#pragma mark Render

- (void)rotateCameraWithDx:(float)dx dy:(float)dy scale:(float)scale
{
    _xAxisAngle -= dy * scale;
    _zAxisAngle += dx * scale;

    _needsToUpdateCameraTransform = YES;
}

- (void)zoomCameraWithScale:(float)scale
{
    _zoomFactor = (scale > maxZoomFactor) ? maxZoomFactor : (scale < minZoomFactor ? minZoomFactor : scale);

    _needsToUpdateCameraTransform = YES;
}

- (void)reshapeView:(MTKView *)view
{
    // When reshape is called, update the view matricies since it means that the view orientation or size has changed.
    [self setupTransform:view];
}

- (void)drawView:(MTKView *)view
{
    if (_needsToUpdateCameraTransform) {
        [self setupTransform:view];
        _needsToUpdateCameraTransform = NO;
    }

    dispatch_semaphore_wait(m_InflightSemaphore, DISPATCH_TIME_FOREVER);

    id <MTLCommandBuffer> commandBuffer = [m_CommandQueue commandBuffer];

    // create a render command encoder so we can render into something
    MTLRenderPassDescriptor *renderPassDescriptor = view.currentRenderPassDescriptor;

    // get a render encoder
    id <MTLRenderCommandEncoder>  renderEncoder = [commandBuffer renderCommandEncoderWithDescriptor:renderPassDescriptor];

    // set context state with the render encoder
    [renderEncoder pushDebugGroup:[NSString stringWithFormat:@"encode terrain"]];
    [renderEncoder setFrontFacingWinding:MTLWindingCounterClockwise];
    [renderEncoder setDepthStencilState:m_DepthState];
    [renderEncoder setRenderPipelineState:m_PipelineState];

    [renderEncoder setVertexBuffer:m_TransformBuffer[m_ConstantDataBufferIndex]
                            offset:0
                           atIndex:2];

    [renderEncoder setVertexBuffer:m_TextureMatrixBuffer
                            offset:0
                           atIndex:3];

    [renderEncoder setFragmentTexture:mpInTexture.texture
                              atIndex:0];

    // Encode vertex and texture coordinate buffers for the terrain
    [mpTerrain encode:renderEncoder];

    // tell the render context we want to draw
    [mpTerrain draw:renderEncoder];

    [renderEncoder popDebugGroup];
    [renderEncoder endEncoding];


    // Dispatch the command buffer
    __block dispatch_semaphore_t dispatchSemaphore = m_InflightSemaphore;

    [commandBuffer addCompletedHandler:^(id <MTLCommandBuffer> cmdb){
        dispatch_semaphore_signal(dispatchSemaphore);
    }];

    // Present and commit the command buffer
    [commandBuffer presentDrawable:view.currentDrawable];

    [commandBuffer commit];

    m_ConstantDataBufferIndex = (m_ConstantDataBufferIndex + 1) % kInFlightCommandBuffers;
}

@end
```

[Next](MetalArrayTexture-AAPLMtkView.h.md)[Previous](MetalArrayTexture-GeoUtils.c.md)

