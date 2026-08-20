---
title: Passing IOSurfaces from one process to another via Mach RPC
apple_id: DTS40010132
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2014-10-13'
source_url: https://developer.apple.com/library/archive/samplecode/MultiGPUIOSurface/Listings/Shaders_color_fsh.html
archived_at: '2026-07-18T03:16:26.369655Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Passing IOSurfaces from one process to another via Mach RPC](Passing%20IOSurfaces%20from%20one%20process%20to%20another%20via%20Mach%20RPC.md)


[Next](Shaders-color.vsh.md)[Previous](ServerShaderDefs.h.md)

# Shaders/color.fsh

```
#version 150

in vec4 color;
out vec4 fragColor;

void main()
{
    fragColor = color;
}
```

[Next](Shaders-color.vsh.md)[Previous](ServerShaderDefs.h.md)

