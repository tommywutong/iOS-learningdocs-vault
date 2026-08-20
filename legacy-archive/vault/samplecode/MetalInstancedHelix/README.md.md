---
title: MetalInstancedHelix
apple_id: TP40015091
resource_type: Sample Code
platform: iOS
topic: null
technology: Metal
published: '2015-01-24'
source_url: https://developer.apple.com/library/archive/samplecode/MetalInstancedHelix/Listings/README_md.html
archived_at: '2026-07-18T03:14:51.473723Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MetalInstancedHelix](MetalInstancedHelix.md)


[Next](MetalInstancedHelix-shaders.metal.md)[Previous](MetalInstancedHelix-main.m.md)

# README.md

```
# MetalInstancedHelix

This example renders a set of cubes using Metal and alternates their colors by modifying each cube's uniforms directly in the shared CPU/GPU memory buffer. Several parameters can be modified directly in the AAPLRenderer.mm file including the number of cubes and their size. The cubes are rendered into a helix path using spherical coordinate system to get x,y,z for the translation matrix. Each cube is renderered individually using a basic 3D phong lighting shader, but drawn in only a single draw call using Metal's instancing API. Note, for each frame, each cube's transformation matrix is update along with its color, therefore in each frame the sample must traverese through 2n cubes. 

## Requirements

### Build

iOS 8 SDK

### Runtime

iOS 8, 64 Bit device

Copyright (C) 2015 Apple Inc. All rights reserved.
```

[Next](MetalInstancedHelix-shaders.metal.md)[Previous](MetalInstancedHelix-main.m.md)

