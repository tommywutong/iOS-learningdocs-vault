---
title: Real-time Video Processing Using AVPlayerItemVideoOutput
apple_id: DTS40013109
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2015-10-01'
source_url: https://developer.apple.com/library/archive/samplecode/AVBasicVideoOutput/Listings/AVBasicVideoOutput_Shaders_Shader_vsh.html
archived_at: '2026-07-18T03:00:01.858937Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Real-time Video Processing Using AVPlayerItemVideoOutput](Real-time%20Video%20Processing%20Using%20AVPlayerItemVideoOutput.md)


[Next](AVBasicVideoOutput-APLEAGLView.h.md)[Previous](AVBasicVideoOutput-Shaders-Shader.fsh.md)

# AVBasicVideoOutput/Shaders/Shader.vsh

```
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Vertex shader that passes attributes through to fragment shader.
 */

attribute vec4 position;
attribute vec2 texCoord;
uniform float preferredRotation;

varying vec2 texCoordVarying;

void main()
{
    mat4 rotationMatrix = mat4( cos(preferredRotation), -sin(preferredRotation), 0.0, 0.0,
                                sin(preferredRotation),  cos(preferredRotation), 0.0, 0.0,
                                                   0.0,                     0.0, 1.0, 0.0,
                                                   0.0,                     0.0, 0.0, 1.0);
    gl_Position = position * rotationMatrix;
    texCoordVarying = texCoord;
}
```

[Next](AVBasicVideoOutput-APLEAGLView.h.md)[Previous](AVBasicVideoOutput-Shaders-Shader.fsh.md)

