---
title: MetalVideoCapture
apple_id: TP40015131
resource_type: Sample Code
platform: iOS
topic: null
technology: Metal
published: '2015-10-29'
source_url: https://developer.apple.com/library/archive/samplecode/MetalVideoCapture/Listings/MetalVideoCapture_AAPLRenderer_h.html
archived_at: '2026-07-18T03:14:54.894610Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MetalVideoCapture](MetalVideoCapture.md)


[Next](MetalVideoCapture-AAPLView.mm.md)[Previous](MetalVideoCapture-AAPLTexture.m.md)

# MetalVideoCapture/AAPLRenderer.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Metal Renderer for MetalVideoCapture sample. Uses AVFoundation video capture APIs to grab video data and CVMetalTextureCache APIs to convert video frames to textures usable within a Metal render pass. A video frame is returned via an AVCapture API Callback which must be synchronized with the Metal renderer (in this case on the main queue). The renderer renders two objects (with two seperate programs). The first is the skybox and the second is a quad with the video texture, a skybox based environment map reflection and a mipmaped pvrtc texture.
 */

#import "AAPLView.h"
#import "AAPLViewController.h"

#import <Metal/Metal.h>
#import <AVFoundation/AVFoundation.h>
#import <QuartzCore/QuartzCore.h>
#import <CoreMedia/CoreMedia.h>
#import <Accelerate/Accelerate.h>

@interface AAPLRenderer : NSObject <AAPLViewControllerDelegate, AAPLViewDelegate, AVCaptureVideoDataOutputSampleBufferDelegate>

// load all assets before triggering rendering
- (void)configure:(AAPLView *)view;

@end
```

[Next](MetalVideoCapture-AAPLView.mm.md)[Previous](MetalVideoCapture-AAPLTexture.m.md)

