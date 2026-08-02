---
title: Passing IOSurfaces from one process to another via Mach RPC
apple_id: DTS40010132
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2014-10-13'
source_url: https://developer.apple.com/library/archive/samplecode/MultiGPUIOSurface/Listings/Shaders_textureRect_fsh.html
archived_at: '2026-07-18T03:16:26.515817Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Passing IOSurfaces from one process to another via Mach RPC](Passing%20IOSurfaces%20from%20one%20process%20to%20another%20via%20Mach%20RPC.md)


[Next](UtilSrc-debug.h.md)[Previous](Shaders-texture.vsh.md)

# Shaders/textureRect.fsh

```
#version 150

in vec2 textureCoord;
out vec4 fragColor;

uniform sampler2DRect tex;

void main()
{
    fragColor = texture(tex, textureCoord);
}
```

[Next](UtilSrc-debug.h.md)[Previous](Shaders-texture.vsh.md)

