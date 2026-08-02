---
title: Passing IOSurfaces from one process to another via Mach RPC
apple_id: DTS40010132
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2014-10-13'
source_url: https://developer.apple.com/library/archive/samplecode/MultiGPUIOSurface/Listings/Shaders_color_vsh.html
archived_at: '2026-07-18T03:16:26.423233Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Passing IOSurfaces from one process to another via Mach RPC](Passing%20IOSurfaces%20from%20one%20process%20to%20another%20via%20Mach%20RPC.md)


[Next](Shaders-lighting.vsh.md)[Previous](Shaders-color.fsh.md)

# Shaders/color.vsh

```
#version 150

in vec4 inVertex;
out vec4 color;

uniform mat4 MVP;
uniform vec4 constantColor;

void main()
{
    gl_Position = MVP * inVertex;
    color = constantColor;
}
```

[Next](Shaders-lighting.vsh.md)[Previous](Shaders-color.fsh.md)

