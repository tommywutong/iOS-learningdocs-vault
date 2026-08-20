---
title: OpenCL N-Body Simulation
apple_id: TP40016610
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_NBody_Simulation/Listings/Sources_Shaders_NBody_nbody_vsh.html
archived_at: '2026-07-18T03:17:43.659298Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL N-Body Simulation](OpenCL%20N-Body%20Simulation.md)


[Next](Sources-Shaders-NBody-nbody.fsh.md)[Previous](Sources-Shaders-Star-star.vsh.md)

# Sources/Shaders/NBody/nbody.vsh

```
/*
 <codex>
 <abstract>
 N-Body vertex shader.
 </abstract>
 </codex>
 */

uniform sampler2D splatTexture;
uniform float pointSize;

void main()
{
    gl_Position = gl_Vertex;
    gl_PointSize = 0.05 * pointSize;
    gl_FrontColor = gl_Color;
}
```

[Next](Sources-Shaders-NBody-nbody.fsh.md)[Previous](Sources-Shaders-Star-star.vsh.md)

