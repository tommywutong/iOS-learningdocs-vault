---
title: MetalShaderShowcase
apple_id: TP40014696
resource_type: Sample Code
platform: iOS
topic: null
technology: Metal
published: '2016-06-13'
source_url: https://developer.apple.com/library/archive/samplecode/MetalShaderShowcase/Listings/MetalShaderShowcase_AAPLView_h.html
archived_at: '2026-07-18T03:14:54.345411Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MetalShaderShowcase](MetalShaderShowcase.md)


[Next](MetalShaderShowcase-AAPLParticleShader.metal.md)[Previous](MetalShaderShowcase-AAPLSphereMapShader.metal.md)

# MetalShaderShowcase/AAPLView.h

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 View for Metal Sample Code. Manages screen drawable framebuffers and expects a delegate to repond to render commands to perform drawing.
 */

#import <QuartzCore/CAMetalLayer.h>
#import <Metal/Metal.h>
#import <UIKit/UIKit.h>

@protocol AAPLViewDelegate;

@interface AAPLView : UIView
@property (nonatomic, weak) IBOutlet id <AAPLViewDelegate> delegate;

// view has a handle to the metal device when created
@property (nonatomic, readonly) id <MTLDevice> device;

// the current drawable created within the view's CAMetalLayer
@property (nonatomic, readonly) id <CAMetalDrawable> currentDrawable;

// The current framebuffer can be read by delegate during -[MetalViewDelegate render:]
// This call may block until the framebuffer is available.
@property (nonatomic, readonly) MTLRenderPassDescriptor *renderPassDescriptor;

// set these pixel formats to have the main drawable framebuffer get created with depth and/or stencil attachments
@property (nonatomic) MTLPixelFormat depthPixelFormat;
@property (nonatomic) MTLPixelFormat stencilPixelFormat;
@property (nonatomic) NSUInteger     sampleCount;

// view controller will be call off the main thread
- (void)display;

// release any color/depth/stencil resources. view controller will call when paused.
- (void)releaseTextures;

@end

// rendering delegate (App must implement a rendering delegate that responds to these messages
@protocol AAPLViewDelegate <NSObject>

@required
// called if the view changes orientation or size, renderer can precompute its view and projection matricies here for example
- (void)reshape:(AAPLView *)view;

// delegate should perform all rendering here
- (void)render:(AAPLView *)view;

@end
```

[Next](MetalShaderShowcase-AAPLParticleShader.metal.md)[Previous](MetalShaderShowcase-AAPLSphereMapShader.metal.md)

