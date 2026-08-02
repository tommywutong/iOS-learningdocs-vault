---
title: MetalVideoCapture
apple_id: TP40015131
resource_type: Sample Code
platform: iOS
topic: null
technology: Metal
published: '2015-10-29'
source_url: https://developer.apple.com/library/archive/samplecode/MetalVideoCapture/Listings/README_md.html
archived_at: '2026-07-18T03:14:55.955238Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MetalVideoCapture](MetalVideoCapture.md)


[Next](MetalVideoCapture-AAPLViewController.mm.md)[Previous](MetalVideoCapture-main.m.md)

# README.md

```
# MetalVideoCapture

This sample demonstrates how to stream captured video textures (from the front facing camera on an iOS device) into a 3D scene rendered with Metal. The video texture is combined with an environment map reflection from a cubemap (which is also rendered seperatly as the starfield skybox) and a 2D mipmap PVRTC texture (copper metal texture). 

AAPLRenderer.mm is the core of the project and where the magic happens. The render is based on Metal and uses AVFoundation capture APIs to obtain video from the camera. Each frame of video is obtained as an individual Metal texture via CVMetalTextureRef and CVMetalTextureCache APIs. The quad spinning in space is renderered by mixing the various textures on the GPU

## Requirements

### Build

iOS 9 SDK

### Runtime

iOS 9, 64 bit device

Copyright (C) 2015 Apple Inc. All rights reserved.
```

[Next](MetalVideoCapture-AAPLViewController.mm.md)[Previous](MetalVideoCapture-main.m.md)

