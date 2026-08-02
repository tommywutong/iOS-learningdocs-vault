---
title: Real-time Video Processing Using AVPlayerItemVideoOutput
apple_id: DTS40013109
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2015-10-01'
source_url: https://developer.apple.com/library/archive/samplecode/AVBasicVideoOutput/Listings/AVBasicVideoOutput_Shaders_Shader_fsh.html
archived_at: '2026-07-18T03:00:01.801644Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Real-time Video Processing Using AVPlayerItemVideoOutput](Real-time%20Video%20Processing%20Using%20AVPlayerItemVideoOutput.md)


[Next](AVBasicVideoOutput-Shaders-Shader.vsh.md)[Previous](AVBasicVideoOutput-APLViewController.h.md)

# AVBasicVideoOutput/Shaders/Shader.fsh

```
/*
    Copyright (C) 2015 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Fragment shader that adjusts the luminance value based on the input sliders and renders the input texture.
 */

varying highp vec2 texCoordVarying;
precision mediump float;

uniform float lumaThreshold;
uniform float chromaThreshold;
uniform sampler2D SamplerY;
uniform sampler2D SamplerUV;
uniform mat3 colorConversionMatrix;

void main()
{
    mediump vec3 yuv;
    lowp vec3 rgb;

    // Subtract constants to map the video range start at 0
    yuv.x = (texture2D(SamplerY, texCoordVarying).r - (16.0/255.0))* lumaThreshold;
    yuv.yz = (texture2D(SamplerUV, texCoordVarying).rg - vec2(0.5, 0.5))* chromaThreshold;

    rgb = colorConversionMatrix * yuv;

    gl_FragColor = vec4(rgb,1);
}
```

[Next](AVBasicVideoOutput-Shaders-Shader.vsh.md)[Previous](AVBasicVideoOutput-APLViewController.h.md)

